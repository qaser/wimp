from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from config.bot_config import bot
from config.gid_config import MY_GID_ID
from config.telegram_config import ADMIN_TELEGRAM_ID
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.collect_energy import collect_energy_func
from config.mongo_config import auth_gid
from handlers.get_courses import get_courses
from handlers.get_feed import get_feeds
from handlers.get_posts import get_posts_and_comments
from handlers.gid_auth import refresh_token_func, send_user_token

router = Router()


class Token(StatesGroup):
    token_value = State()
    csrf_value = State()
    refresh_token_value = State()
    session_value = State()


@router.message(Command('refresh_token'))
async def manual_refresh_token(message: Message):
    await refresh_token_func()


@router.message(Command('send_me_token'))
async def manual_refresh_token(message: Message):
    await send_user_token()


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



@router.message(Command('auth'))
async def manual_auth_func(message: Message, state: FSMContext):
    await message.answer('Введите значение токена')
    await state.set_state(Token.token_value)


@router.message(Token.token_value)
async def get_token(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'gid_id': MY_GID_ID},
        {'$set': {'access_token': message.text, 'id_token': message.text}}
    )
    await message.answer('Введите значение CSRF')
    await state.set_state(Token.csrf_value)


@router.message(Token.csrf_value)
async def get_csrf(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'gid_id': MY_GID_ID},
        {'$set': {'csrf': message.text}}
    )
    await message.answer('Введите значение refresh_token')
    await state.set_state(Token.refresh_token_value)


@router.message(Token.refresh_token_value)
async def get_refresh_token(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'gid_id': MY_GID_ID},
        {'$set': {'refresh_token': message.text}}
    )
    await message.answer('Введите значение session')
    await state.set_state(Token.session_value)


@router.message(Token.session_value)
async def get_session(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'gid_id': MY_GID_ID},
        {'$set': {'session_state': message.text}}
    )
    state.clear()
    await message.answer('Принято')
