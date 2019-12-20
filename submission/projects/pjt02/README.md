## 02 - 파이썬을 활용한 데이터 수집 II

### 1. 네이버 영화 검색 API

* 지난 프로젝트에서 얻은 영화명을 바탕으로 네이버 영화 검색 API를 통해 추가적인 데이터를 수집합니다. 해당 데이터는 향후 영화평점서비스에서 기준 평점 및 영화 포스터 썸네일로 활용될 것입니다.
* 영화별로 '영진위 영화 대표코드', '하이퍼텍스트 link', '영화 썸네일 이미지의 URL', '유저 평점'을 저장합니다.
* 해당 결과를 movie_naver.csv에 저장합니다.



```
Naver의 오픈 API에 URL을 요청한다.
postman을 사용하여 아래와 같은 구성을 확인할 수 있다.
```

```
{
    "lastBuildDate": "Fri, 26 Jul 2019 09:41:53 +0900",
    "total": 22,
    "start": 1,
    "display": 10,
    "items": [
        {
            "title": "<b>알라딘</b>",
            "link": "https://movie.naver.com/movie/bi/mi/basic.nhn?code=163788",
            "image": "https://ssl.pstatic.net/imgmovie/mdi/mit110/1637/163788_P18_105943.jpg",
            "subtitle": "Aladdin",
            "pubDate": "2019",
            "director": "가이 리치|",
            "actor": "나오미 스콧|윌 스미스|메나 마수드|",
            "userRating": "9.43"
        },
        {
            "title": "<b>알라딘</b> 2",
```



*  `naver_API.py `  작성 코드 리뷰

```python
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
```

decouple의 config를 이용하여 숨겨둔 API키값을 받아올 수 있게 한다.

Naver API의 경우 너무 빠르게 요청을 보낼 시 요청을 받지 않을 수도 있어 time.sleep을 사용하여 요청에 딜레이를 준다.

config 받아올 .env 파일에 저장된 id와 secret 키를 변수에 저장한다.

URL에 받아올 movie_name을 결합한다.

headers = {}를 주지 않으면 네이버에서 읽지 않고 응답을 주지 않는다.

response에 위의 URL과 headers로 요청을 보낸다. 그 값 중 dict의 'items'값의 0번째 list index만 get하여 result로 가져온 후 return 한다.



* `movie_naver.py`  작성 코드 리뷰

```python
import requests
import csv, copy
from naver_API import send_naver_movie

# csv에서 (code,name)
movie_name_dict = {}
with open('./movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None) # 첫즐 없이
    for line in reader:
        movie_name_dict[line[0]] = line[1]
```

naver_API.py에서 send_naver_movie라는 함수를 사용하기 위해 import한다.

movie.csv 파일을 열어서 for문으로 line을 돌며 영화코드와 영화이름을 movie_name_dict에 key, value로 넣는다.



```python
all_list = []
final_dict = {}
for code, name in movie_name_dict.items():
    if send_naver_movie(name).get('image'):
        final_dict['code'] = code
        final_dict['link'] = send_naver_movie(name).get('link')
        final_dict['image'] = send_naver_movie(name).get('image')
        final_dict['userRating'] = send_naver_movie(name).get('userRating')
        all_list.append(copy.copy(final_dict))
        print(all_list)
    else: 
        pass

with open('movie_naver.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['code', 'link', 'image', 'userRating']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in all_list:
        writer.writerow(i)
```

movie_name_dict에 저장된 코드와 네임을 for문으로 돌린다.

영화 썸네일 이미지의 URL이 없는 경우 저장하지 않기 위해 가져온 값이 True일 경우에만 if문으로 들어가 다음 코드를 수행한다. False일 경우 pass한다.

key값과 value를 돌리면서 code, link, image, userRating 키 값에 각각 value를 추가한다.

추가된 final_dict를 all_list에 append한다. 저번 프로젝트와 마찬가지로 list에 append가 되지 않는다. copy를 이용하여 복사한다.

all_list값을 movie_naver.csv로 저장한다.



### 2. 영화 포스터 이미지 저장

* 앞서 네이버 영화 검색 API를 통해 얻은 이미지 URL에 요청을 보내 실제 이미지 파일로 저장합니다. 해당 데이터는 향후 영화 목록에서 포스터 이미지로 사용될 것입니다.
* 응답 받은 결과는 wb옵션으로 'images 폴더' 내에 '영진위 영화 대표코드.jpg'로 저장한다.



*  작성 코드 리뷰

```python
import requests
import csv

# csv에서 (image)
movie_image_dict = {}
with open('./movie_naver.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for line in reader:
        movie_image_dict[line[0]] = line[2]

for code, image in movie_image_dict.items():
    movie_image = requests.get(image, stream=True).content
    with open(f'./images/{code}.jpg', 'wb') as f:
        f.write(movie_image)
```

movie_naver.csv 파일을 열어 code와 image의 index를 dic에 추가한다.

movie_image_dict에서 image의 link를 requests의 get에 입력하여 movie_image에 추가한다.

추가한 이미지링크를 images폴더에 code이름.jpg, wb옵션으로 저장한다.



## RESUlT

1. `movie_naver.csv`

![movie_naver.csv_cap](C:\Users\student\submission\projects\pjt02\movie_naver.csv_cap.PNG)



2. `image`

![images_cap](C:\Users\student\submission\projects\pjt02\images_cap.PNG)

