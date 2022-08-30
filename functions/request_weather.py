import requests
import os
import utils.constants as const
from dotenv import load_dotenv

from functions.text_generators import weather_text_generator


load_dotenv()

TOKEN = os.getenv('YANDEX_WEATHER_TOKEN')

def request_weather():
    headers = {'X-Yandex-API-Key': TOKEN}
    url = f'{const.URL_WEATHER}lat={const.LAT_LYHMA}&lon={const.LON_LYHMA}&[lang={const.LANG_CODE}]'
    try:
        resp = requests.get(url=url, headers=headers).json()
        fact_temp = resp['fact']['temp']
        now_condition = resp['fact']['condition']
        fact_cond = const.CONDITIONS_WEATHER[resp['fact']['condition']]
        parts = resp['forecast']['parts']
        forecast_text = ''
        text_prefix = weather_text_generator(fact_temp, now_condition)
        for part in parts:
            day_part = const.DAY_PARTS[part['part_name']]
            temperature = part['temp_avg']
            condition = const.CONDITIONS_WEATHER[part['condition']]
            forecast_text = forecast_text + f'{day_part}: {temperature}\u2103 , {condition}. \n'
        now_text = (f'{text_prefix}'
                f' температура воздуха {fact_temp}\u2103 , {fact_cond}.')
        return '{}\n{}'.format(now_text, forecast_text)
    except:
        return ('С погодой какие-то непонятки. Кто-то не поделился данными. Поэтому советую никуда не ходить.\n\n'
                'Ладно, можете по ссылке посмотреть https://yandex.ru/pogoda/lykhma')

request_weather()
