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
csrf = '345a589d1c287396bf4ba870db8e8ac49a426705c3bf7eeefd424457b5476a25.8d802db0ffa8fa03f0a4a0dd14b58f89faf23cd21a04f19d72b6f77e3f510df58ef30414e635e901f9d7576a0883033e47163adb1d7335d8252e6f400775c1f8c6d9ef9b2481a020a6d7b849452ce991741d09265dba2eee3bcba32495aa651284ce0c8c69e4bd3e43cf20cc06cc75f03a83ec7c6097cbf55824a61a25b416d2a14c1c1527c3943c373f21c218ec2cfb53221feebbb11f695dd6d4f4cec9df514c99bfcb3de5e4136a6d8972dde068765adc738288ad1854f6e4f91be4ce3c9f863019ed749741c6203fee46409677a351c2d228ae82e79dd6747322b9427bb0525d47cb7ff25afbf4f31c77ae423b9f8e58d2ae49c841db8d57177d673b7022'

token = auth_gid.find_one({'username': 'huji'}).get('access_token')

URL = "https://web.gid.ru/api/gratitude"
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
    'Referer: https://web.gid.ru/article/MxzAUoQ8wRNb',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
    # 'baggage: sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=1ecd4865d78e4d9a8c6f5dd8a04566ce',
    f'X-CSRF-TOKEN: {csrf}',
    f'Authorization: Bearer {token}',
    f'Cookie: X-CSRF-TOKEN={csrf}',
]


data = json.dumps({"isAnonymous": False, "recipientAccountId": "733cbc6a-0a87-4a1a-9ad1-1afebd3c01d1", "appreciation": "Коллега, спасибо тебе за то, что ты всегда находишь время для нас, даже когда у тебя самого его не хватает. Твоя способность находить баланс между работой и личной жизнью вдохновляет нас и помогает нам сохранять равновесие в нашей собственной жизни. Твоя поддержка и забота о нас делают нашу работу еще более приятной и продуктивной. Спасибо тебе!"}).encode()


def send_gratitude_func():
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


send_gratitude_func()


"""
сервер возвращает такое
{
	"createdAt": "2024-02-26T13:41:20.891Z",
	"updatedAt": "2024-02-26T13:41:20.891Z",
	"id": "c541b048-d643-4c66-b4ab-851cd6339a10",
	"senderId": "8d68107c-b224-4817-93d2-7144bc428dc3",
	"recipient": "Заяц Денис Сергеевич",
	"appreciation": "Спс!",
	"isAnonymous": false,
	"senderPhotoUrl": "public/photo/4859cc0d-26a6-448b-9354-ae3f5e1dcec3.jpg",
	"recipientPhotoUrl": null,
	"recipientAccountId": "33a4e1fb-5909-4c25-b4e8-62fad4c7b17f",
	"senderAccountId": "a2ad3873-ba7a-4af3-a154-3597ee733792",
	"isViewed": false,
	"isDeleted": false,
	"category": null
}
"""
