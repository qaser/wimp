import pycurl
from io import BytesIO
import certifi
import json
from .constants import HEADERS
from config.mongo_config import auth_gid, buffer_gid, users_gid
from aiogram import F, Router
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from config.giga_chat_config import GIGA_CHAT_TOKEN
from aiogram.filters import Command
import ast
from config.telegram_config import ADMIN_TELEGRAM_ID
from config.bot_config import bot
import datetime as dt


ACTIVATE_MSG = (
    'Напиши хокку коллеге по работе. '
    'Мы работаем на газотранспортной станции. '
    'Только без нежностей и добавь немного сарказма. Будь креативней. '
    'В тексте должны быть проялены уважение и гордость за будущие заслуги. '
    'Только не нужно говорить в начале фразы "Спасибо, коллега". '
    'Коллегу зовут '
)
URL = 'https://web.gid.ru/api/gratitude'
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/my-resource/thanks',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
]


async def send_gratitude_func():
    today = dt.datetime.today().strftime('%d.%m.%Y')
    users = list(users_gid.find({'latest_like': {'$ne': today}}))
    if len(users) != 0:
        user = users[0]
        username = user['username'].split(' ')[1]
        name = username.split(' ')[1]
        user_id = user['id']
        likes = user['likes']
        token = auth_gid.find_one({'username': 'huji'}).get('access_token')
        csrf = auth_gid.find_one({'username': 'huji'}).get('csrf')
        try:
            chat_instance = GigaChat(credentials=GIGA_CHAT_TOKEN, verify_ssl_certs=False)
            gratitude_giga_chat = chat_instance([SystemMessage(content=f'{ACTIVATE_MSG} {name}')]).content
            gratitude_text = f'{gratitude_giga_chat}\n\nСгенерировано нейросетью :)'
        except:
            gratitude_text = 'Спасибо, просто так'
        print(gratitude_text)
        headers_with_tokens = [
            f'X-CSRF-TOKEN: {csrf}',
            f'Authorization: Bearer {token}',
            f'Cookie: X-CSRF-TOKEN={csrf}',
        ]
        data_text = json.dumps({
            'isAnonymous': False,
            'recipientAccountId': user_id,
            f'appreciation': gratitude_text
        }).encode()
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, URL)
        c.setopt(c.WRITEDATA, buffer)
        c.setopt(c.CAINFO, certifi.where())
        c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS + headers_with_tokens)
        c.setopt(c.POST, 1)
        c.setopt(c.TIMEOUT_MS, 10000)
        c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
        c.setopt(c.POSTFIELDS, data_text)
        c.perform()
        resp_code = c.getinfo(c.RESPONSE_CODE)
        body = buffer.getvalue()
        body_str = body.decode('utf-8')
        c.close()
        if resp_code == 201:
            users_gid.update_one(
                {'id': user_id},
                {'$set': {'likes': likes + 1, 'latest_like': today}}
            )
            await bot.send_message(
                chat_id=ADMIN_TELEGRAM_ID,
                text=f'Статус {resp_code}\n{username}\n{gratitude_text}',
                disable_notification=True
            )
        else:
            await bot.send_message(
                chat_id=ADMIN_TELEGRAM_ID,
                text=f'Ошибка {resp_code}\n{username}\n{body_str}',
            )
