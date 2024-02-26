token_url = 'https://app.gid.ru/auth/realms/gid/protocol/openid-connect/token'
likes_url = 'https://web.gid.ru/api/feed/I7GXl8iFfvMS/reactions'
replies_url = "https://web.gid.ru/api/feed/I7GXl8iFfvMS/comments/{айди пользователя}/replies"
comments_url = "https://web.gid.ru/api/feed/MxzAUoQ8wRNb/comments"
me_url = "https://web.gid.ru/api/loyalty/public/v1/profile"
collect_url = 'https://web.gid.ru/api/event-tracker/public/v1/collect'  # для начисления баллов
feed_url = 'https://web.gid.ru/api/public/v3/feed'  # params = {'gidOnly': 'true', 'pinsOnly': 'false', 'recommendationsOnly': 'false', 'limit': '10',}


'''
{
	"0": {
		"id": "UNkQcC2szDtC",
		"title": "Республика Сербская начала платить в рублях за газ из России",
		"description": "Энтитет Боснии и Герцеговины намерен и дальше наращивать импорт российского газа.",
		"cover": "https://portal-static.gid.team/qvant-prod/s69f7yc4x5civvhfzymspmh75nj7?response-content-type=image/jpeg",
		"isCommentsEnabled": true,
		"source": {
			"title": "Пятый канал",
			"logo": null
		},
		"publishAt": "2024-02-26T12:28:46",
		"totalViews": 13,
		"totalComments": 5,
		"featuredImageUrl": null,
		"idFromOwner": null,
		"isHot": null,
		"rubrics": [
			{
				"id": "c9eeaf7b-e38d-46bf-a099-804267aa38b6",
				"key": "energy",
				"name": "Энергетика"
			},
			{
				"id": "de19c441-1d8f-4da1-8661-e34cf5b7f194",
				"key": "economy",
				"name": "Экономика"
			},
			{
				"id": "a7137e65-fc99-4687-a27e-f03b478c2bfd",
				"key": "gid",
				"name": "Газпром"
			}
		],
		"tagsKeys": [],
		"rating": {
			"countLikes": 12,
			"countDislikes": null,
			"myRating": null
		},
		"mark": {
			"avgMark": 100,
			"userMark": null
		}
	}
}
'''
