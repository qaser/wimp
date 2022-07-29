from datetime import datetime
import datetime as dt

from texts.pat import PAT, TU

def plan_tu_check():
    today_month = dt.datetime.today().month
    if str(today_month) in TU.keys():
        today_date = dt.datetime.today().strftime('%d.%m.%Y')
        month_plan = TU.get(str(today_month))
        if today_date in month_plan.keys(): # на каждый месяц идёт словарь с датами
            return {
                'check': True,
                'data': month_plan.get(today_date)
            }
    return {
        'check': False,
        'data': ''
    }

def plan_pat_check():
    today_month = str(dt.datetime.today().month)
    if today_month in PAT.keys():
        return {
            'check': True,
            'data': PAT.get(today_month)
        }
    return {
        'check': False,
        'data': ''
    }
