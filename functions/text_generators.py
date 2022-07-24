import datetime as dt

from texts.mornings import MORNING_HELLO, MORNING_WISHES
from texts.weather import (WEATHER_COLD_PREFIX, WEATHER_HOT_PREFIX,
                           WEATHER_MAIN, WEATHER_RAIN_PREFIX)
from utils.random_list_elem import random_list_elem


def hello_generator():
    rand_num = random_list_elem(MORNING_HELLO)
    morning_text = MORNING_HELLO[rand_num]
    return morning_text


def wish_generator():
    rand_num = random_list_elem(MORNING_WISHES)
    day_week = dt.datetime.today().weekday()
    text_wish = MORNING_WISHES[rand_num]
    if day_week < 5:
        return text_wish
    return '{}\n{}'.format(text_wish, '\nP.S. Дневная смена не забудьте про ГиперФлоу.')


def weather_text_generator(temperature, condition):
    check_rain = condition.find('rain')
    prefix = ''
    if temperature >= 28:
        prefix = WEATHER_HOT_PREFIX[random_list_elem(WEATHER_HOT_PREFIX)]
    if temperature <= -29:
        prefix = WEATHER_COLD_PREFIX[random_list_elem(WEATHER_COLD_PREFIX)]
    if check_rain != -1:
        prefix = WEATHER_RAIN_PREFIX[random_list_elem(WEATHER_RAIN_PREFIX)]
    forecast_text = WEATHER_MAIN[random_list_elem(WEATHER_MAIN)]
    full_text = '{}\n{}'.format(prefix, forecast_text)
    return full_text
