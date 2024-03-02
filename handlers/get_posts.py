import json
import random

from aiogram import Router
from aiogram.filters import Command
from config.gid_config import MY_GID_ID
from handlers.collect_energy import collect_energy_func
from handlers.get_response import get_response

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID
from utils.constants import COMMENTS


URL_POSTS = 'https://web.gid.ru/api/ugc/post/public/v1//post?limit=10'  # эндпоин для списка постов
URL_LIKE = 'https://web.gid.ru/api/ugc/reactions/public/v1/ugc/reaction/'  # эндпоинт для лайка
URL_COMMENTS = 'https://web.gid.ru/api/ugc/comments/public/v1/post/'  # эндпоинт для comments
URL_POST = 'https://web.gid.ru/api/ugc/post/public/v1/post/'  # эндпоинт для одного поста
URL_EMOTIONS = 'https://web.gid.ru/api/my-resource/results'  # отправить настроение
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
]


async def get_posts_and_comments():
    resp_code, resp_data = get_response(URL_POSTS)
    if resp_code == 201 or resp_code == 200:
        posts = resp_data['result']  # list of dicts
        for post in posts:
            post_id = post['id']
            post_title = post['title']
            post_code, post_data = get_response(
                f'{URL_POST}{post_id}',
                add_headers=ADD_HEADERS
            )
            if post_code == 200:
                is_liked = post_data['result']['reactions']['currentReaction']
                if is_liked != 'LIKE':
                    await send_reaction(post_id, post_title)
                await send_replay(post_id)
                await send_comment(post_id, post_title)


async def send_reaction(post_id, post_title):
    like_code, like_data = get_response(
        f'{URL_LIKE}{post_id}/like',
        'POST',
        add_headers=ADD_HEADERS
    )
    if like_code == 200:
        await collect_energy_func(MY_GID_ID, 'reaction_comment_click')
        msg = like_data['message']
        await bot.send_message(ADMIN_TELEGRAM_ID, f'{post_title}: {msg}')
    else:
        await bot.send_message(ADMIN_TELEGRAM_ID, like_data)


async def send_replay(post_id):
    coms_code, coms_data = get_response(
        f'{URL_COMMENTS}{post_id}?offset=0&limit=3',
        add_headers=ADD_HEADERS
    )
    if coms_code == 200:
        total = coms_data['total']
        if total > 0:
            comments = coms_data['items']
            for comment in comments:
                comment_id = comment['id']
                request_data = json.dumps({'content': ':)'})
                get_response(
                    f'{URL_COMMENTS}{post_id}/comments/{comment_id}/replies',
                    'POST',
                    request_data,
                    add_headers=ADD_HEADERS,
                    no_data=True
                )


async def send_comment(post_id, post_title):
    com_text = random.choice(COMMENTS)
    request_data = json.dumps({'content': com_text})
    com_code, _ = get_response(
        f'{URL_COMMENTS}{post_id}',
        'POST', request_data,
        add_headers=ADD_HEADERS
    )
    if com_code == 201:
        await collect_energy_func(MY_GID_ID, 'news_comment_send')
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'{post_title}: мой комментарий - {com_text}',
            add_headers=ADD_HEADERS
        )


async def send_emotion():
    request_data = json.dumps({'values':[1,1,1]})
    code, _ = get_response(
        URL_EMOTIONS,
        'POST',
        request_data,
        add_headers=ADD_HEADERS
    )
    if code == 200:
        await bot.send_message(ADMIN_TELEGRAM_ID, 'Эмоция отправлена')
