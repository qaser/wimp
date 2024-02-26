import pprint
import datetime as dt

import pymongo


client = pymongo.MongoClient('localhost', 27017)
db = client['gks_bot_db']
gid_db = client['gid_db']

users = db['users']
tanks = db['tanks']
oil_actions = db['oil_actions']
oil_reports = db['oil_reports']
gpa_params = db['gpa_params']

auth_gid = gid_db['auth']
cookies_gid = gid_db['cookies']
users_gid = gid_db['users']
