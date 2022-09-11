# TODO сделать отправку стикеров

import datetime as dt
import logging
import math
import os
import random

import gridfs
import pymongo
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import BotCommand
from aiogram.utils import executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

import utils.constants as const
from functions.plan_check import plan_pat_check, plan_tu_check
from functions.request_weather import request_weather
from functions.scrap_history_day import scrap_history_day
from functions.second_level_apk_check import second_level_apk_check
from functions.text_generators import (evening_hello_generator,
                                       hello_generator, month_plan_generator,
                                       wish_generator)
from texts.apk import APK_2_REMAINDER
from texts.initial import (FINAL_TEXT, HELP_TEXT, INITIAL_TEXT, KPB_TEXT,
                           NS_TEXT, QUIZ_TEXT, SERVICE_END_TEXT, SERVICE_TEXT)

load_dotenv()

# Create the client
client = pymongo.MongoClient('localhost', 27017)
# Connect to our database
db = client['gks_bot_db']
fs = gridfs.GridFS(db)
quiz = db['quiz']
users = db['users']
vehicles = db['vehicles']


class ChooseVehicle(StatesGroup):
    waiting_for_vehicle_type = State()
    waiting_for_vehicle_time = State()
    waiting_for_location = State()
    waiting_confirm = State()


scheduler = AsyncIOScheduler()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')  # тестовый чат
TEST_CHAT_ID = '-1001555422626'  # тестовый чат
CHAT_ID_GKS = os.getenv('CHAT_ID_GKS')


logging.basicConfig(
    filename='gks56_bot.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d.%m.%y %H:%M:%S'
)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# проверка наличия юзера в БД и добавление его в БД при отсутствии
def insert_user_db(user):
    check_user = users.find_one({'id': user.id})
    if check_user is None:
        users.insert_one({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'place_of_work': '',
        })


@dp.message_handler(commands=['num'])
async def send_count_users(message: types.Message):
    users_count = users.count_documents({})
    await bot.send_message(
        chat_id=message.chat.id,
        text=f'Количество пользователей в БД: {users_count}'
    )


@dp.message_handler(commands=['exam'])
async def send_exam_answers(message: types.Message):
    insert_user_db(message.from_user)
    for root, dirs, files in os.walk('static/exam/'):
        for filename in files:
            file = f'static/exam/{filename}'
            with open(file, 'rb') as f:
                contents = f.read()
                await bot.send_photo(message.chat.id, photo=contents)


async def send_vehicle_start_message():
    message = ('Уважаемые начальники цехов, '
               'время делать заявки на спец. технику.\n'
               'Для подачи заявки перейдите по ссылке:\n\n'
               '/zayavka\n\n'
               'Заявки принимаются до 16:45.')
    await bot.send_message(chat_id=CHAT_ID_GKS, text=message)


@dp.message_handler(commands=['zayavka'])
async def redirect_vehicle(message: types.Message):
    await bot.send_message(
        chat_id=message.from_user.id,
        text=(
            f'Добрый день {message.from_user.full_name}, '
            'для начала нажмите\n\n/tehnika'
        )
    )


async def send_vehicle_stop_message():
    date = dt.datetime.today().strftime('%d.%m.%Y')
    queryset = vehicles.find({'date': date})
    result = {}
    for i in queryset:
        if result.get(i.get('vehicle')) is None:
            result[i.get('vehicle')] = {}
        result[i.get('vehicle')][i.get('location')] = i.get('time')
    message = ''
    for vehicle, loc_time in result.items():
        part_message = ''
        for location, time in loc_time.items():
            text = '    {} - {}\n'.format(location, time.lower())
            part_message = '{}{}'.format(part_message, text)
        part_text = '{}:\n{}'.format(vehicle, part_message)
        message = '{}{}\n'.format(message, part_text)
    final_message = '{}\n\n{}'.format('Приём заявок завершён.', message)
    await bot.send_message(chat_id=CHAT_ID_GKS, text=final_message)


@dp.message_handler(commands=['tehnika'])
async def vehicle_start(message: types.Message):
    insert_user_db(message.from_user)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    user = message.from_user
    for name in const.VEHICLES:
        keyboard.add(name)
    await bot.send_message(
        chat_id=user.id,
        text='Выберите спец.технику из списка ниже',
        reply_markup=keyboard
    )
    await ChooseVehicle.waiting_for_vehicle_type.set()


async def vehicle_chosen(message: types.Message, state: FSMContext):
    if message.text not in const.VEHICLES:
        await message.answer(
            'Пожалуйста, выберите технику, используя список ниже.'
            'Я не работаю с другой техникой кроме той, что в списке.'
        )
        return
    await state.update_data(chosen_vehicle=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in const.PERIODS:
        keyboard.add(size)
    # для простых шагов можно не указывать название состояния, обходясь next()
    await ChooseVehicle.next()
    # await message.answer(
    #     'Теперь выберите необходимый период времени',
    #     reply_markup=keyboard
    # )
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Теперь выберите необходимый период времени',
        reply_markup=keyboard
    )


async def vehicle_time_chosen(message: types.Message, state: FSMContext):
    if message.text not in const.PERIODS:
        await message.answer(
            'Пожалуйста, выберите период, используя клавиатуру ниже.'
        )
        return
    await state.update_data(chosen_vehicle_time=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for location in const.LOCATIONS:
        keyboard.add(location)
    await ChooseVehicle.next()
    await bot.send_message(
        chat_id=message.from_user.id,
        text='Отлично! Выберите место где будет работать техника.',
        reply_markup=keyboard
    )


async def user_location_chosen(message: types.Message, state: FSMContext):
    if message.text not in const.LOCATIONS:
        await message.answer(
            'Пожалуйста, выберите место работы, используя клавиатуру ниже.'
        )
        return
    await state.update_data(chosen_location=message.text)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Нет', 'Да')
    user_data = await state.get_data()
    vehicle = user_data['chosen_vehicle']
    time = user_data['chosen_vehicle_time']
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Вы выбрали "{vehicle}" {time.lower()}.\nВсё верно?',
        reply_markup=keyboard,
    )
    await ChooseVehicle.next()


async def confirmation(message: types.Message, state: FSMContext):
    if message.text.lower() not in ['нет', 'да']:
        await message.answer(
            'Пожалуйста, выберите ответ, используя клавиатуру ниже.'
        )
        return
    if message.text.lower() == 'нет':
        await message.answer(
            ('Хорошо. Данные не сохранены.\n'
             'Если необходимо выбрать технику снова - нажмите /tehnika'),
            reply_markup=types.ReplyKeyboardRemove()
        )
        await state.reset_state()
    user_data = await state.get_data()
    date = dt.datetime.today().strftime('%d.%m.%Y')
    vehicles.insert_one(
        {
            'date': date,
            'user': message.from_user.id,
            'location': user_data['chosen_location'],
            'vehicle': user_data['chosen_vehicle'],
            'time': user_data['chosen_vehicle_time'],
        }
    )
    await message.answer(
        ('Отлично! Данные успешно сохранены.\n'
         'Если необходимо выбрать ещё технику нажмите /tehnika'),
        reply_markup=types.ReplyKeyboardRemove()
    )
    await state.finish()


def register_handlers_vehicle(dp: Dispatcher):
    dp.register_message_handler(
        vehicle_chosen,
        state=ChooseVehicle.waiting_for_vehicle_type,
    )
    dp.register_message_handler(
        vehicle_time_chosen,
        state=ChooseVehicle.waiting_for_vehicle_time
    )
    dp.register_message_handler(
        user_location_chosen,
        state=ChooseVehicle.waiting_for_location
    )
    dp.register_message_handler(
        confirmation,
        state=ChooseVehicle.waiting_confirm
    )


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(message.chat.id, text=INITIAL_TEXT)


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(
        message.chat.id,
        text=f'{message.from_user.full_name}{HELP_TEXT}'
    )
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['pravila'])
async def pravila_handler(message: types.Message):
    insert_user_db(message.from_user)
    for root, dirs, files in os.walk('static/kpb_lite/'):
        for filename in files:
            file = f'static/kpb_lite/{filename}'
            with open(file, 'rb') as f:
                contents = f.read()
                await bot.send_photo(message.chat.id, photo=contents)
    await bot.send_message(message.chat.id, text=KPB_TEXT)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['vnimanie'])
async def vnimanie_handler(message: types.Message):
    insert_user_db(message.from_user)
    for root, dirs, files in os.walk('static/ns/'):
        for filename in files:
            file = f'static/ns/{filename}'
            with open(file, 'rb') as f:
                contents = f.read()
                await bot.send_photo(message.chat.id, photo=contents)
    await bot.send_message(message.chat.id, text=NS_TEXT)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['service'])
async def service_handler(message: types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(chat_id=CHAT_ID, text=SERVICE_TEXT)


@dp.message_handler(commands=['endservice'])
async def service_end_handler(message: types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(chat_id=CHAT_ID, text=SERVICE_END_TEXT)


@dp.message_handler(commands=['pat'])
async def pat_handler(message: types.Message):
    insert_user_db(message.from_user)
    text = plan_pat_check().get('data')
    full_text = (
        f'Противоаварийная тренировка на КЦ-5,6 в этом месяце:\n\n{text}'
    )
    await bot.send_message(message.chat.id, text=full_text)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['tu'])
async def tu_handler(message: types.Message):
    insert_user_db(message.from_user)
    plan_now = plan_tu_check().get('plan')
    plan_past = plan_tu_check().get('past_plan')
    text_now = ''
    text_past = ''
    for date, theme in plan_now.items():
        theme_text = ''
        for item in theme:
            theme_text = theme_text + f'{item}\n'
        text_now = text_now + f'{date}:\n{theme_text}\n'
    if len(plan_past) == 0:
        text_past = 'Данные отсутствуют'
    else:
        for date, theme in plan_past.items():
            theme_text = ''
            for item in theme:
                theme_text = theme_text + f'{item}\n'
            text_past = text_past + f'{date}:\n{theme_text}\n'
    full_text_now = f'Техническая учёба на КЦ-5,6 в этом месяце:\n\n{text_now}'
    full_text_past = f'В предыдущем месяце:\n\n{text_past}'
    full_text = '{}\n{}'.format(full_text_now, full_text_past)
    await bot.send_message(message.chat.id, text=full_text)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


def get_poll():
    count = quiz.count_documents({})
    rand_num = random.randint(0, count)
    poll = quiz.find_one({'num': rand_num})
    return poll


@dp.message_handler(commands=['menu'])
async def all_commands(message: types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['vopros'])
async def send_quiz(message: types.Message):
    insert_user_db(message.from_user)
    poll = get_poll()
    correct_option_id = poll['correct_answer'] - 1
    explanation = poll['answers'][poll['correct_answer'] - 1]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=poll['question'],
        options=poll['answers'],
        is_anonymous=True,
        type='quiz',
        correct_option_id=correct_option_id,
        explanation=f'Правильный ответ: {explanation}',
        protect_content=True,
    )
    await bot.send_message(message.chat.id, text=QUIZ_TEXT)


async def send_quiz_shedule():
    poll = get_poll()
    correct_option_id = poll['correct_answer'] - 1
    explanation = poll['answers'][poll['correct_answer'] - 1]
    await bot.send_poll(
        chat_id=CHAT_ID,
        question=poll['question'],
        options=poll['answers'],
        is_anonymous=True,
        type='quiz',
        correct_option_id=correct_option_id,
        explanation=f'Правильный ответ: {explanation}',
        protect_content=True,
    )


async def send_morning_hello():
    month = str(dt.datetime.today().month)
    day = dt.datetime.today().day
    if day == 31:
        day_trinity = '10'
    else:
        day_trinity = str(math.ceil(day/3))
    avo_temp = const.RECOMMEND_TEMP[month][day_trinity]
    text_avo_temp = (
        f'Рекомендуемая температура газа после АВО:\n{avo_temp} град. Цельсия'
    )
    text_morning_hello = hello_generator()
    text_weather = request_weather()
    message = '{}\n{}\n{}'.format(
        text_morning_hello,
        text_weather,
        text_avo_temp,
    )
    await bot.send_message(chat_id=CHAT_ID, text=message)


async def send_evening_hello():
    text_evening_hello = evening_hello_generator()
    text_weather = request_weather()
    message = '{}\n{}'.format(
        text_evening_hello,
        text_weather
    )
    await bot.send_message(chat_id=CHAT_ID, text=message)


async def send_morning_wish():
    now_day = dt.datetime.today().day
    if now_day == 1:
        text_month_plan = month_plan_generator()
    else:
        text_month_plan = ''
    message = '{}\n\n{}'.format(wish_generator(), text_month_plan)
    await bot.send_message(chat_id=CHAT_ID, text=message)


async def send_history_day():
    text_history_day = scrap_history_day()
    prefix = 'Доставайте чай, наливайте печенюшки'
    full_text = '{}\n\n{}'.format(prefix, text_history_day)
    await bot.send_message(
        chat_id=CHAT_ID,
        text=full_text,
        parse_mode=types.ParseMode.HTML
    )


async def send_apk_2_remainder():
    # в ответе функции second_apk_check приходит словарь
    check = second_level_apk_check().get('check')
    if check:
        today = second_level_apk_check().get('date')
        weekday = second_level_apk_check().get('weekday')
        text_today = f'Сегодня {today} число месяца, {weekday}.'
        message = '{}\n{}'.format(text_today, APK_2_REMAINDER)
        await bot.send_message(chat_id=CHAT_ID, text=message)


async def send_tu_theme():
    check = plan_tu_check().get('check')
    if check:
        list_tu = plan_tu_check().get('data')
        text = ''
        for theme in list_tu:
            text = '{}\n{}\n'.format(text, theme)
        message = (
            f'Сегодня по плану должна быть техучёба.\nТемы занятий:\n{text}'
        )
        await bot.send_message(chat_id=CHAT_ID, text=message)


def scheduler_jobs():
    # по будням в 15:00 отправляет заметку о сегодняшнем дне
    scheduler.add_job(
        send_history_day,
        'cron',
        day_of_week='mon-sun',
        hour=15,
        minute=0,
        timezone=const.TIME_ZONE
    )
    # по будням в 07:05 отправляет утреннее приветствие
    scheduler.add_job(
        send_morning_hello,
        'cron',
        day_of_week='mon-sun',
        hour=7,
        minute=00,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_evening_hello,
        'cron',
        day_of_week='mon-sun',
        hour=19,
        minute=00,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_morning_wish,
        'cron',
        day_of_week='mon-sun',
        hour=8,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_quiz_shedule,
        'cron',
        day_of_week='mon-sun',
        hour=10,
        minute=0,
        timezone=const.TIME_ZONE
    )
    # по будням проверяет дату и отправляет напоминание о 2-ом уровне АПК
    scheduler.add_job(
        send_apk_2_remainder,
        'cron',
        day_of_week='mon-fri',
        hour=10,
        minute=15,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_tu_theme,
        'cron',
        day_of_week='mon-sun',
        hour=8,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_vehicle_start_message,
        'cron',
        day_of_week='mon-thu',
        hour=16,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_vehicle_stop_message,
        'cron',
        day_of_week='mon-thu',
        hour=16,
        minute=30,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_vehicle_start_message,
        'cron',
        day_of_week='fri',
        hour=14,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_vehicle_stop_message,
        'cron',
        day_of_week='fri',
        hour=14,
        minute=30,
        timezone=const.TIME_ZONE
    )
    # scheduler.add_job(
    #   send_morning_hello,
    #   'interval',
    #   seconds=10,
    #   timezone=const.TIME_ZONE
    # )


async def on_startup(_):
    scheduler_jobs()


if __name__ == '__main__':
    scheduler.start()
    register_handlers_vehicle(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
