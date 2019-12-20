import csv

movie_name_list = []

with open('./movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        movie_name_list.append(line[0])

movie_name_list = movie_name_list[1:]
print(movie_name_list)