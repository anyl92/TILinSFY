import requests
import bs4
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866'

response = requests.get(url).text
text = bs4.BeautifulSoup(response, 'html.parser')
# print(type(response))  # response == "{"totSellamnt":81961886000, ... ,"drwtNo1":9}" -> str
# print(response)

data = json.loads(response)
# print(type(data), data)
print(data['bnusNo'])

real_numbers = []
for key, value in data.items():
    if 'drwtNo' in key:
        real_numbers.append(value)
    # real_numbers[i] = data[f'drwtNo{i+1}']  # format
print(real_numbers)
