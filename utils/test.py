import pprint
import datetime as dt

import pymongo


client = pymongo.MongoClient('localhost', 27017)
db = client['gks_bot_db']
gid_db = client['gid_db']


auth_gid = gid_db['auth_gid']
users_gid = gid_db['users']


mbd = {
  "username": "huji",
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDkwNjM3NTMsImlhdCI6MTcwOTA2MTk1MywiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiIyYTE4NWIxNy1jMzg0LTRhNmItYTIwOC03NzdjMDZkMzczMzUiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI1MjEzZWZkOS02ZjMxLTQ2NzItODFiNC02NmQ0ZTU4NmY2N2QiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.OXZm7qvzHfaavFxcK8SrYJ3ggQEn3j5OVU7I2akhGtbSg7j44jvUmC-MTIHQi_pCbkBwNjIBRE67kBf_ivVsSjLFNY4dZMyJ5j2iyNjc_PlXeWFODiWPy_HKn87OZrboX_JTMUOMMUbwKIE9pWjHOZE6r3loTFzKAkjPde2HlSghvrO4j4_2OB7-p-KyR6PYIsu-PYOc6ufhCjLddEU5Y8A0MuXcqQzp-12D1PvPeQ7BKjslBKr839qRAvMh7XwIEnt1RzZHckl-NfrhWJVDzbq77Zb2gswycVc3W0riA3knYjCQsKJEKfgaU5Uzq9sWrwhMM3TkTJhAIP6_NMPy_w",
  "expires_in": 1800,
  "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDkwNjM3NTMsImlhdCI6MTcwOTA2MTk1MywiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJiNmNiZjljZS03Y2Y1LTRkNDMtOTNiNi02OTEyMDZmNzNiMmIiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwiYXVkIjoid2ViYXBwIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiSUQiLCJhenAiOiJ3ZWJhcHAiLCJub25jZSI6IjUyMTNlZmQ5LTZmMzEtNDY3Mi04MWI0LTY2ZDRlNTg2ZjY3ZCIsInNlc3Npb25fc3RhdGUiOiI5NjQwZmY4Yi1jN2FiLTQxOTctOTFhZS00ZGEwYzRlZWUzN2UiLCJhdF9oYXNoIjoic0l1SnVQYW1pdnhjOWF3RW4wQWZEUSIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.Ni4-xAhD9Skxsy3Pi4ALee9YvtMtdMof2CxpXj9dZscpSCj7b9IpGNjFut63cJ79yd6lQhGhp1ki2CNiV4b2S8y-WwZvSIpRrMPHsWU7flCywRqbB3fstr0hFKEinVnT_kgB3Iqw2m0_l5pX5Xj8t8Zf6pS6WRGKGt76KcW92H9BQK0XmbsUuwt2lXfkd2PH3KdeGyO3fMSFBZSYlQVr7UzUqS29rvrC7wVsMLCB4m0fnB-p1HNHk7DHFdQ5-pL_giXBG988UnX-QFg0NlmgtzrM-aKA26FWiV8VP-6wuyjbJSfy6FBLoajtTkELkA5PcSYVSIhhAGnlkP6PDUD3pQ",
  "not_before_policy": 1706779079,
  "refresh_expires_in": 2411821,
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlY2E4MjE5Ni0yZWEyLTRhZTItYjg0OS0yMjA1NDZjYzJlMWIifQ.eyJleHAiOjE3MTE0NzM3NzQsImlhdCI6MTcwOTA2MTk1MywianRpIjoiZTc5MzJjOWYtYTJlMS00ZWEwLWI3NzYtMDg2MGRkOGFkZWE4IiwiaXNzIjoiaHR0cHM6Ly9hcHAuZ2lkLnJ1L2F1dGgvcmVhbG1zL2dpZCIsImF1ZCI6Imh0dHBzOi8vYXBwLmdpZC5ydS9hdXRoL3JlYWxtcy9naWQiLCJzdWIiOiJhMmFkMzg3My1iYTdhLTRhZjMtYTE1NC0zNTk3ZWU3MzM3OTIiLCJ0eXAiOiJSZWZyZXNoIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI1MjEzZWZkOS02ZjMxLTQ2NzItODFiNC02NmQ0ZTU4NmY2N2QiLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwic2NvcGUiOiJvcGVuaWQiLCJzaWQiOiI5NjQwZmY4Yi1jN2FiLTQxOTctOTFhZS00ZGEwYzRlZWUzN2UifQ.CoplS0hJHfY8kKGLRzaFDuxoOHxjppXO3aY8vgw4Ino",
  "scope": "openid",
  "session_state": "9640ff8b-c7ab-4197-91ae-4da0c4eee37e",
  "token_type": "Bearer",
  'csrf': 'dc2b7f5a39a2e9e9253812caba6ffe02ad8f4a41c54a3ea113a32f078adce3e6.9fc11d20084007878ea84080387b42e05de88d947746a74d1bf68a37e800a7aba06c5144ff31e2516250d0f4ea36115065296fca1dab631afeb51740f58e29d1264dba433e2c0b210fc28553feefabc27628993aff947477d93d4436c333b3efd2ce7f88a47ac31c1ff3efaa9d8d495b0e7167fe5d18561b17ac988252562806853065660fdc585d8703b11a52c24e0a2ccfd8c1929f6dfaee3d8fdf8f1fa3499475e0caa339bb998f962eacec8aa6ac8177ee2979c60e5665f81880749e252abff15082cf9403614278a7d067ca228b1765c28b588f7274ac5ebffc30d1c2129589e4b5850b2c676448b9aa4690a0b9ae78977223c15692dc54838e6f7f5fa3'
}

USERS = {
    'Алферов Евгений Александрович': '733cbc6a-0a87-4a1a-9ad1-1afebd3c01d1',
    'Заяц Денис Сергеевич': '28169937-4b30-45da-8852-9e87084d5d58',
    'Волохов Олег Александрович': '1eee5748-e563-431a-b1de-bad45de05c69',
    'Андриенко Никита Владимирович': 'c5b413a4-de6c-4ec0-96db-8a12acc34cfb',
    'Калинин Андрей Александрович': '76dec40c-fac2-454c-88e4-349d4de27c49',
    'Иванов Сергей Николаевич': 'c7c9aa6c-6eb8-4446-99a8-995439291ff8',
    'Шевцов Сергей Иванович': 'b22b9353-7e34-4ab7-b67e-860926af3502',
    'Муравлев Валерий Геннадьевич': '6d602e0d-7f42-45b4-b049-b7348851edb4',
    'Ковальский Иван Николаевич': '4cc5acb8-24fb-47e2-b99e-e18c0c3c39a0',
    'Подлисецкий Дмитрий Олегович': 'f252763d-6cdf-4848-9e38-1b54597a34eb',
    'Кукатов Михаил Вячеславович': '18113ee7-2f88-449c-8720-04ecf0c37a24',
    'Сабитов Тимур Фаридович': '9ebc0cdf-83a3-471a-9d1c-bac5ad4d7040',
	'Сайко Олег Анатольевич': '06a175aa-2747-469a-b7d1-9c263614007d',
    'Антоненков Дмитрий Александрович': 'b7e470cd-9a1e-4e8b-ba5a-344c8ce67cdf',
    'Нурдинов Рамиль Гайнуллович': 'd6f857a0-7942-4a4e-8d39-d9348539bc1f',
    'Игуменщев Антон Владимирович': '79749adb-f1d1-41f9-9c8c-20c9412ccb9e',
    'Деревянко Александр Иванович': 'b30eaff5-5a7e-403c-986a-3b45da4dae3c',
    'Кудряшов Геннадий Алексеевич': '24223a29-061b-40dc-8b78-3805ca921118',
    'Сулоев Иван Владимирович': '2c99c733-8f28-490a-bbcf-93ed3437d230',
    'Синенко Александр Александрович': '2e8d8e73-d128-45c7-86f7-b7197d64588d',
    'Газзаев Егор Казбекович': '5f5ec211-d726-4714-a34d-9d7e4edafae2',
    'Матушевский Ян Вячеславович': '2a86847c-0369-4e0b-beb5-732d7861d6b3',
    'Матушевский Иван Вячеславович': '79c566dd-18cc-4f16-83b8-e6c201fd6ade',
    'Артемьев Сергей Юрьевич': 'a82cbcda-6e6d-4f08-b36e-47675a85af6d',
    'Дашковский Игорь Юрьевич': '83e1d148-d173-401b-9d16-a97547e8907d',
    'Погорелов Андрей Сергеевич': 'c1a0dad3-48e5-4d54-b262-b619a6da891b',
    'Кокарев Александр Алексеевич': '0559a0b2-97f9-416a-8a73-96a7a59891f3',
    'Мартьянов Максим Александрович': '6d802cf8-1a9e-407f-abe3-88af28081d6d',
}

auth_gid.update_one(
    {'username': 'huji'},
    {'$set': {
        'datetime': dt.datetime.now(),
        'access_token': mbd['access_token'],
        'refresh_expires_in': mbd['refresh_expires_in'],
        'expires_in': mbd['expires_in'],
        'refresh_token': mbd['refresh_token'],
        'token_type': mbd['token_type'],
        'id_token': mbd['id_token'],
        'not_before_policy': mbd['not_before_policy'],
        'session_state': mbd['session_state'],
        'scope': mbd['scope'],
        'csrf': mbd['csrf'],
    }},
    upsert=True
)

today = dt.datetime.today().strftime('%d.%m.%Y')
for name, id in USERS.items():
    users_gid.insert_one({'username': name, 'id': id, 'likes': 0, 'latest_like': '27.02.2024'})
