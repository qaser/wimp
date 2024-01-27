import re
import datetime as dt
import time
from dateutil.relativedelta import relativedelta

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
            pass
            # составить отчёт
    else:
        pass
        # составить отчёт
