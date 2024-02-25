import datetime as dt

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import utils.constants as const


def month_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    cur_month = dt.datetime.now().month
    year = dt.datetime.now().year
    cur_month_name = const.MONTH_NAMES[str(cur_month)]
    if cur_month > 1:
        prev_month = cur_month - 1
        prev_month_name = const.MONTH_NAMES[str(prev_month)]
        kb.button(text=f'{prev_month_name}', callback_data=f'report_{year}_{prev_month}')
        kb.button(text=f'{cur_month_name}', callback_data=f'report_{year}_{cur_month}')
    else:
        prev_year = year - 1
        kb.button(text=f'декабрь ({prev_year})', callback_data=f'report_{prev_year}_12')
        kb.button(text=f'{cur_month_name}', callback_data=f'report_{year}_{cur_month}')
    kb.adjust(2)
    return kb.as_markup()


def report_type_menu(year, month) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='текущий', callback_data=f'type_{year}_{month}_current')
    kb.button(text='итоговый', callback_data=f'type_{year}_{month}_final')
    kb.adjust(2)
    return kb.as_markup()


def report_yes_no(year, month, report_type) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Да', callback_data=f'exec_{year}_{month}_{report_type}')
    kb.button(text='Нет', callback_data='close')
    kb.adjust(2)
    return kb.as_markup()
