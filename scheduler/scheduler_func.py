import datetime as dt
import math

import utils.constants as const
from config.bot_config import bot
from config.telegram_config import CHAT_ID
from functions.plan_check import plan_tu_check
from functions.request_weather import request_weather
from functions.second_level_apk_check import second_level_apk_check
from functions.text_generators import month_plan_generator
from texts.apk import APK_2_REMAINDER


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
