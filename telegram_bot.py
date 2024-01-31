import asyncio
import logging

from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import F, Router

from config.bot_config import bot, dp
from config.telegram_config import ADMIN_TELEGRAM_ID
from handlers import service, oil, report, gpa_params


@dp.message(Command('reset'))
async def cmd_reset(message: Message, state: FSMContext):
    await message.delete()
    await state.clear()
    await message.answer('Ошибки сброшены')


# @dp.message(F.text)
# async def archive_messages(message: Message):
#     await bot.send_message(
#         chat_id=ADMIN_TELEGRAM_ID,
#         text=f'{message.chat.id}\n{message.message_thread_id}'
#     )


async def main():
    dp.include_router(service.router)
    dp.include_router(report.router)
    dp.include_router(gpa_params.router)
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
