import json
import time
from io import BytesIO

import certifi
import pycurl
from aiogram import Router
from aiogram.filters import Command

from config.bot_config import bot
from config.mongo_config import auth_gid, courses_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from utils.constants import HEADERS

router = Router()

URL_COURSES = "https://web.gid.ru/api/lms/v2/courses"  # эндпоин для списка курсов
URL_LESSONS = "https://web.gid.ru/api/lms/courses/"  # эндпоинт для списка занятий на курсе
URL_LESSON = 'https://web.gid.ru/api/lms/lessons/'  # эндпоинт для прохождения занятия
ADD_HEADERS = [
    'Accept: application/json, text/plain, */*',
    'Content-Type: application/json; charset=utf-8',
    'Referer: https://web.gid.ru/',
    'X-Requested-With: XMLHttpRequest',
    'sentry-trace: 24745024fbbc4112903eb33b91fec441-ba8792fcbb7852c7',
]


def get_response(url, method='GET', fields_data='', no_data=False):
    time.sleep(2)
    token = auth_gid.find_one({'username': 'huji'}).get('access_token')
    csrf = auth_gid.find_one({'username': 'huji'}).get('csrf')
    auth_headers = [
        f'X-CSRF-TOKEN: {csrf}',
        f'Authorization: Bearer {token}',
        f'Cookie: X-CSRF-TOKEN={csrf}',
    ]
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(c.CAINFO, certifi.where())
    c.setopt(c.HTTPHEADER, HEADERS + ADD_HEADERS + auth_headers)
    c.setopt(c.TIMEOUT_MS, 10000)
    c.setopt(c.COOKIEFILE, f'X-CSRF-TOKEN={csrf}')
    if method == 'PUT':
        c.setopt(c.CUSTOMREQUEST, "PUT")
        c.setopt(c.POSTFIELDS, fields_data)
    c.perform()
    resp_code = c.getinfo(c.RESPONSE_CODE)
    body = buffer.getvalue()
    c.close()
    if no_data:
        return resp_code
    resp_data = json.loads(body.decode())
    return (resp_code, resp_data)



async def get_courses():
    resp_code, resp_data = get_response(URL_COURSES)
    if resp_code == 201:
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
                        new_courses += 1
                        lessons = [lesson['id'] for lesson in resp_data['lessons']]
                        courses_gid.insert_one({
                            'course_id': course_id,
                            'course_name': course_name,
                            'chapter_name': chapter_name,
                            'lessons': lessons,
                            'is_complete': False,
                        })
    new_courses = list(courses_gid.find({'is_complete': False}))
    count_new_courses = len(new_courses)
    if count_new_courses > 0:
        await bot.send_message(
            ADMIN_TELEGRAM_ID,
            f'Появились новые курсы: {count_new_courses}'
        )
        for course in new_courses:
            await check_course_status(course['course_id'])
    await bot.send_message(ADMIN_TELEGRAM_ID, 'Новых курсов пока нет')


async def check_course_status(course_id):
    resp_code, resp_data = get_response(f'{URL_LESSONS}{course_id}')
    if resp_code == 200:
        course_status = resp_data['status']
        if course_status == 'finished':
            courses_gid.update_one({'course_id': course_id}, {'$set': {'is_complete': True}})
        elif course_status == 'available':
            resp_code = get_response(f'{URL_LESSONS}{course_id}/start', no_data=True)
            if resp_code == 201:
                await complete_course(course_id)
        elif course_status == 'started':
            await complete_course(course_id)


async def complete_course(course_id):
    course = courses_gid.find_one({'course_id': course_id})
    course_name = course['course_name']
    lessons = course.get('lessons')
    data_start = json.dumps({'action': 'start'})
    data_finish = json.dumps({'action': 'finish'})
    len_lessons = len(lessons)
    count = 0
    if len_lessons > 0:
        for lesson_id in lessons:
            resp_code, resp_data = get_response(f'{URL_LESSON}{lesson_id}')
            if resp_code == 200:
                if resp_data['userStatus'] == 'finished':
                    count += 1 if resp_code == 200 else count
                if resp_data['userStatus'] == 'started':
                    resp_code = get_response(f'{URL_LESSON}{lesson_id}', 'PUT', data_finish, True)
                    count += 1 if resp_code == 200 else count
                elif resp_data['userStatus'] == 'available':
                    resp_code = get_response(f'{URL_LESSON}{lesson_id}', 'PUT', data_start, True)
                    resp_code = get_response(f'{URL_LESSON}{lesson_id}', 'PUT', data_finish, True)
                    count += 1 if resp_code == 200 else count
            if len_lessons == count:
                courses_gid.update_one(
                    {'course_id': course_id},
                    {'$set': {'is_complete': True}}
                )
                await bot.send_message(ADMIN_TELEGRAM_ID, f'Курс "{course_name}" пройден')
