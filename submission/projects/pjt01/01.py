from datetime import datetime, timedelta
import requests
from decouple import config
import copy
import csv

API_KEY = config('API_KEY')
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&weekGb=0&targetDt='

result = {}
movie_codes = []
movie_list = []

for i in range(50):
    date_set = datetime(2019, 7, 12) - timedelta(weeks=i)
    date = requests.get(URL + str(date_set.strftime("%Y%m%d"))).json()

    for movie in date.get('boxOfficeResult').get('weeklyBoxOfficeList'):
        if not movie.get('movieCd') in movie_codes:
            movie_codes.append(movie.get('movieCd'))
            result['movieNm'] = movie.get('movieNm')
            result['movieCd'] = movie.get('movieCd')
            result['audiAcc'] = movie.get('audiAcc')
            movie_list.append(copy.copy(result))

with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'audiAcc']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in movie_list:
        writer.writerow(i)
