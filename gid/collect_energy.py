import pycurl
from io import BytesIO
import certifi
import json
# from .constants import HEADERS
import pymongo

client = pymongo.MongoClient('localhost', 27017)
gid_db = client['gid_db']
auth_gid = gid_db['auth']
cookies_gid = gid_db['cookies']
users_gid = gid_db['users']
csrf = 'dc2b7f5a39a2e9e9253812caba6ffe02ad8f4a41c54a3ea113a32f078adce3e6.9fc11d20084007878ea84080387b42e05de88d947746a74d1bf68a37e800a7aba06c5144ff31e2516250d0f4ea36115065296fca1dab631afeb51740f58e29d1264dba433e2c0b210fc28553feefabc27628993aff947477d93d4436c333b3efd2ce7f88a47ac31c1ff3efaa9d8d495b0e7167fe5d18561b17ac988252562806853065660fdc585d8703b11a52c24e0a2ccfd8c1929f6dfaee3d8fdf8f1fa3499475e0caa339bb998f962eacec8aa6ac8177ee2979c60e5665f81880749e252abff15082cf9403614278a7d067ca228b1765c28b588f7274ac5ebffc30d1c2129589e4b5850b2c676448b9aa4690a0b9ae78977223c15692dc54838e6f7f5fa3'

# token = auth_gid.find_one({'username': 'huji'}).get('access_token')
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDkxMDIxMjYsImlhdCI6MTcwOTEwMDMyNiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiIwYmJhMTk3Ni01M2YwLTQ0ZDUtOWRkNC0xYmFkMDA4Mzc0NWYiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI1MjEzZWZkOS02ZjMxLTQ2NzItODFiNC02NmQ0ZTU4NmY2N2QiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.eBCRN8J8kDdgzPFMCr6igUslg8CVzNRbjcGfsAaDqHh8gw6bXhTn1q2zt8fjoXfv3g2n-lPvc_OwqZZUCPfgYdER_pZn9WRJkAn4HW5mv1fdD_txoFYdc8hB8F0-TxYG74T0rD34XP7nqJKy6yPmt31rTeodXJdrdH6O2bLEg8D0ttFHZo7wUD3uL1E-gYNkWfBbHtDGy4hZTbww-xSGPCKhFknaxlnCGiIJh8Qx3UgSSLQNCFPY7Spy7nXZMT3Wc8VcH_XyiC1a0vUVbfNjmfA8Aita3ntfRVMWzMNuiXrVnmIntY02xPS_3LU0uQVGOEHUfCLZ_dYfOwM8QVyPwA'

URL = "https://web.gid.ru/api/event-tracker/public/v1/collect"
HEADERS = [
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Origin: https://web.gid.ru',
    'DNT: 1',
    'Sec-Fetch-Dest: empty',
    'Sec-Fetch-Mode: cors',
    'Sec-Fetch-Site: same-site',
    'Connection: keep-alive',
    'TE: trailers',
]
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/my-resource/thanks',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
    # 'baggage: sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=1ecd4865d78e4d9a8c6f5dd8a04566ce',
    f'X-CSRF-TOKEN: {csrf}',
    f'Authorization: Bearer {token}',
    f'Cookie: X-CSRF-TOKEN={csrf}',
]


data = json.dumps(
    {
        "batch": [
            {
                "anonymousId": "cf0c67b1-80a5-4c4b-b5af-58c324e345ba",
                "event": "thanks_new_create_click",
                "messageId": "e824954c-b3c9-4ea2-8905-40438c85adc1",
                "properties": {
                    "recipient": "733cbc6a-0a87-4a1a-9ad1-1afebd3c01d1"
                },
                "timestamp": "2024-02-28T13:41:19.850Z",
                "type": "track",
                "userId": "[a2ad3873-ba7a-4af3-a154-3597ee733792,80f8a415-c1ad-4d70-957b-587e42f6ac03]"
            }
        ],
        "sentAt": "2024-02-26T13:41:19.850Z",
        "writeKey": "sdk"
    }
).encode()


def collect_energy_func():
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, URL)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS)
    c.setopt(c.POST, 1)
    c.setopt(c.TIMEOUT_MS, 10000)
    c.setopt(c.POSTFIELDS, data)
    c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
    c.perform()
    print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
    c.close()
    body = buffer.getvalue()
    print(body.decode('utf-8'))


collect_energy_func()


'''
    "createdAt": "2024-02-26T13:41:20.891Z",
	"updatedAt": "2024-02-26T13:41:20.891Z",
	"id": "c541b048-d643-4c66-b4ab-851cd6339a10",
	"senderId": "8d68107c-b224-4817-93d2-7144bc428dc3",
	"senderPhotoUrl": "public/photo/4859cc0d-26a6-448b-9354-ae3f5e1dcec3.jpg",
	"recipientPhotoUrl": null,
	"recipientAccountId": "33a4e1fb-5909-4c25-b4e8-62fad4c7b17f",
	"senderAccountId": "a2ad3873-ba7a-4af3-a154-3597ee733792",
'''
