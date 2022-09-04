# TODO сделать отправку стикеров

import datetime as dt
import logging
import math
import os
import random
import time

import gridfs
import pymongo
from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

import utils.constants as const
from functions.plan_check import plan_tu_check, plan_pat_check
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

scheduler = AsyncIOScheduler()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')  # чат КС-5,6
# CHAT_ID = '-1001555422626'  # тестовый чат
CHAT_ID_TEST = '-1001555422626'  # тестовый чат


logging.basicConfig(
    filename='gks56_bot.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d.%m.%y %H:%M:%S'
)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


def insert_user_db(user):
    # user = message.from_user
    print(user)
    # print(users)
    check_user = users.find_one({'id': user.id})
    print(check_user)
    if check_user is None:
        users.insert_one({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'place_of_work': '',
        })
        # send_new_user_note()



async def send_new_user_note(message:types.Message):
    await bot.send_message(
        chat_id=CHAT_ID_TEST,
        text=f'Добавлен новый пользователь.'
    )


@dp.message_handler(commands=['test'])
async def send_poll(message:types.Message):
    user = message.from_user
    insert_user_db(user)
    global this_poll
    this_poll = await poll()


# @dp.poll_answer_handler()
# async def handle_poll_answer(quiz_answer: types.PollAnswer):
#     print(quiz_answer)
#     print(this_poll.poll.id)
#     await bot.send_poll(
#         chat_id=quiz_answer.user.id,
#         question=f'Выберите время для {const.VEHICLES_1[quiz_answer.option_ids[0]]}',
#         options=const.VEHICLES_1,
#         type='regular',
#         allows_multiple_answers=True,
#         is_anonymous=False,
#     )
    # if this_quiz.poll.correct_option_id == quiz_answer:
    #     print('Правильно!')
    # else:
    #     print('Неправильно!')


async def poll():
    poll_1 = await bot.send_poll(
        chat_id=CHAT_ID_TEST,
        question='Выберите технику',
        options=const.VEHICLES_1,
        type='regular',
        allows_multiple_answers=True,
        is_anonymous=False,
    )
    return poll_1


@dp.message_handler(commands=['start'])
async def start_handler(message:types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(message.chat.id, text=INITIAL_TEXT)


@dp.message_handler(commands=['help'])
async def help_handler(message:types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(message.chat.id, text=f'{message.from_user.full_name}{HELP_TEXT}')
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['pravila'])
async def pravila_handler(message:types.Message):
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
async def vnimanie_handler(message:types.Message):
    insert_user_db(message.from_user)
    for root, dirs, files in os.walk('static/kpb_lite/'):
        for filename in files:
            file = f'static/ns/{filename}'
            with open(file, 'rb') as f:
                contents = f.read()
                await bot.send_photo(message.chat.id, photo=contents)
    await bot.send_message(message.chat.id, text=NS_TEXT)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['service'])
async def service_handler(message:types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(chat_id=CHAT_ID, text=SERVICE_TEXT)


@dp.message_handler(commands=['endservice'])
async def service_end_handler(message:types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(chat_id=CHAT_ID, text=SERVICE_END_TEXT)


@dp.message_handler(commands=['pat'])
async def pat_handler(message:types.Message):
    insert_user_db(message.from_user)
    text = plan_pat_check().get('data')
    full_text = f'Противоаварийная тренировка на КЦ-5,6 в этом месяце:\n\n{text}'
    await bot.send_message(message.chat.id, text=full_text)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['tu'])
async def pat_handler(message:types.Message):
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
    poll = quiz.find({'num': rand_num}).next()
    return poll


@dp.message_handler(commands=['menu'])
async def all_commands(message:types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)

@dp.message_handler(commands=['vopros'])
async def send_quiz(message:types.Message):
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
    text_avo_temp = f'Рекомендуемая температура газа после АВО:\n{avo_temp} град. Цельсия'
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
    await bot.send_message(chat_id=CHAT_ID, text=full_text, parse_mode=types.ParseMode.HTML)


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
        message = f'Сегодня по плану должна быть техучёба.\nТемы занятий:\n{text}'
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
    # scheduler.add_job(send_morning_hello, 'interval', seconds=10, timezone=const.TIME_ZONE)


async def on_startup(_):
    scheduler_jobs()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
