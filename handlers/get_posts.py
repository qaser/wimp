import json
import random

from config.gid_config import MY_GID_ID
from handlers.collect_energy import collect_energy_func
from handlers.get_response import get_response

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID
from handlers.gid_auth import refresh_token_func
from utils.constants import COMMENTS_POST
from config.mongo_config import auth_gid


URL_POSTS = 'https://web.gid.ru/api/ugc/post/public/v1//post?limit=8'  # эндпоин для списка постов
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
    await bot.send_message(ADMIN_TELEGRAM_ID, 'Запуск задачи чтения постов')
    resp_code, resp_data = get_response(URL_POSTS)
    if resp_code == 201 or resp_code == 200:
        # users = list(auth_gid.find({}))
        posts = resp_data['result']  # list of dicts
        # for user in users:
        user_id = MY_GID_ID
        for post in posts:
            post_id = post['id']
            post_title = post['title']
            post_code, post_data = get_response(
                f'{URL_POST}{post_id}',
                add_headers=ADD_HEADERS,
                user_id=user_id
            )
            if post_code == 200:
                is_liked = post_data['result']['reactions']['currentReaction']
                if is_liked != 'LIKE':
                    await send_reaction(post_id, post_title, user_id)
                await send_replay(post_id, user_id)
                await send_comment(post_id, post_title, user_id)
            else:
                await bot.send_message(ADMIN_TELEGRAM_ID, post_data['error'])
        else:
            await bot.send_message(
                ADMIN_TELEGRAM_ID,
                f'Получение списка постов: {resp_data["error"]}'
            )


async def send_reaction(post_id, post_title, user_id):
    like_code, like_data = get_response(
        f'{URL_LIKE}{post_id}/like',
        'POST',
        add_headers=ADD_HEADERS,
        user_id=user_id,
    )
    if like_code == 200:
        await collect_energy_func(user_id, 'reaction_comment_click')
        msg = like_data['message']
        await bot.send_message(ADMIN_TELEGRAM_ID, f'{post_title}: {msg}')
    else:
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'Отправка лайка за пост: {like_data["error"]}'
        )


async def send_replay(post_id, user_id):
    coms_code, coms_data = get_response(
        f'{URL_COMMENTS}{post_id}?offset=0&limit=3',
        add_headers=ADD_HEADERS,
        user_id=user_id
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
                    no_data=True,
                    user_id=user_id,
                )
    else:
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'Получение комментариев.\n{coms_data["error"]}'
        )


async def send_comment(post_id, post_title, user_id):
    com_text = random.choice(COMMENTS_POST)
    request_data = json.dumps({'content': com_text})
    com_code, com_data = get_response(
        f'{URL_COMMENTS}{post_id}',
        'POST',
        request_data,
        add_headers=ADD_HEADERS,
        user_id=user_id,
    )
    if com_code == 201:
        await collect_energy_func(user_id, 'news_comment_send')
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'{post_title}: мой комментарий - {com_text}',
        )
    else:
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'Отправка комментария.\n{com_data["error"]}'
        )


async def send_emotion():
    await bot.send_message(ADMIN_TELEGRAM_ID, 'Запуск задачи отправки эмоции')
    request_data = json.dumps({'values':[1,1,1]})
    code, data = get_response(
        URL_EMOTIONS,
        'POST',
        request_data,
        add_headers=ADD_HEADERS
    )
    if code == 201 or code == 200:
        await bot.send_message(ADMIN_TELEGRAM_ID, 'Эмоция отправлена')
    else:
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'Отправка настроения.\n{data["error"]}'
        )
