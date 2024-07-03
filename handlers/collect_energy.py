import datetime as dt
import json
import time
import uuid
from io import BytesIO

import certifi
import pycurl

from config.bot_config import bot
from config.gid_config import MY_GID_ID
from config.mongo_config import auth_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from handlers.get_profile import get_profile
from handlers.get_response import get_response
from handlers.gid_auth import refresh_token_func
from utils.constants import HEADERS


URL = 'https://web.gid.ru/api/event-tracker/public/v1/collect'
TRANSFER_URL = 'https://app.gid.ru/api/loyalty/public/v1/operations/transfer'
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/my-resource/thanks',
    'X-Requested-With: XMLHttpRequest',
]


async def collect_energy_daily():
    await bot.send_message(ADMIN_TELEGRAM_ID, 'Запуск задачи майнинга энергии')
    users = list(auth_gid.find({'automatization': True}))
    for user in users:
        user_id = user['gid_id']
        for _ in range(2):
            await collect_energy_func(user_id, 'course_lesson_finish')
    await bot.send_message(ADMIN_TELEGRAM_ID, 'Задача майнинга энергии завершена')


async def transfer_power():
    await bot.send_message(ADMIN_TELEGRAM_ID, 'Запуск задачи трансфера баллов')
    await refresh_token_func()
    await get_profile(MY_GID_ID, 'Сайгин А.В.')
    users = list(auth_gid.find({'donor': True}))
    for user in users:
        user_id = user['gid_id']
        data = json.dumps({'power': 150, 'comment': '', 'accountId': MY_GID_ID})
        resp_code = get_response(
            TRANSFER_URL,
            'POST',
            fields_data=data,
            no_data=True,
            add_headers=ADD_HEADERS,
            user_id=user_id
        )
        if resp_code == 201:
            await bot.send_message(ADMIN_TELEGRAM_ID, 'Задача трансфера баллов завершена успешно')
            await get_profile(MY_GID_ID, 'Сайгин А.В.')
        else:
            await bot.send_message(ADMIN_TELEGRAM_ID, f'Трансфер баллов не удался: ошибка {resp_code}')


async def collect_energy_func(user_id, event):
    time.sleep(4)
    user = auth_gid.find_one({'gid_id': user_id})
    headers_with_tokens = []
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, URL)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS + headers_with_tokens)
    c.setopt(c.POST, 1)
    c.setopt(c.TIMEOUT_MS, 10000)
    if event == 'news_comment_send':
        c.setopt(c.POSTFIELDS, get_request_data_comment(user_id))
    elif event == 'thanks_new_create_click':
        c.setopt(c.POSTFIELDS, get_request_data_thanks(user_id))
    elif event == 'reaction_comment_click':
        c.setopt(c.POSTFIELDS, get_request_data_reaction(user_id))
    elif event == 'course_lesson_finish':
        c.setopt(c.POSTFIELDS, get_request_data_course(user_id))
    elif event == 'course_lesson_start':
        c.setopt(c.POSTFIELDS, get_request_course_start(user_id))
    c.perform()
    resp_code = c.getinfo(c.RESPONSE_CODE)
    body = buffer.getvalue()
    c.close()
    resp_data = f'Ошибка {resp_code}\n{body}'
    await bot.send_message(ADMIN_TELEGRAM_ID, resp_data)


def get_request_data_comment(user_id):
    today = dt.datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
    data = json.dumps({
        'batch': [
            {
                'anonymousId': str(uuid.uuid4()),
                'event': 'news_comment_send',
                'messageId': str(uuid.uuid4()),
                'properties': {'replay': ''},
                'timestamp': f'{today}.916Z',
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': f'{today}.916Z',
        'writeKey': 'sdk'
    }).encode()
    return data


def get_request_data_thanks(user_id):
    today = dt.datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
    data = json.dumps({
        'batch': [
            {
                'anonymousId': str(uuid.uuid4()),
                'event': 'thanks_new_create_click',
                'messageId': str(uuid.uuid4()),
                'properties': {
                    'recipient': '83e1d148-d173-401b-9d16-a97547e8907d'
                },
                'timestamp': f'{today}.916Z',
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': f'{today}.916Z',
        'writeKey': 'sdk'
    }).encode()
    return data


def get_request_data_reaction(user_id):
    today = dt.datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
    data = json.dumps({
        'batch': [
            {
                'anonymousId': str(uuid.uuid4()),
                'event': 'reaction_comment_click',
                'messageId': str(uuid.uuid4()),
                'properties': {
                    'replay': 'aae15b58-9f04-4685-8dc6-2175db7ac79a'
                },
                'timestamp': f'{today}.967Z',
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': f'{today}.916Z',
        'writeKey': 'sdk'
    }).encode()
    return data


def get_request_data_course(user_id):
    today = dt.datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
    data = json.dumps({
        'batch': [
            {
                'anonymousId': str(uuid.uuid4()),
                'event': 'lms_course_lesson_finish',
                'messageId': str(uuid.uuid4()),
                'properties': {
                    'course_id':'0499488b-00d3-4a59-9f32-283dc4e079dd',
                    'lesson_id':'e992f695-36ea-4566-9815-9dab6bc07c09',
                    'user_id':'8d68107c-b224-4817-93d2-7144bc428dc3'
                },
                'timestamp': f'{today}.967Z',
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': f'{today}.916Z',
        'writeKey': '900100'
    }).encode()
    return data


def get_request_course_start(user_id):
    today = dt.datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
    data = json.dumps({
        'batch': [
            {
                'anonymousId': str(uuid.uuid4()),
                'event': 'en_lms_course_started',
                'messageId': str(uuid.uuid4()),
                'properties': {
                    'course_id': '0499488b-00d3-4a59-9f32-283dc4e079dd',
                    'lesson_id': 'e992f695-36ea-4566-9815-9dab6bc07c09',
                    'user_id': f'{user_id}'
                },
                'timestamp': f'{today}.967Z',
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': f'{today}.916Z',
        'writeKey': '900100'
    }).encode()
    return data
