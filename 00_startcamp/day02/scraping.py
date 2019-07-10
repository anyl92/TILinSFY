import requests
import bs4

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text  # url에서 텍스트추출
text = bs4.BeautifulSoup(response, 'html.parser')  # 파이썬에서 보기편하기위함
kospi = text.select_one('#KOSPI_now')  # 필요한코드 하나만 추출
print(kospi.text)  # 텍스트만 추출
