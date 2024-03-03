import json
import random

from config.gid_config import MY_GID_ID
from handlers.collect_energy import collect_energy_func
from handlers.get_response import get_response

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID
from utils.constants import COMMENTS_FEED


URL_FEEDS = 'https://web.gid.ru/api/public/v3/feed?gidOnly=true&pinsOnly=false&recommendationsOnly=false&limit=10'  # эндпоин для списка новостей
URL_FEED = 'https://web.gid.ru/api/feed/'  # эндпоинт для лайка h9qT5wJyHPbw/reactions
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
]


async def get_feeds():
    resp_code, resp_data = get_response(URL_FEEDS)
    if resp_code == 200:
        feeds = resp_data['items']  # list of dicts
        for feed in feeds:
            feed_id = feed['id']
            feed_title = feed['title']
            comment_enabled = feed['isCommentsEnabled']
            is_liked = feed['rating']['myRating']
            if is_liked != 'LIKE':
                await send_like(feed_id, feed_title)
            if comment_enabled is True:
                await send_comment(feed_id, feed_title)


async def send_like(feed_id, feed_title):
    request_data = json.dumps({'type': 'like'})
    like_code = get_response(
        f'{URL_FEED}{feed_id}/reactions',
        'POST',
        request_data,
        add_headers=ADD_HEADERS,
        no_data=True
    )
    if like_code == 201:
        await bot.send_message(ADMIN_TELEGRAM_ID, f'{feed_title}: лайк поставлен')
    else:
        await bot.send_message(ADMIN_TELEGRAM_ID, 'c лайком новостей что-то не так :(')


async def send_comment(feed_id, feed_title):
    com_text = random.choice(COMMENTS_FEED)
    request_data = json.dumps({'content': com_text})
    com_code, com_data = get_response(
        f'{URL_FEED}{feed_id}/comments',
        'POST',
        request_data,
        add_headers=ADD_HEADERS
    )
    if com_code == 201:
        await collect_energy_func(MY_GID_ID, 'news_comment_send')
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'Новость "{feed_title}": мой комментарий - {com_text}',
        )
    else:
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'Отправка комментария.\n{com_data["error"]}'
        )
