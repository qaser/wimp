import datetime as dt
import os

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext

from config.bot_config import bot
from config.telegram_config import MY_TELEGRAM_ID


# обработка команды /reset - сброс клавиатуры и состояния
async def reset_handler(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text='Сброс настроек бота выполнен, текущее действие отменено.',
        reply_markup=types.ReplyKeyboardRemove(),
    )


# обработка команды /log
async def send_logs(message: types.Message):
    file = f'logs_bot.log'
    with open(file, 'rb') as f:
        content = f.read()
        await bot.send_document(chat_id=MY_TELEGRAM_ID, document=content)


def register_handlers_service(dp: Dispatcher):
    dp.register_message_handler(reset_handler, commands='reset', state='*')
    dp.register_message_handler(send_logs, commands='log')
