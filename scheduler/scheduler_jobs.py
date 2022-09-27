from apscheduler.schedulers.asyncio import AsyncIOScheduler

import utils.constants as const
from handlers.quiz import send_quiz_shedule
from scheduler.scheduler_func import (send_apk_2_remainder, send_evening_hello,
                                      send_history_day, send_morning_hello,
                                      send_morning_wish, send_tu_theme, send_vehicle_notify)

scheduler = AsyncIOScheduler()


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
        send_vehicle_notify,
        'cron',
        day_of_week='mon-fri',
        hour=16,
        minute=0,
        timezone=const.TIME_ZONE
    )
    # scheduler.add_job(
    #   send_vehi_message,
    #   'interval',
    #   seconds=10,
    #   timezone=const.TIME_ZONE
    # )
