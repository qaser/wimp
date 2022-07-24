# TODO сделать отправку стикеров

import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

from functions.text_generators import hello_generator, wish_generator
from functions.request_weather import request_weather
from functions.scrap_history_day import scrap_history_day
from functions.second_level_apk_check import second_level_apk_check
import utils.constants as const
from texts.apk import APK_2_REMAINDER


load_dotenv()


scheduler = AsyncIOScheduler()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
# CHAT_ID = os.getenv('CHAT_ID')  # чат КС-5,6
CHAT_ID = '-1001412759045'  # тестовый чат


logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d.%m.%y %H:%M:%S'
)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


async def send_morning_hello():
    text_morning_hello = hello_generator()
    text_weather = request_weather()
    message = '{}\n{}'.format(
        text_morning_hello,
        text_weather
        )
    await bot.send_message(chat_id=CHAT_ID, text=message)

async def send_morning_wish():
    message = wish_generator()
    await bot.send_message(chat_id=CHAT_ID, text=message)


async def send_history_day():
    text_history_day = scrap_history_day
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


def scheduler_jobs():
    # по буням в 15:00 отправляет заметку о сегодняшнем дне
    # scheduler.add_job(
    #     send_history_day,
    #     'cron',
    #     day_of_week='mon-fri',
    #     hour=15,
    #     minute=0,
    #     timezone=const.TIME_ZONE
    # )
    # по будням в 06:45 отправляет утреннее приветствие
    scheduler.add_job(
        send_morning_hello,
        'cron',
        day_of_week='mon-fri',
        hour=7,
        minute=0,
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
    scheduler.add_job(send_morning_wish, 'interval', seconds=10, timezone=const.TIME_ZONE)


async def on_startup(_):
    scheduler_jobs()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
