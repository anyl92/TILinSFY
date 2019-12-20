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