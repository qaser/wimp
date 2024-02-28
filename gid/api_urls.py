token_url = 'https://app.gid.ru/auth/realms/gid/protocol/openid-connect/token'
likes_url = 'https://web.gid.ru/api/feed/I7GXl8iFfvMS/reactions'
replies_url = "https://web.gid.ru/api/feed/I7GXl8iFfvMS/comments/{айди пользователя}/replies"
comments_url = "https://web.gid.ru/api/feed/MxzAUoQ8wRNb/comments"
me_url = "https://web.gid.ru/api/loyalty/public/v1/profile"
collect_url = 'https://web.gid.ru/api/event-tracker/public/v1/collect'  # для начисления баллов
feed_url = 'https://web.gid.ru/api/public/v3/feed'  # params = {'gidOnly': 'true', 'pinsOnly': 'false', 'recommendationsOnly': 'false', 'limit': '10',}
get_courses = 'https://web.gid.ru/api/lms/v2/courses'
get_lessons = 'https://web.gid.ru/api/lms/courses/{айди курса}'
put_lesson = 'https://web.gid.ru/api/lms/lessons/{айди урока}'


'''
{
	"0": {
		"id": "UNkQcC2szDtC",
		"title": "Республика Сербская начала платить в рублях за газ из России",
		"description": "Энтитет Боснии и Герцеговины намерен и дальше наращивать импорт российского газа.",
		"cover": "https://portal-static.gid.team/qvant-prod/s69f7yc4x5civvhfzymspmh75nj7?response-content-type=image/jpeg",
		"isCommentsEnabled": true,
		"source": {
			"title": "Пятый канал",
			"logo": null
		},
		"publishAt": "2024-02-26T12:28:46",
		"totalViews": 13,
		"totalComments": 5,
		"featuredImageUrl": null,
		"idFromOwner": null,
		"isHot": null,
		"rubrics": [
			{
				"id": "c9eeaf7b-e38d-46bf-a099-804267aa38b6",
				"key": "energy",
				"name": "Энергетика"
			},
			{
				"id": "de19c441-1d8f-4da1-8661-e34cf5b7f194",
				"key": "economy",
				"name": "Экономика"
			},
			{
				"id": "a7137e65-fc99-4687-a27e-f03b478c2bfd",
				"key": "gid",
				"name": "Газпром"
			}
		],
		"tagsKeys": [],
		"rating": {
			"countLikes": 12,
			"countDislikes": null,
			"myRating": null
		},
		"mark": {
			"avgMark": 100,
			"userMark": null
		}
	}
}
'''

import pycurl
from io import BytesIO
import certifi
import json
import pymongo
import ast
import time

client = pymongo.MongoClient('localhost', 27017)
gid_db = client['gid_db']
auth_gid = gid_db['auth']
cookies_gid = gid_db['cookies']
users_gid = gid_db['users']
courses_gid = gid_db['courses']

csrf = '312fef0e2dbb99f03253a42955ce69d5d21db14299a2e8c3c8bf1192aa739c30.1f4640d0643f3a39313d46d1dafa117783a2cf6351f295398e0bdad819f58313e7f55f5bc559480a59906768a23ff4b4f88c2da29adba32036ab5e67517d205f5e3eeccadadd5c1b3214a6bfcdad74a626e99949041bdd91ec71a04d7b1d6851320b0ade7761ef3f741a13d2444a41543056fb4563481096d6ca77d4830baa7798f623916131630dc74dc85f486f87463aca8ff095239b89fffbf57096b4db85fd0a75643f7e20b27ed9583f3bf7914ffc0bdaddd84d671a6b16e0dbc7ebee6c64e52df98a7d280f47371687745de9e0c014cb0e98a3646ed196e931df348ab397cb790f3c8da14a11a8652e720951ded8c9f892b4694e9976af7b9f78b66aeb'
token = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJBLWFMMDZBRmduOGxoNDBXakV0bXo0a2owNzdKX3lXWFhIUXJHT2lnSzZVIn0.eyJleHAiOjE3MDkxMTE5ODksImlhdCI6MTcwOTExMDE4OSwiYXV0aF90aW1lIjoxNzA4ODgxNzc0LCJqdGkiOiJlYjg4MmE1OS00M2FkLTRhYzUtOGQ3Ni0yNTI4MmNjYjUzMDUiLCJpc3MiOiJodHRwczovL2FwcC5naWQucnUvYXV0aC9yZWFsbXMvZ2lkIiwic3ViIjoiYTJhZDM4NzMtYmE3YS00YWYzLWExNTQtMzU5N2VlNzMzNzkyIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoid2ViYXBwIiwibm9uY2UiOiJmNzE3YzQ3Ni0zOGRjLTQ0N2UtYjBjNi1kMTUyMTM3YzU2NTciLCJzZXNzaW9uX3N0YXRlIjoiOTY0MGZmOGItYzdhYi00MTk3LTkxYWUtNGRhMGM0ZWVlMzdlIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImVtcGxveWVlIl19LCJzY29wZSI6Im9wZW5pZCIsInNpZCI6Ijk2NDBmZjhiLWM3YWItNDE5Ny05MWFlLTRkYTBjNGVlZTM3ZSJ9.HRHaMBPCenSWR6AY2BG3_mJuDlq0oVcugvPwK3uiySebryJGv4l8-ZEBru0JnOx8ZM0Qqqa16cIxaQPU4NC7SUNz3erN7vCK8AyOTtDkXDM1kPbtNHKq0LFvD0B42K4O60po4gtYywI4d3fG5AxxhW_crzxAxXXh0ILWwUZ6xMwe9ky6z-w3ZEwxsqFPGMzrzoKrUficn6eo6LlQBGgMJSOnbdqacuqlfGGWc-gFXFwbn6JEKhXl-ReRBs9keebpN9SelxqoyIOszzNkuTgeztKfmQE7hT-ArBQCKWbPjvRYrZEKzi6b0ne2wkcdXD088PwegEOONEeX8SPpDGNuGw'

URL_COURSES = "https://web.gid.ru/api/lms/v2/courses"
URL_LESSONS = "https://web.gid.ru/api/lms/courses/"
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
    'Referer: https://web.gid.ru/',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
    # 'baggage: sentry-environment=production,sentry-public_key=bb91aa88b03040fa9497506d5fa8e028,sentry-trace_id=1ecd4865d78e4d9a8c6f5dd8a04566ce',
    f'X-CSRF-TOKEN: {csrf}',
    f'Authorization: Bearer {token}',
    f'Cookie: X-CSRF-TOKEN={csrf}',
]


def get_response(url):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS)
    c.setopt(c.TIMEOUT_MS, 10000)
    c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
    c.perform()
    resp_code = c.getinfo(c.RESPONSE_CODE)
    body = buffer.getvalue()
    resp_data = json.loads(body.decode())
    c.close()
    return (resp_code, resp_data)


def get_courses():
    resp_code, resp_data = get_response(URL_COURSES)
    if resp_code == 201 or resp_code == 200:
        chapters = resp_data['items']  # list of dicts
        for chapter in chapters:
            courses = chapter['items']  # list of dicts
            chapter_name = chapter.get('name')
            if len(courses) != 0 and chapter_name is not None:
                for course in courses:
                    course_id = course.get('id')
                    course_name = course.get('name')
                    course_check = courses_gid.find_one({'course_id': course_id})
                    if course_check is None:
                        resp_code, resp_data = get_response(f'{URL_LESSONS}{course_id}')
                        time.sleep(11)
                        lessons = [lesson['id'] for lesson in resp_data['lessons']]
                        courses_gid.insert_one({
                            'course_id': course_id,
                            'course_name': course_name,
                            'chapter_name': chapter_name,
                            'lessons': lessons,
                            'is_complete': False,
                        })

get_courses()
