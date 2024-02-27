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
csrf = 'f9debdc7b3eab9cd21e0b8a79991e983070934503aa112f75ca6f97d8b5e2fcf.4b8d3001c5399ebb9fe0dfb4d8e267219e167a95efa3280a4e7198badeec3c52ae5e0c1256c64067bb6e771a3f515a01f31142bca0b2344893ee231acabf4ecf424aa24072fe4d61ebc194166d2b4df0c80fc4ec519a74cb954157cf5d6eb510eee57822cee2173b7149c53c7071545c6804a9e7bb2fea4305e0735846fc8d01da81e870aca431e5b3d800d7126e58e5ff6d101e7a38f501e12c8a6133218b22957a4f7b371d4f4ebfcc7b8ef4764f3bf140a533d7d3f94452da6bd1e919e6609fa3a4ef9c428ce8b67ccdd4de9f45b5a9a92a245e671ac76687ca0bf7e9743b813009275e81199af276d374b77734db18a551f31153c53631c6795d7ecc65f8'

# token = auth_gid.find_one({'username': 'huji'}).get('access_token')
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDkwNTM5ODYsImlhdCI6MTcwOTA1MjE4NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiI0MDdjYmJmMy1lZjVlLTRhYzgtYTE4Ny1kN2ZhYTMxOWFkNzAiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiIxZDBhMDIzMy05MjkyLTQ5ZjItYWEzOS05MTliZWUxNWJiOGEiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.KfkEvYLeqtQepyaC42W6sEm77JGtrNsKIhKbULAQinkiG8yDeb9SRTUCsaGGgYPoO6KyaQ-OmwONMxUutSK85zPnAgmiHSvdnUFNaeRcwTnTB8k1f-enkO34yaDn-USAPxZyR9T_6cf7grQora41_1FGlPhf8DTmwc0V_Dq7qLslPCd5aZDmV9Y0Ok7xn2zPtxk_s1M2GukE98R8aSLd1zrgY_RLFbOPx_Y-tW7TqoRHYk3pwQ2mnDuZjUSdJ5bju44p_y6Ja4EsMFaVcICVXgTwkzhjJDYDeqqy4M7HE25DiheQFokLwaDblPRRU04UhTWQsTJznY0H5vJQHmgBsw'

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
                    "recipient": "a2ad3873-ba7a-4af3-a154-3597ee733792"
                },
                "timestamp": "2024-02-27T13:41:19.850Z",
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
