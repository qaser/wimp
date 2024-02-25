HEADERS = [
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    # 'Accept: */*',
    'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Content-Type: application/x-www-form-urlencoded',
    # 'Referer: https://web.gid.ru/',
    'Origin: https://web.gid.ru',
    'DNT: 1',
    'Sec-Fetch-Dest: empty',
    'Sec-Fetch-Mode: cors',
    'Sec-Fetch-Site: same-site',
    'Connection: keep-alive',
    'TE: trailers',
]


auth = {
	"Куки запроса": {
		"das_d_tag2": "63992525-d4bf-4040-853c-31137d0e67c4",
		"das_d_tag2_legacy": "63992525-d4bf-4040-853c-31137d0e67c4",
		"uwyiert": "eb17bff5-a03d-41f1-e2ea-a3fe79a37c71"
	}
}


code = '050373a9-0948-4c3d-b5b3-1d026f8a71a8  .  67fa496c-811b-48c7-91b2-e88350469c1d  .  0b5ac12b-3392-421d-b858-3b4227ee41eb'
code = '0a92e2ba-d3c5-46ac-a59e-9e902b7ec948  .  9640ff8b-c7ab-4197-91ae-4da0c4eee37e  .  0b5ac12b-3392-421d-b858-3b4227ee41eb'

# структура первого кода: {хер знает что}.{айди сессии}.{что-то постоянное}
# {хер знает что}.{айди сессии}.{0b5ac12b-3392-421d-b858-3b4227ee41eb}


import requests

cookies = {
    'X-CSRF-TOKEN': '',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/article/cHAcJnu4luia',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': '',
    'sentry-trace': '',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=b05d0cab19814704a6a4dd65c273f4d5',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer ',
    'Connection': 'keep-alive',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = '{batch:^[{type:track,event:reaction_comment_click,properties:{replay:f585ee2f-f440-493a-a753-7db8a39b41a4},anonymousId:d334613e-eda5-4195-8386-ba2588f39bb9,userId:^[a2ad3873-ba7a-4af3-a154-3597ee733792,80f8a415-c1ad-4d70-957b-587e42f6ac03^],messageId:92fb67d8-9a7e-4eec-9839-c0b034302549,timestamp:2024-02-25T19:15:59.988Z}^],sentAt:2024-02-25T19:15:59.988Z,writeKey:sdk}'

response = requests.post('https://web.gid.ru/api/event-tracker/public/v1/collect', cookies=cookies, headers=headers, data=data)
