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
    'X-CSRF-TOKEN': '345a589d1c287396bf4ba870db8e8ac49a426705c3bf7eeefd424457b5476a25.8d802db0ffa8fa03f0a4a0dd14b58f89faf23cd21a04f19d72b6f77e3f510df58ef30414e635e901f9d7576a0883033e47163adb1d7335d8252e6f400775c1f8c6d9ef9b2481a020a6d7b849452ce991741d09265dba2eee3bcba32495aa651284ce0c8c69e4bd3e43cf20cc06cc75f03a83ec7c6097cbf55824a61a25b416d2a14c1c1527c3943c373f21c218ec2cfb53221feebbb11f695dd6d4f4cec9df514c99bfcb3de5e4136a6d8972dde068765adc738288ad1854f6e4f91be4ce3c9f863019ed749741c6203fee46409677a351c2d228ae82e79dd6747322b9427bb0525d47cb7ff25afbf4f31c77ae423b9f8e58d2ae49c841db8d57177d673b7022',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/article/cHAcJnu4luia',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': '345a589d1c287396bf4ba870db8e8ac49a426705c3bf7eeefd424457b5476a25.8d802db0ffa8fa03f0a4a0dd14b58f89faf23cd21a04f19d72b6f77e3f510df58ef30414e635e901f9d7576a0883033e47163adb1d7335d8252e6f400775c1f8c6d9ef9b2481a020a6d7b849452ce991741d09265dba2eee3bcba32495aa651284ce0c8c69e4bd3e43cf20cc06cc75f03a83ec7c6097cbf55824a61a25b416d2a14c1c1527c3943c373f21c218ec2cfb53221feebbb11f695dd6d4f4cec9df514c99bfcb3de5e4136a6d8972dde068765adc738288ad1854f6e4f91be4ce3c9f863019ed749741c6203fee46409677a351c2d228ae82e79dd6747322b9427bb0525d47cb7ff25afbf4f31c77ae423b9f8e58d2ae49c841db8d57177d673b7022',
    'sentry-trace': 'b05d0cab19814704a6a4dd65c273f4d5-ab70aef6abd79ca8',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=b05d0cab19814704a6a4dd65c273f4d5',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg4ODk5NzQsImlhdCI6MTcwODg4ODE3NCwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJmM2I0MzJjNi1kNTk2LTQ3YmQtODVjOS01ZGVjYWM1MTRjNmMiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI1NGRiMDU3OC0wM2Y0LTQ4MTgtYjFhMC1mNTgwODBhNWY5ODciLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.Zpa6cjbRZi7hnMDkKKj_HKrwXxz-NdxCeQxRVRombARkCfNQ7aAVyzeA2A6KuCoOWcB09drxSsotbeosb_k-7n-NhoSpdGYPcBXYX6q7MVaesxaI-mCaM7tFRIJdKI-cWMKwQ3EnZjmDICV7VsAWyxbO8GzkfWnxkvqKFgZCs5uqg_02PaKIQ-dgs2ioJAehlcoRzkaQ8QB0ruX_ieleR_QLFom266zphInwhj1Qc_ZlOIQDhhExSxhLaorsFsFYbYcdIdeC_932m23bSkc_4PC5UP1EQLQMB7UYQGrsVJnXj5pqmx2s_5YMQ238f9YCu3Hi45hp-v9iRM6ObS0_fA',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=345a589d1c287396bf4ba870db8e8ac49a426705c3bf7eeefd424457b5476a25.8d802db0ffa8fa03f0a4a0dd14b58f89faf23cd21a04f19d72b6f77e3f510df58ef30414e635e901f9d7576a0883033e47163adb1d7335d8252e6f400775c1f8c6d9ef9b2481a020a6d7b849452ce991741d09265dba2eee3bcba32495aa651284ce0c8c69e4bd3e43cf20cc06cc75f03a83ec7c6097cbf55824a61a25b416d2a14c1c1527c3943c373f21c218ec2cfb53221feebbb11f695dd6d4f4cec9df514c99bfcb3de5e4136a6d8972dde068765adc738288ad1854f6e4f91be4ce3c9f863019ed749741c6203fee46409677a351c2d228ae82e79dd6747322b9427bb0525d47cb7ff25afbf4f31c77ae423b9f8e58d2ae49c841db8d57177d673b7022',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = '{batch:^[{type:track,event:reaction_comment_click,properties:{replay:f585ee2f-f440-493a-a753-7db8a39b41a4},anonymousId:d334613e-eda5-4195-8386-ba2588f39bb9,userId:^[a2ad3873-ba7a-4af3-a154-3597ee733792,80f8a415-c1ad-4d70-957b-587e42f6ac03^],messageId:92fb67d8-9a7e-4eec-9839-c0b034302549,timestamp:2024-02-25T19:15:59.988Z}^],sentAt:2024-02-25T19:15:59.988Z,writeKey:sdk}'

response = requests.post('https://web.gid.ru/api/event-tracker/public/v1/collect', cookies=cookies, headers=headers, data=data)
