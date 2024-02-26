import pprint
import datetime as dt

import pymongo


client = pymongo.MongoClient('localhost', 27017)
db = client['gks_bot_db']
gid_db = client['gid_db']

users = db['users']
tanks = db['tanks']
oil_actions = db['oil_actions']
oil_reports = db['oil_reports']
gpa_params = db['gpa_params']

auth_gid = gid_db['auth']
cookies_gid = gid_db['cookies']
users_gid = gid_db['users']


mbd = {
  "username": "huji",
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5MjQ1MjYsImlhdCI6MTcwODkyMjcyNiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiIyZjU2YzQ0ZS1kMDg4LTRiNmQtYTNjMi1jZjY2NDM2OGZiMTgiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI1NGRiMDU3OC0wM2Y0LTQ4MTgtYjFhMC1mNTgwODBhNWY5ODciLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.O75MpMfu34QmTvo8tsedFbadiO8X46FlatoGpvQbe_J0dO-xheOCIFhP0l0AvXnvjHg3CrEbcTNjOCbNbh9H6FWBNL6ikFwqLwv9-r6TdoPSMpt3baJ4o0XW4sktWggrBLD8g3Cyb9jX5nki3WZdA7UJn_lsvROjv4mbHeKS3nBSQoZYPcS5utyQePFh64AYM0dtFJ-odknzpTXIsCit6Rlup4ymYfMOge-kmRhCksExyDflSWqK50tBKkBAFT-saycJVRCjgo3frJlzwvPwgZnkQwFjKF7M1YabA-EoxNPi2zKiE4VGRWpNe_9xN9AFZSmX5TMyVi5Q0x9zE58SYA",
  "expires_in": 1800,
  "id_token": "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDg5MjQ1MjYsImlhdCI6MTcwODkyMjcyNiwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiIyMGRhOTEyMS03YzdhLTQ2YWItOWNhYy0wMTdhMjA0N2EyOGIiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwiYXVkIjoid2ViYXBwIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiSUQiLCJhenAiOiJ3ZWJhcHAiLCJub25jZSI6IjU0ZGIwNTc4LTAzZjQtNDgxOC1iMWEwLWY1ODA4MGE1Zjk4NyIsInNlc3Npb25fc3RhdGUiOiI5NjQwZmY4Yi1jN2FiLTQxOTctOTFhZS00ZGEwYzRlZWUzN2UiLCJhdF9oYXNoIjoiX2h3WEc1d0dFWDA2dkFyQ3QyUTM0ZyIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.AoPevw6UkIRrWaNtGgECVu6VMH7_7BUdP0iaH_GaLckeh5HvGawGSeHt-KjXcBo-R-2515DHnVogud-2yEhBX_5Rn72C4FKm-v2yKNdu5jM3-3AYwPmcK0qtgh6CUuxAtVfAh8Qg8dO_CxhnuJBc7l4QeP3ejyHPw-NVisxB8ScwryJwCjPu7DCh1nCy-wbZs6QhID9xcviLeU2jDhAPmiOoooJ2WjVa6OO7Ip0m-b388t2AfBaeNnKbvFmUhxy2CaZ4rdYx9j461X3h2E_3JdhsPg3uQoHBgSgfbvgLyfLQzk-3IC-VNTMJmUhzemBXoM7BlJzdFyPElWWKN1KLhw",
  "not_before_policy": 1706779079,
  "refresh_expires_in": 2551048,
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlY2E4MjE5Ni0yZWEyLTRhZTItYjg0OS0yMjA1NDZjYzJlMWIifQ.eyJleHAiOjE3MTE0NzM3NzQsImlhdCI6MTcwODkyMjcyNiwianRpIjoiY2RiYjA4OTEtODE3ZC00M2QyLWEwNzItNzQwZThmYmIxZTI1IiwiaXNzIjoiaHR0cHM6Ly9hcHAuZ2lkLnJ1L2F1dGgvcmVhbG1zL2dpZCIsImF1ZCI6Imh0dHBzOi8vYXBwLmdpZC5ydS9hdXRoL3JlYWxtcy9naWQiLCJzdWIiOiJhMmFkMzg3My1iYTdhLTRhZjMtYTE1NC0zNTk3ZWU3MzM3OTIiLCJ0eXAiOiJSZWZyZXNoIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiI1NGRiMDU3OC0wM2Y0LTQ4MTgtYjFhMC1mNTgwODBhNWY5ODciLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwic2NvcGUiOiJvcGVuaWQiLCJzaWQiOiI5NjQwZmY4Yi1jN2FiLTQxOTctOTFhZS00ZGEwYzRlZWUzN2UifQ.3gsND_2oh57gD5I4GJsTjAYYjQqwoagNURTiLceJ6Bc",
  "scope": "openid",
  "session_state": "9640ff8b-c7ab-4197-91ae-4da0c4eee37e",
  "token_type": "Bearer",
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
    }},
    upsert=True
)
