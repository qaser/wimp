import json
import time
from io import BytesIO

import certifi
import pycurl
from aiogram import Router
from aiogram.filters import Command
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import SystemMessage

from config.bot_config import bot
from config.mongo_config import auth_gid, courses_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from config.giga_chat_config import GIGA_CHAT_TOKEN
from utils.constants import HEADERS

router = Router()

URL_POSTS = "https://web.gid.ru/api/ugc/post/public/v1//post?limit=5"  # эндпоин для списка постов
URL_LIKE = "https://web.gid.ru/api/ugc/reactions/public/v1/ugc/reaction/"  # эндпоинт для лайка
URL_COMMENTS = "https://web.gid.ru/api/ugc/comments/public/v1/post/"  # эндпоинт для comments
URL_POST = 'https://web.gid.ru/api/ugc/post/public/v1/post/'  # эндпоинт для одного поста
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
]
ACTIVATE_MSG = ('Представь, что ты один из пользователей корпоративного форума. '
                'Напиши очень короткий доброжелательный комментарий на абстрактную статью')


def get_response(url, method='GET', fields_data='', no_data=False):
    time.sleep(3)
    auth_param = auth_gid.find_one({'username': 'huji'})
    token = auth_param['access_token']
    csrf = auth_param['csrf']
    auth_headers = [
        f'X-CSRF-TOKEN: {csrf}',
        f'Authorization: Bearer {token}',
        f'Cookie: X-CSRF-TOKEN={csrf}',
    ]
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS + auth_headers)
    c.setopt(c.TIMEOUT_MS, 10000)
    c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
    if method == 'PUT':
        c.setopt(c.CUSTOMREQUEST, "PUT")
        c.setopt(c.POSTFIELDS, fields_data)
    if method == 'POST':
        c.setopt(c.POST, 1)
        c.setopt(c.POSTFIELDS, fields_data)
    c.perform()
    resp_code = c.getinfo(c.RESPONSE_CODE)
    body = buffer.getvalue()
    c.close()
    if no_data:
        return resp_code
    resp_data = json.loads(body.decode())
    return (resp_code, resp_data)


async def get_posts_and_comments():
    resp_code, resp_data = get_response(URL_POSTS)
    if resp_code == 201 or resp_code == 200:
        posts = resp_data['result']  # list of dicts
        for post in posts:
            post_id = post['id']
            post_title = post['title']
            post_code, post_data = get_response(f'{URL_POST}{post_id}')
            if post_code == 200:
                is_liked = post_data['result']['reactions']['currentReaction']
                if is_liked != 'LIKE':
                    await send_reaction(post_id, post_title)
                await send_replay(post_id)
                await send_comment(post_id, post_title)


async def send_reaction(post_id, post_title):
    like_code, like_data = get_response(f'{URL_LIKE}{post_id}/like', 'POST')
    if like_code == 200:
        msg = like_data['message']
        await bot.send_message(ADMIN_TELEGRAM_ID, f'{post_title}: {msg}')


async def send_replay(post_id):
    coms_code, coms_data = get_response(f'{URL_COMMENTS}{post_id}?offset=0&limit=3')
    if coms_code == 200:
        total = coms_data['total']
        if total > 0:
            comments = coms_data['items']
            for comment in comments:
                comment_id = comment['id']
                request_data = json.dumps({'content': ':)'})
                get_response(f'{URL_COMMENTS}{post_id}/comments/{comment_id}/replies', 'POST', request_data)


async def send_comment(post_id, post_title):
    try:
        chat_instance = GigaChat(credentials=GIGA_CHAT_TOKEN, verify_ssl_certs=False)
        com_text = chat_instance([SystemMessage(content=ACTIVATE_MSG)]).content
    except:
        com_text = 'Спасибо за информацию, продолжайте'
    request_data = json.dumps({'content': com_text})
    com_code, _ = get_response(f'{URL_COMMENTS}{post_id}', 'POST', request_data)
    if com_code == 201:
        await bot.send_message(ADMIN_TELEGRAM_ID, f'{post_title}: мой комментарий - {com_text}')
