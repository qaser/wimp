import datetime as dt

import openai

from functions.plan_check import plan_pat_check
from texts.evening import EVENING_HELLO
from texts.mornings import MORNING_HELLO, MORNING_WISHES
from texts.pat import MONTH_TEXT, TU
from texts.weather import (WEATHER_COLD_PREFIX, WEATHER_HOT_PREFIX,
                           WEATHER_MAIN, WEATHER_RAIN_PREFIX)
from utils.random_list_elem import random_list_elem


def weather_text_generator(temperature, condition):
    check_rain = condition.find('rain')
    prefix = ''
    if temperature >= 25:
        prefix = WEATHER_HOT_PREFIX[random_list_elem(WEATHER_HOT_PREFIX)]
    if temperature <= -25:
        prefix = WEATHER_COLD_PREFIX[random_list_elem(WEATHER_COLD_PREFIX)]
    if check_rain != -1:
        prefix = WEATHER_RAIN_PREFIX[random_list_elem(WEATHER_RAIN_PREFIX)]
    forecast_text = WEATHER_MAIN[random_list_elem(WEATHER_MAIN)]
    full_text = '{}\n{}'.format(prefix, forecast_text)
    return full_text


def month_plan_generator():
    pat_check = plan_pat_check()
    text_tu = 'У меня отстутствует информация об учёбе'
    if pat_check.get('check'):
        text_pat = pat_check.get('data')
    else:
        text_pat = 'У меня отстутствует информация о ПАТ'
    date_month = str(dt.datetime.today().month)
    if date_month in TU:
        tu_dict = TU.get(date_month)
        text_tu = ''
        for day in tu_dict.keys():
            text_tu = text_tu + day + '\n'
    rand_num = random_list_elem(MONTH_TEXT)
    text_prefix = MONTH_TEXT[rand_num]
    full_text = '{}\n\nПротивоаварийная тренировка в этом месяце:\n{}\n\nДаты технической учёбы:\n{}'.format(text_prefix, text_pat, text_tu)
    return full_text
