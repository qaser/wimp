import re
import datetime as dt
import time
from math import ceil
from dateutil.relativedelta import relativedelta
from openpyxl import load_workbook

import keyboards.for_report as kb
import utils.pipelines as pipeline

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import AiogramError

from config.telegram_config import CHAT_ID, ADMIN_TELEGRAM_ID, MESSAGE_THREAD_ID
from config.mongo_config import tanks, oil_actions, oil_reports
from pymongo.errors import PyMongoError
from utils import constants as const
from config.bot_config import bot


router = Router()


@router.message(Command('report'))
async def oil_report(message: Message):
    await message.delete()
    await message.answer(
        'Выберите отчётный месяц',
        reply_markup=kb.month_menu()
    )


@router.callback_query(F.data.startswith('report_'))
async def get_month(call: CallbackQuery):
    _, year, month = call.data.split('_')
    await call.message.edit_text(
        text='Выберите тип отчёта:',
        reply_markup=kb.report_type_menu(year, month),
    )


@router.callback_query(F.data.startswith('type_'))
async def get_report_type(call: CallbackQuery):
    _, year, month, report_type = call.data.split('_')
    start_date = dt.datetime(int(year), int(month), 1)
    end_date = start_date + relativedelta(months=1)
    if report_type == 'final':
        check_report = oil_reports.find_one(
            {
                'type': 'final',
                'date': {'$gte': start_date, '$lt': end_date}
            }
        )
        if check_report is not None:
            await call.message.edit_text(
                text=('Итоговый отчёт для данного месяца уже существует.\n'
                      'Хотите составить новый итоговый отчёт вместо старого?'),
                reply_markup=kb.report_yes_no(year, month, report_type),
            )
        else:
            old_last_updates = list_old_data(start_date, end_date)
            print(old_last_updates)
            if  len(old_last_updates) == 0:
                await call.message.edit_text(
                    text=('Будет составлен итоговый отчёт за '
                          f'{const.MONTH_NAMES[month]} месяц.\nПродолжить?'),
                    reply_markup=kb.report_yes_no(year, month, report_type),
                )
            else:
                tanks_text = ''
                for tank in old_last_updates:
                    tanks_text = f'{tanks_text}{tank},\n'
                await call.message.edit_text(
                    text=('Для следующих ёмкостей давно не обновлялись данные:\n'
                          f'{tanks_text}\nДля формирования точного отчёта рекомендую '
                          'актуализировать данные по этим объектам.\n'
                          'Всё равно хотите продолжить?'),
                    reply_markup=kb.report_yes_no(year, month, report_type),
                )
    else:
        await call.message.edit_text('Данная функция в разработке')


@router.callback_query(F.data.startswith('exec_'))
async def get_report(call: CallbackQuery):
    _, year, month, report_type = call.data.split('_')
    start_date = dt.datetime(int(year), int(month), 1)
    end_date = start_date + relativedelta(months=1)
    last_report_date = start_date - relativedelta(months=1)
    wb = load_workbook('./static/oil_reports/oil_report_template.xlsx')
    last_report = oil_reports.find_one(
        {
            'year': last_report_date.year,
            'month': last_report_date.month,
            'type': report_type
        }
    )
    current_tanks = list(tanks.find({}))
    last_volumes = last_report['volumes_after']
    # заполнение параметрами прошлого месяца
    for tank, volumes in last_volumes.items():
        # wb['Цех5,6']['C8']
        wb[const.EXCEL_COORDINATES[tank][0]][const.EXCEL_COORDINATES[tank][1]] = volumes[0]
        if tank.split('_')[0] == 'ГПА':
            wb[const.EXCEL_COORDINATES[tank][0]][const.EXCEL_COORDINATES[tank][2]] = volumes[1]
    # заполнение параметрами текущего месяца
    for tank_obj in current_tanks:
        tank = f'{tank_obj["type"]}_{tank_obj["num"]}_{tank_obj["tank"]}'
        wb[const.EXCEL_COORDINATES[tank][0]][const.EXCEL_COORDINATES[tank][3]] = ceil(tank_obj['cur_volume'] * 0.88)
        if tank_obj['type'] == 'ГПА':
            if tank_obj['tank'] == 'Н' and tank_obj['is_work'] is True:
                ms_volume = 1870
            elif tank_obj['tank'] == 'Н' and tank_obj['is_work'] is False:
                ms_volume = 768
            else:
                ms_volume = 618
            wb[const.EXCEL_COORDINATES[tank][0]][const.EXCEL_COORDINATES[tank][4]] = ms_volume
    # заполнение параметрами расхода ГПА
    pipeline = [
        {'$match': {'date': {'$gte': start_date, '$lt': end_date}, 'action': 'outlay'}},
        {'$group':{'_id': '$source_id', 'sum':{'$sum':'$cost'}}}
    ]
    outlays = oil_actions.aggregate(pipeline)
    for obj in outlays:
        tank_obj = tanks.find_one({'_id': obj['_id']})
        tank = f'{tank_obj["type"]}_{tank_obj["num"]}_{tank_obj["tank"]}'
        wb[const.EXCEL_COORDINATES[tank][0]][const.EXCEL_COORDINATES[tank][5]] = obj['sum']
    wb.save(f'./static/oil_reports/{month}_{year}.xlsx')
    await call.message.delete()


def list_old_data(start_date, end_date):
    queryset = tanks.find(
        {
            '$and': [
                {'last_update': {'$gt': end_date}},
                {'last_update': {'$lte': start_date}}
            ]
        }
    )
    tanks_list = list(queryset) if queryset is not None else []
    if len(tanks_list) != 0:
        res = [tank['description'] for tank in tanks_list]
        return res
    return []
