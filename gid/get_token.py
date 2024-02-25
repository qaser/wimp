import pycurl
from io import BytesIO
import certifi


KEYCLOAK_SESSION = 'gid/a2ad3873-ba7a-4af3-a154-3597ee733792/67fa496c-811b-48c7-91b2-e88350469c1d'
KEYCLOAK_SESSION_LEGACY = 'gid/a2ad3873-ba7a-4af3-a154-3597ee733792/67fa496c-811b-48c7-91b2-e88350469c1d'
AUTH_SESSION_ID_LEGACY = 'd612ee51-7155-4aec-ad8a-0ae0d9783cb9.auth-quarkus-3-13815'
AUTH_SESSION_ID = 'd612ee51-7155-4aec-ad8a-0ae0d9783cb9.auth-quarkus-3-13815'
KEYCLOAK_IDENTITY = 'eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlY2E4MjE5Ni0yZWEyLTRhZTItYjg0OS0yMjA1NDZjYzJlMWIifQ.eyJleHAiOjE3MTE0NjMwMTcsImlhdCI6MTcwODg3MTAxNywianRpIjoiMmUxNDNiMDYtOWMyYy00NDNkLTlhMjAtNzM0YWNkMjM0NjIwIiwiaXNzIjoiaHR0cHM6Ly9hcHAuZ2lkLnJ1L2F1dGgvcmVhbG1zL2dpZCIsInN1YiI6ImEyYWQzODczLWJhN2EtNGFmMy1hMTU0LTM1OTdlZTczMzc5MiIsInR5cCI6IlNlcmlhbGl6ZWQtSUQiLCJzZXNzaW9uX3N0YXRlIjoiNjdmYTQ5NmMtODExYi00OGM3LTkxYjItZTg4MzUwNDY5YzFkIiwic2lkIjoiNjdmYTQ5NmMtODExYi00OGM3LTkxYjItZTg4MzUwNDY5YzFkIiwic3RhdGVfY2hlY2tlciI6ImlYU2lOdl96azJ4RHhHQ2xqc2hrSVJZMS1RS0ItMGM1RndEMGhTQ3lzanMifQ.LT7XfrrF8BM9Gzz9D8ooKTSBuCjZgTL6zTlKmAEZRTo'
KEYCLOAK_IDENTITY_LEGACY = 'eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlY2E4MjE5Ni0yZWEyLTRhZTItYjg0OS0yMjA1NDZjYzJlMWIifQ.eyJleHAiOjE3MTE0NjMwMTcsImlhdCI6MTcwODg3MTAxNywianRpIjoiMmUxNDNiMDYtOWMyYy00NDNkLTlhMjAtNzM0YWNkMjM0NjIwIiwiaXNzIjoiaHR0cHM6Ly9hcHAuZ2lkLnJ1L2F1dGgvcmVhbG1zL2dpZCIsInN1YiI6ImEyYWQzODczLWJhN2EtNGFmMy1hMTU0LTM1OTdlZTczMzc5MiIsInR5cCI6IlNlcmlhbGl6ZWQtSUQiLCJzZXNzaW9uX3N0YXRlIjoiNjdmYTQ5NmMtODExYi00OGM3LTkxYjItZTg4MzUwNDY5YzFkIiwic2lkIjoiNjdmYTQ5NmMtODExYi00OGM3LTkxYjItZTg4MzUwNDY5YzFkIiwic3RhdGVfY2hlY2tlciI6ImlYU2lOdl96azJ4RHhHQ2xqc2hrSVJZMS1RS0ItMGM1RndEMGhTQ3lzanMifQ.LT7XfrrF8BM9Gzz9D8ooKTSBuCjZgTL6zTlKmAEZRTo'

cookies = {
    'KEYCLOAK_SESSION': KEYCLOAK_SESSION,
    'KEYCLOAK_SESSION_LEGACY': KEYCLOAK_SESSION_LEGACY,
    'AUTH_SESSION_ID_LEGACY': AUTH_SESSION_ID_LEGACY,
    'AUTH_SESSION_ID': AUTH_SESSION_ID,
    'KEYCLOAK_IDENTITY': KEYCLOAK_IDENTITY,
    'KEYCLOAK_IDENTITY_LEGACY': KEYCLOAK_IDENTITY_LEGACY,
}
code = '050373a9-0948-4c3d-b5b3-1d026f8a71a8.67fa496c-811b-48c7-91b2-e88350469c1d.0b5ac12b-3392-421d-b858-3b4227ee41eb'
code = '0a92e2ba-d3c5-46ac-a59e-9e902b7ec948.9640ff8b-c7ab-4197-91ae-4da0c4eee37e.0b5ac12b-3392-421d-b858-3b4227ee41eb'
data = {
    'grant_type': 'authorization_code',
    'code': code,
    'client_id': 'webapp',
    'redirect_uri': 'https://web.gid.ru/'
}
data_text = ''
for key, value in data.items():
    data_text = f'{data_text}{key}={value}&'
data_text = data_text[:-1]

cookies_text = ''
for key, value in cookies.items():
    cookies_text = f'{cookies_text}{key}={value}; '
cookies_text = cookies_text[:-2]


def get_token():
    url = "https://app.gid.ru/auth/realms/gid/protocol/openid-connect/token"
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER,
        [
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0',
            'Accept: */*',
            'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Content-Type: application/x-www-form-urlencoded',
            'Referer: https://web.gid.ru/',
            'Origin: https://web.gid.ru',
            'DNT: 1',
            'Sec-Fetch-Dest: empty',
            'Sec-Fetch-Mode: cors',
            'Sec-Fetch-Site: same-site',
            'Connection: keep-alive',
            # f'Cookie: {cookies_text}',
            'TE: trailers',
        ]
    )
    c.setopt(c.POST, 1)
    # c.setopt(c.TIMEOUT_MS, 3000)
    c.setopt(c.POSTFIELDS, data_text)
    c.setopt(c.COOKIEFILE, cookies_text)
    c.perform()
    print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
    c.close()
    body = buffer.getvalue()
    print(body.decode('utf-8'))


get_token()
