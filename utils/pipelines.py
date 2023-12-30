GPA_PIPELINE = [
    {'$match': {'type': 'ГПА'}},
    {'$group': {
        '_id': '$num',
        'tanks': {
            '$push': {
                'tank': '$tank',
                'vol': '$cur_volume',
                'cal': '$calibration',
                'date': '$last_update'
            }
        }
    }},
    {'$sort': { '_id': 1}}
]

BPM_PIPELINE = [
    {'$match': {'type': 'БПМ'}},
    {'$group': {
        '_id': '$num',
        'tanks': {
            '$push': {
                'tank': '$tank',
                'vol': '$cur_volume',
                'cal': '$calibration',
                'date': '$last_update'
            }
        }
    }},
    {'$sort': { '_id': 1}}
]

MH_PIPELINE = [
    {'$match': {'type': 'МХ'}},
    {'$group': {
        '_id': '$tank',
        'data': {
            '$push': {
                'vol': '$cur_volume',
                'cal': '$calibration',
                'date': '$last_update'
            }
        }
    }},
    {'$sort': { '_id': 1}}
]

GSM_PIPELINE = [
    {'$match': {'type': 'ГСМ'}},
    {'$group': {
        '_id': '$tank',
        'data': {
            '$push': {
                'vol': '$cur_volume',
                'cal': '$calibration',
                'date': '$last_update'
            }
        }
    }},
    {'$sort': { '_id': 1}}
]
