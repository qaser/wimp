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
csrf = '24b66c5ef3777c6c6cda206f79d52fc382d78a5553e96a17691534aa7e54ca1f.b9492edad0a8880da46821366993888c68e6f55fef4eb8b8ba29d42b7a6956adf93c499e903803d84bfcc2e8a9a467662c104fd6198cea5b29803f3d37dabf69aff4462806032dbb17842b21ed7472f7da170e5ed70956052384a87a709449267e94f84180959e83ad2a9980152eb8b98494c7f67f3a3f2983cc39d78899a64a552434107e3451c8f8308076ecf210f97380c199fbe9b54109d9a7640b9dae520ae133f89d5c8db2c3f895c9547a785065d8347517303752d8e7a6f1d80aebc3a638e92aabc58dd99f734243ca17973d86c638a4d87fed64f067179b487f0a60522724824cbc32c7fac746c9cd731037eb79fa7403a6b1480b013f1c47476c6c'

# token = auth_gid.find_one({'username': 'huji'}).get('access_token')
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDkxMDQyMzksImlhdCI6MTcwOTEwMjQzOSwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJjM2FhOGI3My0xYzEwLTRiYWEtYmI0NC04NTQ5MWVjNDVhYjUiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiJlOTRlMTVjMi1kNTEzLTRjYWMtODk3MS1hMzg4M2U3NzBlNGEiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.bl-OL6Zi7D819EA1U24yzlXk6PuRf9PcwNHj6VaGXC1ZgY7IFdsz7isoGCTIBYH1gg3ZovvYMnkVVzAajvheqzwtAFVerAkbKEXBG4MVhSPprtrSSCeKFUdwDZxYVL2jftwKIidA7WF1YTZAHpgSRgLficFOVP4JgigcuJKGpH2ozpQrKzUMIOK_uF8XsAfV_3vMBO-Mhc1AxkHMDAou1T7YaPNvWGxcvgF36Y3FplnBRzQCEJqUgRF1eehV-TC1pqZGY5K5SX5mZaUtr6Egm-Xjh1vUSQ_OuohXIQEpTNlxiHVbr6jbvqgDaPB2pFeBeKetae4qlRjJtDt6ZfEL7w'

URL = "https://web.gid.ru/api/lms/v2/courses/f0ef3232-078b-403a-bb65-9fcf29d84f12"
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
    'Referer: https://web.gid.ru/sputnik/courses/',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
    # 'baggage: sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=1ecd4865d78e4d9a8c6f5dd8a04566ce',
    f'X-CSRF-TOKEN: {csrf}',
    f'Authorization: Bearer {token}',
    f'Cookie: X-CSRF-TOKEN={csrf}',
]


data = json.dumps('{action:finish}')


def collect_energy_func():
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, URL)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS)
    c.setopt(c.PUT, 1)
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
