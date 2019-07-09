import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:  # f라고 부르겠다
    items = csv.reader(f)

    for item in items:
        print(item)
