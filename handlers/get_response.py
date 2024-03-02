import json
import random
import time
from io import BytesIO

import certifi
import pycurl
from aiogram import Router
from aiogram.filters import Command
from langchain.chat_models.gigachat import GigaChat
from langchain.schema import SystemMessage
from config.gid_config import MY_GID_ID

from config.mongo_config import auth_gid
from utils.constants import HEADERS


def get_response(url, method='GET', fields_data='', no_data=False, add_headers=[], user_id=MY_GID_ID):
    time.sleep(5)
    auth_param = auth_gid.find_one({'gid_id': user_id})
    token = auth_param['access_token']
    csrf = auth_param['csrf']
    auth_headers = [
        f'X-CSRF-TOKEN: {csrf}',
        f'Authorization: Bearer {token}',
        f'Cookie: X-CSRF-TOKEN={csrf}',
    ]
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER, HEADERS + add_headers + auth_headers)
    c.setopt(c.TIMEOUT_MS, 10000)
    c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
    if method == 'PUT':
        c.setopt(c.CUSTOMREQUEST, 'PUT')
        c.setopt(c.POSTFIELDS, fields_data)
    if method == 'POST':
        c.setopt(c.POST, 1)
        c.setopt(c.POSTFIELDS, fields_data)
    c.perform()
    resp_code = c.getinfo(c.RESPONSE_CODE)
    body = buffer.getvalue()
    c.close()
    if no_data:
        return resp_code
    resp_data = json.loads(body.decode())
    return (resp_code, resp_data)
