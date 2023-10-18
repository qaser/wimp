import logging

from aiogram import types
from aiogram.utils import executor

from config.bot_config import bot, dp
from config.mongo_config import users
from config.telegram_config import MY_TELEGRAM_ID
from handlers.service import register_handlers_service
from scheduler.scheduler_jobs import scheduler, scheduler_jobs
from texts.initial import FINAL_TEXT, HELP_TEXT, INITIAL_TEXT


logging.basicConfig(
    filename='logs_bot.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d.%m.%y %H:%M:%S',
    encoding='UTF-8'
)


async def on_startup(_):
    scheduler_jobs()


if __name__ == '__main__':
    scheduler.start()
    register_handlers_service(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
