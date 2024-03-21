import ast
import datetime as dt
from io import BytesIO
import time

import certifi
import pycurl
from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery, Message
from bson.objectid import ObjectId

import keyboards.for_gid as kb
from config.bot_config import bot
from config.gid_config import MY_GID_ID
from config.mongo_config import auth_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from utils.constants import HEADERS

router = Router()

URL = "https://app.gid.ru/auth/realms/gid/protocol/openid-connect/token"
ADD_HEADERS = [
    'Accept: */*',
    'Content-Type: application/x-www-form-urlencoded',
    'Referer: https://web.gid.ru/',
]


async def refresh_token_func():
    users = list(auth_gid.find({'automatization': True}))
    await bot.send_message(ADMIN_TELEGRAM_ID, 'Запуск задачи обновления токена')
    for user in users:
        time.sleep(5)
        username = user['username']
        refresh_token = user.get('refresh_token')
        data = {'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'client_id': 'webapp'}
        data_text = ''
        for key, value in data.items():
            data_text = f'{data_text}{key}={value}&'
        data_text = data_text[:-1]
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, URL)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CAINFO, certifi.where())
        c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS)
        c.setopt(c.POST, 1)
        c.setopt(c.TIMEOUT_MS, 10000)
        c.setopt(c.POSTFIELDS, data_text)
        c.perform()
        resp_code = c.getinfo(c.RESPONSE_CODE)
        body = buffer.getvalue()
        body_str = body.decode('utf-8')
        resp_data = ast.literal_eval(body_str)  # перевод строки в словарь
        c.close()
        if resp_code == 200:
            gid_id = user['gid_id']
            auth_gid.update_one(
                {'gid_id': gid_id},
                {'$set': {
                    'datetime': dt.datetime.now(),
                    'access_token': resp_data['access_token'],
                    'refresh_expires_in': resp_data['refresh_expires_in'],
                    'expires_in': resp_data['expires_in'],
                    'refresh_token': resp_data['refresh_token'],
                    'token_type': resp_data['token_type'],
                    'id_token': resp_data['id_token'],
                    'not_before_policy': resp_data['not-before-policy'],
                    'session_state': resp_data['session_state'],
                    'scope': resp_data['scope'],
                }},
                upsert=True
            )
            await bot.send_message(
                ADMIN_TELEGRAM_ID,
                f'Токен пользователя "{username}" успешно обновлен'
            )
        else:
            await bot.send_message(
                chat_id=ADMIN_TELEGRAM_ID,
                text=f'Ошибка обновления токена: {resp_code}\n{body_str}\n{username}',
            )


async def choose_user(message, handler):
    users_list = list(auth_gid.find({}))
    await message.answer(
        'Выберите пользователя',
        parse_mode=ParseMode.HTML,
        reply_markup=kb.users_menu(users_list, handler),
    )


@router.callback_query(F.data.startswith('auth-get_'))
async def get_users_tokens(callback: CallbackQuery):
    await callback.message.delete()
    _, id = callback.data.split('_')
    tokens = auth_gid.find_one({'_id': ObjectId(id)})
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text='Access_token')
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=tokens['access_token'])
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text='Refresh_token')
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=tokens['refresh_token'])
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text='CSRF')
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=tokens['csrf'])


@router.callback_query(F.data.startswith('auth-auto_'))
async def set_users_automatization(callback: CallbackQuery):
    await callback.message.delete()
    _, id = callback.data.split('_')
    user = auth_gid.find_one({'_id': ObjectId(id)})
    user_state = user.get('automatization')
    username = user['username']
    if user_state is False or user_state is None:
        await bot.send_message(
            chat_id=ADMIN_TELEGRAM_ID,
            text=f'Автоматизация для пользователя "{username}" выключена.\nХотите включить?',
            reply_markup=kb.yes_or_no(id, 'disabled'),
        )
    else:
        await bot.send_message(
            chat_id=ADMIN_TELEGRAM_ID,
            text=f'Автоматизация для пользователя "{username}" включена.\nХотите выключить?',
            reply_markup=kb.yes_or_no(id, 'enabled'),
        )


@router.callback_query(F.data.startswith('auto_'))
async def confirm_automatization(callback: CallbackQuery):
    await callback.message.delete()
    _, choose, id = callback.data.split('_')
    if choose == 'yes':
        auth_gid.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'automatization': True}}
        )
    elif choose == 'no':
        auth_gid.update_one(
            {'_id': ObjectId(id)},
            {'$set': {'automatization': False}}
        )
