from handlers.get_response import get_response

from config.bot_config import bot
from config.telegram_config import ADMIN_TELEGRAM_ID


PROFILE_URL = 'https://web.gid.ru/api/loyalty/public/v1/profile'
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
]

async def get_profile(user_id, username):
    resp_code, resp_data = get_response(PROFILE_URL, add_headers=ADD_HEADERS, user_id=user_id)
    if resp_code == 200:
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'Ресурсы пользователя {username}\nЭнергия: {resp_data["energy"]}\nБаллы: {resp_data["power"]}',
        )
    # else:
    #     await bot.send_message(
    #         ADMIN_TELEGRAM_ID,
    #         f'Получение информации об энергии: {resp_data["error"]}',
    #     )
