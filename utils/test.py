import pymongo
import random

client = pymongo.MongoClient('localhost', 27017)
# Connect to our database
db = client['gks_bot_db']
quiz = db['quiz']

num = quiz.find()
print(quiz.count_documents({}))


count = quiz.count_documents({})
rand_num = random.randint(0, count)
poll = quiz.find({'num': rand_num}).next()
print(poll['correct_answer'])
