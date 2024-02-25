import pycurl
from io import BytesIO
import certifi
import json

# data = json.dumps({"content": "ok"})  # для комментов
data = json.dumps({"isAnonymous": False, "recipientAccountId": "733cbc6a-0a87-4a1a-9ad1-1afebd3c01d1", "appreciation": "Спасибо"}).encode()
# data = json.dumps({"type": "like"})  # для лайков
# data = json.dumps({"content": "ок"})  # для реакций на комменты


token = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg4NjY5MDYsImlhdCI6MTcwODg2NTEwNiwiYXV0aF90aW1lIjoxNzA4Nzk4Njk5LCJqdGkiOiJhMWFlODE0Yi1iZDdiLTQwZjctYTBkMi1mODExODdlYTg0NDciLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiJmYWE5MjAyNi1mNjI3LTQ5ZjAtODQ1Ny01YzcyYmNhYTJjNjAiLCJzZXNzaW9uX3N0YXRlIjoiNjdmYTQ5NmMtODExYi00OGM3LTkxYjItZTg4MzUwNDY5YzFkIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6IjY3ZmE0OTZjLTgxMWItNDhjNy05MWIyLWU4ODM1MDQ2OWMxZCJ9.Jh4liKotDxUKDcUMZK3MJqfb_5vnahCoOS7-DKfC_Mom6pIR3uNbRu-gF3rFf0MoUemWcUGXVBLZFYZpPmp1Km9_Ji17-Wch3CFQT19htMACuFDxSwLQ-_y6Mm9ZEQQGVBuPLJhtEstzqwrAT4Es-PP1m3f_l2ZCX_nejKbD-qscIaSKKaMazvSzlGjYZtb_b2zwUWQYm5Vu5v23k2ZzfRx-9_SfMG9QS_rdWtTOlfBvHM6xwJmUz0fM9hYX9FPCvLajqKM0er89JLlSD8Z9FH5WNnvlW9v4gid3BspfXH4WOr50RR1h9n5t30NvuZAXEnRl_sxatlpL_rzNxgh56w'
csrf = 'e07d0679f5fa4224caf0791c272c1c789bb3e28f3a7233a306b6eeea7cbf5b3a.7c7bae441bc95fbaa674fcc563251239d74f9323687e9d963788f82d8d87b4493645ddb63cb160fcac6387e240251abb1f6af8459c7e08fd979598be3425d299af8cb4a98f4f834926e8aabbf807f664094ac9e52765ce96677e1e3bc97c51d803da0969e147957ea1bbd9ec6c5177138fb36730559fcc05a48e390735d0cb32e719de829b8a80e9e00bd53eb440285e19344b78d471119b3fcc731f099b1fdda740ec17e3c48bcfac7e53f3902f7bec95d4f805c8174d34b93a642eac1dabb3f8ed8aad7d6f88f4c9c003294e3c5d8fbf3e6530866ae995bdd8c87c78313f088b338fa696a927560185615b7caff70708051e4315056814380e459ee94d672c'

def get_git():
    # url = "https://web.gid.ru/api/feed/I7GXl8iFfvMS/reactions"
    url = "https://web.gid.ru/api/gratitude"
    # url = "https://web.gid.ru/api/feed/I7GXl8iFfvMS/comments/{айди пользователя}/replies"
    # url = "https://web.gid.ru/api/feed/MxzAUoQ8wRNb/comments"
    # url = "https://web.gid.ru/api/loyalty/public/v1/profile"
    # url = 'https://web.gid.ru/api/event-tracker/public/v1/collect'  # для начисления баллов
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER,
        [
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
            'Accept: application/json, text/plain, */*',
            'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type: application/json; charset=utf-8',
            # 'Referer: https://web.gid.ru/article/MxzAUoQ8wRNb',
            'X-Requested-With: XMLHttpRequest',
            f'X-CSRF-TOKEN: {csrf}',
            'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
            'baggage: sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=1ecd4865d78e4d9a8c6f5dd8a04566ce',
            'Origin: https://web.gid.ru',
            'DNT: 1',
            'Sec-Fetch-Dest: empty',
            'Sec-Fetch-Mode: cors',
            'Sec-Fetch-Site: same-origin',
            f'Authorization: {token}',
            'Connection: keep-alive',
            f'Cookie: X-CSRF-TOKEN={csrf}',
            'TE: trailers',
        ]
    )
    c.setopt(c.POST, 1)
    c.setopt(c.TIMEOUT_MS, 3000)
    c.setopt(c.POSTFIELDS, data)
    c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
    c.perform()
    print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
    c.close()
    body = buffer.getvalue()
    print(body.decode('utf-8'))


get_git()
