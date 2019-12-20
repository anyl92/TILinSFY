from naver_API import send_naver_movie  # , send_naver_movie_img
import requests

# print(send_naver_movie('알라딘')['items'][0])

# 이미지저장
# image_urls = []
# for movie_name in movie_names:
#     image_urls.append(send_naver_movie_img(movie_name))

url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9doKwlIPqicmGCkpMg2V-7NiyH2-8MvSCBjEzcOfTxvjrtOzt'

with open(f'./images/{movieCd}.jpg', 'wb') as f:
    image = requests.get(url, stream=True).content #사진이담김
    f.write(image) #저장될것

#읽는다,날린다,모은다, ->다시요청날리고,저장한다