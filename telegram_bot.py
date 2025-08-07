import asyncio
import logging

from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.collect_energy import collect_energy_daily

from handlers.get_posts import send_emotion
import utils.constants as const
from config.bot_config import bot, dp
from config.telegram_config import ADMIN_TELEGRAM_ID
from handlers import gid_auth, gpa_params, oil, report, service
from handlers.get_courses import get_courses
from subprocess import run


@dp.message(Command('reset'))
async def cmd_reset(message: Message, state: FSMContext):
    await message.delete()
    await state.clear()
    await message.answer('Ошибки и состояния сброшены')


@dp.message(Command('stop_spelljack'))
async def stop_bot2(message: Message):
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        await message.answer("⛔ Доступ запрещён")
        return
    run(["pm2", "stop", "spelljack"])  # Убедись, что такой процесс есть в pm2
    await message.answer("🛑 Бот Spelljack остановлен")


@dp.message(Command('start_spelljack'))
async def start_bot2(message: Message):
    if message.from_user.id == ADMIN_TELEGRAM_ID:
        await message.answer("⛔ Доступ запрещён")
        return
    run(["pm2", "start", "spelljack"])
    await message.answer("✅ Бот Spelljack запущен")


async def main():
    scheduler = AsyncIOScheduler()
    # scheduler.add_job(
    #     send_gratitude_func,
    #     'interval',
    #     minutes=30,
    #     timezone=const.TIME_ZONE
    # )
    # scheduler.add_job(
    #     send_emotion,
    #     'cron',
    #     day_of_week='mon-sun',
    #     hour=8,
    #     minute=0,
    #     timezone=const.TIME_ZONE
    # )
    # scheduler.add_job(
    #     get_posts_and_comments,
    #     'cron',
    #     day_of_week='mon-sun',
    #     hour=8,
    #     minute=0,
    #     timezone=const.TIME_ZONE
    # )
    # scheduler.add_job(
    #     get_courses,
    #     'cron',
    #     day_of_week='mon-sun',
    #     hour=12,
    #     minute=0,
    #     timezone=const.TIME_ZONE
    # )
    scheduler.add_job(
        collect_energy_daily,
        'cron',
        day_of_week='mon-sun',
        hour=10,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        collect_energy_daily,
        'cron',
        day_of_week='mon-sun',
        hour=15,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        collect_energy_daily,
        'cron',
        day_of_week='mon-sun',
        hour=20,
        minute=0,
        timezone=const.TIME_ZONE
    )

    scheduler.start()
    dp.include_router(service.router)
    dp.include_router(report.router)
    dp.include_router(gpa_params.router)
    dp.include_router(oil.router)
    dp.include_router(gid_auth.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        filename='logs_bot.log',
        level=logging.INFO,
        filemode='a',
        format='%(asctime)s - %(message)s',
        datefmt='%d.%m.%y %H:%M:%S',
        encoding='utf-8',
    )
    asyncio.run(main())
