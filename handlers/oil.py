from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID


router = Router()

@router.message(F.message_thread_id)
async def set_oil(message: Message):
    pass
