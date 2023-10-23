import pymongo
from aiogram.fsm.storage.base import BaseStorage


# Create an instance of the MongoDB client
client = pymongo.MongoClient('localhost', 27017)
db = client['gks_bot_db']
users = db['users']
tanks = db['tanks']
oil_actions = db['oil_actions']


'''
структура хранения данных о масле
    'type' - это ГПА, МХ, БПМ, ГСМ, АВТО или безвозвратные потери (расход)
    'num' - это станционный номер
    'tank' - это тип бака (Д, Н) или номер бака
    'cur_volume' - текущий уровень масла
    'last_update' - последнее изменение
'''

'''
это данные о закачке/скачке
    date, дата записи
    action, (upload, download, outlay)
    source_tank, id первого резервуара масла
    target_tank, id второго резервуара масла
    user_id, id пользователя
    before_vol, уровень до
    after_vol, уровень после
    cost, изменение уровня
'''

'''
шаблоны сообщений
ГПА62Д 225/253 МХ2
ГСМ5 106/145 АВТО
ГПА54Д 230
'''
