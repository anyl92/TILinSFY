import requests
import bs4
import csv

url = 'https://www.melon.com/chart/index.htm'

headers = {'User-Agent': ':)'}

response = requests.get(url, headers=headers).text
text = bs4.BeautifulSoup(response, 'html.parser')
rows = top50 = text.select('.lst50')

# with open('melon50.csv', 'w', encoding='utf-8') as f:
    # f.write('순위, 제목, 가수\n')
    # for row in rows:
    #     rank = row.select_one('td:nth-child(2) > div > span.rank').text
    #     title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    #     artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    #     # print(rank, title, artist)
    #     f.write(f'{rank},{title},{artist}\n')

writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8', newline=''))
writer.writerow(['순위', '제목', '가수'])  # writerow에는 \n포함

for row in rows:
        rank = row.select_one('td:nth-child(2) > div > span.rank').text
        title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
        artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
        # print(rank, title, artist)
        writer.writerow([rank, title, artist])

# print(rows)
