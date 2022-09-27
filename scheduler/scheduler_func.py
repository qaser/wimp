import datetime as dt
import math

from aiogram import types

import utils.constants as const
from config.bot_config import bot
from config.mongo_config import vehicles
from config.telegram_config import CHAT_ID, CHAT_ID_GKS, MY_TELEGRAM_ID
from functions.plan_check import plan_tu_check
from functions.word_conjugate import word_conjugate
from functions.request_weather import request_weather
from functions.scrap_history_day import scrap_history_day
from functions.second_level_apk_check import second_level_apk_check
from functions.text_generators import (evening_hello_generator,
                                       hello_generator, month_plan_generator,
                                       wish_generator)
from texts.apk import APK_2_REMAINDER


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


async def send_vehicle_notify():
    date = dt.datetime.today().strftime('%d.%m.%Y')
    text_prefix = 'Добрый день. Напоминаю о возможности заявить технику.'
    text_suffix = '/zayavka'
    pipeline = [
        {'$match': {'date': date}},
        {'$group': {'_id': '$location', 'count': {'$sum': 1}}},
    ]
    res = list(vehicles.aggregate(pipeline))
    text = ''
    if len(res) != 0:
        for i in res:
            text = '{}{}\n'.format(text, i.get('_id'))
        final_text = f'На данный момент заявились:\n{text}'
    else:
        final_text = ''
    message = '{}\n{}\n{}'.format(text_prefix, final_text, text_suffix)
    await bot.send_message(chat_id=CHAT_ID_GKS, text=message)



async def send_vehicle_month_resume():
    WORDS = ['Не будет', 'Нету', 'Нет']
    denial_count = 0
    month_now = dt.datetime.today().month
    year_now = dt.datetime.today().year
    previous_month = str(month_now - 1) if str(month_now) != '1' else '12'
    year = year_now if str(month_now) != '1' else (int(year_now) - 1)
    for word in WORDS:
        len_queryset = len(list(vehicles.find(
            {
                'confirm_comment': word,
                'date': { '$gt': f'01.{previous_month}.{year}' }
            }
        )))
        denial_count = denial_count + len_queryset
    location_resume = {}
    vehicle_resume = {}
    queryset = list(vehicles.find(
        {'date': { '$gt': f'01.{previous_month}.{year}' }}
    ))
    for loc in const.LOCATIONS:
        len_queryset = len(list(vehicles.find(
            {
                'location': loc,
                'date': { '$gt': f'01.{previous_month}.{year}' }
            }
        )))
        location_resume.update({loc: len_queryset})
    sorted_locations = sorted(
        location_resume.items(),
        key=lambda kv: kv[1],
        reverse=True
    )
    for veh in const.VEHICLES:
        len_queryset = len(list(vehicles.find(
            {
                'vehicle': veh,
                'date': { '$gt': f'01.{previous_month}.{year}' }
            }
        )))
        vehicle_resume.update({veh: len_queryset})
    sorted_vehicles = sorted(
        vehicle_resume.items(),
        key=lambda kv: kv[1],
        reverse=True
    )
    sum_doc = len(queryset)
    word_sum = word_conjugate(sum_doc)
    loc_max, loc_count_max = sorted_locations[0]
    word_loc = word_conjugate(loc_count_max)
    veh_max_1, veh_count_1 = sorted_vehicles[0]
    word_veh_1 = word_conjugate(veh_count_1)
    veh_max_2, veh_count_2 = sorted_vehicles[1]
    word_veh_2 = word_conjugate(veh_count_2)
    veh_max_3, veh_count_3 = sorted_vehicles[2]
    word_veh_3 = word_conjugate(veh_count_3)
    veh_max_last, veh_count_last = sorted_vehicles[-1]
    word_veh_last = word_conjugate(veh_count_last)
    accept_percent = math.ceil(100 - ((denial_count / sum_doc) * 100))
    message = (
        'Сегодня будет немного статистики за мой неполный рабочий месяц.\n'
        f'Всего мной обработано {sum_doc} {word_sum} на спец. технику.\n'
        f'Самое активное направление - {loc_max} ({loc_count_max} {word_loc}).\n'
        'Самый популярный вид техники - '
        f'{veh_max_1} ({veh_count_1} {word_veh_1}).\n'
        f'На втором месте - {veh_max_2} ({veh_count_2} {word_veh_2}).\n'
        f'Замыкает тройку - {veh_max_3} ({veh_count_3} {word_veh_3}).\n'
        'Где-то в сторонке "рыдает" '
        f'{veh_max_last} - {veh_count_last} {word_veh_last}.\n\n'
        'Но заявки - это одна сторона монеты, другая - подтверждение.\n'
        f'{accept_percent}% из всего количества заявок были одобрены '
        '(эта информация может быть не точна).\n'
        'На этом всё. Ваш зануда.'
    )
    await bot.send_message(chat_id=CHAT_ID_GKS, text=message)
