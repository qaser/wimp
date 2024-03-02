import json
import time
from io import BytesIO

import certifi
import pycurl
from aiogram import Router
from aiogram.filters import Command

from config.bot_config import bot
from config.mongo_config import courses_gid, auth_gid
from config.telegram_config import ADMIN_TELEGRAM_ID
from handlers.get_response import get_response


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


async def get_courses():
    users = list(auth_gid.find({}))
    for user in users:
        new_courses = 0
        user_id = user['gid_id']
        username = user['username']
        resp_code, resp_data = get_response(
            URL_COURSES,
            add_headers=ADD_HEADERS,
            user_id=user_id
        )
        if resp_code == 201:
            chapters = resp_data['items']  # list of dicts
            for chapter in chapters:
                courses = chapter['items']  # list of dicts
                chapter_name = chapter.get('name')
                if len(courses) != 0 and chapter_name is not None:
                    for course in courses:
                        n_courses = 0
                        course_id = course.get('id')
                        course_name = course.get('name')
                        course_check = courses_gid.find_one(
                            {'course_id': course_id, 'user_id': user_id}
                        )
                        if course_check is None:
                            resp_code, resp_data = get_response(
                                f'{URL_LESSONS}{course_id}',
                                add_headers=ADD_HEADERS,
                                user_id=user_id
                            )
                            n_courses += 1
                            lessons = [lesson['id'] for lesson in resp_data['lessons']]
                            courses_gid.insert_one({
                                'course_id': course_id,
                                'course_name': course_name,
                                'chapter_name': chapter_name,
                                'lessons': lessons,
                                'is_complete': False,
                                'user_id': user_id
                            })
        new_courses = list(courses_gid.find({'is_complete': False, 'user_id': user_id}))
        count_new_courses = len(new_courses)
        if count_new_courses > 0:
            await bot.send_message(
                ADMIN_TELEGRAM_ID,
                f'Появились новые курсы для {username}: {count_new_courses}'
            )
            for course in new_courses:
                await check_course_status(course['course_id'], user_id, username)
        await bot.send_message(ADMIN_TELEGRAM_ID, f'Новых курсов для {username} пока нет')


async def check_course_status(course_id, user_id, username):
    resp_code, resp_data = get_response(
        f'{URL_LESSONS}{course_id}',
        add_headers=ADD_HEADERS,
        user_id=user_id
    )
    if resp_code == 200:
        course_status = resp_data['status']
        if course_status == 'finished':
            courses_gid.update_one(
                {'course_id': course_id, 'user_id': user_id},
                {'$set': {'is_complete': True}}
            )
        elif course_status == 'available':
            resp_code = get_response(
                f'{URL_LESSONS}{course_id}/start',
                no_data=True,
                add_headers=ADD_HEADERS,
                user_id=user_id
            )
            if resp_code == 201:
                await complete_course(course_id, user_id)
        elif course_status == 'started':
            await complete_course(course_id, user_id, username)


async def complete_course(course_id, user_id, username):
    course = courses_gid.find_one({'course_id': course_id, 'user_id': user_id})
    course_name = course['course_name']
    lessons = course.get('lessons')
    data_start = json.dumps({'action': 'start'})
    data_finish = json.dumps({'action': 'finish'})
    len_lessons = len(lessons)
    count = 0
    if len_lessons > 0:
        for lesson_id in lessons:
            resp_code, resp_data = get_response(
                f'{URL_LESSON}{lesson_id}',
                add_headers=ADD_HEADERS,
                user_id=user_id
            )
            if resp_code == 200:
                if resp_data['userStatus'] == 'finished':
                    count += 1 if resp_code == 200 else count
                if resp_data['userStatus'] == 'started':
                    resp_code = get_response(
                        f'{URL_LESSON}{lesson_id}',
                        'PUT',
                        data_finish,
                        True,
                        ADD_HEADERS,
                        user_id
                    )
                    count += 1 if resp_code == 200 else count
                elif resp_data['userStatus'] == 'available':
                    resp_code = get_response(
                        f'{URL_LESSON}{lesson_id}',
                        'PUT',
                        data_start,
                        True,
                        ADD_HEADERS,
                        user_id
                    )
                    resp_code = get_response(
                        f'{URL_LESSON}{lesson_id}',
                        'PUT',
                        data_finish,
                        True,
                        ADD_HEADERS,
                        user_id
                    )
                    count += 1 if resp_code == 200 else count
            if len_lessons == count:
                courses_gid.update_one(
                    {'course_id': course_id, 'user_id':user_id},
                    {'$set': {'is_complete': True}}
                )
                await bot.send_message(
                    ADMIN_TELEGRAM_ID,
                    f'Курс "{course_name}" пройден. Пользователь {username}'
                )
