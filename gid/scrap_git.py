import pycurl
from io import BytesIO
import certifi
import json

# data = json.dumps({"content": "ok"})  # для комментов
data = json.dumps({"isAnonymous": False, "recipientAccountId": "733cbc6a-0a87-4a1a-9ad1-1afebd3c01d1", "appreciation": "Это бот"}).encode()
# data = json.dumps({"type": "like"})  # для лайков
# data = json.dumps({"content": "ок"})  # для реакций на комменты


token = 'Bearer ..'
csrf = '.'

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
