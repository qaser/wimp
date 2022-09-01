import math
import pymongo
import random
import datetime as dt

client = pymongo.MongoClient('localhost', 27017)
# Connect to our database
db = client['gks_bot_db']
quiz = db['quiz']

num = quiz.find()
