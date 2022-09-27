from cgitb import reset
import datetime as dt
import collections, operator
import pprint

import pymongo
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
# from config.telegram_config import MY_TELEGRAM_ID

client = pymongo.MongoClient('localhost', 27017)
db = client['gks_bot_db']
# fs = gridfs.GridFS(db)
quiz = db['quiz']
users = db['users']
vehicles = db['vehicles']
offers = db['offers']


VEHICLES = [
    'Автокран 25тн',
    'Автокран LIEBHERR',
    'Амкадор',
    'Бортовая',
    'Бортовая - "кислородка"',
    'Бульдозер гусеничный',
    'Водокачка',
    'Вышка',
    'ГАЗ-34031 "Газушка"',
    'Длиномер',
    'ППУА',
    'ПРМ',
    'ПРМ с фаркопом',
    'Самосвал',
    'Трубовоз',
    'УМП',
    'Экскаватор гусеничный',
    'Экскаватор колёсный',
]

# всего заказов техники
# количество заказов по видам техники

result = {}

for v in VEHICLES:
    len_queryset = len(list(vehicles.find({'vehicle': v})))
    result.update({v: len_queryset})

sorted_x = sorted(result.items(), key=lambda kv: kv[1], reverse=True)

pprint.pprint(sorted_x)


pipeline_sum = [
    {'$group': {'_id': '$None', 'count': {'$sum': 1}}},
]

today_date = dt.datetime.today().strftime('%d.%m.%Y')
queryset = vehicles.find({'date': today_date})
pipeline = [
    {'$match': {'date': '15.09.2022'}},
    {'$group': {'_id': '$location', 'count': {'$sum': 1}}},
]

text_prefix = 'Добрый день. Напоминаю о возможности сделать заявку на технику.'
text_suffix = '/zayavka'
pipeline = [
    {'$match': {'date': '25.09.2022'}},
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
print(message)

text = (
    'Сегодня будет немного статистики за мой неполный рабочий месяц.\n'
    'Всего мной обработано 105 заявок на спец. технику.\n'
    'Самое активное направление - КЦ-2,3 (35 заявок).\n'
    'Самый популярный вид техники - Автокран 25тн (35 заявок).\n'
    'На втором месте - Самосвал (30 заявок).\n'
    'Замыкает тройку - Бортовая (15 заявок).\n'
    'Где-то в сторонке "рыдает" Трубовоз - 0 заявок.\n\n'
    'Но заявки - это одна сторона монеты, другая - подтверждение.\n'
    '58% из всего количества заявок были одобрены (эта информация может быть не точна).\n'
    'На этом всё. Ваш зануда.'
)
