import re
import datetime as dt

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID
from config.mongo_config import tanks, oil_actions


router = Router()

@router.message((F.message_thread_id == 19) & (F.chat.id == -1001902490328))
async def set_oil(message: Message):
    text = message.text
    check_date = re.search(r'\d{2}.\d{2}.\d{4}', text)
    date = dt.datetime.strptime(check_date[0], '%d.%m.%Y') if check_date else dt.datetime.today()
    check_keyword = re.search(r'кач', text)
    gpa_levels = re.findall(r'\w+\s(?:д|н)\d{1,3}\s(?:д|н)\d{1,3}', text)
    gpa_loads = re.findall(r'\w+\s\d*/\d*\s\w+', text)
    other_levels = re.findall(r'((?:\w+|\w+\d)(?:\s\d-\d*){1,6})', text)
    print(other_levels)
    if len(gpa_loads) > 0:
        for rec in gpa_loads:
            await load_handler(rec, date, message)
    if len(gpa_levels) > 0:
        for rec in gpa_levels:
            await level_handler(rec, date, message)
    if len(other_levels) > 0:
        for rec in other_levels:
            await gsm_handler(rec, date, message)


def load_handler(record, date, message):
    print(f'Это закачка {record}')


async def level_handler(record, date, message):
    gpa_num = re.search(r'\d\d', record)[0]
    d_level = re.search(r'д(\d{1,3})', record)[0][1:]
    n_level = re.search(r'н(\d{1,3})', record)[0][1:]
    try:
        tanks.update_one(
            {'type': 'ГПА', 'num': gpa_num, 'tank': 'Д'},
            {'$set': {'cur_volume': int(d_level), 'last_update': date}}
        )
        tanks.update_one({
            {'type': 'ГПА', 'num': gpa_num, 'tank': 'Н'},
            {'$set': {'cur_volume': int(n_level), 'last_update': date}}
        })
    except Exception as err:
        await message.answer(
            f'Не могу обработать запись "{record}"',
            disable_notification=True
        )
        await bot.send_message(
            chat_id=ADMIN_TELEGRAM_ID,
            text=f'Ошибка при обработке записи {err}'
        )
    try:
        oil_actions.insert_one(
            {
                'date', date,
                'action', 'outlay',
                'in_tank', 'id первого резервуара масла',
                'out_tank', 'id второго резервуара масла',
                'user_id', message.from_user.id,
                'before_vol', 'уровень до',
                'after_vol', 'уровень после',
                'cost', 'изменение уровня',
            }
        )
    except:
        await bot.send_message(
            chat_id=ADMIN_TELEGRAM_ID,
            text=f'Ошибка при обработке записи {err}'
        )


def gsm_handler(record, date, message):
    print(f'Это актуализация уровня {record}')



def tank_parse(tank_name):
    tank_types = tanks.find().distinct('type')
