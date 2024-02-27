import re
import datetime as dt
import time
from gid.send_gratitude import send_gratitude_func

import keyboards.for_oil as kb
import utils.pipelines as pipeline

from math import pi, sqrt, pow, acos, sin, degrees, radians
from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import AiogramError

from config.telegram_config import CHAT_ID, ADMIN_TELEGRAM_ID, MESSAGE_THREAD_ID
from config.mongo_config import tanks, oil_actions
from pymongo.errors import PyMongoError
from utils import constants as const
from config.bot_config import bot


router = Router()


@router.message(Command('qwerty'))
async def manual_refresh_token(message):
    print('ccc')
    await send_gratitude_func()

@router.message(
    Command('oil'),
    # (F.message_thread_id == int(MESSAGE_THREAD_ID)) & (F.chat.id == int(CHAT_ID))
)
async def oil_level_show(message: Message):
    await message.delete()
    res_text = '<b>Количество масла в МБ ГПА:</b>\n'
    gpa_queryset = tanks.aggregate(pipeline.GPA_PIPELINE)
    for rec in gpa_queryset:
        tank_text = f'<u>ГПА №{rec["_id"]}:</u>'
        for tank in rec['tanks']:
            t_type = tank['tank']
            t_vol = tank['vol']
            t_cal = tank['cal']
            t_level = int(t_vol / t_cal)
            t_date = tank['date'].strftime('%d.%m.%Y') if tank['date'] != '' else '30.11.2023'
            tank_text = f'{tank_text}\nМБ{t_type} <b>{t_vol}л / {t_level}мм</b> (<i>{t_date}</i>)'
        res_text = f'{res_text}{tank_text}\n'
    await message.answer(
        res_text,
        disable_notification=True,
        parse_mode=ParseMode.HTML,
        reply_markup=kb.unit_choose_kb('ГПА'),
    )


@router.message()
# @router.message((F.message_thread_id == int(MESSAGE_THREAD_ID)) & (F.chat.id == int(CHAT_ID)))
async def counting_oil(message: Message):
    load_ids = []
    count_objects = 0
    text = message.text
    check_date = re.search(r'\d{2}.\d{2}.\d{4}', text)
    date = dt.datetime.strptime(check_date[0], '%d.%m.%Y') if check_date else dt.datetime.today()
    actions = text.split('\n')
    for rec in actions:
        if re.match(r'\w+\s\d+/\d+\s\w+', rec.lower()):
            id = await load_handler(rec, date, message)
            load_ids.append(id)
        elif re.match(r'((?:гсм\w*|мх\w*|\dбпм\w*|\w*\d\d\w*)(?:\s\S-\d+){1,6})', rec.lower()):
            count_obj = await level_handler(rec, date, message)
            count_objects += count_obj
    await send_report(message, load_ids, count_objects)


async def send_report(message: Message, load_list: list, count_objects: int):
    if len(load_list) != 0 or count_objects > 0:
        if len(load_list) != 0:
            load_text = '\n<i><u>Раскачка масла:</u></i>\n'
            for id in load_list:
                rec = oil_actions.find_one({'_id': id})
                target = tanks.find_one({'_id': rec['target_id']})['description']
                cost = rec['cost']
                action = 'закачано' if rec['action'] == 'upload' else 'скачано'
                rec_text = f'{target}: {action} <b>{cost}</b> л.'
                load_text = f'{load_text}{rec_text}\n'
        else:
            load_text = ''
        if count_objects > 0:
            level_text = f'<i><u>Обновлено уровней:</u></i> <b>{count_objects}</b>'
        else:
            level_text = ''
        await message.answer(
            ('<b>Получены данные:</b>'
            f'{load_text}\n{level_text}'),
            parse_mode=ParseMode.HTML,
            disable_notification=True,
        )


async def load_handler(record, date, message):
    target, levels, source = record.split(' ')
    before_vol, after_vol = levels.split('/')
    load_params = {
        'tanks': (tank_parse(target), tank_parse(source)),  # [type, num, tank]
        'before_vol': int(before_vol),
        'after_vol': int(after_vol),
        'date': date
    }
    return await insert_records_db(load_params, message)


def tank_parse(record):
    tank_type = re.search(r'\D{2,3}', record)
    if (tank_type is None and len(record) == 3) or tank_type[0].lower() == 'гпа' or tank_type[0].lower() == 'та':
        return ['ГПА', record[-3:-1], record[-1]]
    elif tank_type[0].lower() == 'бпм':
        return ['БПМ', record[0], record[-1]]
    elif tank_type[0].lower() == 'гсм':
        return ['ГСМ', '5', record[-1]]
    elif tank_type[0].lower() == 'мх':
        return ['МХ', '5', record[-1]]
    elif tank_type[0].lower() == 'ац':
        return ['АЦ', '5', '0']  # это автоцистерна для пятого цеха
    else:
        return ['КОЛОДЕЦ', '5', '0']  # это безвозвратный расход для пятого цеха


async def insert_records_db(params, message: Message):
    target_tank, source_tank = params['tanks']
    before_vol = params['before_vol']
    after_vol = params['after_vol']
    action = 'download' if before_vol > after_vol else 'upload'
    target_id, caliber = update_target(target_tank, after_vol, params['date'])
    cost = before_vol - after_vol
    cost = int(max(cost, -cost) * caliber)
    source_id = update_source(source_tank, cost, params['date'], action)
    record = oil_actions.insert_one(
        {
            'date': params['date'],
            'action': action,
            'target_id': target_id,
            'source_id': source_id,
            'user_id': message.from_user.id,
            'cost': cost,
        }
    )
    return record.inserted_id


def update_target(tank, after_vol, date):
    res = tanks.find_one({'type': tank[0], 'num': tank[1], 'tank': tank[2].upper()})
    tank_id = res['_id']
    caliber = res['calibration']
    volume = int(after_vol * caliber)
    if tank[0].upper() == 'ГСМ':
        volume = gsm_vol_calc(volume, tank[2])
    tanks.update_one(
        {'type': tank[0], 'num': tank[1], 'tank': tank[2].upper()},
        {'$set': {'cur_volume': volume, 'last_update': date}},
    )
    return [tank_id, caliber]


def update_source(tank, cost, date, action):
    res = tanks.find_one({'type': tank[0], 'num': tank[1], 'tank': tank[2].upper()})
    cur_volume = res['cur_volume']
    volume = cur_volume + cost if action == 'download' else cur_volume - cost
    tanks.update_one(
        {'type': tank[0], 'num': tank[1], 'tank': tank[2].upper()},
        {'$set': {'cur_volume': volume, 'last_update': date}},
    )
    return res['_id']


async def level_handler(record, date, message: Message):
    count_level = 0
    gpa_check = re.fullmatch(r'\w+\s(?:д|н)-\d{1,3}\s(?:д|н)-\d{1,3}', record.lower())
    unit_check = re.fullmatch(r'((?:гсм\w*|мх\w*|\w*\dбпм\w*)(?:\s\d-\d*){1,6})', record.lower())
    if gpa_check:
        gpa_num = re.search(r'\d\d', record)[0]
        unit_tanks = re.findall(r'(?:д-|н-)\d+', record.lower())
        is_work = False if record.find('р') == -1 else True
        update_level(unit_tanks, 'ГПА', gpa_num, date, is_work)
        count_level += 1
    elif unit_check:
        unit = re.search(r'(?:гсм|мх|\dбпм)', record.lower())[0]
        unit_tanks = re.findall(r'\d-\d+', record)
        unit_type = unit if unit.isalpha() else unit[1:]
        unit_num = '5' if unit.isalpha() else unit[0]  # все относится к пятому КЦ
        update_level(unit_tanks, unit_type, unit_num, date)
        count_level += 1
    else:
        msg = await message.answer(
            f'Ошибка обработки записи "{record}"\nВнесите запись согласно шаблону',
            disable_notification=True
        )
        time.sleep(10)
        await bot.delete_message(msg.chat.id, msg.message_id)
    return count_level


def update_level(unit_tanks, unit_type, unit_num, date, is_work=False):
    for rec in unit_tanks:
        tank, vol = rec.split('-')
        res = tanks.find_one({'type': unit_type.upper(), 'num': unit_num, 'tank': tank.upper()})
        caliber = res['calibration']
        last_vol = res['cur_volume']
        last_is_work = res['is_work']
        real_vol = int(int(vol) * caliber)
        if ((tank.upper() == 'Д' and last_vol > real_vol)
            or (tank.upper() == 'Н' and last_is_work == is_work and last_vol > real_vol)):
            cost = last_vol - real_vol
            insert_oil_outlay(cost, date, res['_id'])
        if tank.upper() == 'Н' and last_is_work is True and is_work is False and last_vol > (real_vol - 1252):
            cost = last_vol - (real_vol - 1252)
            insert_oil_outlay(cost, date, res['_id'])
        if tank.upper() == 'Н' and last_is_work is False and is_work is True and (last_vol - 1252) > real_vol:
            cost = last_vol - 1252 - real_vol
            insert_oil_outlay(cost, date, res['_id'])
        if unit_type.upper() == 'ГСМ':
            real_vol = gsm_vol_calc(int(vol), tank)
        try:
            tanks.update_one(
                {'type': unit_type.upper(), 'num': unit_num, 'tank': tank.upper()},
                {'$set': {'cur_volume': real_vol, 'last_update': date, 'is_work': is_work}},
            )
        except PyMongoError:
            pass


def insert_oil_outlay(cost, date, tank_id):
    target_id = tanks.find_one({'type': 'КОЛОДЕЦ'})['_id']
    record = oil_actions.insert_one(
        {
            'date': date,
            'action': 'outlay',
            'target_id': target_id,
            'source_id': tank_id,
            'user_id': int(ADMIN_TELEGRAM_ID),
            'cost': cost,
        }
    )
    return record.inserted_id



def gsm_vol_calc(level, num_tank):
    l = const.GSM_TANKS[num_tank]['length']
    r = const.GSM_TANKS[num_tank]['radius']
    full_s = pi * pow(r, 2)
    # определение стороны
    a = 2 * sqrt(pow(r, 2) - pow((r - level), 2))
    #  определение угла раскрытия
    beta = 180 - (2 * degrees(acos(a / (2 * r))))
    # определение площади сегмента
    s = (pow(r, 2) / 2) * (pi * (beta / 180) - sin(radians(beta)))
    if level > r:
        s = full_s - s
    # определение объёма
    v = int(s * l / 1000000)
    return v


@router.callback_query(F.data.startswith('close'))
async def report_close(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.delete()


@router.callback_query(F.data.startswith('choose_'))
async def change_unit(callback: CallbackQuery):
    _, unit = callback.data.split('_')
    if unit == 'gpa':
        unit_kb = 'ГПА'
        res_text = '<b>Количество масла в МБ ГПА:</b>\n'
        queryset = tanks.aggregate(pipeline.GPA_PIPELINE)
        for rec in queryset:
            tank_text = f'<u>ГПА №{rec["_id"]}:</u>'
            for tank in rec['tanks']:
                t_type = tank['tank']
                t_vol = tank['vol']
                t_cal = tank['cal']
                t_level = int(t_vol / t_cal)
                t_date = tank['date'].strftime('%d.%m.%Y') if tank['date'] != '' else '30.11.2023'
                tank_text = f'{tank_text}\nМБ{t_type} <b>{t_vol}л / {t_level}мм</b> (<i>{t_date}</i>)'
            res_text = f'{res_text}{tank_text}\n'
    elif unit == 'bpm':
        unit_kb = 'БПМ'
        res_text = '<b>Количество масла в БПМ:</b>\n'
        queryset = tanks.aggregate(pipeline.BPM_PIPELINE)
        for rec in queryset:
            tank_text = f'<u>БПМ №{rec["_id"]}:</u>'
            for tank in rec['tanks']:
                t_type = tank['tank']
                t_vol = tank['vol']
                t_cal = tank['cal']
                t_level = int(t_vol / t_cal)
                t_date = tank['date'].strftime('%d.%m.%Y') if tank['date'] != '' else '30.11.2023'
                tank_text = f'{tank_text}\nБак №{t_type} <b>{t_vol}л / {t_level}мм</b> (<i>{t_date}</i>)'
            res_text = f'{res_text}{tank_text}\n'
    elif unit == 'gsm':
        unit_kb = 'ГСМ'
        res_text = '<b>Количество масла на складе ГСМ:</b>\n'
        queryset = tanks.aggregate(pipeline.GSM_PIPELINE)
        for tank in queryset:
            tank_text = ''
            for param in tank['data']:
                t_vol = param['vol']
                t_cal = param['cal']
                t_level = int(t_vol / t_cal)
                t_date = param['date'].strftime('%d.%m.%Y') if param['date'] != '' else '30.11.2023'
                tank_text = f'{tank_text}<u>Емк №{tank["_id"]}:</u>\n<b>{t_vol} л</b> (<i>{t_date}</i>)'
            res_text = f'{res_text}{tank_text}\n'
    elif unit == 'mh':
        unit_kb = 'МХ'
        res_text = '<b>Количество масла в м/х КЦ-6:</b>\n'
        queryset = tanks.aggregate(pipeline.MH_PIPELINE)
        for tank in queryset:
            tank_text = ''
            for param in tank['data']:
                t_vol = param['vol']
                t_cal = param['cal']
                t_level = int(t_vol / t_cal)
                t_date = param['date'].strftime('%d.%m.%Y') if param['date'] != '' else '30.11.2023'
                tank_text = f'{tank_text}<u>Бак №{tank["_id"]}:</u> <b>{t_vol} л / {t_level}мм</b> (<i>{t_date}</i>)'
            res_text = f'{res_text}{tank_text}\n'
    try:
        await callback.message.edit_text(
            res_text,
            parse_mode=ParseMode.HTML,
            reply_markup=kb.unit_choose_kb(unit_kb),
        )
    except AiogramError as err:
        pass
