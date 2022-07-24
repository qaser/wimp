"""
Функция проверяет число месяца и день недели.
Каждое 10, 20 и 30 число месяца (не выходной день).
Каждое число, кратное 9, если это пятница.
Каждое число, оканчивающаеся на 1, если это понедельник.
"""

import datetime as dt


def second_level_apk_check():
    today_date = dt.datetime.today().day
    day_week = dt.datetime.today().weekday()
    if (today_date == 9 or today_date == 19 or today_date == 29) and (day_week == 4):
        return {
            'check': True,
            'date': today_date,
            'weekday': 'пятница'
        }
    if (today_date == 10 or today_date == 20 or today_date == 30) and (day_week < 5):
        return {
            'check': True,
            'date': today_date,
            'weekday': 'отличный денёк'
        }
    if (today_date == 11 or today_date == 21 or today_date == 31) and (day_week == 0):
        return {
            'check': True,
            'date': today_date,
            'weekday': 'понедельник'
        }
    return {
        'check': False,
        'date': today_date,
        'weekday': ''
    }
