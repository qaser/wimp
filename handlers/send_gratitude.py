import datetime as dt
import json
import random
import time
from io import BytesIO

import certifi
import pycurl
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import SystemMessage

from config.bot_config import bot
from config.gid_config import MY_GID_ID
from config.giga_chat_config import GIGA_CHAT_TOKEN
from config.mongo_config import auth_gid, users_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from handlers.collect_energy import collect_energy_func
from utils.constants import HEADERS
from utils.constants import AUTHORS, GIGACHAT_ACTIVATE_MSG

TEXT_FOOTER = ('Сгенерировано нейросетью...\n'
               'Рассылается автоматически...\n'
               '...но это не значит, что я Вас не ценю :)')
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
        author = random.choice(AUTHORS)
        user = users[0]
        username = user['username']
        user_id = user['id']
        likes = user['likes']
        token = auth_gid.find_one({'gid_id': MY_GID_ID}).get('access_token')
        csrf = auth_gid.find_one({'gid_id': MY_GID_ID}).get('csrf')
        try:
            chat_instance = GigaChat(credentials=GIGA_CHAT_TOKEN, verify_ssl_certs=False)
            gratitude_giga_chat = chat_instance([SystemMessage(content=f'{GIGACHAT_ACTIVATE_MSG}{author}')]).content
            gratitude_text = f'{gratitude_giga_chat}\n\n{TEXT_FOOTER}'
        except:
            gratitude_text = 'Спасибо, просто так'
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
            await collect_energy_func(MY_GID_ID, 'thanks_new_create_click')
            await bot.send_message(
                chat_id=ADMIN_TELEGRAM_ID,
                text=f'Статус {resp_code}\n{username}\n\n{gratitude_text}',
                disable_notification=True
            )
        else:
            await bot.send_message(
                chat_id=ADMIN_TELEGRAM_ID,
                text=f'Ошибка {resp_code}\n{username}\n{body_str}',
            )
