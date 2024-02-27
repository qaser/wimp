import datetime as dt
import pymongo


client = pymongo.MongoClient('localhost', 27017)
# Connect to our database
db = client['gks_bot_db']
tanks = db['tanks']
oil_actions = db['oil_actions']
oil_reports = db['oil_reports']


REPORT = {
    'type': 'final',
    'date': dt.datetime(2023, 12, 31),
    'year': 2023,
    'month': 12,
    'volumes_before': {
        'ГПА_52_Д': (243, 618),
        'ГПА_52_Н': (1038, 1870),
        'ГПА_53_Д': (225, 618),
        'ГПА_53_Н': (1958, 768),
        'ГПА_54_Д': (259, 618),
        'ГПА_54_Н': (1029, 1870),
        'ГПА_55_Д': (234, 618),
        'ГПА_55_Н': (1901, 768),
        'ГПА_61_Д': (207, 618),
        'ГПА_61_Н': (1958, 768),
        'ГПА_62_Д': (189, 618),
        'ГПА_62_Н': (2002, 768),
        'ГПА_63_Д': (286, 618),
        'ГПА_63_Н': (1065, 1870),
        'ГПА_64_Д': (293, 618),
        'ГПА_64_Н': (1047, 1870),
        'ГПА_65_Д': (251, 618),
        'ГПА_65_Н': (1914, 768),
        'МХ_5_1': (0, 0),
        'МХ_5_2': (383, 0),
        'МХ_5_3': (1314, 0),
        'МХ_5_4': (1212, 0),
        'ГСМ_5_1': (0, 0),
        'ГСМ_5_2': (0, 0),
        'ГСМ_5_3': (15575, 0),
        'ГСМ_5_4': (243, 0),
        'ГСМ_5_5': (15324, 0),
        'ГСМ_5_6': (0, 0),
        'БПМ_2_1': (1442, 0),
        'БПМ_2_2': (1620, 0),
        'БПМ_3_1': (446, 0),
        'БПМ_3_2': (446, 0),
        'АЦ_5_1': (0, 0),
        'КОЛОДЕЦ_5_0': (0, 0),
    },
    'volumes_after': {
        'ГПА_52_Д': (283, 618),
        'ГПА_52_Н': (1038, 1870),
        'ГПА_53_Д': (337, 618),
        'ГПА_53_Н': (1998, 768),
        'ГПА_54_Д': (300, 618),
        'ГПА_54_Н': (981, 1870),
        'ГПА_55_Д': (223, 618),
        'ГПА_55_Н': (1901, 768),
        'ГПА_61_Д': (255, 618),
        'ГПА_61_Н': (1034, 1870),
        'ГПА_62_Д': (220, 618),
        'ГПА_62_Н': (1989, 768),
        'ГПА_63_Д': (250, 618),
        'ГПА_63_Н': (1998, 768),
        'ГПА_64_Д': (268, 618),
        'ГПА_64_Н': (1835, 768),
        'ГПА_65_Д': (220, 618),
        'ГПА_65_Н': (1232, 1870),
        'МХ_5_1': (906, 0),
        'МХ_5_2': (0, 0),
        'МХ_5_3': (1340, 0),
        'МХ_5_4': (1225, 0),
        'ГСМ_5_1': (0, 0),
        'ГСМ_5_2': (0, 0),
        'ГСМ_5_3': (15575, 0),
        'ГСМ_5_4': (243, 0),
        'ГСМ_5_5': (14980, 0),
        'ГСМ_5_6': (0, 0),
        'БПМ_2_1': (1442, 0),
        'БПМ_2_2': (1620, 0),
        'БПМ_3_1': (446, 0),
        'БПМ_3_2': (446, 0),
        'АЦ_5_1': (0, 0),
        'КОЛОДЕЦ_5_0': (0, 0),
    },
}

oil_reports.insert_one({
    'type': REPORT['type'],
    'date': REPORT['date'],
    'year': REPORT['year'],
    'month': REPORT['month'],
    'volumes_before': REPORT['volumes_before'],
    'volumes_after': REPORT['volumes_after'],
})