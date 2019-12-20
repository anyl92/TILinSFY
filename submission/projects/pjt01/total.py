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

info_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd='

movie_info = {}
movie_info_list = []
movie_director_list = []

for movie_code in movie_codes:
    information = requests.get(info_URL + movie_code).json().get('movieInfoResult').get('movieInfo')
    
    movie_info['movieNm'] = information.get('movieNm')
    movie_info['movieNmEn'] = information.get('movieNmEn')
    movie_info['movieNmOg'] = information.get('movieNmOg')
    if information['audits'] :
        movie_info['watchGradeNm'] = information.get('audits')[0].get('watchGradeNm')
    movie_info['openDt'] = information.get('openDt')
    movie_info['showTm'] = information.get('showTm')
    movie_info['genreNm'] = information.get('genres')[0].get('genreNm')
    if information['directors'] :
        movie_info['peopleNm'] = information.get('directors')[0].get('peopleNm')
        movie_director_list.append(copy.copy(movie_info['peopleNm']))
    movie_info_list.append(copy.copy(movie_info))
    
with open('movie.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieNm', 'movieNmEn', 'movieNmOg', 'watchGradeNm', 'openDt', 'showTm', 'genreNm', 'peopleNm']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in movie_info_list:
        writer.writerow(i)

director_URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={API_KEY}&peopleNm='

director_info = {}
director_info_list = []

for movie_director in movie_director_list:
    director = requests.get(director_URL + movie_director).json().get('peopleListResult').get('peopleList')[0]
    
    director_info['peopleCd'] = director.get('peopleCd')
    director_info['peopleNm'] = director.get('peopleNm')
    director_info['repRoleNm'] = director.get('repRoleNm')
    director_info['filmoNames'] = director.get('filmoNames')

    director_info_list.append(copy.copy(director_info))

with open('director.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['peopleCd', 'peopleNm', 'repRoleNm', 'filmoNames']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in director_info_list:
        writer.writerow(i)