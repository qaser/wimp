from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID
from gid.refresh_token import refresh_token_func
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from config.mongo_config import auth_gid


router = Router()

class Token(StatesGroup):
    token_value = State()
    csrf_value = State()
    refresh_token_value = State()
    session_value = State()


@router.message(Command('token'))
async def manual_refresh_token(message):
    await refresh_token_func()


@router.message(Command('auth'))
async def manual_auth(message, state):
    await manual_auth_func(message, state)


# обработка команды /reset - сброс клавиатуры и состояния
@router.message(Command('reset'))
async def reset_handler(message: Message, state: FSMContext):
    await message.delete()
    await state.clear()
    await message.answer(
        text='Сброс настроек бота выполнен, текущее действие отменено.',
        reply_markup=ReplyKeyboardRemove(),
    )


# обработка команды /log
@router.message(Command('log'))
async def send_logs(message: Message):
    file = f'logs_bot.log'
    with open(file, 'rb') as f:
        content = f.read()
        await bot.send_document(chat_id=ADMIN_TELEGRAM_ID, document=content)


async def manual_auth_func(message: Message, state: FSMContext):
    await message.answer('Введите значение токена')
    await state.set_state(Token.token_value)


@router.message(Token.token_value)
async def get_token(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'username': 'huji'},
        {'$set': {'access_token': message.text, 'id_token': message.text}}
    )
    await message.answer('Введите значение CSRF')
    await state.set_state(Token.csrf_value)


@router.message(Token.csrf_value)
async def get_csrf(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'username': 'huji'},
        {'$set': {'csrf': message.text}}
    )
    await message.answer('Введите значение refresh_token')
    await state.set_state(Token.refresh_token_value)


@router.message(Token.refresh_token_value)
async def get_refresh_token(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'username': 'huji'},
        {'$set': {'refresh_token': message.text}}
    )
    await message.answer('Введите значение session')
    await state.set_state(Token.session_value)


@router.message(Token.session_value)
async def get_session(message: Message, state: FSMContext):
    auth_gid.update_one(
        {'username': 'huji'},
        {'$set': {'session_state': message.text}}
    )
    await message.answer('Принято')
