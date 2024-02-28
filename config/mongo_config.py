import pymongo
from aiogram.fsm.storage.base import BaseStorage


# Create an instance of the MongoDB client
client = pymongo.MongoClient('localhost', 27017)
db = client['gks_bot_db']
gid_db = client['gid_db']

# коллекции для масла и обходов
users = db['users']
tanks = db['tanks']
oil_actions = db['oil_actions']
oil_reports = db['oil_reports']
gpa_params = db['gpa_params']

# коллекциии для ГИДа
auth_gid = gid_db['auth_gid']
users_gid = gid_db['users']
courses_gid = gid_db['courses']
quiz_gid = gid_db['quiz']
buffer_gid = gid_db['buffer']


'''
структура хранения данных о курсах
    'course_id': айди курса (items.раздел.items.id)
    'lessons': [] список айди уроков в курсе
    'is_complete' true/false

структура хранения gpa_params
    'user_id':
    'date'
    'gpa_num':
    'params': {
        fsn
        fun
        mbd
        fsd
        mbn
        rso
        dst
        dmn
    }

структура хранения данных о масле
    'type' - это ГПА, МХ, БПМ, ГСМ, АВТО или безвозвратные потери (расход)
    'num' - это станционный номер
    'tank' - это тип бака (Д, Н) или номер бака
    'cur_volume' - текущий уровень масла
    'last_update' - последнее изменение
    'calibration' - тарировка бака
    'description' - описание бака
    'is_work' - в каком состоянии на данный момент находится Оборудование
'''

'''
структура хранения данных об отчетах
    'type' - тип отчета, промежуточный или окончательный (final, current)
    'date' - это дата формирования отчета
    'volumes_before' - это словарь с данными уровней за прошлый период
    'volumes_after' - это словарь с данными уровней на текущий момент
'''

'''
это данные о закачке/скачке
    date, дата записи
    action, (upload, download, outlay)
    in_tank, id первого резервуара масла
    out_tank, id второго резервуара масла
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


'''
два сценария:
    1. Скачка - перекачка - закачка
    2. актуализация уровня масла
'''
