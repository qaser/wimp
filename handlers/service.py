from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID


router = Router()

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
