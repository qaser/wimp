# TODO сделать отправку стикеров

import logging
import os
import datetime as dt
import pymongo
import gridfs

from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

from functions.text_generators import evening_hello_generator, hello_generator, wish_generator, month_plan_generator
from functions.request_weather import request_weather
from functions.scrap_history_day import scrap_history_day
from functions.second_level_apk_check import second_level_apk_check
from functions.plan_check import plan_pat_check, plan_tu_check
import utils.constants as const
from texts.apk import APK_2_REMAINDER
from texts.initial import INITIAL_TEXT, FINAL_TEXT, HELP_TEXT, KPB_TEXT, NS_TEXT


load_dotenv()

# Create the client
client = pymongo.MongoClient('localhost', 27017)
# Connect to our database
db = client['gks_bot_db']
fs = gridfs.GridFS(db)
# Fetch our series collection
key_rules = db['key_rules']
quiz = db['quiz']

scheduler = AsyncIOScheduler()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
# CHAT_ID = os.getenv('CHAT_ID')  # чат КС-5,6
CHAT_ID = '-1001412759045'  # тестовый чат


logging.basicConfig(
    filename='gks56_bot.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d.%m.%y %H:%M:%S'
)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message:types.Message):
    await bot.send_message(message.chat.id, text=INITIAL_TEXT)


@dp.message_handler(commands=['help'])
async def help_handler(message:types.Message):
    await bot.send_message(message.chat.id, text=f'{message.from_user.full_name}{HELP_TEXT}')
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['pravila'])
async def pravila_handler(message:types.Message):
    photos = fs.find({'unit': 'kpb'})
    for photo in photos:
        await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_message(message.chat.id, text=KPB_TEXT)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['vnimanie'])
async def vnimanie_handler(message:types.Message):
    photos = fs.find({'unit': 'ns'})
    for photo in photos:
        await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_message(message.chat.id, text=NS_TEXT)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['service'])
async def service_handler():
    await bot.send_message(chat_id=CHAT_ID, text='Я отключусь пока, получаю обновление. Если к утру меня не будет, то вы знаете кто виноват.')


@dp.message_handler(commands=['hello'])
async def hello_handler():
    await bot.send_message(chat_id=CHAT_ID, text='Я снова с вами! Такое чувство, будто что-то поменялось.')


async def send_morning_hello():
    text_morning_hello = hello_generator()
    text_weather = request_weather()
    message = '{}\n{}'.format(
        text_morning_hello,
        text_weather
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
    await bot.send_message(chat_id=CHAT_ID, text=text_history_day, parse_mode=types.ParseMode.HTML)


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
    print(check)
    if check:
        list_tu = plan_tu_check().get('data')
        text = ''
        for theme in list_tu:
            text = '{}\n{}\n'.format(text, theme)
        message = f'Сегодня по плану должна быть техучёба.\nТемы занятий:\n{text}'
        await bot.send_message(chat_id=CHAT_ID, text=message)


def scheduler_jobs():
    # по будням в 15:00 отправляет заметку о сегодняшнем дне
    # scheduler.add_job(
    #     send_history_day,
    #     'cron',
    #     day_of_week='mon-fri',
    #     hour=15,
    #     minute=0,
    #     timezone=const.TIME_ZONE
    # )
    # по будням в 07:05 отправляет утреннее приветствие
    scheduler.add_job(
        send_morning_hello,
        'cron',
        day_of_week='mon-fri',
        hour=7,
        minute=20,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_evening_hello,
        'cron',
        day_of_week='mon-fri',
        hour=19,
        minute=20,
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
    # scheduler.add_job(cmd_random, 'interval', seconds=5, timezone=const.TIME_ZONE)


async def on_startup(_):
    scheduler_jobs()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
