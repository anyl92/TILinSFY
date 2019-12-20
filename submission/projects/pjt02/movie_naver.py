import requests
import csv, copy
from naver_API import send_naver_movie

# csv에서 (code,name)
movie_name_dict = {}
with open('./movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader, None)
    for line in reader:
        movie_name_dict[line[0]] = line[1]

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