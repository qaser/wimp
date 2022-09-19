import os

from aiogram import Dispatcher, types

from config.bot_config import bot
from functions.plan_check import plan_pat_check, plan_tu_check
from texts.initial import FINAL_TEXT, KPB_TEXT, NS_TEXT


async def send_exam_answers(message: types.Message):
    media = types.MediaGroup()
    for _, _, files in os.walk('static/exam/'):
        for filename in files:
            file = f'static/exam/{filename}'
            media.attach_photo(types.InputFile(file))
    await bot.send_media_group(message.chat.id, media=media)


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


async def pat_handler(message: types.Message):
    text = plan_pat_check().get('data')
    full_text = (
        f'Противоаварийная тренировка на КЦ-5,6 в этом месяце:\n\n{text}'
    )
    await bot.send_message(message.chat.id, text=full_text)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


async def tu_handler(message: types.Message):
    plan_now = plan_tu_check().get('plan')
    plan_past = plan_tu_check().get('past_plan')
    text_now = ''
    text_past = ''
    for date, theme in plan_now.items():
        theme_text = ''
        for item in theme:
            theme_text = theme_text + f'{item}\n'
        text_now = text_now + f'{date}:\n{theme_text}\n'
    if len(plan_past) == 0:
        text_past = 'Данные отсутствуют'
    else:
        for date, theme in plan_past.items():
            theme_text = ''
            for item in theme:
                theme_text = theme_text + f'{item}\n'
            text_past = text_past + f'{date}:\n{theme_text}\n'
    full_text_now = f'Техническая учёба на КЦ-5,6 в этом месяце:\n\n{text_now}'
    full_text_past = f'В предыдущем месяце:\n\n{text_past}'
    full_text = '{}\n{}'.format(full_text_now, full_text_past)
    await bot.send_message(message.chat.id, text=full_text)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


def register_handlers_labor_safety(dp: Dispatcher):
    dp.register_message_handler(send_exam_answers, commands='exam')
    dp.register_message_handler(send_pravila, commands='pravila')
    dp.register_message_handler(send_vnimanie, commands='vnimanie')
    dp.register_message_handler(pat_handler, commands='pat')
    dp.register_message_handler(tu_handler, commands='tu')
