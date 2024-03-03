from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from config.bot_config import bot
from config.gid_config import MY_GID_ID
from config.telegram_config import ADMIN_TELEGRAM_ID
from handlers.collect_energy import collect_energy_func
from handlers.get_courses import get_courses
from handlers.get_feed import get_feeds
from handlers.get_posts import get_posts_and_comments
from handlers.gid_auth import (manual_auth_func, refresh_token_func,
                               send_user_token)

router = Router()


@router.message(Command('refresh_token'))
async def manual_refresh_token(message: Message):
    await refresh_token_func()


@router.message(Command('send_me_token'))
async def manual_refresh_token(message: Message):
    await send_user_token()


@router.message(Command('auth'))
async def manual_auth(message):
    await manual_auth_func(message)


@router.message(Command('courses'))
async def manual_complete_courses(message: Message):
    await get_courses()


@router.message(Command('posts'))
async def manual_get_posts(message: Message):
    await get_posts_and_comments()


@router.message(Command('feeds'))
async def manual_get_feeds(message: Message):
    await get_feeds()


@router.message(Command('collect'))
async def manual_collect_energy(message: Message):
    await collect_energy_func(MY_GID_ID, 'news_comment_send')


@router.message(Command('log'))
async def send_logs(message: Message):
    file = f'logs_bot.log'
    with open(file, 'rb') as f:
        content = f.read()
        await bot.send_document(chat_id=ADMIN_TELEGRAM_ID, document=content)
