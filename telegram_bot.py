import asyncio
import logging

from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F, Router

from config.bot_config import bot, dp
from handlers import service, oil


@dp.message(Command('reset'))
async def cmd_reset(message: Message, state: FSMContext):
    await message.delete()
    await state.clear()
    await message.answer('Ошибки сброшены')


# @dp.message(F.text)
# async def archive_messages(message: Message):
#     print(message)


async def main():
    dp.include_router(service.router)
    dp.include_router(oil.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(
        filename='logs_bot.log',
        level=logging.INFO,
        filemode='a',
        format='%(asctime)s - %(message)s',
        datefmt='%d.%m.%y %H:%M:%S',
        encoding='utf-8',
    )
    asyncio.run(main())
