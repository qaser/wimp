from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID
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
async def manual_auth(message, state):
    await manual_auth_func(message, state)


# обработка команды /log
@router.message(Command('log'))
async def send_logs(message: Message):
    file = f'logs_bot.log'
    with open(file, 'rb') as f:
        content = f.read()
        await bot.send_document(chat_id=ADMIN_TELEGRAM_ID, document=content)
