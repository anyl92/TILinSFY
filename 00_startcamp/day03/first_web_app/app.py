from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')  # / 붙으면 아래 일을 해라
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def pick_lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return str(lucky)


# @app.route('/get_lotto/<int:num>')
# def get_lotto():


@app.route('/hello/<name>')
def hello(name):
    return f'hi, {name}'


@app.route('/pick_lunch/<int:count>')
def pick_lunch(count):
    menus = [
        '짜장면',
        '짬뽕',
        '탕수육',
        '볶음밥',
        '사천탕면',
        '쟁반짜장'
    ]
    picks = random.sample(menus, count)
    return str(picks)


@app.route('/cube/<int:n>')
def cube(n):
    number = n ** 3
    return str(number)

if __name__ == '__main__':
    app.run(debug=True)
