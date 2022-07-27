from datetime import datetime
import datetime as dt

from texts.pat import PAT, TU

def plan_tu_check():
    today_date = dt.datetime.today().strftime('%d.%m.%Y')
    if today_date in TU.keys():
        return {
            'check': True,
            'data': TU.get(today_date)
        }
    return {
        'check': False,
        'data': ''
    }

def plan_pat_check():
    today_month = dt.datetime.today().month
    if today_month in PAT.keys():
        return {
            'check': True,
            'data': PAT.get(today_month)
        }
    return {
        'check': False,
        'data': ''

    }
