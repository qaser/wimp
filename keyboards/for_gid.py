import datetime as dt

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import utils.constants as const


def users_menu(users_list, action) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for user in users_list:
        username = user['username']
        user_id = user['_id']
        kb.button(text=f'{username}', callback_data=f'auth-{action}_{user_id}')
    if action == 'set':
        kb.button(text='* Новый пользователь', callback_data=f'auth-{action}_new')
    kb.button(text='< Отмена >', callback_data='close')
    kb.adjust(1)
    return kb.as_markup()
