from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def close_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(
        text=f'Закрыть',
        callback_data='close'
    )
    return kb.as_markup()


def unit_choose_kb(unit) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    if unit == 'БПМ':
        kb.button(text='ГПА', callback_data='choose_gpa')
        kb.button(text='МХ', callback_data='choose_mh')
        kb.button(text='Склад ГСМ', callback_data='choose_gsm')
    elif unit == 'МХ':
        kb.button(text='ГПА', callback_data='choose_gpa')
        kb.button(text='БПМ', callback_data='choose_bpm')
        kb.button(text='Склад ГСМ', callback_data='choose_gsm')
    elif unit == 'ГСМ':
        kb.button(text='ГПА', callback_data='choose_gpa')
        kb.button(text='БПМ', callback_data='choose_bpm')
        kb.button(text='МХ', callback_data='choose_mh')
    elif unit == 'ГПА':
        kb.button(text='БПМ', callback_data='choose_bpm')
        kb.button(text='МХ', callback_data='choose_mh')
        kb.button(text='Склад ГСМ', callback_data='choose_gsm')
    kb.button(text='< Закрыть >', callback_data='close')
    kb.adjust(2)
    return kb.as_markup()
