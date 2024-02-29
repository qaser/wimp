import datetime as dt
import json
from io import BytesIO

import certifi
import pycurl

from config.bot_config import bot
from config.mongo_config import auth_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from utils.constants import HEADERS

URL = "https://web.gid.ru/api/event-tracker/public/v1/collect"

ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/my-resource/thanks',
    'X-Requested-With: XMLHttpRequest',
]


def get_request_data(user_id, recipient_id):
    date = str(dt.datetime.now())
    data = json.dumps({
        'batch': [
            {
                'anonymousId': 'cf0c67b1-80a5-4c4b-b5af-58c324e345ba',
                'event': 'thanks_new_create_click',
                'messageId': 'e824954c-b3c9-4ea2-8905-40438c85adc1',
                'properties': {
                    'recipient': recipient_id
                },
                'timestamp': date,
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': date,
        'writeKey': 'sdk'}).encode()
    return data


async def collect_energy_func(user_id, recipient_id):
    token = auth_gid.find_one({'username': 'huji'}).get('access_token')
    csrf = auth_gid.find_one({'username': 'huji'}).get('csrf')
    headers_with_tokens = [
        f'X-CSRF-TOKEN: {csrf}',
        f'Authorization: Bearer {token}',
        f'Cookie: X-CSRF-TOKEN={csrf}',
    ]
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, URL)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS + headers_with_tokens)
    c.setopt(c.POST, 1)
    c.setopt(c.TIMEOUT_MS, 10000)
    c.setopt(c.POSTFIELDS, get_request_data(user_id, recipient_id))
    c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
    c.perform()
    resp_code = c.getinfo(c.RESPONSE_CODE)
    body = buffer.getvalue()
    body_str = body.decode('utf-8')
    c.close()
    await bot.send_message(
        chat_id=ADMIN_TELEGRAM_ID,
        text=f'Статус {resp_code}\n{body_str}',
        disable_notification=True
    )
