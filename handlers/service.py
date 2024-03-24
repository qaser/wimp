from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, FSInputFile
from bson.objectid import ObjectId

from config.bot_config import bot
from config.gid_config import MY_GID_ID
from config.telegram_config import ADMIN_TELEGRAM_ID
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from handlers.collect_energy import collect_energy_daily, collect_energy_func
from config.mongo_config import auth_gid
from handlers.get_courses import get_courses
from handlers.get_feed import get_feeds
from handlers.get_posts import change_name, get_posts_and_comments
from handlers.get_profile import get_profile
from handlers.gid_auth import refresh_token_func, choose_user

router = Router()


class Token(StatesGroup):
    username_value = State()
    id_value = State()
    token_value = State()
    csrf_value = State()
    refresh_token_value = State()
    session_value = State()


@router.message(Command('refresh_token'))
async def manual_refresh_token(message: Message):
    await refresh_token_func()


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
    await collect_energy_daily()


@router.message(Command('name'))
async def manual_change_name(message: Message):
    await change_name()


@router.message(Command('set_automatization'))
async def set_automatization(message: Message):
    await choose_user(message, 'auto')


@router.message(Command('get_tokens'))
async def get_tokens(message: Message):
    await choose_user(message, 'get')


@router.message(Command('set_tokens'))
async def set_tokens(message: Message):
    await choose_user(message, 'set')


@router.message(Command('log'))
async def send_logs(message: Message):
    document = FSInputFile(path=r'logs_bot.log')
    await message.answer_document(document=document)
    await message.delete()


@router.callback_query(F.data.startswith('auth-set_'))
async def manual_auth_func(callback: CallbackQuery, state: FSMContext):
    _, id = callback.data.split('_')
    if id != 'new':
        # user_id = auth_gid.find_one({'_id': ObjectId(id)})
        await state.update_data({'user_id': ObjectId(id)})
        await callback.message.answer('Введите значение токена')
        await state.set_state(Token.token_value)
    else:
        await callback.message.answer('Введите "username" нового пользователя')
        await state.set_state(Token.username_value)
    await callback.message.delete()


@router.message(Token.username_value)
async def get_username(message: Message, state: FSMContext):
    user_id = auth_gid.insert_one({'username': message.text}).inserted_id
    await state.update_data({'user_id': user_id})
    await message.answer('Введите id пользователя')
    await state.set_state(Token.id_value)


@router.message(Token.id_value)
async def get_id(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = user_data['user_id']
    auth_gid.update_one({'_id': user_id}, {'$set': {'gid_id': message.text}})
    await message.answer('Введите значение токена')
    await state.set_state(Token.token_value)


@router.message(Token.token_value)
async def get_token(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = user_data['user_id']
    auth_gid.update_one(
        {'_id': user_id},
        {'$set': {'access_token': message.text, 'id_token': message.text}}
    )
    await message.answer('Введите значение CSRF')
    await state.set_state(Token.csrf_value)


@router.message(Token.csrf_value)
async def get_csrf(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = user_data['user_id']
    auth_gid.update_one({'_id': user_id}, {'$set': {'csrf': message.text}})
    await message.answer('Введите значение refresh_token')
    await state.set_state(Token.refresh_token_value)


@router.message(Token.refresh_token_value)
async def get_refresh_token(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = user_data['user_id']
    auth_gid.update_one({'_id': user_id}, {'$set': {'refresh_token': message.text}})
    await message.answer('Введите значение session')
    await state.set_state(Token.session_value)


@router.message(Token.session_value)
async def get_session(message: Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = user_data['user_id']
    auth_gid.update_one({'_id': user_id}, {'$set': {'session_state': message.text}})
    await state.clear()
    await message.answer('Принято')
