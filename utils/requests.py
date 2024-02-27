# запрос на просмотр статей
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://web.gid.ru/feed',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': 'ac3d36e6c3dcba4fe82f2718488e689c0b364c3059b9cc5616f8cbefc4d28c8b.8d0ff03ea67089dd4cc71abc9cf2a723de3aff6c7320e15be9b4cb61fcfe1b5ad8e3d5cce3de95523a0b2dabc8f32ae09006db302560b7b1554eee1519ec5e9a7bcec9729f52541885eaf6742228f3f9054d091b32361b4bf167dd3537d59adc8c6fe4bc6f8bda13ef6e227caa1e451a9d6ad53efc1c98ae658c8481d5c922c686d6511ee1452459a5ced3ed47c126ca42680cb0792647df57b1b8f53606c3d94cd894ec3037968c8fe9f94f4ba622cc652ddcdf8d401a940082116c59a229fc80939530c41f5304bc067c41adf2252c8b12332d31725c2200e689b4ec92cae08807812f7a47192a476009246657c5dc4fd8da4ba6f0a17a5cb81e2dd6b46dcb',
    'sentry-trace': '2473b635fd604b729b746b1ec5a05344-bb8aa3348de06787-1',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=2473b635fd604b729b746b1ec5a05344,sentry-sample_rate=1,sentry-sampled=true',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTM4OTYsImlhdCI6MTcwODk1MjA5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJiZjVkNmFmOC02ZTRhLTQ0MWMtYjZhYS03MWYwY2E0MmI1M2UiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.JY8yWfHg7X5Qbis6HKZBjQU8sDNrT8wwmSIqyd_28zBM_N_0GCYCdjHWobQOS_R8dhVqpDcYgXXOM7p6AD6sNXQ21IgXbITpEXA-29PSkiyXvYAw263tFeGiz0EzgTkq0zAVAJe8t71hpDpAaQcDmYBTNb9kKNrgxan-0DOmXi6xWRRp3_nTueSCU4Bk8c1YFoS28-c2c43bgMwFTF3wH5jd_0HfaSp8K8mFte5nmDxO_KqaACoT5mKuLgv2a8F74aT6BqDLdAdhHvLZQWoDWmN_Un-VzzTxJMMBIOR2VPlweQbIwXd6lw5grnyXB5fLNDBGGNdz4iKRQsFUApatRQ',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=ac3d36e6c3dcba4fe82f2718488e689c0b364c3059b9cc5616f8cbefc4d28c8b.8d0ff03ea67089dd4cc71abc9cf2a723de3aff6c7320e15be9b4cb61fcfe1b5ad8e3d5cce3de95523a0b2dabc8f32ae09006db302560b7b1554eee1519ec5e9a7bcec9729f52541885eaf6742228f3f9054d091b32361b4bf167dd3537d59adc8c6fe4bc6f8bda13ef6e227caa1e451a9d6ad53efc1c98ae658c8481d5c922c686d6511ee1452459a5ced3ed47c126ca42680cb0792647df57b1b8f53606c3d94cd894ec3037968c8fe9f94f4ba622cc652ddcdf8d401a940082116c59a229fc80939530c41f5304bc067c41adf2252c8b12332d31725c2200e689b4ec92cae08807812f7a47192a476009246657c5dc4fd8da4ba6f0a17a5cb81e2dd6b46dcb',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'gidOnly': 'true',
    'pinsOnly': 'false',
    'recommendationsOnly': 'false',
    'limit': '10',
}

response = requests.get('https://web.gid.ru/api/public/v3/feed', params=params, cookies=cookies, headers=headers)


# запрос на комментирование статьи
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/article/UNkQcC2szDtC',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': 'ac3d36e6c3dcba4fe82f2718488e689c0b364c3059b9cc5616f8cbefc4d28c8b.8d0ff03ea67089dd4cc71abc9cf2a723de3aff6c7320e15be9b4cb61fcfe1b5ad8e3d5cce3de95523a0b2dabc8f32ae09006db302560b7b1554eee1519ec5e9a7bcec9729f52541885eaf6742228f3f9054d091b32361b4bf167dd3537d59adc8c6fe4bc6f8bda13ef6e227caa1e451a9d6ad53efc1c98ae658c8481d5c922c686d6511ee1452459a5ced3ed47c126ca42680cb0792647df57b1b8f53606c3d94cd894ec3037968c8fe9f94f4ba622cc652ddcdf8d401a940082116c59a229fc80939530c41f5304bc067c41adf2252c8b12332d31725c2200e689b4ec92cae08807812f7a47192a476009246657c5dc4fd8da4ba6f0a17a5cb81e2dd6b46dcb',
    'sentry-trace': '690ba6597e1f41b5a31e9732d587682d-889938f04628195f',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=690ba6597e1f41b5a31e9732d587682d',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTM4OTYsImlhdCI6MTcwODk1MjA5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJiZjVkNmFmOC02ZTRhLTQ0MWMtYjZhYS03MWYwY2E0MmI1M2UiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.JY8yWfHg7X5Qbis6HKZBjQU8sDNrT8wwmSIqyd_28zBM_N_0GCYCdjHWobQOS_R8dhVqpDcYgXXOM7p6AD6sNXQ21IgXbITpEXA-29PSkiyXvYAw263tFeGiz0EzgTkq0zAVAJe8t71hpDpAaQcDmYBTNb9kKNrgxan-0DOmXi6xWRRp3_nTueSCU4Bk8c1YFoS28-c2c43bgMwFTF3wH5jd_0HfaSp8K8mFte5nmDxO_KqaACoT5mKuLgv2a8F74aT6BqDLdAdhHvLZQWoDWmN_Un-VzzTxJMMBIOR2VPlweQbIwXd6lw5grnyXB5fLNDBGGNdz4iKRQsFUApatRQ',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=ac3d36e6c3dcba4fe82f2718488e689c0b364c3059b9cc5616f8cbefc4d28c8b.8d0ff03ea67089dd4cc71abc9cf2a723de3aff6c7320e15be9b4cb61fcfe1b5ad8e3d5cce3de95523a0b2dabc8f32ae09006db302560b7b1554eee1519ec5e9a7bcec9729f52541885eaf6742228f3f9054d091b32361b4bf167dd3537d59adc8c6fe4bc6f8bda13ef6e227caa1e451a9d6ad53efc1c98ae658c8481d5c922c686d6511ee1452459a5ced3ed47c126ca42680cb0792647df57b1b8f53606c3d94cd894ec3037968c8fe9f94f4ba622cc652ddcdf8d401a940082116c59a229fc80939530c41f5304bc067c41adf2252c8b12332d31725c2200e689b4ec92cae08807812f7a47192a476009246657c5dc4fd8da4ba6f0a17a5cb81e2dd6b46dcb',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = '{content:^о^к}'.encode()

response = requests.post('https://web.gid.ru/api/feed/UNkQcC2szDtC/comments', cookies=cookies, headers=headers, data=data)
response = {
	"id": "d60fde1d-2a59-4bfb-b8ab-18fb29056efc",
	"content": "ок",
	"attachments": [],
	"createdAt": "2024-02-26T13:02:36.09334",
	"updatedAt": "2024-02-26T13:02:36.09334",
	"deletedAt": null,
	"parentId": null,
	"threadId": null,
	"status": "approved",
	"moderation": {
		"grchc": null,
		"icl": null
	},
	"feedId": "UNkQcC2szDtC",
	"userId": "8d68107c-b224-4817-93d2-7144bc428dc3"
}



# запрос на добавление энергии после комментирования статьи
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/article/UNkQcC2szDtC',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': 'a018fbfc24940ed9c393ffde97be54c9bd5c73a4c8553afea261e074d9602b3a.84401c2ba177f97d98216e8e6e543fef3b2626f9fa4c0e6dcf9e2e6bdb4b83e9f86116c4a41cd115bd22d0aaa3cd0cc124c525f0c539af06a790105c1f8b908a4e17074a5cfd895a7556542e8bb4bab75a698901d071981daa21ddf3a190528ff1f09d23fe57af37d4dfc951766def62335e133fcdcc11cc27d7a1aebd4e5fe760b6d408bed84dc18da9b4d879d537328f6ff9ba130f456bfdf1b0dcbc047dc41dd309979c64569ed1d07f1f566f4ae9a3af5c9f30b244fa428e269ac6d45296f3fcd9cd12f86293a2dedf3d7e27588007e414153f1b57b90b888be5abed9596f8c8c851bf41c74696ffad7ee7b7792ed27076a754d72bd221614e6b537cc2db',
    'sentry-trace': '690ba6597e1f41b5a31e9732d587682d-889938f04628195f',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=690ba6597e1f41b5a31e9732d587682d',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTM4OTYsImlhdCI6MTcwODk1MjA5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJiZjVkNmFmOC02ZTRhLTQ0MWMtYjZhYS03MWYwY2E0MmI1M2UiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.JY8yWfHg7X5Qbis6HKZBjQU8sDNrT8wwmSIqyd_28zBM_N_0GCYCdjHWobQOS_R8dhVqpDcYgXXOM7p6AD6sNXQ21IgXbITpEXA-29PSkiyXvYAw263tFeGiz0EzgTkq0zAVAJe8t71hpDpAaQcDmYBTNb9kKNrgxan-0DOmXi6xWRRp3_nTueSCU4Bk8c1YFoS28-c2c43bgMwFTF3wH5jd_0HfaSp8K8mFte5nmDxO_KqaACoT5mKuLgv2a8F74aT6BqDLdAdhHvLZQWoDWmN_Un-VzzTxJMMBIOR2VPlweQbIwXd6lw5grnyXB5fLNDBGGNdz4iKRQsFUApatRQ',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=a018fbfc24940ed9c393ffde97be54c9bd5c73a4c8553afea261e074d9602b3a.84401c2ba177f97d98216e8e6e543fef3b2626f9fa4c0e6dcf9e2e6bdb4b83e9f86116c4a41cd115bd22d0aaa3cd0cc124c525f0c539af06a790105c1f8b908a4e17074a5cfd895a7556542e8bb4bab75a698901d071981daa21ddf3a190528ff1f09d23fe57af37d4dfc951766def62335e133fcdcc11cc27d7a1aebd4e5fe760b6d408bed84dc18da9b4d879d537328f6ff9ba130f456bfdf1b0dcbc047dc41dd309979c64569ed1d07f1f566f4ae9a3af5c9f30b244fa428e269ac6d45296f3fcd9cd12f86293a2dedf3d7e27588007e414153f1b57b90b888be5abed9596f8c8c851bf41c74696ffad7ee7b7792ed27076a754d72bd221614e6b537cc2db',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
	"batch": [
		{
			"anonymousId": "59c4e6fb-b9e2-450b-ab05-69ce8ad9e2a3",
			"event": "news_comment_send",
			"messageId": "50ca6af6-48e1-4924-92b3-b87400328082",
			"properties": {
				"replay": ""
			},
			"timestamp": "2024-02-26T13:02:34.806Z",
			"type": "track",
			"userId": "[a2ad3873-ba7a-4af3-a154-3597ee733792,80f8a415-c1ad-4d70-957b-587e42f6ac03]"
		}
	],
	"sentAt": "2024-02-26T13:02:34.806Z",
	"writeKey": "sdk"
}

response = requests.post('https://web.gid.ru/api/event-tracker/public/v1/collect', cookies=cookies, headers=headers, data=data)



# запрос на просомтр комментариев к статье
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://web.gid.ru/article/UNkQcC2szDtC',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': 'a018fbfc24940ed9c393ffde97be54c9bd5c73a4c8553afea261e074d9602b3a.84401c2ba177f97d98216e8e6e543fef3b2626f9fa4c0e6dcf9e2e6bdb4b83e9f86116c4a41cd115bd22d0aaa3cd0cc124c525f0c539af06a790105c1f8b908a4e17074a5cfd895a7556542e8bb4bab75a698901d071981daa21ddf3a190528ff1f09d23fe57af37d4dfc951766def62335e133fcdcc11cc27d7a1aebd4e5fe760b6d408bed84dc18da9b4d879d537328f6ff9ba130f456bfdf1b0dcbc047dc41dd309979c64569ed1d07f1f566f4ae9a3af5c9f30b244fa428e269ac6d45296f3fcd9cd12f86293a2dedf3d7e27588007e414153f1b57b90b888be5abed9596f8c8c851bf41c74696ffad7ee7b7792ed27076a754d72bd221614e6b537cc2db',
    'sentry-trace': '690ba6597e1f41b5a31e9732d587682d-889938f04628195f',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=690ba6597e1f41b5a31e9732d587682d',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTM4OTYsImlhdCI6MTcwODk1MjA5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJiZjVkNmFmOC02ZTRhLTQ0MWMtYjZhYS03MWYwY2E0MmI1M2UiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.JY8yWfHg7X5Qbis6HKZBjQU8sDNrT8wwmSIqyd_28zBM_N_0GCYCdjHWobQOS_R8dhVqpDcYgXXOM7p6AD6sNXQ21IgXbITpEXA-29PSkiyXvYAw263tFeGiz0EzgTkq0zAVAJe8t71hpDpAaQcDmYBTNb9kKNrgxan-0DOmXi6xWRRp3_nTueSCU4Bk8c1YFoS28-c2c43bgMwFTF3wH5jd_0HfaSp8K8mFte5nmDxO_KqaACoT5mKuLgv2a8F74aT6BqDLdAdhHvLZQWoDWmN_Un-VzzTxJMMBIOR2VPlweQbIwXd6lw5grnyXB5fLNDBGGNdz4iKRQsFUApatRQ',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=a018fbfc24940ed9c393ffde97be54c9bd5c73a4c8553afea261e074d9602b3a.84401c2ba177f97d98216e8e6e543fef3b2626f9fa4c0e6dcf9e2e6bdb4b83e9f86116c4a41cd115bd22d0aaa3cd0cc124c525f0c539af06a790105c1f8b908a4e17074a5cfd895a7556542e8bb4bab75a698901d071981daa21ddf3a190528ff1f09d23fe57af37d4dfc951766def62335e133fcdcc11cc27d7a1aebd4e5fe760b6d408bed84dc18da9b4d879d537328f6ff9ba130f456bfdf1b0dcbc047dc41dd309979c64569ed1d07f1f566f4ae9a3af5c9f30b244fa428e269ac6d45296f3fcd9cd12f86293a2dedf3d7e27588007e414153f1b57b90b888be5abed9596f8c8c851bf41c74696ffad7ee7b7792ed27076a754d72bd221614e6b537cc2db',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'offset': '0',
    'limit': '50',
}

response = requests.get('https://web.gid.ru/api/feed/UNkQcC2szDtC/comments', params=params, cookies=cookies, headers=headers)



# запрос на отправку реакции на комментарий
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/article/UNkQcC2szDtC',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': 'a018fbfc24940ed9c393ffde97be54c9bd5c73a4c8553afea261e074d9602b3a.84401c2ba177f97d98216e8e6e543fef3b2626f9fa4c0e6dcf9e2e6bdb4b83e9f86116c4a41cd115bd22d0aaa3cd0cc124c525f0c539af06a790105c1f8b908a4e17074a5cfd895a7556542e8bb4bab75a698901d071981daa21ddf3a190528ff1f09d23fe57af37d4dfc951766def62335e133fcdcc11cc27d7a1aebd4e5fe760b6d408bed84dc18da9b4d879d537328f6ff9ba130f456bfdf1b0dcbc047dc41dd309979c64569ed1d07f1f566f4ae9a3af5c9f30b244fa428e269ac6d45296f3fcd9cd12f86293a2dedf3d7e27588007e414153f1b57b90b888be5abed9596f8c8c851bf41c74696ffad7ee7b7792ed27076a754d72bd221614e6b537cc2db',
    'sentry-trace': '690ba6597e1f41b5a31e9732d587682d-889938f04628195f',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=690ba6597e1f41b5a31e9732d587682d',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTM4OTYsImlhdCI6MTcwODk1MjA5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJiZjVkNmFmOC02ZTRhLTQ0MWMtYjZhYS03MWYwY2E0MmI1M2UiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.JY8yWfHg7X5Qbis6HKZBjQU8sDNrT8wwmSIqyd_28zBM_N_0GCYCdjHWobQOS_R8dhVqpDcYgXXOM7p6AD6sNXQ21IgXbITpEXA-29PSkiyXvYAw263tFeGiz0EzgTkq0zAVAJe8t71hpDpAaQcDmYBTNb9kKNrgxan-0DOmXi6xWRRp3_nTueSCU4Bk8c1YFoS28-c2c43bgMwFTF3wH5jd_0HfaSp8K8mFte5nmDxO_KqaACoT5mKuLgv2a8F74aT6BqDLdAdhHvLZQWoDWmN_Un-VzzTxJMMBIOR2VPlweQbIwXd6lw5grnyXB5fLNDBGGNdz4iKRQsFUApatRQ',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=a018fbfc24940ed9c393ffde97be54c9bd5c73a4c8553afea261e074d9602b3a.84401c2ba177f97d98216e8e6e543fef3b2626f9fa4c0e6dcf9e2e6bdb4b83e9f86116c4a41cd115bd22d0aaa3cd0cc124c525f0c539af06a790105c1f8b908a4e17074a5cfd895a7556542e8bb4bab75a698901d071981daa21ddf3a190528ff1f09d23fe57af37d4dfc951766def62335e133fcdcc11cc27d7a1aebd4e5fe760b6d408bed84dc18da9b4d879d537328f6ff9ba130f456bfdf1b0dcbc047dc41dd309979c64569ed1d07f1f566f4ae9a3af5c9f30b244fa428e269ac6d45296f3fcd9cd12f86293a2dedf3d7e27588007e414153f1b57b90b888be5abed9596f8c8c851bf41c74696ffad7ee7b7792ed27076a754d72bd221614e6b537cc2db',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = '{type:Lol}'

response = requests.post(
    'https://web.gid.ru/api/feed/UNkQcC2szDtC/comments/4cd881d9-2e44-4e67-919c-c702ce7e7617/reactions',
    cookies=cookies,
    headers=headers,
    data=data,
)
resp = {
	"objectId": "4cd881d9-2e44-4e67-919c-c702ce7e7617",
	"objectType": "feed-comment",
	"userId": "a2ad3873-ba7a-4af3-a154-3597ee733792",
	"type": "Lol",
	"id": "c3d4ba76-26e2-445e-adb6-e7e2a7424598",
	"createdAt": "2024-02-26T13:24:52.559515"
}



# запрос на добавление энергии после реакции на комментарий
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/article/UNkQcC2szDtC',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': '036f3f1017df624a5a0149210b9898d2893305da95a107e5064be52bdda3e53a.9dbb57cdd9351113b419ff7728483f24c4a4080a402d3d93971ca36b38ca5376464f38b4b0e0e54da9b6aed79155ec8d76a4d2ae0c7076ac2edef43444f076184ef56cbf19d6f195fb5a6902833159ccfd96eee6419c5f465e7b0b2aaa92476ffba4a279010e35901e6ad6a0dc74bdd2f5ea4e997038a4400bfe3ef6d53f33619ca23de6a228ed9da5f0ce8ff15fc72576dedb795515cfb63d3f02e0d3f7ddba9aebb65caff6108116ab018f6b388a835f79256c3110a0e21fbb2671c8a69ad0fa30edf1cb433699ccf588babbebb4424e2415ce373ef8a21d35fb288c2e12288eea1363f752142c70974fec8ff02708e26415515531d01fff915315d273b08c',
    'sentry-trace': '690ba6597e1f41b5a31e9732d587682d-889938f04628195f',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=690ba6597e1f41b5a31e9732d587682d',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTM4OTYsImlhdCI6MTcwODk1MjA5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJiZjVkNmFmOC02ZTRhLTQ0MWMtYjZhYS03MWYwY2E0MmI1M2UiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.JY8yWfHg7X5Qbis6HKZBjQU8sDNrT8wwmSIqyd_28zBM_N_0GCYCdjHWobQOS_R8dhVqpDcYgXXOM7p6AD6sNXQ21IgXbITpEXA-29PSkiyXvYAw263tFeGiz0EzgTkq0zAVAJe8t71hpDpAaQcDmYBTNb9kKNrgxan-0DOmXi6xWRRp3_nTueSCU4Bk8c1YFoS28-c2c43bgMwFTF3wH5jd_0HfaSp8K8mFte5nmDxO_KqaACoT5mKuLgv2a8F74aT6BqDLdAdhHvLZQWoDWmN_Un-VzzTxJMMBIOR2VPlweQbIwXd6lw5grnyXB5fLNDBGGNdz4iKRQsFUApatRQ',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=036f3f1017df624a5a0149210b9898d2893305da95a107e5064be52bdda3e53a.9dbb57cdd9351113b419ff7728483f24c4a4080a402d3d93971ca36b38ca5376464f38b4b0e0e54da9b6aed79155ec8d76a4d2ae0c7076ac2edef43444f076184ef56cbf19d6f195fb5a6902833159ccfd96eee6419c5f465e7b0b2aaa92476ffba4a279010e35901e6ad6a0dc74bdd2f5ea4e997038a4400bfe3ef6d53f33619ca23de6a228ed9da5f0ce8ff15fc72576dedb795515cfb63d3f02e0d3f7ddba9aebb65caff6108116ab018f6b388a835f79256c3110a0e21fbb2671c8a69ad0fa30edf1cb433699ccf588babbebb4424e2415ce373ef8a21d35fb288c2e12288eea1363f752142c70974fec8ff02708e26415515531d01fff915315d273b08c',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
data = {
	"batch": [
		{
			"anonymousId": "8439b4f6-04bd-4366-ae6b-6323ed4fa93d",
			"event": "reaction_comment_click",
			"messageId": "c06bd1ba-fe47-4bac-8c86-56999f195725",
			"properties": {
				"replay": "4cd881d9-2e44-4e67-919c-c702ce7e7617"
			},
			"timestamp": "2024-02-26T13:24:51.211Z",
			"type": "track",
			"userId": "[a2ad3873-ba7a-4af3-a154-3597ee733792,80f8a415-c1ad-4d70-957b-587e42f6ac03]"
		}
	],
	"sentAt": "2024-02-26T13:24:51.211Z",
	"writeKey": "sdk"
}

response = requests.post('https://web.gid.ru/api/event-tracker/public/v1/collect', cookies=cookies, headers=headers, data=data)


# запрос на нгачисление энергии за спасибо
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/my-resource/thanks',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': '8d7c7cbeb6ddad2a6a801a121e6e78de7d7a81aded5d1e0d34c5c49e1a6df5ad.30a518f6334f2a6d2ec0c59ba2328068248c53222ba49bcbcc32e22cec23f9b681db449876f0d5684a6eb28afa53ab0fdd1bf536539640da3f402e10f8980fea23c90ba812fbc400ab51c4ac16d3427cd3831bdc9d828bf2e711a5f4016985ffce357f346116fca53c2b32b0a653b12ceebfbeb60c2db44024189fc296dbcd34da1321ce2336a837c03a13866cc7abb4b288717f07c2ca6ce1fa9cf2a3bda189b3db5722fb43c291d83f8da396be67279f886f9bb89987ff09573dc354152b3eecc9e0ed6821a5f525880ea373bbc90de32b4dbf8ebda1989fd7f44acdef865731c02be323c7d3aa3233f13cc3957e7ad4adfb77d9076599f6a23dc1f9f0cdfb',
    'sentry-trace': '690ba6597e1f41b5a31e9732d587682d-889938f04628195f',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=690ba6597e1f41b5a31e9732d587682d',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTU2OTYsImlhdCI6MTcwODk1Mzg5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiI1ZjVmY2YzNy1jZjliLTQzMjQtOGQ5Yi1lMjFmY2FkYzQxMjkiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.cht6MCVQRNUwruzE-7zp-m9gh4DkqmRMTdgA01Zv2b5ggFL8SrDqgW5eXVUeo4-N6azZmKru_Y1neQ7Hb1iOHnRc0B-kl6WgjMm3szbyeo5YVs5LuH9DcaiS1Mz3ob1gyWBVI-0kXmZmWo46mnxka47txre7TPP-Pt7Z6Up554RGat27bLRQyeHt3R3T_CaABdzdJO0EOmP3xhg9u_WX7DAeokcO6py-eJMScSMKM0TfziFePzlChM4ZVUzCsIC316hZnRoKfP_RN82rLLXVs2iiRl9aRePGTET6B7GUqX1LIRmANa-cXPFPdz8VeUHg5dNtFtTsuG7wxQu0QYCZlA',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=8d7c7cbeb6ddad2a6a801a121e6e78de7d7a81aded5d1e0d34c5c49e1a6df5ad.30a518f6334f2a6d2ec0c59ba2328068248c53222ba49bcbcc32e22cec23f9b681db449876f0d5684a6eb28afa53ab0fdd1bf536539640da3f402e10f8980fea23c90ba812fbc400ab51c4ac16d3427cd3831bdc9d828bf2e711a5f4016985ffce357f346116fca53c2b32b0a653b12ceebfbeb60c2db44024189fc296dbcd34da1321ce2336a837c03a13866cc7abb4b288717f07c2ca6ce1fa9cf2a3bda189b3db5722fb43c291d83f8da396be67279f886f9bb89987ff09573dc354152b3eecc9e0ed6821a5f525880ea373bbc90de32b4dbf8ebda1989fd7f44acdef865731c02be323c7d3aa3233f13cc3957e7ad4adfb77d9076599f6a23dc1f9f0cdfb',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
	"batch": [
		{
			"anonymousId": "cf0c67b1-80a5-4c4b-b5af-58c324e345ba",
			"event": "thanks_new_create_click",
			"messageId": "e824954c-b3c9-4ea2-8905-40438c85adc1",
			"properties": {
				"recipient": "28169937-4b30-45da-8852-9e87084d5d58"
			},
			"timestamp": "2024-02-26T13:41:19.850Z",
			"type": "track",
			"userId": "[a2ad3873-ba7a-4af3-a154-3597ee733792,80f8a415-c1ad-4d70-957b-587e42f6ac03]"
		}
	],
	"sentAt": "2024-02-26T13:41:19.850Z",
	"writeKey": "sdk"
}
response = requests.post('https://web.gid.ru/api/event-tracker/public/v1/collect', cookies=cookies, headers=headers, data=data)
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


# просмотр курсов
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://web.gid.ru/sputnik/',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': '8d7c7cbeb6ddad2a6a801a121e6e78de7d7a81aded5d1e0d34c5c49e1a6df5ad.30a518f6334f2a6d2ec0c59ba2328068248c53222ba49bcbcc32e22cec23f9b681db449876f0d5684a6eb28afa53ab0fdd1bf536539640da3f402e10f8980fea23c90ba812fbc400ab51c4ac16d3427cd3831bdc9d828bf2e711a5f4016985ffce357f346116fca53c2b32b0a653b12ceebfbeb60c2db44024189fc296dbcd34da1321ce2336a837c03a13866cc7abb4b288717f07c2ca6ce1fa9cf2a3bda189b3db5722fb43c291d83f8da396be67279f886f9bb89987ff09573dc354152b3eecc9e0ed6821a5f525880ea373bbc90de32b4dbf8ebda1989fd7f44acdef865731c02be323c7d3aa3233f13cc3957e7ad4adfb77d9076599f6a23dc1f9f0cdfb',
    'sentry-trace': 'c4820db2f10f497bb86f84bbeaf375e0-8c30596c38b0e3bc-1',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=c4820db2f10f497bb86f84bbeaf375e0,sentry-sample_rate=1,sentry-sampled=true',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTU2OTYsImlhdCI6MTcwODk1Mzg5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiI1ZjVmY2YzNy1jZjliLTQzMjQtOGQ5Yi1lMjFmY2FkYzQxMjkiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.cht6MCVQRNUwruzE-7zp-m9gh4DkqmRMTdgA01Zv2b5ggFL8SrDqgW5eXVUeo4-N6azZmKru_Y1neQ7Hb1iOHnRc0B-kl6WgjMm3szbyeo5YVs5LuH9DcaiS1Mz3ob1gyWBVI-0kXmZmWo46mnxka47txre7TPP-Pt7Z6Up554RGat27bLRQyeHt3R3T_CaABdzdJO0EOmP3xhg9u_WX7DAeokcO6py-eJMScSMKM0TfziFePzlChM4ZVUzCsIC316hZnRoKfP_RN82rLLXVs2iiRl9aRePGTET6B7GUqX1LIRmANa-cXPFPdz8VeUHg5dNtFtTsuG7wxQu0QYCZlA',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=8d7c7cbeb6ddad2a6a801a121e6e78de7d7a81aded5d1e0d34c5c49e1a6df5ad.30a518f6334f2a6d2ec0c59ba2328068248c53222ba49bcbcc32e22cec23f9b681db449876f0d5684a6eb28afa53ab0fdd1bf536539640da3f402e10f8980fea23c90ba812fbc400ab51c4ac16d3427cd3831bdc9d828bf2e711a5f4016985ffce357f346116fca53c2b32b0a653b12ceebfbeb60c2db44024189fc296dbcd34da1321ce2336a837c03a13866cc7abb4b288717f07c2ca6ce1fa9cf2a3bda189b3db5722fb43c291d83f8da396be67279f886f9bb89987ff09573dc354152b3eecc9e0ed6821a5f525880ea373bbc90de32b4dbf8ebda1989fd7f44acdef865731c02be323c7d3aa3233f13cc3957e7ad4adfb77d9076599f6a23dc1f9f0cdfb',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

response = requests.get('https://web.gid.ru/api/lms/v2/courses', cookies=cookies, headers=headers)
resp = {
	"items": [
		{
			"id": "88667f2c-fc7d-470f-842a-29ab702c7bf7",
			"name": "Продолжить обучение",
			"items": [
				{
					"id": "4447b359-6998-4c96-8687-d87583a0fc9e",
					"name": "Тестирование по культуре производственной безопасности",
					"difficulty": "medium",
					"duration": 10,
					"subtitle": "Закрепите материал курса «Культура производственной безопасности»",
					"pictureLink": "lms-prod/courses-covers/ea982a15-d905-475c-934e-77ce5fad904f.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "started",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 1
				}
			]
		},
		{
			"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
			"name": "Карьера",
			"items": [
				{
					"id": "f0ef3232-078b-403a-bb65-9fcf29d84f12",
					"name": "Идеальное выступление: как впечатлять своими идеями",
					"difficulty": "medium",
					"duration": 70,
					"subtitle": "Создайте презентацию мечты и добейтесь успехов",
					"pictureLink": "lms-prod/courses-covers/97b86cdc-3860-4b11-b544-206db1fef1d5.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [],
					"totalLessons": 8
				},
				{
					"id": "c1ff2bc7-0a3f-4b2f-8710-0361293b8811",
					"name": "Как работать, когда вокруг все меняется",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Узнайте, как работать в условиях изменений",
					"pictureLink": "lms-prod/courses-covers/7703b433-c893-4652-9a02-cafc914d81ca.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [],
					"totalLessons": 6
				},
				{
					"id": "c4af6bbb-2526-4d1e-a34b-b4a0f7da023e",
					"name": "Тайм-менеджмент: заставляем время работать на себя",
					"difficulty": "medium",
					"duration": 90,
					"subtitle": "Станьте властелином времени и личной эффективности!",
					"pictureLink": "lms-prod/courses-covers/b565d2c9-d6a7-4acb-8817-4a500bc38027.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 8
				},
				{
					"id": "e59c239e-2070-470e-a81d-1dfc2aebea1d",
					"name": "Гибкие навыки: что это и почему важно их прокачивать",
					"difficulty": "medium",
					"duration": 30,
					"subtitle": "Главное о самых важных soft skills для вашего карьерного роста.",
					"pictureLink": "lms-prod/courses-covers/a07001bb-33b0-4788-998c-0c74dcbeeb38.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 7
				},
				{
					"id": "e5a051dd-2227-44fb-9b01-531ea24e7996",
					"name": "Как решать конфликты на работе",
					"difficulty": "easy",
					"duration": 30,
					"subtitle": "Узнайте, как предостеречь появление, сдержать развитие и способствовать разрешению конфликтов на рабочем месте",
					"pictureLink": "lms-prod/courses-covers/3cdd2927-f09f-4603-aff3-5a2ec0212308.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 5
				},
				{
					"id": "f067c4a0-0896-4f22-a3dc-b20f04b7c4b8",
					"name": "Обратная связь: секреты эффективной коммуникации",
					"difficulty": "medium",
					"duration": 45,
					"subtitle": "Учимся говорить, чтобы поняли, и слушать, чтобы услышать",
					"pictureLink": "lms-prod/courses-covers/5ea2b097-63a1-415b-89ac-30e73849bc73.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 7
				},
				{
					"id": "ddbc8998-695b-497c-8d25-096a365dc3f8",
					"name": "От хаоса к порядку: гибкие методологии для работы и жизни",
					"difficulty": "medium",
					"duration": 50,
					"subtitle": "Узнайте, как организовать работу в команде и довести проект до конца",
					"pictureLink": "lms-prod/courses-covers/8285db00-60a6-46cc-bff0-fe17f341eaa1.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 7
				},
				{
					"id": "eef95d64-9da8-4c97-92bd-9cecb181779b",
					"name": "Корпоративная культура. Стань частью успешной команды!",
					"difficulty": "easy",
					"duration": 21,
					"subtitle": "Почувствуйте все преимущества развитой корпоративной культуры на себе и в команде!",
					"pictureLink": "lms-prod/courses-covers/52d562b9-6d1a-42dc-a819-f14a676cf292.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [],
					"totalLessons": 3
				}
			]
		},
		{
			"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
			"name": "Здоровье",
			"items": [
				{
					"id": "f61bdad7-1925-4b8f-a848-63280dcf3796",
					"name": "Как справиться с тревогой: причины, практики и помощь",
					"difficulty": "easy",
					"duration": 45,
					"subtitle": "Научитесь управлять тревожными состояниями и брать эмоции под контроль",
					"pictureLink": "lms-prod/courses-covers/fde0f798-b8f5-4e9d-aa0f-91918d584997.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [],
					"totalLessons": 10
				},
				{
					"id": "8372237c-be82-43e8-bb80-6f764e6e435a",
					"name": "Здоровое питание: как найти баланс",
					"difficulty": "easy",
					"duration": 60,
					"subtitle": "Ваш путеводитель в здоровую жизнь: составляем меню на каждый день и учимся принимать себя",
					"pictureLink": "lms-prod/courses-covers/47127303-7e8e-4653-8b1d-53832e0eaecc.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						},
						{
							"id": "f41020bb-e46e-4e66-82f4-e15ab17b5762",
							"name": "Питание"
						}
					],
					"totalLessons": 6
				},
				{
					"id": "431b4167-1bf3-445e-bd7f-6aee405d7ca5",
					"name": "Секреты отдыха: перезагрузка без последствий",
					"difficulty": "medium",
					"duration": 40,
					"subtitle": "Главное об отдыхе и о том, как провести его удачно.",
					"pictureLink": "lms-prod/courses-covers/768e206c-020d-48fb-b691-45064ab553e5.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 5
				},
				{
					"id": "a8cae4fa-e182-42d4-aa88-d9b00c4b5f1c",
					"name": "Как начать и не бросить бегать",
					"difficulty": "medium",
					"duration": 45,
					"subtitle": "Начните бегать и сделайте это своим любимым и полезным хобби!",
					"pictureLink": "lms-prod/courses-covers/a1214834-fdc2-4513-9cf5-c29f5d680531.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [],
					"totalLessons": 5
				},
				{
					"id": "94046294-0b90-4e13-9d21-1378e04a4b45",
					"name": "Пойдем ходить! Руководство по северной ходьбе для начинающих",
					"difficulty": "easy",
					"duration": 30,
					"subtitle": "Откройте для себя новый вид спорта, станьте здоровее и зарядитесь на успех!",
					"pictureLink": "lms-prod/courses-covers/523508d8-1ea2-40d5-9c05-e1de7f0643c3.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [],
					"totalLessons": 4
				}
			]
		},
		{
			"id": "56069470-86be-4d4f-b023-162f6be62e3d",
			"name": "Наука и искусство",
			"items": [
				{
					"id": "2f708fc3-0de4-498b-accd-ce00b0c96f46",
					"name": "Компьютерные технологии будущего",
					"difficulty": "medium",
					"duration": 45,
					"subtitle": "Сравниваем технологические мечты и реальность, разбираемся в работе окружающих нас устройств",
					"pictureLink": "lms-prod/courses-covers/60a74ba7-e440-4477-bf43-d02dee19841a.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 5
				},
				{
					"id": "e1256cfc-bbf8-47f9-9f09-0029576d0800",
					"name": "Древние цивилизации: как жили люди прошлого и что досталось потомкам",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Узнайте все подробности жизни предков современного человека",
					"pictureLink": "lms-prod/courses-covers/b81e3a4b-8ebc-4545-8e69-81d44d314d33.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 9
				},
				{
					"id": "e7849b91-50c4-49a5-83b2-8a98fea0d7e9",
					"name": "За кадром: киностудия нашего времени",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Узнайте, как создается настоящее кино и где в нем скрыта магия.",
					"pictureLink": "lms-prod/courses-covers/26a92b11-8e81-43c9-9b61-2b632b284bf6.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 10
				},
				{
					"id": "09e52d60-996c-499e-b1c8-bf38f02e87f9",
					"name": "Далекий космос: история освоения и влияние на нашу жизнь",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Найдите космос вокруг себя и узнайте, с чего началось его покорение!",
					"pictureLink": "lms-prod/courses-covers/2357dc94-25f3-4ba8-9b0f-5d1b89d2ba08.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 5
				},
				{
					"id": "e2315bbb-abac-4291-b8f9-86b5a9d18130",
					"name": "6 неочевидных русских изобретений",
					"difficulty": "easy",
					"duration": 30,
					"subtitle": "Курс, в котором изобретатели сами расскажут вам о своих открытиях. Так вы еще не изучали историю!",
					"pictureLink": "lms-prod/courses-covers/936be8c3-5840-4c0c-aeb8-ecfde85da987.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 7
				}
			]
		},
		{
			"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
			"name": "Я выбираю безопасность",
			"items": [
				{
					"id": "22bbc87e-34fa-4edd-abeb-456f70722673",
					"name": "Культура и приверженность производственной безопасности: видеокурс",
					"difficulty": "hard",
					"duration": 90,
					"subtitle": "Учимся оценивать риски, предотвращать последствия и достигать целей безопасным образом!",
					"pictureLink": "lms-prod/courses-covers/513efd80-5653-495d-9bef-ba1deffc7734.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 4
				},
				{
					"id": "9a0cb068-8750-41f1-88ef-223f6022081b",
					"name": "Тестирование по риск-ориентированному подходу",
					"difficulty": "medium",
					"duration": 10,
					"subtitle": "Проверьте свои знания по управлению рисками",
					"pictureLink": "lms-prod/courses-covers/aeb1799c-b42e-4d4f-80d1-07ab2541ce42.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 1
				},
				{
					"id": "4447b359-6998-4c96-8687-d87583a0fc9e",
					"name": "Тестирование по культуре производственной безопасности",
					"difficulty": "medium",
					"duration": 10,
					"subtitle": "Закрепите материал курса «Культура производственной безопасности»",
					"pictureLink": "lms-prod/courses-covers/ea982a15-d905-475c-934e-77ce5fad904f.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "started",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 1
				},
				{
					"id": "0499488b-00d3-4a59-9f32-283dc4e079dd",
					"name": "Риск-ориентированный подход",
					"difficulty": "medium",
					"duration": 30,
					"subtitle": "Откройте для себя все стороны риска и научитесь ими управлять!",
					"pictureLink": "lms-prod/courses-covers/90a2cbe7-e4ca-4b52-9a8e-ea4495bb1b7d.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "finished",
					"completeLessons": 6,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 6
				},
				{
					"id": "519b7f1c-9acd-4978-9717-b02fadfed952",
					"name": "Культура производственной безопасности",
					"difficulty": "easy",
					"duration": 30,
					"subtitle": "Все, что вы боялись спросить о культуре производственной безопасности и инструментах ее развития.",
					"pictureLink": "lms-prod/courses-covers/0ee1e5dd-be72-4979-8405-e62ce1409079.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "finished",
					"completeLessons": 6,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 6
				}
			]
		},
		{
			"id": "640b8e46-e3b2-4726-9c08-56c04897a0d6",
			"name": "Финансы",
			"items": [
				{
					"id": "05d4bbe6-2aca-4cf5-91f4-a129b4f23c61",
					"name": "(Не)детские деньги: говорим о финансах с детьми",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Узнайте, что поможет вырастить будущего миллионера!",
					"pictureLink": "lms-prod/courses-covers/6a68379e-9bb8-4559-ac3d-a8f856cf4c08.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6E8FF",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:21:19.503Z",
							"updatedAt": "2024-01-15T12:38:33.859Z",
							"id": "640b8e46-e3b2-4726-9c08-56c04897a0d6",
							"name": "Финансы",
							"isActive": true,
							"activatedAt": "2024-01-15T12:38:33.858Z"
						}
					],
					"tags": [
						{
							"id": "390b2fdc-8e13-475b-8d54-38775760d881",
							"name": "Сбережения"
						}
					],
					"totalLessons": 7
				},
				{
					"id": "d2f45367-9cce-4d24-b2b8-8bbf6eed67ec",
					"name": "Налоговые вычеты. Инструкция по получению",
					"difficulty": "easy",
					"duration": 35,
					"subtitle": "Пошаговый алгоритм для возврата части уплаченного налога",
					"pictureLink": "lms-prod/courses-covers/edfc4a58-38e7-4850-9006-102271664f3f.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6E8FF",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:21:19.503Z",
							"updatedAt": "2024-01-15T12:38:33.859Z",
							"id": "640b8e46-e3b2-4726-9c08-56c04897a0d6",
							"name": "Финансы",
							"isActive": true,
							"activatedAt": "2024-01-15T12:38:33.858Z"
						}
					],
					"tags": [],
					"totalLessons": 8
				},
				{
					"id": "dd010712-ad47-4024-a96d-e863b2678083",
					"name": "Мастер над монетой: 5 шагов к финансовому благополучию",
					"difficulty": "easy",
					"duration": 60,
					"subtitle": "Все о финансовой грамотности для начинающих: учимся управлять бюджетом, копить на любые цели и приумножать свои доходы",
					"pictureLink": "lms-prod/courses-covers/b23e136d-da36-4ed0-8c01-447c1291de2b.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6E8FF",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:21:19.503Z",
							"updatedAt": "2024-01-15T12:38:33.859Z",
							"id": "640b8e46-e3b2-4726-9c08-56c04897a0d6",
							"name": "Финансы",
							"isActive": true,
							"activatedAt": "2024-01-15T12:38:33.858Z"
						}
					],
					"tags": [
						{
							"id": "390b2fdc-8e13-475b-8d54-38775760d881",
							"name": "Сбережения"
						}
					],
					"totalLessons": 5
				}
			]
		},
		{
			"id": "808cc170-8ca9-4ef6-acdc-9b0bf1ef096c",
			"name": "Жизнь",
			"items": [
				{
					"id": "a50a491c-0337-4810-badd-8f2dce1e3e9c",
					"name": "Будет сделано: как побороть страх новых начинаний",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Глаза боятся, а вы нет!",
					"pictureLink": "lms-prod/courses-covers/8a4d1ef1-7bf5-4f1d-8c42-2c3e139a021c.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#FFE6E1",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-10-19T08:14:02.812Z",
							"updatedAt": "2023-10-19T08:14:02.812Z",
							"id": "808cc170-8ca9-4ef6-acdc-9b0bf1ef096c",
							"name": "Жизнь",
							"isActive": true,
							"activatedAt": "2023-10-19T08:14:02.800Z"
						}
					],
					"tags": [],
					"totalLessons": 6
				},
				{
					"id": "8905e328-cfe9-4e33-bede-f1286510dec2",
					"name": "Абьюзер и газлайтер: 10 слов из современной психологии",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Избежать сегодня таких слов, как прокрастинация, ресурс или токсичность, кажется просто невозможным. Давайте разбираться",
					"pictureLink": "lms-prod/courses-covers/68530515-7560-455b-a466-d714bca3232d.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#FFE6E1",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-10-19T08:14:02.812Z",
							"updatedAt": "2023-10-19T08:14:02.812Z",
							"id": "808cc170-8ca9-4ef6-acdc-9b0bf1ef096c",
							"name": "Жизнь",
							"isActive": true,
							"activatedAt": "2023-10-19T08:14:02.800Z"
						}
					],
					"tags": [],
					"totalLessons": 10
				}
			]
		},
		{
			"id": "coursesFromUserGroup",
			"items": []
		}
	]
}


# запрос на энергию за курс
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/sputnik/courses/f0ef3232-078b-403a-bb65-9fcf29d84f12/program',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': '8d7c7cbeb6ddad2a6a801a121e6e78de7d7a81aded5d1e0d34c5c49e1a6df5ad.30a518f6334f2a6d2ec0c59ba2328068248c53222ba49bcbcc32e22cec23f9b681db449876f0d5684a6eb28afa53ab0fdd1bf536539640da3f402e10f8980fea23c90ba812fbc400ab51c4ac16d3427cd3831bdc9d828bf2e711a5f4016985ffce357f346116fca53c2b32b0a653b12ceebfbeb60c2db44024189fc296dbcd34da1321ce2336a837c03a13866cc7abb4b288717f07c2ca6ce1fa9cf2a3bda189b3db5722fb43c291d83f8da396be67279f886f9bb89987ff09573dc354152b3eecc9e0ed6821a5f525880ea373bbc90de32b4dbf8ebda1989fd7f44acdef865731c02be323c7d3aa3233f13cc3957e7ad4adfb77d9076599f6a23dc1f9f0cdfb',
    'sentry-trace': '90a85f708d6c49038a1b4355cfb8afde-8429b8ca4f278c3c-1',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=90a85f708d6c49038a1b4355cfb8afde,sentry-sample_rate=1,sentry-sampled=true',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5NTU2OTYsImlhdCI6MTcwODk1Mzg5NiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiI1ZjVmY2YzNy1jZjliLTQzMjQtOGQ5Yi1lMjFmY2FkYzQxMjkiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5YmIzMWVjYi1hM2ZjLTQwYWYtODcwMy1iYTViMDkxZmE4MjIiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.cht6MCVQRNUwruzE-7zp-m9gh4DkqmRMTdgA01Zv2b5ggFL8SrDqgW5eXVUeo4-N6azZmKru_Y1neQ7Hb1iOHnRc0B-kl6WgjMm3szbyeo5YVs5LuH9DcaiS1Mz3ob1gyWBVI-0kXmZmWo46mnxka47txre7TPP-Pt7Z6Up554RGat27bLRQyeHt3R3T_CaABdzdJO0EOmP3xhg9u_WX7DAeokcO6py-eJMScSMKM0TfziFePzlChM4ZVUzCsIC316hZnRoKfP_RN82rLLXVs2iiRl9aRePGTET6B7GUqX1LIRmANa-cXPFPdz8VeUHg5dNtFtTsuG7wxQu0QYCZlA',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=8d7c7cbeb6ddad2a6a801a121e6e78de7d7a81aded5d1e0d34c5c49e1a6df5ad.30a518f6334f2a6d2ec0c59ba2328068248c53222ba49bcbcc32e22cec23f9b681db449876f0d5684a6eb28afa53ab0fdd1bf536539640da3f402e10f8980fea23c90ba812fbc400ab51c4ac16d3427cd3831bdc9d828bf2e711a5f4016985ffce357f346116fca53c2b32b0a653b12ceebfbeb60c2db44024189fc296dbcd34da1321ce2336a837c03a13866cc7abb4b288717f07c2ca6ce1fa9cf2a3bda189b3db5722fb43c291d83f8da396be67279f886f9bb89987ff09573dc354152b3eecc9e0ed6821a5f525880ea373bbc90de32b4dbf8ebda1989fd7f44acdef865731c02be323c7d3aa3233f13cc3957e7ad4adfb77d9076599f6a23dc1f9f0cdfb',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = {
	"batch": [
		{
			"anonymousId": "5234f7bf-1c1a-4ba9-b6d1-653492ad973f",
			"event": "lms_course_started",
			"messageId": "28a01d07-d1d7-49f2-82a9-f1eb9a921998",
			"properties": {
				"course_id": "f0ef3232-078b-403a-bb65-9fcf29d84f12"
			},
			"timestamp": "2024-02-26T13:53:04.961Z",
			"type": "track",
			"userId": "[a2ad3873-ba7a-4af3-a154-3597ee733792,80f8a415-c1ad-4d70-957b-587e42f6ac03]"
		}
	],
	"sentAt": "2024-02-26T13:53:04.961Z",
	"writeKey": "sdk"
}
response = requests.post('https://web.gid.ru/api/event-tracker/public/v1/collect', cookies=cookies, headers=headers, data=data)



# ответ на запрос курсов https://web.gid.ru/api/lms/v2/courses
{
	"items": [
		{
			"id": "88667f2c-fc7d-470f-842a-29ab702c7bf7",
			"name": "Продолжить обучение",
			"items": [
				{
					"id": "f0ef3232-078b-403a-bb65-9fcf29d84f12",
					"name": "Идеальное выступление: как впечатлять своими идеями",
					"difficulty": "medium",
					"duration": 70,
					"subtitle": "Создайте презентацию мечты и добейтесь успехов",
					"pictureLink": "lms-prod/courses-covers/97b86cdc-3860-4b11-b544-206db1fef1d5.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "started",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [],
					"totalLessons": 8
				},
				{
					"id": "4447b359-6998-4c96-8687-d87583a0fc9e",
					"name": "Тестирование по культуре производственной безопасности",
					"difficulty": "medium",
					"duration": 10,
					"subtitle": "Закрепите материал курса «Культура производственной безопасности»",
					"pictureLink": "lms-prod/courses-covers/ea982a15-d905-475c-934e-77ce5fad904f.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "started",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 1
				}
			]
		},
		{
			"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
			"name": "Карьера",
			"items": [
				{
					"id": "c1ff2bc7-0a3f-4b2f-8710-0361293b8811",
					"name": "Как работать, когда вокруг все меняется",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Узнайте, как работать в условиях изменений",
					"pictureLink": "lms-prod/courses-covers/7703b433-c893-4652-9a02-cafc914d81ca.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [],
					"totalLessons": 6
				},
				{
					"id": "c4af6bbb-2526-4d1e-a34b-b4a0f7da023e",
					"name": "Тайм-менеджмент: заставляем время работать на себя",
					"difficulty": "medium",
					"duration": 90,
					"subtitle": "Станьте властелином времени и личной эффективности!",
					"pictureLink": "lms-prod/courses-covers/b565d2c9-d6a7-4acb-8817-4a500bc38027.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 8
				},
				{
					"id": "e59c239e-2070-470e-a81d-1dfc2aebea1d",
					"name": "Гибкие навыки: что это и почему важно их прокачивать",
					"difficulty": "medium",
					"duration": 30,
					"subtitle": "Главное о самых важных soft skills для вашего карьерного роста.",
					"pictureLink": "lms-prod/courses-covers/a07001bb-33b0-4788-998c-0c74dcbeeb38.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 7
				},
				{
					"id": "e5a051dd-2227-44fb-9b01-531ea24e7996",
					"name": "Как решать конфликты на работе",
					"difficulty": "easy",
					"duration": 30,
					"subtitle": "Узнайте, как предостеречь появление, сдержать развитие и способствовать разрешению конфликтов на рабочем месте",
					"pictureLink": "lms-prod/courses-covers/3cdd2927-f09f-4603-aff3-5a2ec0212308.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 5
				},
				{
					"id": "f067c4a0-0896-4f22-a3dc-b20f04b7c4b8",
					"name": "Обратная связь: секреты эффективной коммуникации",
					"difficulty": "medium",
					"duration": 45,
					"subtitle": "Учимся говорить, чтобы поняли, и слушать, чтобы услышать",
					"pictureLink": "lms-prod/courses-covers/5ea2b097-63a1-415b-89ac-30e73849bc73.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 7
				},
				{
					"id": "ddbc8998-695b-497c-8d25-096a365dc3f8",
					"name": "От хаоса к порядку: гибкие методологии для работы и жизни",
					"difficulty": "medium",
					"duration": 50,
					"subtitle": "Узнайте, как организовать работу в команде и довести проект до конца",
					"pictureLink": "lms-prod/courses-covers/8285db00-60a6-46cc-bff0-fe17f341eaa1.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 7
				},
				{
					"id": "eef95d64-9da8-4c97-92bd-9cecb181779b",
					"name": "Корпоративная культура. Стань частью успешной команды!",
					"difficulty": "easy",
					"duration": 21,
					"subtitle": "Почувствуйте все преимущества развитой корпоративной культуры на себе и в команде!",
					"pictureLink": "lms-prod/courses-covers/52d562b9-6d1a-42dc-a819-f14a676cf292.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [],
					"totalLessons": 3
				},
				{
					"id": "f0ef3232-078b-403a-bb65-9fcf29d84f12",
					"name": "Идеальное выступление: как впечатлять своими идеями",
					"difficulty": "medium",
					"duration": 70,
					"subtitle": "Создайте презентацию мечты и добейтесь успехов",
					"pictureLink": "lms-prod/courses-covers/97b86cdc-3860-4b11-b544-206db1fef1d5.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#F3F0E3",
					"status": "started",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:29:25.537Z",
							"updatedAt": "2023-06-09T06:16:40.058Z",
							"id": "891f2d20-9bdd-4510-8f86-7788fcc30620",
							"name": "Карьера",
							"isActive": true,
							"activatedAt": "2023-06-08T12:29:25.528Z"
						}
					],
					"tags": [],
					"totalLessons": 8
				}
			]
		},
		{
			"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
			"name": "Здоровье",
			"items": [
				{
					"id": "f61bdad7-1925-4b8f-a848-63280dcf3796",
					"name": "Как справиться с тревогой: причины, практики и помощь",
					"difficulty": "easy",
					"duration": 45,
					"subtitle": "Научитесь управлять тревожными состояниями и брать эмоции под контроль",
					"pictureLink": "lms-prod/courses-covers/fde0f798-b8f5-4e9d-aa0f-91918d584997.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [],
					"totalLessons": 10
				},
				{
					"id": "8372237c-be82-43e8-bb80-6f764e6e435a",
					"name": "Здоровое питание: как найти баланс",
					"difficulty": "easy",
					"duration": 60,
					"subtitle": "Ваш путеводитель в здоровую жизнь: составляем меню на каждый день и учимся принимать себя",
					"pictureLink": "lms-prod/courses-covers/47127303-7e8e-4653-8b1d-53832e0eaecc.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						},
						{
							"id": "f41020bb-e46e-4e66-82f4-e15ab17b5762",
							"name": "Питание"
						}
					],
					"totalLessons": 6
				},
				{
					"id": "431b4167-1bf3-445e-bd7f-6aee405d7ca5",
					"name": "Секреты отдыха: перезагрузка без последствий",
					"difficulty": "medium",
					"duration": 40,
					"subtitle": "Главное об отдыхе и о том, как провести его удачно.",
					"pictureLink": "lms-prod/courses-covers/768e206c-020d-48fb-b691-45064ab553e5.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [
						{
							"id": "f6ce731e-d521-46ce-b5e0-68fc5ef35033",
							"name": "Продуктивность"
						}
					],
					"totalLessons": 5
				},
				{
					"id": "a8cae4fa-e182-42d4-aa88-d9b00c4b5f1c",
					"name": "Как начать и не бросить бегать",
					"difficulty": "medium",
					"duration": 45,
					"subtitle": "Начните бегать и сделайте это своим любимым и полезным хобби!",
					"pictureLink": "lms-prod/courses-covers/a1214834-fdc2-4513-9cf5-c29f5d680531.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [],
					"totalLessons": 5
				},
				{
					"id": "94046294-0b90-4e13-9d21-1378e04a4b45",
					"name": "Пойдем ходить! Руководство по северной ходьбе для начинающих",
					"difficulty": "easy",
					"duration": 30,
					"subtitle": "Откройте для себя новый вид спорта, станьте здоровее и зарядитесь на успех!",
					"pictureLink": "lms-prod/courses-covers/523508d8-1ea2-40d5-9c05-e1de7f0643c3.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6EED3",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:56.513Z",
							"updatedAt": "2023-06-09T06:16:28.601Z",
							"id": "6e497e28-ded7-4797-bdfe-2aad89a99eea",
							"name": "Здоровье",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:56.507Z"
						}
					],
					"tags": [],
					"totalLessons": 4
				}
			]
		},
		{
			"id": "56069470-86be-4d4f-b023-162f6be62e3d",
			"name": "Наука и искусство",
			"items": [
				{
					"id": "2f708fc3-0de4-498b-accd-ce00b0c96f46",
					"name": "Компьютерные технологии будущего",
					"difficulty": "medium",
					"duration": 45,
					"subtitle": "Сравниваем технологические мечты и реальность, разбираемся в работе окружающих нас устройств",
					"pictureLink": "lms-prod/courses-covers/60a74ba7-e440-4477-bf43-d02dee19841a.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 5
				},
				{
					"id": "e1256cfc-bbf8-47f9-9f09-0029576d0800",
					"name": "Древние цивилизации: как жили люди прошлого и что досталось потомкам",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Узнайте все подробности жизни предков современного человека",
					"pictureLink": "lms-prod/courses-covers/b81e3a4b-8ebc-4545-8e69-81d44d314d33.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 9
				},
				{
					"id": "e7849b91-50c4-49a5-83b2-8a98fea0d7e9",
					"name": "За кадром: киностудия нашего времени",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Узнайте, как создается настоящее кино и где в нем скрыта магия.",
					"pictureLink": "lms-prod/courses-covers/26a92b11-8e81-43c9-9b61-2b632b284bf6.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 10
				},
				{
					"id": "09e52d60-996c-499e-b1c8-bf38f02e87f9",
					"name": "Далекий космос: история освоения и влияние на нашу жизнь",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Найдите космос вокруг себя и узнайте, с чего началось его покорение!",
					"pictureLink": "lms-prod/courses-covers/2357dc94-25f3-4ba8-9b0f-5d1b89d2ba08.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 5
				},
				{
					"id": "e2315bbb-abac-4291-b8f9-86b5a9d18130",
					"name": "6 неочевидных русских изобретений",
					"difficulty": "easy",
					"duration": 30,
					"subtitle": "Курс, в котором изобретатели сами расскажут вам о своих открытиях. Так вы еще не изучали историю!",
					"pictureLink": "lms-prod/courses-covers/936be8c3-5840-4c0c-aeb8-ecfde85da987.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#E6E2F4",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:27:12.058Z",
							"updatedAt": "2023-07-05T09:04:19.564Z",
							"id": "56069470-86be-4d4f-b023-162f6be62e3d",
							"name": "Наука и искусство",
							"isActive": true,
							"activatedAt": "2023-06-08T12:27:15.848Z"
						}
					],
					"tags": [],
					"totalLessons": 7
				}
			]
		},
		{
			"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
			"name": "Я выбираю безопасность",
			"items": [
				{
					"id": "22bbc87e-34fa-4edd-abeb-456f70722673",
					"name": "Культура и приверженность производственной безопасности: видеокурс",
					"difficulty": "hard",
					"duration": 90,
					"subtitle": "Учимся оценивать риски, предотвращать последствия и достигать целей безопасным образом!",
					"pictureLink": "lms-prod/courses-covers/513efd80-5653-495d-9bef-ba1deffc7734.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 4
				},
				{
					"id": "9a0cb068-8750-41f1-88ef-223f6022081b",
					"name": "Тестирование по риск-ориентированному подходу",
					"difficulty": "medium",
					"duration": 10,
					"subtitle": "Проверьте свои знания по управлению рисками",
					"pictureLink": "lms-prod/courses-covers/aeb1799c-b42e-4d4f-80d1-07ab2541ce42.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 1
				},
				{
					"id": "4447b359-6998-4c96-8687-d87583a0fc9e",
					"name": "Тестирование по культуре производственной безопасности",
					"difficulty": "medium",
					"duration": 10,
					"subtitle": "Закрепите материал курса «Культура производственной безопасности»",
					"pictureLink": "lms-prod/courses-covers/ea982a15-d905-475c-934e-77ce5fad904f.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "started",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 1
				},
				{
					"id": "0499488b-00d3-4a59-9f32-283dc4e079dd",
					"name": "Риск-ориентированный подход",
					"difficulty": "medium",
					"duration": 30,
					"subtitle": "Откройте для себя все стороны риска и научитесь ими управлять!",
					"pictureLink": "lms-prod/courses-covers/90a2cbe7-e4ca-4b52-9a8e-ea4495bb1b7d.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "finished",
					"completeLessons": 6,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 6
				},
				{
					"id": "519b7f1c-9acd-4978-9717-b02fadfed952",
					"name": "Культура производственной безопасности",
					"difficulty": "easy",
					"duration": 30,
					"subtitle": "Все, что вы боялись спросить о культуре производственной безопасности и инструментах ее развития.",
					"pictureLink": "lms-prod/courses-covers/0ee1e5dd-be72-4979-8405-e62ce1409079.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D9E3F0",
					"status": "finished",
					"completeLessons": 6,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:20:02.748Z",
							"updatedAt": "2023-06-08T12:20:02.748Z",
							"id": "b8e18bb1-3280-4da2-8ffc-a15e1730d0d8",
							"name": "Я выбираю безопасность",
							"isActive": true,
							"activatedAt": "2023-06-08T12:20:02.739Z"
						}
					],
					"tags": [],
					"totalLessons": 6
				}
			]
		},
		{
			"id": "640b8e46-e3b2-4726-9c08-56c04897a0d6",
			"name": "Финансы",
			"items": [
				{
					"id": "05d4bbe6-2aca-4cf5-91f4-a129b4f23c61",
					"name": "(Не)детские деньги: говорим о финансах с детьми",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Узнайте, что поможет вырастить будущего миллионера!",
					"pictureLink": "lms-prod/courses-covers/6a68379e-9bb8-4559-ac3d-a8f856cf4c08.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6E8FF",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:21:19.503Z",
							"updatedAt": "2024-01-15T12:38:33.859Z",
							"id": "640b8e46-e3b2-4726-9c08-56c04897a0d6",
							"name": "Финансы",
							"isActive": true,
							"activatedAt": "2024-01-15T12:38:33.858Z"
						}
					],
					"tags": [
						{
							"id": "390b2fdc-8e13-475b-8d54-38775760d881",
							"name": "Сбережения"
						}
					],
					"totalLessons": 7
				},
				{
					"id": "d2f45367-9cce-4d24-b2b8-8bbf6eed67ec",
					"name": "Налоговые вычеты. Инструкция по получению",
					"difficulty": "easy",
					"duration": 35,
					"subtitle": "Пошаговый алгоритм для возврата части уплаченного налога",
					"pictureLink": "lms-prod/courses-covers/edfc4a58-38e7-4850-9006-102271664f3f.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6E8FF",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:21:19.503Z",
							"updatedAt": "2024-01-15T12:38:33.859Z",
							"id": "640b8e46-e3b2-4726-9c08-56c04897a0d6",
							"name": "Финансы",
							"isActive": true,
							"activatedAt": "2024-01-15T12:38:33.858Z"
						}
					],
					"tags": [],
					"totalLessons": 8
				},
				{
					"id": "dd010712-ad47-4024-a96d-e863b2678083",
					"name": "Мастер над монетой: 5 шагов к финансовому благополучию",
					"difficulty": "easy",
					"duration": 60,
					"subtitle": "Все о финансовой грамотности для начинающих: учимся управлять бюджетом, копить на любые цели и приумножать свои доходы",
					"pictureLink": "lms-prod/courses-covers/b23e136d-da36-4ed0-8c01-447c1291de2b.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#D6E8FF",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-06-08T12:21:19.503Z",
							"updatedAt": "2024-01-15T12:38:33.859Z",
							"id": "640b8e46-e3b2-4726-9c08-56c04897a0d6",
							"name": "Финансы",
							"isActive": true,
							"activatedAt": "2024-01-15T12:38:33.858Z"
						}
					],
					"tags": [
						{
							"id": "390b2fdc-8e13-475b-8d54-38775760d881",
							"name": "Сбережения"
						}
					],
					"totalLessons": 5
				}
			]
		},
		{
			"id": "808cc170-8ca9-4ef6-acdc-9b0bf1ef096c",
			"name": "Жизнь",
			"items": [
				{
					"id": "a50a491c-0337-4810-badd-8f2dce1e3e9c",
					"name": "Будет сделано: как побороть страх новых начинаний",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Глаза боятся, а вы нет!",
					"pictureLink": "lms-prod/courses-covers/8a4d1ef1-7bf5-4f1d-8c42-2c3e139a021c.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#FFE6E1",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-10-19T08:14:02.812Z",
							"updatedAt": "2023-10-19T08:14:02.812Z",
							"id": "808cc170-8ca9-4ef6-acdc-9b0bf1ef096c",
							"name": "Жизнь",
							"isActive": true,
							"activatedAt": "2023-10-19T08:14:02.800Z"
						}
					],
					"tags": [],
					"totalLessons": 6
				},
				{
					"id": "8905e328-cfe9-4e33-bede-f1286510dec2",
					"name": "Абьюзер и газлайтер: 10 слов из современной психологии",
					"difficulty": "medium",
					"duration": 60,
					"subtitle": "Избежать сегодня таких слов, как прокрастинация, ресурс или токсичность, кажется просто невозможным. Давайте разбираться",
					"pictureLink": "lms-prod/courses-covers/68530515-7560-455b-a466-d714bca3232d.png",
					"hasCoverBackground": true,
					"coverBackgroundColor": "#FFE6E1",
					"status": "available",
					"completeLessons": 0,
					"publishingStatus": "published",
					"chapters": [
						{
							"createdAt": "2023-10-19T08:14:02.812Z",
							"updatedAt": "2023-10-19T08:14:02.812Z",
							"id": "808cc170-8ca9-4ef6-acdc-9b0bf1ef096c",
							"name": "Жизнь",
							"isActive": true,
							"activatedAt": "2023-10-19T08:14:02.800Z"
						}
					],
					"tags": [],
					"totalLessons": 10
				}
			]
		},
		{
			"id": "coursesFromUserGroup",
			"items": []
		}
	]
}


# запрос на окончание прохождения курса
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8',
    'Referer': 'https://web.gid.ru/sputnik/courses/4447b359-6998-4c96-8687-d87583a0fc9e/a9200281-48ad-48cb-ad88-95ef9bf5a20f',
    'X-Requested-With': 'XMLHttpRequest',
    'X-CSRF-TOKEN': '2a54a6466d58071749465c399b5caf337bcdad0170a543c2b4596c44e65809fd.4fecafe026a615d613c54af53d0ca6d07efea5ec230457b06b164e52e60bec8d88da77aa3ad0ca3fc0ff854f3969f0a85ebd017376b0d5d5ecf6e18816656ba62239b85b12ca3797568cee96594ecce1292de7b920e93cc344d4935d096d5eb95ff6a0b604e221fd357e582116ae52884eb5c7290ba9f1a60ac965a13488872157e1881c4ed18fc0aa5a9b7536b69ef7dc65b02a8d48a349a66955f8a7a99fb1f286f0cf9d1dc2e3a6847943056088b726ac87245db62e54dad544d438ad7cc0390eb73aff23961575dcbc0fd069dadf6eda4403936676d7446f9ebb44890f47c1018b11a953139fd725b1e3629745244d1b296093fe1f0a55efc7f709bfca22',
    'sentry-trace': '9478783c46f7417a84b8ebded61007bc-93069038ac07a35f',
    'baggage': 'sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=9478783c46f7417a84b8ebded61007bc',
    'Origin': 'https://web.gid.ru',
    'DNT': '1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDkwMTY0OTAsImlhdCI6MTcwOTAxNDY5MCwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJjYjdkODQ2MC04N2FjLTQzMzctYWI5Ni02NzJhMTE2YTcyYTgiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI5ZjU5YzAzZC1hOTlhLTQ4YWEtYmExMC01ZmZkODc4NTY2ZmEiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.XZx6zOE4C8gLnOiCeKdGXBBTufFE_YvZjUrWcpjeEvMEaUhjin9jHqbMAbLk0j84SYaAExBs4ChtEUfRVxk_YgRlq1gTbhmvWHpRsmACniTipPbwfye8eehJnlVKxvVH6eS4KdfZOasZ2wVaSE4jzdFNU8uQ2Ps0e_38EsosU4LySi24JXRGJ4FI52JuevnYs-INv8YVsGNi0-n969hjImrRHEfrHHZHu73Fu7p-P1NTowMuLjjRaqOgGawkJ8zmdsyujxHnR_6rp_wchcYAVYysBF4_jYs12pbb3B6Jl9j38EM5Q82p_B5Inur-z_Iw-gmZx4tpFb6oAPZQI3BtWg',
    'Connection': 'keep-alive',
    # 'Cookie': 'X-CSRF-TOKEN=2a54a6466d58071749465c399b5caf337bcdad0170a543c2b4596c44e65809fd.4fecafe026a615d613c54af53d0ca6d07efea5ec230457b06b164e52e60bec8d88da77aa3ad0ca3fc0ff854f3969f0a85ebd017376b0d5d5ecf6e18816656ba62239b85b12ca3797568cee96594ecce1292de7b920e93cc344d4935d096d5eb95ff6a0b604e221fd357e582116ae52884eb5c7290ba9f1a60ac965a13488872157e1881c4ed18fc0aa5a9b7536b69ef7dc65b02a8d48a349a66955f8a7a99fb1f286f0cf9d1dc2e3a6847943056088b726ac87245db62e54dad544d438ad7cc0390eb73aff23961575dcbc0fd069dadf6eda4403936676d7446f9ebb44890f47c1018b11a953139fd725b1e3629745244d1b296093fe1f0a55efc7f709bfca22',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

data = '{action:finish}'

response = requests.put(
    'https://web.gid.ru/api/lms/lessons/a9200281-48ad-48cb-ad88-95ef9bf5a20f',
    cookies=cookies,
    headers=headers,
    data=data,
)
