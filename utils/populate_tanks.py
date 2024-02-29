import datetime as dt
import os

import pymongo

client = pymongo.MongoClient('localhost', 27017)
# Connect to our database
db = client['gks_bot_db']
tanks = db['tanks']
oil_actions = db['oil_actions']


# pipeline = [
#     {'$match': {
#         'date': {'$gte': dt.datetime(2024, 1, 1), '$lt': dt.datetime(2024, 1, 31)},
#         'action': 'outlay'
#     }},
#     {'$group':{'_id': '$source_id', 'sum':{'$sum':'$cost'}}}
# ]
pipeline = [
    {'$match': {'date': {'$gte': dt.datetime(2024, 1, 1), '$lt': dt.datetime(2024, 1, 31)}, 'action': 'upload'}},
    {'$group':{'_id': '$target_id', 'sum':{'$sum':'$cost'}, 'source': {'$push': '$source_id'}}}
]

res = oil_actions.aggregate(pipeline)
for i in res:
    print(i)

# TANKS = [
#     {
#         'type': 'ГПА',
#         'num': '52',
#         'tank': 'Д',
#         'cur_volume': 276,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 52',
#         'is_work': True,
#     },
#     {
#         'type': 'ГПА',
#         'num': '52',
#         'tank': 'Н',
#         'cur_volume': 1180,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 52',
#         'is_work': True,
#     },
#     {
#         'type': 'ГПА',
#         'num': '53',
#         'tank': 'Д',
#         'cur_volume': 256,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 53',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '53',
#         'tank': 'Н',
#         'cur_volume': 2225,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 53',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '54',
#         'tank': 'Д',
#         'cur_volume': 294,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 54',
#         'is_work': True,
#     },
#     {
#         'type': 'ГПА',
#         'num': '54',
#         'tank': 'Н',
#         'cur_volume': 1170,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 54',
#         'is_work': True,
#     },
#     {
#         'type': 'ГПА',
#         'num': '55',
#         'tank': 'Д',
#         'cur_volume': 266,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 55',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '55',
#         'tank': 'Н',
#         'cur_volume': 2160,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 55',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '61',
#         'tank': 'Д',
#         'cur_volume': 235,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 61',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '61',
#         'tank': 'Н',
#         'cur_volume': 2225,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 61',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '62',
#         'tank': 'Д',
#         'cur_volume': 215,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 62',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '62',
#         'tank': 'Н',
#         'cur_volume': 2275,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 62',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '63',
#         'tank': 'Д',
#         'cur_volume': 325,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 63',
#         'is_work': True,
#     },
#     {
#         'type': 'ГПА',
#         'num': '63',
#         'tank': 'Н',
#         'cur_volume': 1210,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 63',
#         'is_work': True,
#     },
#     {
#         'type': 'ГПА',
#         'num': '64',
#         'tank': 'Д',
#         'cur_volume': 333,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 64',
#         'is_work': True,
#     },
#     {
#         'type': 'ГПА',
#         'num': '64',
#         'tank': 'Н',
#         'cur_volume': 1190,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 64',
#         'is_work': True,
#     },
#     {
#         'type': 'ГПА',
#         'num': '65',
#         'tank': 'Д',
#         'cur_volume': 285,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Маслобак двигателя ГПА 65',
#         'is_work': False,
#     },
#     {
#         'type': 'ГПА',
#         'num': '65',
#         'tank': 'Н',
#         'cur_volume': 2175,
#         'last_update': '',
#         'calibration': 5,
#         'description': 'Маслобак нагнетателя ГПА 65',
#         'is_work': False,
#     },
#     {
#         'type': 'МХ',
#         'num': '5',
#         'tank': '1',
#         'cur_volume': 0,
#         'last_update': '',
#         'calibration': 1.45,
#         'description': 'Маслобак №1 маслохозяйства КЦ-6',
#         'is_work': False,
#     },
#     {
#         'type': 'МХ',
#         'num': '5',
#         'tank': '2',
#         'cur_volume': 435,
#         'last_update': '',
#         'calibration': 1.45,
#         'description': 'Маслобак №2 маслохозяйства КЦ-6',
#         'is_work': False,
#     },
#     {
#         'type': 'МХ',
#         'num': '5',
#         'tank': '3',
#         'cur_volume': 1493,
#         'last_update': '',
#         'calibration': 1.45,
#         'description': 'Маслобак №3 маслохозяйства КЦ-6',
#         'is_work': False,
#     },
#     {
#         'type': 'МХ',
#         'num': '5',
#         'tank': '4',
#         'cur_volume': 1377,
#         'last_update': '',
#         'calibration': 1.45,
#         'description': 'Маслобак №4 маслохозяйства КЦ-6',
#         'is_work': False,
#     },
#     {
#         'type': 'ГСМ',
#         'num': '5',
#         'tank': '1',
#         'cur_volume': 0,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Емкость №1 склада ГСМ КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'ГСМ',
#         'num': '5',
#         'tank': '6',
#         'cur_volume': 0,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Емкость №6 склада ГСМ КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'ГСМ',
#         'num': '5',
#         'tank': '2',
#         'cur_volume': 0,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Емкость №2 склада ГСМ КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'ГСМ',
#         'num': '5',
#         'tank': '3',
#         'cur_volume': 17693,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Емкость №3 склада ГСМ КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'ГСМ',
#         'num': '5',
#         'tank': '4',
#         'cur_volume': 276,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Емкость №4 склада ГСМ КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'ГСМ',
#         'num': '5',
#         'tank': '5',
#         'cur_volume': 17408,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Емкость №5 склада ГСМ КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'БПМ',
#         'num': '2',
#         'tank': '1',
#         'cur_volume': 1638,
#         'last_update': '',
#         'calibration': 1.45,
#         'description': 'Емкость №1 БПМ№2 КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'БПМ',
#         'num': '2',
#         'tank': '2',
#         'cur_volume': 1840,
#         'last_update': '',
#         'calibration': 1.45,
#         'description': 'Емкость №2 БПМ№2 КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'БПМ',
#         'num': '3',
#         'tank': '1',
#         'cur_volume': 506,
#         'last_update': '',
#         'calibration': 1.45,
#         'description': 'Емкость №1 БПМ№3 КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'БПМ',
#         'num': '3',
#         'tank': '2',
#         'cur_volume': 506,
#         'last_update': '',
#         'calibration': 1.45,
#         'description': 'Емкость №2 БПМ№3 КЦ-5',
#         'is_work': False,
#     },
#     {
#         'type': 'АЦ',
#         'num': '5',
#         'tank': '1',
#         'cur_volume': 0,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Автоцистерна',
#         'is_work': False,
#     },
#     {
#         'type': 'КОЛОДЕЦ',
#         'num': '5',
#         'tank': '0',
#         'cur_volume': 0,
#         'last_update': '',
#         'calibration': 1,
#         'description': 'Безвозвратные потери масла',
#         'is_work': False,
#     },
# ]

# for tank in TANKS:
#     tanks.insert_one({
#         'type': tank.get('type'),
#         'num': tank.get('num'),
#         'tank': tank.get('tank'),
#         'cur_volume': tank.get('cur_volume'),
#         'last_update': tank.get('last_update'),
#         'calibration': float(tank.get('calibration')),
#         'description': tank.get('description'),
#         'is_work': tank.get('is_work')
#     })
