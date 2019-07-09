import webbrowser

urls = [
    'github',
    'google',
    'youtube',
    'edu.ssafy',
    'naver'
]

#리스트 
for url in urls:
    webbrowser.open('http://' + url + '.com')
