import asyncio
import logging

from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers.collect_energy import collect_energy_daily, transfer_power

from handlers.get_posts import send_emotion
import utils.constants as const
from config.bot_config import bot, dp
from handlers import gid_auth, gpa_params, oil, report, service
from handlers.get_courses import get_courses


@dp.message(Command('reset'))
async def cmd_reset(message: Message, state: FSMContext):
    await message.delete()
    await state.clear()
    await message.answer('Ошибки и состояния сброшены')


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
    scheduler.add_job(
        transfer_power,
        'cron',
        day_of_week='mon-sun',
        hour=3,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        get_courses,
        'cron',
        day_of_week='mon-sun',
        hour=12,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        collect_energy_daily,
        'cron',
        day_of_week='mon-sun',
        hour=21,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        collect_energy_daily,
        'cron',
        day_of_week='mon-sun',
        hour=22,
        minute=0,
        timezone=const.TIME_ZONE
    )
    scheduler.add_job(
        collect_energy_daily,
        'cron',
        day_of_week='mon-sun',
        hour=23,
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
