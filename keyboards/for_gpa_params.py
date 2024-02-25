import datetime as dt

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
import utils.constants as const


def main_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Новая запись', callback_data=f'inspect_new')
    kb.button(text='Сохраненные записи', callback_data='inspect_last')
    kb.button(text='Отмена', callback_data='close')
    kb.adjust(1)
    return kb.as_markup()


def num_gpa_menu(choose) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for gpa in const.GPA_NUMS:
        kb.button(text=f'{gpa}', callback_data=f'choose_{choose}_{gpa}')
    kb.adjust(2)
    kb.button(text='Отмена', callback_data='close')
    return kb.as_markup()


def params_menu(gpa_num, params) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for param in params:
        kb.button(text=f'{const.GPA_PARAMS[param]}', callback_data=f'params_{gpa_num}_{param}')
    kb.adjust(2)
    kb.button(text='< Завершить >', callback_data=f'params_{gpa_num}_stop')
    return kb.as_markup()


def close_menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Отмена', callback_data='close')
    return kb.as_markup()
