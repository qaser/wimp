import datetime as dt

import keyboards.for_gpa_params as kb

from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config.mongo_config import gpa_params
from utils import constants as const
from config.bot_config import bot


router = Router()


class Parameter(StatesGroup):
    value = State()


@router.message(Command('obhod'))
async def inspect(message: Message):
    await message.delete()
    await message.answer(
        'Выберите желаемое действие:',
        reply_markup=kb.main_menu()
    )


@router.callback_query(F.data.startswith('inspect_'))
async def get_gpa_num(call: CallbackQuery):
    _, choose = call.data.split('_')
    await call.message.edit_text(
        text='Выберите номер ГПА:',
        reply_markup=kb.num_gpa_menu(choose)
    )


@router.callback_query(F.data.startswith('choose_'))
async def get_params(call: CallbackQuery):
    _, choose, gpa_num = call.data.split('_')
    user_id = call.message.chat.id
    if choose == 'new':
        gpa_params.update_one(
            {'user_id': user_id, 'gpa_num': gpa_num},
            {'$set': {
                'date': dt.datetime.now(),
                'params': {
                    'fsn': '',
                    'fun': '',
                    'mbd': '',
                    'fsd': '',
                    'mbn': '',
                    'rso': '',
                    'dst': '',
                    'dvh': '',
                }
            }},
            upsert=True
        )
        doc = gpa_params.find_one({'user_id': user_id, 'gpa_num': gpa_num})
        params = doc['params'].keys()
        await call.message.edit_text(
            text='Выберите контролируемый параметр',
            reply_markup=kb.params_menu(gpa_num, params),
        )
    else:
        doc = gpa_params.find_one({'user_id': user_id, 'gpa_num': gpa_num})
        if doc is not None:
            params_text = ''
            params = doc['params']
            for key, value in params.items():
                p_name = const.GPA_PARAMS[key]
                text = f'<b>{p_name}</b>: <i>{value}</i>'
                params_text = f'{params_text}{text}\n'
            final_text = f'<u>ГПА {gpa_num}</u>\n{params_text}'
            await call.message.edit_text(
                text=f'Ранее введенные параметры:\n{final_text}\n\n/obhod',
                parse_mode=ParseMode.HTML,
            )
        else:
            await call.message.edit_text(
                text=f'Для этого ГПА Вы не вводили данных\n',
                reply_markup=kb.num_gpa_menu('last')
            )


@router.callback_query(F.data.startswith('params_'))
async def get_params(call: CallbackQuery, state: FSMContext):
    _, gpa_num, parameter = call.data.split('_')
    await state.update_data(gpa_num=gpa_num)
    await state.update_data(parameter=parameter)
    if parameter == 'stop':
        user_id = call.message.chat.id
        doc = gpa_params.find_one({'user_id': user_id, 'gpa_num': gpa_num})
        params_text = ''
        params = doc['params']
        for key, value in params.items():
            p_name = const.GPA_PARAMS[key]
            text = f'<b>{p_name}</b>: <i>{value}</i>'
            params_text = f'{params_text}{text}\n'
        final_text = f'<u>ГПА {gpa_num}</u>\n{params_text}'
        await call.message.answer(
            text=f'Введенные параметры:\n{final_text}',
            parse_mode=ParseMode.HTML,
        )
        await call.message.answer('Если необходимо внести данные другого ГПА нажмите /obhod')
    else:
        msg = await call.message.edit_text(
            text='Введите значение параметра',
            reply_markup=kb.close_menu(),
        )
        await state.update_data(msg_id=msg.message_id)
        await state.set_state(Parameter.value)


@router.message(Parameter.value)
async def get_value(message: Message, state: FSMContext):
    await state.update_data(value=message.text)
    buffer_data = await state.get_data()
    value = buffer_data['value']
    parameter = buffer_data['parameter']
    gpa_num = buffer_data['gpa_num']
    msg_id = buffer_data['msg_id']
    user_id = message.from_user.id
    await bot.delete_message(chat_id=user_id, message_id=msg_id)
    rec = gpa_params.find_one({'user_id': user_id, 'gpa_num': gpa_num})
    params = rec['params']
    params[parameter] = value
    empty_params = [key for key, value in params.items() if value == '']
    gpa_params.update_one(
        {'user_id': user_id, 'gpa_num': gpa_num},
        {'$set':{'date': dt.datetime.now(), 'params': params}},
    )
    await message.delete()
    if len(empty_params) == 0:
        doc = gpa_params.find_one({'user_id': user_id, 'gpa_num': gpa_num})
        params_text = ''
        params = doc['params']
        for key, value in params.items():
            p_name = const.GPA_PARAMS[key]
            text = f'<b>{p_name}</b>: <i>{value}</i>'
            params_text = f'{params_text}{text}\n'
        final_text = f'<u>ГПА {gpa_num}</u>\n{params_text}'
        await message.answer(
            text=f'Введенные параметры:\n{final_text}',
            parse_mode=ParseMode.HTML,
        )
        await message.answer('Если необходимо внести данные другого ГПА нажмите /obhod')
    else:
        await message.answer(
            text=f'Принято. Если необходимо выберите еще параметр',
            reply_markup=kb.params_menu(gpa_num, empty_params),
        )
