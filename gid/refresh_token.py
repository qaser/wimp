import pycurl
from io import BytesIO
import certifi
import ast
import datetime as dt

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config.telegram_config import ADMIN_TELEGRAM_ID
from config.bot_config import bot

from .constants import HEADERS
from config.mongo_config import auth_gid, cookies_gid


router = Router()


URL = "https://app.gid.ru/auth/realms/gid/protocol/openid-connect/token"
ADD_HEADERS = [
    'Accept: */*',
    'Content-Type: application/x-www-form-urlencoded',
    'Referer: https://web.gid.ru/',
]


@router.message(Command('token'))
async def manual_refresh_token(message):
    await refresh_token_func()


async def refresh_token_func():
    refresh_token = auth_gid.find_one({'username': 'huji'}).get('refresh_token')
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
        auth_gid.update_one(
            {'username': 'huji'},
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
            text=f'Токен ГИД обновлен',
            disable_notification=True
        )
        await bot.send_message(
            chat_id=ADMIN_TELEGRAM_ID,
            text=resp_data['access_token'],
            disable_notification=True
        )
    else:
        await bot.send_message(
            chat_id=ADMIN_TELEGRAM_ID,
            text=f'Ошибка {resp_code}\n{body_str}',
            disable_notification=True
        )
