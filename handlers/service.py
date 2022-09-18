from aiogram import Dispatcher, types

from config.bot_config import bot
from config.mongo_config import users
from config.telegram_config import CHAT_ID
from texts.initial import SERVICE_END_TEXT, SERVICE_TEXT


async def service_handler(message: types.Message):
    await bot.send_message(chat_id=CHAT_ID, text=SERVICE_TEXT)


async def service_end_handler(message: types.Message):
    await bot.send_message(chat_id=CHAT_ID, text=SERVICE_END_TEXT)


async def reset_handler(message: types.Message):
    await bot.send_message(
        message.chat.id,
        text='Сброс моих настроек выполнен',
        reply_markup=types.ReplyKeyboardRemove(),
    )


async def count_users(message: types.Message):
    queryset = list(users.find({}))
    users_count = len(queryset)
    final_text = ''
    for user in queryset:
        username = '{} {}'.format(user['first_name'], user['last_name'])
        final_text = '{}\n{}'.format(username, final_text)
    await message.answer(
        text=f'Количество пользователей в БД: {users_count}\n{final_text}'
    )


def register_handlers_service(dp: Dispatcher):
    dp.register_message_handler(service_end_handler, commands='service_end')
    dp.register_message_handler(service_handler, commands='service')
    dp.register_message_handler(reset_handler, commands='reset')
    dp.register_message_handler(count_users, commands='users')
