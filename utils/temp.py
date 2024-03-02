import pymongo
import datetime as dt

# Create an instance of the MongoDB client
client = pymongo.MongoClient('localhost', 27017)
gid_db = client['gid_db']


# коллекциии для ГИДа
auth_gid = gid_db['auth_gid']
users_gid = gid_db['users']
courses_gid = gid_db['courses']
quiz_gid = gid_db['quiz']
buffer_gid = gid_db['buffer']


auth_gid.update_one(
    {'username': 'huji'},
    {'$set': {'gid_id': 'a2ad3873-ba7a-4af3-a154-3597ee733792'}},
    upsert=True
)
