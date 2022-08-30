import math
import pymongo
import random
import datetime as dt

client = pymongo.MongoClient('localhost', 27017)
# Connect to our database
db = client['gks_bot_db']
quiz = db['quiz']

num = quiz.find()

recommend_temp = {
    '1': {
        '1': '10.0',
        '2': '10.0',
        '3': '10.0',
        '4': '10.0',
        '5': '10.0',
        '6': '10.0',
        '7': '10.0',
        '8': '10.0',
        '9': '10.0',
        '10': '10.0',
    },
    '2': {
        '1': '10.0',
        '2': '10.0',
        '3': '10.0',
        '4': '10.0',
        '5': '10.0',
        '6': '10.0',
        '7': '10.0',
        '8': '10.0',
        '9': '10.0',
        '10': '10.0',
    },
    '3': {
        '1': '10.0',
        '2': '10.0',
        '3': '10.0',
        '4': '10.0',
        '5': '10.0',
        '6': '10.0',
        '7': '10.1',
        '8': '10.2',
        '9': '10.3',
        '10': '10.4',
    },
    '4': {
        '1': '10.6',
        '2': '10.7',
        '3': '10.8',
        '4': '10.9',
        '5': '11.0',
        '6': '11.0',
        '7': '11.3',
        '8': '11.7',
        '9': '12.0',
        '10': '12.3',
    },
    '5': {
        '1': '12.7',
        '2': '13.0',
        '3': '13.3',
        '4': '13.7',
        '5': '14.0',
        '6': '14.0',
        '7': '14.8',
        '8': '15.6',
        '9': '16.3',
        '10': '17.1',
    },
    '6': {
        '1': '17.9',
        '2': '18.7',
        '3': '19.4',
        '4': '20.2',
        '5': '21.0',
        '6': '21.0',
        '7': '21.3',
        '8': '21.7',
        '9': '22.0',
        '10': '22.3',
    },
    '7': {
        '1': '22.7',
        '2': '23.0',
        '3': '23.3',
        '4': '23.7',
        '5': '24.0',
        '6': '24.0',
        '7': '23.9',
        '8': '23.8',
        '9': '23.7',
        '10': '23.6',
    },
    '8': {
        '1': '23.4',
        '2': '23.3',
        '3': '23.2',
        '4': '23.1',
        '5': '23.0',
        '6': '23.0',
        '7': '22.4',
        '8': '21.9',
        '9': '21.3',
        '10': '20.8',
    },
    '9': {
        '1': '20.2',
        '2': '19.7',
        '3': '19.1',
        '4': '18.6',
        '5': '18.0',
        '6': '18.0',
        '7': '17.7',
        '8': '17.3',
        '9': '17.0',
        '10': '16.7',
    },
    '10': {
        '1': '16.3',
        '2': '16.0',
        '3': '15.7',
        '4': '15.3',
        '5': '15.0',
        '6': '15.0',
        '7': '14.7',
        '8': '14.3',
        '9': '14.0',
        '10': '13.7',
    },
    '11': {
        '1': '13.3',
        '2': '13.0',
        '3': '12.7',
        '4': '12.3',
        '5': '12.0',
        '6': '12.0',
        '7': '11.8',
        '8': '11.6',
        '9': '11.3',
        '10': '11.1',
    },
    '12': {
        '1': '10.9',
        '2': '10.7',
        '3': '10.4',
        '4': '10.2',
        '5': '10.0',
        '6': '10.0',
        '7': '10.0',
        '8': '10.0',
        '9': '10.0',
        '10': '10.0',
    },
}

month = str(dt.datetime.today().month)
day = dt.datetime.today().day
if day == 31:
    day_trinity = '10'
else:
    day_trinity = str(math.ceil(day/3))
avo_temp = recommend_temp[month][day_trinity]
print(avo_temp)