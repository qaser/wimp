import pymongo

client = pymongo.MongoClient('localhost', 27017)
# Connect to our database
db = client['gks_bot_db']
quiz = db['quiz']
quiz_count = quiz.count_documents({})
answer_num = quiz_count

file = 'quiz_raw.csv'
quiz_dict = {}
with open(file, 'r', encoding='UTF-8') as f:
    contents = f.readlines()
    for id, row in enumerate(contents):
        row_list = row.rstrip('\n').split(';')
        theme, question, correct_answer, num_answers, *answers = row_list
        for ind, ans in enumerate(answers):
            str_len = len(ans)
            if str_len > 100:
                print(id, question, ind, str_len)
