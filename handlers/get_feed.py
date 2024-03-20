import json
import random
import datetime as dt

from config.gid_config import MY_GID_ID
from handlers.collect_energy import collect_energy_func
from handlers.get_response import get_response

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID
from handlers.gid_auth import refresh_token_func
from utils.constants import COMMENTS_FEED
from config.mongo_config import buffer_gid, auth_gid
from aiogram.enums import ParseMode


LIKE_OR_DISLIKE = ['like', 'dislike']
URL_FEEDS = 'https://web.gid.ru/api/public/v3/feed?gidOnly=true&pinsOnly=false&recommendationsOnly=false&limit=5'  # эндпоин для списка новостей
URL_FEED = 'https://web.gid.ru/api/feed/'  # эндпоинт для лайка h9qT5wJyHPbw/reactions
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
]


async def get_feeds():
    users = list(auth_gid.find({'automatization': True}))
    # user_id = MY_GID_ID
    await bot.send_message(ADMIN_TELEGRAM_ID, 'Запуск задачи чтения новостей')
    await refresh_token_func()
    for user in users:
        user_id = user['gid_id']
        username = user['username']
        resp_code, resp_data = get_response(URL_FEEDS)
        if resp_code == 200:
            buffer_id = buffer_gid.insert_one({
                'likes': 0,
                'feeds': [],
                'errors': 0,
                'errors_log': [],
                'energy': 0,
            }).inserted_id
            feeds = resp_data['items']  # list of dicts
            for feed in feeds:
                feed_id = feed['id']
                feed_title = feed['title']
                comment_enabled = feed['isCommentsEnabled']
                is_liked = feed['rating']['myRating']
                if is_liked != 'LIKE':
                    await send_like(feed_id, user_id, buffer_id)
                if comment_enabled is True:
                    await send_comment(feed_id, feed_title, user_id, buffer_id)
            # формирование отчета по работе бота
            res = buffer_gid.find_one({'_id': buffer_id})
            report = ''
            if len(res['feeds']) > 0:
                for f in res['feeds']:
                    report = f'{report}{f}\n'
            report = f'{report}\nЛайков: {res["likes"]}\n'
            report = f'{report}Энергия: {res["energy"]}\n'
            report = f'{report}Ошибок: {res["errors"]}\n'
            if res['errors'] > 0:
                for e in res['errors_log']:
                    report = f'{report}{e}\n'
            await bot.send_message(
                ADMIN_TELEGRAM_ID,
                f'Задачa чтения новостей пользователем <i>"{username}"</i> завершена\n\n{report}',
                parse_mode=ParseMode.HTML,
            )
            buffer_gid.delete_one({'_id': buffer_id})
        else:
            await bot.send_message(
                ADMIN_TELEGRAM_ID,
                f'Получение списка новостей: {resp_data["error"]}'
            )
            break


async def send_like(feed_id, user_id, buffer_id):
    request_data = json.dumps({'type': random.choice(LIKE_OR_DISLIKE)})
    like_code = get_response(
        f'{URL_FEED}{feed_id}/reactions',
        'POST',
        request_data,
        add_headers=ADD_HEADERS,
        no_data=True,
        user_id=user_id
    )
    if like_code == 201:
        buffer_gid.update_one({'_id': buffer_id}, {'$inc': {'likes': 1}})
    else:
        buffer_gid.update_one({'_id': buffer_id}, {'$inc': {'errors': 1}})


async def send_comment(feed_id, feed_title, user_id, buffer_id):
    com_text = random.choice(COMMENTS_FEED)
    request_data = json.dumps({'content': com_text})
    com_code, com_data = get_response(
        f'{URL_FEED}{feed_id}/comments',
        'POST',
        request_data,
        add_headers=ADD_HEADERS,
        user_id=user_id
    )
    if com_code == 201:
        await collect_energy_func(user_id, 'news_comment_send', buffer_id)
        buffer_gid.update_one(
            {'_id': buffer_id},
            {'$push': {'feeds': f'<b>"{feed_title}"</b>: {com_text}'}}
        )
    else:
        buffer_gid.update_one({'_id': buffer_id}, {'$inc': {'errors': 1}})
        buffer_gid.update_one({'_id': buffer_id}, {'$push': {'errors_log': com_data}})
