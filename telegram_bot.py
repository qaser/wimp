import logging

from aiogram import types
from aiogram.utils import executor

from config.bot_config import bot, dp
from config.mongo_config import users
from functions.plan_check import plan_pat_check, plan_tu_check
from handlers.labor_safety import register_handlers_labor_safety
from handlers.quiz import register_handlers_quiz
from handlers.service import register_handlers_service
from handlers.vehicles import (register_handlers_confirm,
                               register_handlers_vehicle)
from scheduler.scheduler_jobs import scheduler, scheduler_jobs
from texts.initial import FINAL_TEXT, HELP_TEXT, INITIAL_TEXT

logging.basicConfig(
    filename='gks56_bot.log',
    level=logging.INFO,
    filemode='a',
    format='%(asctime)s - %(message)s',
    datefmt='%d.%m.%y %H:%M:%S'
)


# проверка наличия юзера в БД и добавление его в БД при отсутствии
def insert_user_db(user):
    check_user = users.find_one({'id': user.id})
    if check_user is None:
        users.insert_one({
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'place_of_work': '',
        })


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    insert_user_db(message.from_user)
    await bot.send_message(message.chat.id, text=INITIAL_TEXT)


@dp.message_handler(commands=['help'])
async def help_handler(message: types.Message):
    await bot.send_message(
        message.chat.id,
        text=f'{message.from_user.full_name}{HELP_TEXT}'
    )
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['pat'])
async def pat_handler(message: types.Message):
    text = plan_pat_check().get('data')
    full_text = (
        f'Противоаварийная тренировка на КЦ-5,6 в этом месяце:\n\n{text}'
    )
    await bot.send_message(message.chat.id, text=full_text)
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


@dp.message_handler(commands=['tu'])
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


@dp.message_handler(commands=['menu'])
async def all_commands(message: types.Message):
    await bot.send_message(message.chat.id, text=FINAL_TEXT)


async def on_startup(_):
    scheduler_jobs()


if __name__ == '__main__':
    scheduler.start()
    register_handlers_vehicle(dp)
    register_handlers_confirm(dp)
    register_handlers_service(dp)
    register_handlers_quiz(dp)
    register_handlers_labor_safety(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
