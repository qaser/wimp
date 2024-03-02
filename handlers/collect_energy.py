import datetime as dt
import json
from io import BytesIO
import uuid

import certifi
import pycurl

from config.bot_config import bot
from config.gid_config import MY_GID_ID
from config.mongo_config import auth_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from utils.constants import HEADERS

URL = 'https://web.gid.ru/api/event-tracker/public/v1/collect'

ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/my-resource/thanks',
    'X-Requested-With: XMLHttpRequest',
]


def get_request_data_comment(user_id):
    data = json.dumps({
        'batch': [
            {
                'anonymousId': '923f1183-d088-402a-8928-e33d5824de37',
                'event': 'news_comment_send',
                'messageId': '466bd2ad-4f23-44fe-a16d-3d8ae7d04535',
                    'properties': {
                        'replay': ''
                    },
                'timestamp': '2024-03-02T16:21:29.916Z',
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': '2024-03-02T16:21:29.916Z',
        'writeKey': 'sdk'}).encode()
    return data


def get_request_data_thanks(user_id):
    data = json.dumps({
        'batch': [
            {
                'anonymousId': '3264914a-d571-435f-ae9e-f73b970a3821',
                'event': 'thanks_new_create_click',
                'messageId': '1b038208-8e0c-4037-8f25-a6712fd33d70',
                'properties': {
                    'recipient': '83e1d148-d173-401b-9d16-a97547e8907d'
                },
                'timestamp': '2024-03-02T16:21:29.916Z',
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': '2024-03-02T16:21:29.916Z',
        'writeKey': 'sdk'}).encode()
    return data


def get_request_data_reaction(user_id):
    data = json.dumps({
        'batch': [
            {
                'anonymousId': 'ace33759-1301-464d-a8dd-9e7f9b92c543',
                'event': 'reaction_comment_click',
                'messageId': '161ade63-ea81-430d-b8ac-f998ab0a336c',
                'properties': {
                    'replay': 'aae15b58-9f04-4685-8dc6-2175db7ac79a'
                },
                'timestamp': '2024-03-02T17:24:52.967Z',
                'type': 'track',
                'userId': f'[{user_id},80f8a415-c1ad-4d70-957b-587e42f6ac03]'
            }
        ],
        'sentAt': '2024-03-02T16:21:29.916Z',
        'writeKey': 'sdk'}).encode()
    return data


async def collect_energy_func(user_id, event):
    user = auth_gid.find_one({'gid_id': user_id})
    token = user.get('access_token')
    csrf = user.get('csrf')
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
    c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
    if event == 'news_comment_send':
        c.setopt(c.POSTFIELDS, get_request_data_comment(user_id))
    elif event == 'thanks_new_create_click':
        c.setopt(c.POSTFIELDS, get_request_data_thanks(user_id))
    elif event == 'reaction_comment_click':
        c.setopt(c.POSTFIELDS, get_request_data_reaction(user_id))
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



{
	'batch': [
		{
			"anonymousId": "ace33759-1301-464d-a8dd-9e7f9b92c543",
			"event": "reaction_comment_click",
			"messageId": "161ade63-ea81-430d-b8ac-f998ab0a336c",
			"properties": {
				"replay": "aae15b58-9f04-4685-8dc6-2175db7ac79a"
			},
			"timestamp": "2024-03-02T17:24:52.967Z",
			"type": "track",
			"userId": "[a2ad3873-ba7a-4af3-a154-3597ee733792,80f8a415-c1ad-4d70-957b-587e42f6ac03]"
		}
	],
	"sentAt": "2024-03-02T17:24:52.967Z",
	"writeKey": "sdk"
}
