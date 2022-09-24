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
# количество заказв по видам техники

# result = {}

# for v in VEHICLES:
#     len_queryset = len(list(vehicles.find({'vehicle': v})))
#     result.update({v: len_queryset})

# sorted_x = sorted(result.items(), key=lambda kv: kv[1], reverse=True)
# # sorted_dict = collections.OrderedDict(sorted_x)

# # print(result)
# pprint.pprint(sorted_x)


pipeline = [
    {'$group': {'_id': '$vehicle', 'count': {'$sum': 1}}},
    {'$sort': {'count': -1}}
]

res = vehicles.aggregate(pipeline)

for document in res:
       print(document)
