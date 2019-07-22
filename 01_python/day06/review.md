## 04.data_structure

### 문자열 메소드

#### 변형

`.capitalize()`: 맨앞글자는 대문자, 나머지는 소문자

`.title()`: '나 공백 이후를 대문자로

`.upper()`: 모두 대문자로

`.lower()`: 모두 소문자로

`.swapcase()`: 대<->소문자 변환

`.strip([chars])`: 특정한 문자 양쪽을 제거하거나 입력안할 시 공백을 제거. lstrip왼,rstrip오



V `.join(iterable)`: 특정한 문자열로 만들어 반환

```python
exc = '!'
exc.join('배고파')
= '배!고!파'

'#'.join(['월요일', '졸리다', 'python', 'ssafy'])
= '월요일#졸리다#python#ssafy'
```



V`<class str>.replace(old, new[, count])`: 글자를 새로운 글자로 바꿔서 반환

```python
'yayaya!'.replace('a', '_')
= 'y_y_y_!'

'wooooowoooo'.replace('o', '', 3)
= 'woowoooo'
```



#### 탐색 및 검증

`.find(x)`: x의 첫 번째 위치를 반환, 없으면 -1을 반환. 많이 쓰이긴 하지만 있냐 없냐가 더 중요

`.index(x)`: x의 첫 번째 위치를 반환, 없으면 error. 



V`.split([chars=''])`: 문자열을 특정한 단위로 나누어 리스트로 반환. 기본적으로 띄어쓰기

```python
insta = '#월요일 #밥시간 #미세먼지 오늘은 어쩌고 저쩌고'
words = insta.split()

hashtags = []
for word in words:
    if word[0] == '#':
        hashtags.append(word[1:])
        
= ['a', 'b', 'c']
```



#### 확인 메소드

`dir('string')`: string으로 할 수 있는, int ... 등등 사용 가능

---

### 리스트 메소드 - 리스트는 원본을 변경한다.

#### 값 추가 및 삭제

V`.append(x)`: 리스트에 값을 추가

```python
result = caffe.append('ediya')
print(result)
= None
```

* 추가하는 다른 방법

```python
caffe = caffe + [droptop]
caffe[len(caffe):] = ['ediya']
```



`.extend(iterable)`: 리스트에 iterable 값을 붙일 수 있다. 여러 개를 붙일 수 있다. 그렇지만 '+'연산을 조금 더 많이 쓴다.







* 함수에 return이 없으면 None 반환

```python
def a():
    return 1
def b():
    useless = 1 + 1
    # return None

c = a()
d = b()
print(c, d)
= 1, None
```

