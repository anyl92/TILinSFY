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



V`<class str> .replace(old, new[, count])`: 글자를 새로운 글자로 바꿔서 반환

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

V`.append(x)`: 리스트에 값을 추가 / 원본을 변경

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



`.extend(iterable)`: 리스트에 iterable 값을 붙일 수 있다. 여러 개를 붙일 수 있다. 그렇지만 '+' 연산을 조금 더 많이 쓴다.

```python
caffe.extend(['droptop', 'starbucks'])
```

```python
# list concatenate
caffe += ['tomntoms', 'hollys']
```

* `append`는 [['a', 'b']] `extend`는 ['a', 'b'] 로 출력

```python
caffe.append(['coffeenie'])
print(caffe)
= ['starbucks', 'tomntoms', 'hollys', ['coffeenie']]

# extend 안에있는걸 분리해서 하나하나 추가하니까 string 추가 시 유의
caffe.extend('coffeegurunaru')
print(caffe)  
= ['starbucks', 'tomntoms', 'hollys', ['coffeenie'], 'c', 'o', 'f', 'f', 'e', 'e', 'g', 'u', 'r', 'u', 'n', 'a', 'r', 'u']
```



`.insert(i, x)`: 정해진 위치 i에 값을 추가 / return None

```python
lunches.insert(0, '')  맨앞
lunches.insert(len(lunches), '')  맨뒤
lunches.insert(len(lunches) + 100, '')  길이를 넘어서도 마지막에 하나만
```



V`.remove(x)`: 리스트에서 값이 x인 것을 삭제

```python
numbers.remove(1)  # 1을 삭제
# 값이 없으면 오류가 발생
```



`.pop(i)`: 정해진 위치 i에 있는 값(지정x시 마지막)을 삭제, 그 항목을 반환 / return 있음

```python
# 값이 return이 된다는 것은 별도의 변수에 저장할 수 있다는 것입니다. 
pop_value = numbers.pop()
print(f'{pop_value}가 삭제되어 {numbers}가 남았습니다.')

=[2, 3, 4, 5, 6]
6가 삭제되어 [2, 3, 4, 5]가 남았습니다.
```



#### 탐색 및 정렬

`.index(x)`: 원하는 값을 찾아 index값을 반환, index 없을 시 ValueError 발생

```python
numbers = [1, 2, 3, 4, 5]
numbers.index(3)
= 2
```



V`.count(x)`: 원하는 값의 갯수를 확인

```python
# 따라서 원하는 값을 모두 삭제하려면 다음과 같이 할 수 있습니다.
numbers.remove(1)

target = 1
for _ in range(numbers.count(target)):  
    numbers.remove(target)
```



V`.sort()`: 정렬, 원본 list 변형시킨다. / return None

`.sorted()`: 정렬, 원본 list 변하지 않는다. / return 있음



`.reverse()`: 반대로 뒤집는다. 정렬은 안해줌



V`.copy`: 복사

리스트를 복사했을 때 원본과 복사본 모두 멍청하게 자리만 가리키고 있다.
pointing 하고 있는 애들, call by reference, mutable
tuple은 재할당이 가능하지만 바꾸는 게 불가능, 복사할 필요가 없어서 영향 X

```python
# shallow copy 얕은 복사
a = [1, 2, 3]
b = a[:]  # 슬라이싱 - 리턴

b = list(a)

b = copy.copy(a)
```

```python
# 중첩된 상황에서 복사를 하고 싶다면, deep copy 깊은 복사
# 내부에 있는 모든 객체까지 새롭게 값이 변경
import copy
l1 = [
    [1, 2, 3],
    [4, 5, 6]
]
l2 = copy.deepcopy(l1)
```



`.clear()`: 리스트의 모든 항목 삭제 / 원본 변경



### List Comprehension

* [(나와야 할 값) for 첫번째 조건 if 두번째 조건]

```python
cubic_list = []
for number in numbers:
    cubic_list.append(number ** 3)
```

```python
cubic_list = [number ** 3 for number in numbers]
```



```python
even_list = [number for number in numbers if number % 2 == 0]
```



---

### 딕셔너리 메소드 활용

#### 추가 및 삭제

`.pop(key[, default])`: 키가 딕셔너리에 있으면 제거하고 그 값을 돌려준다. 그렇지 않으면 default 반환한다. default 없는데 키 없으면 에러 발생. KeyError

```python
my_dict = {'apple': '사과', 'banana': '바나나'}
pop = my_dict.pop('apple')
print(pop, my_dict)

=사과 {'banana': '바나나'}
```

```python
# 두번째 인자로 default를 설정할 수 있습니다
my_dict.pop('melon', '') # 없으면 뒷인자를 리턴해
```



`.update()`: 값을 제공하는 키, 밸류로 덮어쓴다

```python
my_dict.update(apple='삭와')
my_dict['qwer'] = 'qwer'
```



V`.get(key[, default]): 키를 통해 밸류를 가져온다. KeyError발생하지 않음, None리턴

```python
print(my_dict.get('asdf', '그런거 없다'))
```



### dictionary comprehension

```python
cubic = {x: x**3 for x in range(1, 11)}
={1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216,....
```



---

### 세트 메소드 활용

#### 추가 및 삭제

`.add(elem)`: elem을 세트에 추가한다. 중복되지 않는다.

`.update(*others)`: 여러가지 값을 추가한다. iterable한 값만 가능

```python
fruits = {"사과", "바나나", "수박"}
fruits.update({'토마토', '떡'},{'두리안', '딸기'},{'토마토', '딸기'})
= {'두리안', '딸기', '떡', '바나나', '사과', '수박', '토마토'}
```



`.remove(elem)`: elem을 세트에서 삭제한다. 없으면 KeyError 발생, default X

`.discard(elem)`: elem을 세트에서 삭제한다. 에러가 발생하지 않음. return None

`.pop`: 임의의 원소를 제거해 반환한다.



---

### map(), zip(), filter()

#### `map(function, iterable)`

* iterable의 모든 원소에 function을 적용한 후 결과를 반환
* return은 map_object형태이지만 list로 사용할 수 있다

```python
# 문자열 '123'으로
numbers = [1, 2, 3]
chars = []
for number in numbers:
    chars.append(str(number))
print(chars)
''.join(chars)
```

```python
# list comprehension
chars = [str(number) for number in numbers]
print(chars)
''.join(chars)
```



```python
tags = ['오늘', '회식', '월요일']
def make_hashtag(word):
    return '#' + word

hashtags = list(map(make_hashtag, tags))
print(tags, hashtags)
= ['오늘', '회식', '월요일'] ['#오늘', '#회식', '#월요일']
```



```python
def cube(n):
    return n ** 3
cubes = list(map(cube, range(1, 11)))

= [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
```



#### `zip(*iterables)`

* 복수 iterable한 것들을 모아준다
* 결과는 튜플의 모음으로 구성된 zip object를 반환한다
* 길이가 같을 때 사용, 짧은 것을 기준으로 구성

```python
girls = ['jane', 'iu', 'mary']
boys = ['justin', 'david', 'kim']
list(zip(girls, boys))
= [('jane', 'justin'), ('iu', 'david'), ('mary', 'kim')]
```

```python
my_dict = {}
for girl, boy in zip(girls, boys):
    my_dics[girl] = boy
my_dict
= {'jane': 'justin', 'iu': 'david', 'mary': 'kim'}
```

```python
my_dict = {girl: boy for girl, boy in zip(girls, boys)}
```



```python
a = '가나다'
b = '다나가'

for char_a, char_b in zip(a, b):
    print(char_a + char_b)
```



#### `filter(function, iterable)`

* iterable에서 function의 반환된 결과가 참인 것들만 구성하여 반환

```python
def is_even(num):
    return num % 2 == 0

numbers = range(1, 10)
list(filter(is_even, numbers))
```

```python
[n for n in numbers if n % 2 == 0]
[n for n in numbers if is_even(n)]
```

```python
phone_numbers = [
    '01012341234', 
    '0212345678',
    '010123456789',
    '01015978423',
    '+82)10998894',
]

def is_valid_phone(phone_number):
    if phone_number [:3] == '010' and len(phone_number) == 11:
        #if phone_number[3:]:
        #if len(phone_number) == 11
        
    # return None 통과못하면 어차피 얘가 나와서 아래가 필요없다
#         else: 
#             return False
#     else:
#         return False

is_valid_phone('01015151515')
list(filter(is_valid_phone, phone_numbers))

= ['01012341234', '01015978423']
```





---

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
