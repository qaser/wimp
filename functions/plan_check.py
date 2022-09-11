import datetime as dt
from datetime import datetime

from texts.pat import PAT, TU


def plan_tu_check():
    today_month = dt.datetime.today().month
    past_month = today_month - 1
    month_plan = TU.get(str(today_month))
    past_month_plan = TU.get(str(past_month))
    if past_month_plan == None:
        past_month_plan = {}
    if str(today_month) in TU.keys():
        today_date = dt.datetime.today().strftime('%d.%m.%Y')
        if today_date in month_plan.keys(): # на каждый месяц идёт словарь с датами
            return {
                'check': True,
                'data': month_plan.get(today_date),
                'plan': month_plan,
                'past_plan': past_month_plan,
            }
    return {
        'check': False,
        'data': '',
        'plan': month_plan,
        'past_plan': past_month_plan,
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
