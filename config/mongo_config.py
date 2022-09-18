import gridfs
import pymongo

# Create the client
client = pymongo.MongoClient('localhost', 27017)
db = client['gks_bot_db']
fs = gridfs.GridFS(db)
quiz = db['quiz']
users = db['users']
vehicles = db['vehicles']
