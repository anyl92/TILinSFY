import datetime
from art import *
from flask import Flask, render_template, request
from iexfinance.stocks import Stock
import requests
import bs4
import csv
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/art')
def art():
    return render_template('art.html')


@app.route('/result')
def result():
    input_text = request.args.get('input_text')
    font = request.args.get('font')
    print(input_text, font)
    result = text2art(input_text, font=font)
    return render_template('result.html', result=result)


@app.route('/add')
def add():
    return render_template('add.html')


# @app.route('/result')
# def result():
#     one = request.args.get('one')
#     two = request.args.get('two')
#     add = int(one) + int(two)
#     return render_template('result.html', add=add)


@app.route('/send')
def send():
    return render_template('send.html')


# @app.route('/receive', methods=['POST'])
# def receive():
#     data = request.form.get('msg')
#     token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
#     stock = Stock(data, token=token).get_quote()

#     url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'  # 네이버금융

#     response = requests.get(url).text  # url에서 텍스트를 받아용
#     text = bs4.BeautifulSoup(response, 'html.parser')  # 파이썬이 읽게ㅎㅎ
#     rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
#     # 데이터(리스트)에서 하나를 골라 텍스트만 남겨욥
#     rate = float(rate.replace(',', ''))  # list를 float으로 만들건데 ,를 없애줘야행

#     company_name = stock['companyName']
#     latest_price = stock['iexRealtimePrice']
#     print(type(stock['iexRealtimePrice']))  # float 타입이어따!

#     mul = latest_price * rate
#     return render_template('receive.html', mul=mul)


@app.route('/receive')
def receive():
    data = request.args.get('comp_name')
    money_data = request.args.get('money')

    token = 'pk_63c229409ff14b67a6cc81e38927f1c4'
    stock = Stock(data, token=token).get_quote()
    latest_price = stock['iexRealtimePrice']
    url = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=z6oY8VPVLsFt5DwacY4xg5cyuxU2XDYg&searchdate=20190711&data=AP01'
    response = requests.get(url).text
    currencies = json.loads(response)

    print(money_data)
    
    # info = currencies[12]['deal_bas_r']

    for currency in currencies:
        if currency['cur_unit'] == money_data:
            mul = latest_price * float(currency['deal_bas_r'].replace(',', ''))
    # dal_kor = money[]
    print(mul)
    # mul = latest_price * int(info)
    return render_template('receive.html', mul=mul)

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    end_date = datetime.datetime(2019, 11, 29)
    left = end_date - today
    return render_template('dday.html', left_days=left.days)


@app.route('/boxoffice')
def boxoffice():
    top_5 = [
        '스파이더맨 파 프롬 홈',
        '알라딘',
        '토이스토리4',
        '존윅3',
        '라이온킹'
    ]
    return render_template('boxoffice.html', movies=top_5)

if __name__ == '__main__':
    app.run(debug=True)
