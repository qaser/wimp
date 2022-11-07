import pymongo

# Create the client
client = pymongo.MongoClient('localhost', 27017)
db = client['gks_bot_db']
quiz = db['quiz']
users = db['users']
offers = db['offers']
