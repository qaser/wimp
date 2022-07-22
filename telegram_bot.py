import logging
import os

from aiogram import Bot, Dispatcher, executor, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

from functions.hello_generator import hello_generator
from functions.request_weather import request_weather
from functions.scrap_history_day import scrap_history_day
from functions.wish_generator import wish_generator
import utils.constants as const


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
    await bot.send_message(chat_id=CHAT_ID, text=text_morning_hello)


async def send_morning_wish():
    text_morning_wish = wish_generator()
    await bot.send_message(chat_id=CHAT_ID, text=text_morning_wish)


async def send_morning_wish_weekend():
    text_morning_wish = '{}\n{}'.format(wish_generator(), 'Дневная смена не забудьте про ГиперФлоу.')
    await bot.send_message(chat_id=CHAT_ID, text=text_morning_wish)


async def send_weather():
    text_weather = request_weather()
    await bot.send_message(chat_id=CHAT_ID, text=text_weather)


async def send_history_day():
    text_history_day = scrap_history_day
    await bot.send_message(chat_id=CHAT_ID, text=text_history_day, parse_mode=types.ParseMode.HTML)


def scheduler_jobs():
    scheduler.add_job(
        send_weather,
        'cron',
        day_of_week='mon-sun',
        hour=7,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_history_day,
        'cron',
        day_of_week='mon-fri',
        hour=15,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_morning_hello,
        'cron',
        day_of_week='mon-fri',
        hour=6,
        minute=45,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_morning_wish,
        'cron',
        day_of_week='mon-fri',
        hour=8,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        send_morning_wish_weekend,
        'cron',
        day_of_week='sat-sun',
        hour=8,
        minute=0,
        timezone=const.TIME_ZONE
    )
    # scheduler.add_job(send_weather, 'interval', seconds=10, timezone=const.TIME_ZONE)


async def on_startup(_):
    scheduler_jobs()


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
