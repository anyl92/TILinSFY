## PJT01 - 파이썬을 활용한 데이터 수집 I

### 1. 영화진흥위원회 오픈 API(주간/주말 박스오피스 데이터)

 *	최근 50주간 데이터 중에 주간 박스오피스 TOP10데이터를 수집합니다. 해당 데이터는 향후 영화평점서비스에서 기본으로 제공되는 영화 목록으로 사용됩니다.
   1. 주간(월-일) 데이터 조회
   2. 조회기간은 총 50주, 기준일은 2019년 7월 13일
   3. 다양성 영화 / 상업 영화 모두 포함
   4. 한국 / 외국 영화 포함
   5. 모든 상영지역 포함
*	수집된 데이터에서 '영화 대표코드', '영화명', '해당일 누적관객수'를 기록합니다.
*	'해당일 누적관객수' 중복시 최신 정보를 반영합니다.
*	해당 결과를 boxoffice.csv에 저장합니다.



	*	영진위 주간/주말 박스오피스 API
	*	크게 dic으로 구성되어 있으며 weeklyBoxOfficeList의 value는 list, list의 내부는 다시 dic

```
{
  "boxOfficeResult": {
    "boxofficeType": "주말 박스오피스",
    "showRange": "20190712~20190714",
    "yearWeekTime": "201928",
    "weeklyBoxOfficeList": [
      {
        "rnum": "1",
        "rank": "1",
        "rankInten": "0",
        "rankOldAndNew": "OLD",
        "movieCd": "20196309",
        "movieNm": "스파이더맨: 파 프롬 홈",
        "openDt": "2019-07-02",
        "salesAmt": "11554695230",
        "salesShare": "49.5",
        "salesInten": "-13567994520",
        "salesChange": "-54.0",
        "salesAcc": "57709375740",
        "audiCnt": "1302522",
        "audiInten": "-1555307",
        "audiChange": "-54.4",
        "audiAcc": "6685143",
        "scrnCnt": "1708",
        "showCnt": "25563"
      },
      {  ...
```

* 작성 코드 리뷰

```python
from datetime import datetime, timedelta  # 날짜와 시간 계산
import requests  # API 요청시
from decouple import config  # API 요청 key를 다른 
import copy  # list에 append시 같은 값이 계속 입력, copy사용
import csv  # 엑셀파일로 저장

API_KEY = config('API_KEY')  # 저장된 APIkey 가져옴
URL = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={API_KEY}&weekGb=0&targetDt='
```

```python
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
```

date_set 함수를 이용해 기준일에서 일주일 전으로 계속 for문을 돌린다.

URL 주소에 날짜를 더하여 API요청을 보낸다.

dic형태로 구성된 데이터에서 'boxOfficeResult' 의 value값, 'weeklyBoxOfficeList' 의 value값을 차례로 movie에 가져온다.

movie에 들어온 값은 list이며 list 내에 dic형태로 구성되어있다.

movieCd의 value값을 찾아서 movie_codes list에 채워넣는데, 중복된 값을 제거하기 위하여 movieCd에 없는 값만을 movie_codes list에 append한다.

그리고 result dic에 Nm, Cd, audi 키밸류값을 추가하여 result를 move_list에 append한다.

이 때 result는 value가 아닌 address값을 가리키고 있기 때문에 copy를 사용해준다.

```python
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ['movieCd', 'movieNm', 'audiAcc']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in movie_list:
        writer.writerow(i)
```

csv파일을 생성한다. write가능한 파일, 인코딩utf-8

행의 첫 줄은 제목으로 지정한다. 이 때 이름이 동일해야 한다.

movie_list의 행을 for문으로 반복하며 입력한다.



### 2. 영화진흥위원회 오픈 API(영화 상세정보)

* 위에서 수집한 영화 대표코드를 활용하여 상세 정보를 수집합니다.
* '영화 대표코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '관람등급', '개봉연도', '상영시간', '장르', '감독명' 을 찾아 csv파일로 저장합니다.



* 작성 코드 리뷰

```python
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
```

1번과 같은 방식으로 URL에 키값과 영화코드를 활용하여 api를 요청한다.

1번에서 movie_code만 모아둔 movie_codes list를 이용해 영화코드를 URL에 반복해서 넣는다.

영화코드별 정보에서 get을 이용하여 'movieInfoResult', 'movieInfo' dic 내의 자료를 가져온다.

필요한 정보를 get으로 추출하여 movie_info에 저장한다.

get은 key값이 있어야 value를 가져올 수 있음, list는 [0]으로 

이 때 가져온 값이 없는 경우(None)가 있음. error 발생을 방지하여 if로 값이 있을 때만 코드를 수행한다.



### 3. 영화진흥위원회 오픈 API(영화인 정보)

* 위에서 수집한 영화 감독정보를 활용하여 상세 정보를 수집합니다.
* '영화인 코드', '영화인명', '분야', '필모리스트' 를 찾아 csv파일로 저장합니다.



* 작성 코드 리뷰

```python
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
```

1, 2번과 같은 방식으로 URL에 키값과 영화인정보를 활용하여 api를 요청한다.

2번에서 movie_director만 모아둔 movie_director_list를 이용해 감독명을 URL에 반복해서 넣는다.

감독별 정보에서 get을 이용하여 'peopleListResult', 'peopleList' dic 내의 list 0번째 자료를 가져온다.



## RESULT

1. boxoffice.csv

![boxoffice.csv_cap](C:\Users\student\submission\projects\pjt01\boxoffice.csv_cap.PNG)



2. movie.csv

![movie.csv_cap](C:\Users\student\submission\projects\pjt01\movie.csv_cap.PNG)



3. director.csv

![director.csv_cap](C:\Users\student\submission\projects\pjt01\director.csv_cap.PNG)