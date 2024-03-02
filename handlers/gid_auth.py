import ast
import datetime as dt
from io import BytesIO
import time

import certifi
import pycurl
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from config.bot_config import bot
from config.gid_config import MY_GID_ID
from config.mongo_config import auth_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from utils.constants import HEADERS

router = Router()


class Token(StatesGroup):
    token_value = State()
    csrf_value = State()
    refresh_token_value = State()
    session_value = State()


URL = "https://app.gid.ru/auth/realms/gid/protocol/openid-connect/token"
ADD_HEADERS = [
    'Accept: */*',
    'Content-Type: application/x-www-form-urlencoded',
    'Referer: https://web.gid.ru/',
]


async def refresh_token_func():
    users = list(auth_gid.find({}))
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
                chat_id=ADMIN_TELEGRAM_ID,
                text=f'Обновление токена удалось.\nПользователь {username}',
            )
        else:
            await bot.send_message(
                chat_id=ADMIN_TELEGRAM_ID,
                text=f'Обновление токена не удалось.\nОшибка {resp_code}\n{body_str}\n{username}',
            )


async def manual_auth_func(message: Message, state: FSMContext):
    await message.answer('Введите значение токена')
    await state.set_state(Token.token_value)


@router.message(Token.token_value)
async def get_token(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'gid_id': MY_GID_ID},
        {'$set': {'access_token': message.text, 'id_token': message.text}}
    )
    await message.answer('Введите значение CSRF')
    await state.set_state(Token.csrf_value)


@router.message(Token.csrf_value)
async def get_csrf(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'gid_id': MY_GID_ID},
        {'$set': {'csrf': message.text}}
    )
    await message.answer('Введите значение refresh_token')
    await state.set_state(Token.refresh_token_value)


@router.message(Token.refresh_token_value)
async def get_refresh_token(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'gid_id': MY_GID_ID},
        {'$set': {'refresh_token': message.text}}
    )
    await message.answer('Введите значение session')
    await state.set_state(Token.session_value)


@router.message(Token.session_value)
async def get_session(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'gid_id': MY_GID_ID},
        {'$set': {'session_state': message.text}}
    )
    await message.answer('Принято')


async def send_user_token():
    tokens = auth_gid.find_one({'gid_id': MY_GID_ID})
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text='Access_token')
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=tokens['access_token'])
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text='Refresh_token')
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=tokens['refresh_token'])
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text='CSRF')
    await bot.send_message(chat_id=ADMIN_TELEGRAM_ID, text=tokens['csrf'])
