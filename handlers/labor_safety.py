import os

from aiogram import Dispatcher, types

from config.bot_config import bot
from texts.initial import FINAL_TEXT, KPB_TEXT, NS_TEXT


async def send_exam_answers(message: types.Message):
    for _, _, files in os.walk('static/exam/'):
        for filename in files:
            file = f'static/exam/{filename}'
            with open(file, 'rb') as f:
                contents = f.read()
                await bot.send_photo(message.chat.id, photo=contents)


async def send_pravila(message: types.Message):
    for _, _, files in os.walk('static/kpb_lite/'):
        for filename in files:
            file = f'static/kpb_lite/{filename}'
            with open(file, 'rb') as f:
                contents = f.read()
                await bot.send_photo(message.chat.id, photo=contents)
    await bot.send_message(message.chat.id, text=KPB_TEXT)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


async def send_vnimanie(message: types.Message):
    for _, _, files in os.walk('static/ns/'):
        for filename in files:
            file = f'static/ns/{filename}'
            with open(file, 'rb') as f:
                contents = f.read()
                await bot.send_photo(message.chat.id, photo=contents)
    await bot.send_message(message.chat.id, text=NS_TEXT)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


def register_handlers_labor_safety(dp: Dispatcher):
    dp.register_message_handler(send_exam_answers, commands='exam')
    dp.register_message_handler(send_pravila, commands='pravila')
    dp.register_message_handler(send_vnimanie, commands='vnimanie')
