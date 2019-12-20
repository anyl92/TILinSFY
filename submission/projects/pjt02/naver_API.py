from decouple import config
import requests
import time

def send_naver_movie(movie_name):
    for i in range(100):
        time.sleep(0.5)

        naver_client_id = config('NAVER_CLIENT_ID')
        naver_client_secret = config('NAVER_CLIENT_SECRET')

        BASE_URL = 'https://openapi.naver.com/v1/search/movie.json'
        URL = BASE_URL + '?query=' + movie_name

        headers = {
            'X-Naver-Client-Id': naver_client_id,
            'X-Naver-Client-Secret': naver_client_secret,
        }

        response = requests.get(URL, headers=headers).json()
        result = response.get('items')[0]
        return result