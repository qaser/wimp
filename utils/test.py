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


def word_conjugate(number):
    args = ['заявка', 'заявки', 'заявок']
    int_num = int(number)
    last_digit = int_num % 10
    last_two_digit = int_num % 100  # для проверки 11...14
    if last_digit == 1 and last_two_digit != 11:
        return f'{args[0]}'  # заявка
    if 1 < last_digit < 5 and last_two_digit not in range(11, 15):
        return f'{args[1]}'  # заявки
    return f'{args[2]}'  # заявок


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

LOCATIONS = [
    'КЦ-1,4',
    'КЦ-2,3',
    'КЦ-5,6',
    'КЦ-7,8',
    'КЦ-9,10',
    'ПТП',
]

# всего заказов техники
# количество заказов по видам техники

location_resume = {}
vehicle_resume = {}
previous_month = dt.datetime.today().month - 1


queryset = list(vehicles.find({'date': { '$gt': f"01.{previous_month}.2022" }}))
for loc in LOCATIONS:
    len_queryset = len(list(vehicles.find({'location': loc, 'date': { '$gt': f"01.{previous_month}.2022" }})))
    location_resume.update({loc: len_queryset})

sorted_locations = sorted(location_resume.items(), key=lambda kv: kv[1], reverse=True)

for veh in VEHICLES:
    len_queryset = len(list(vehicles.find({'vehicle': veh, 'date': { '$gt': f"01.{previous_month}.2022" }})))
    vehicle_resume.update({veh: len_queryset})

sorted_vehicles = sorted(vehicle_resume.items(), key=lambda kv: kv[1], reverse=True)


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


pipeline_date = [
    { '$match': { 'date': { '$gte': f"01.09.2022" } } },
    { '$group': { '_id': {'vehicle': '$vehicle', 'location': '$location'}, 'count': { '$sum': 1 } } },
    { '$group': {
            '_id': '$_id.vehicle',
            'locations': {
                "$push": {
                    "location": "$_id.location",
                    "count": "$count"
                }
            },
        }
    },
    { '$sort': { '_id': 1} }
]
queryset_date = vehicles.aggregate(pipeline_date)


text = (
    'Сегодня будет немного статистики за мой неполный рабочий месяц.\n'
    f'Всего мной обработано {sum_doc} {word_sum} на спец. технику.\n'
    f'Самое активное направление - {loc_max} ({loc_count_max} {word_loc}).\n'
    f'Самый популярный вид техники - {veh_max_1} ({veh_count_1} {word_veh_1}).\n'
    f'На втором месте - {veh_max_2} ({veh_count_2} {word_veh_2}).\n'
    f'Замыкает тройку - {veh_max_3} ({veh_count_3} {word_veh_3}).\n'
    f'Где-то в сторонке "рыдает" {veh_max_last} - {veh_count_last} {word_veh_last}.\n\n'
    'Но заявки - это одна сторона монеты, другая - подтверждение.\n'
    '58% из всего количества заявок были одобрены (эта информация может быть не точна).\n'
    'На этом всё. Ваш зануда.'
)

print(text)
