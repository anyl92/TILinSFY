## 기본 문법

1. 변수

   var - es6 이전 , function 스코프, 재선언 가능

   let / const - block 스코프, 재선언 불가능 . const 는 상수라 재할당 불가능

   변수 키워드를 사용하지 않으면 전역 변수 취급

   

2. 자료형

   typeof()  : 함수가 아니고 특수연산자임. 다른(문자)거랑 붙이면 안됨

   * number

     1, 1/0, infinity, NaN 

     infinity - infinity / 'asdf' - 1 등 숫자 연산인데 값이 이상한 것을 Not A Number

   * boolean

     true, false

   * string

     'asdf', 'asdf'+2 = 'asdf2'

   * object

     [1, 2], {a:1, b:2}, null(내가 의도한 없음)

   * function

     function() {}

   * undefined

     내가 의도하지 않음, 아 몰라,, 없어,,,

   Array.isArray() 배열이 아니면 false



3. 조건/반복

   if () {}

   else if  () {}

   else {}

   condition ? yes : no ;

   while () {}

   for (let j=0; j < 5; j++) {}

   for (const number of [1, 2, 3, 4, 5]) {}

   0 == "0" / 0 == [] true / "0" == [] false

   === 로 하면 다 false

   

4. 배열 object

   배열의 index는 양의 정수만 가능

   numbers.length  === len

   

   원본 파괴 methods

   .reverse()

   .push('a')

   .pop()

   .unshift('a')  // 앞에다 push

   .shift()  // 앞에껄 pop

   

   원본 그대로 methods

   .includes('a')  // true of false return

   .indexOf(1)  // 1의 인덱스

   .indexOf(100)  // 없으면 -1 return

   .join() // '1, 2, 3, 4'  스트링으로

   .join('')  //  , 떼고 '1234'

   .join('-')  // - 로 join '1-2-3-4'

   

5. dic object

   {key : value}
   
   key string이 한 단어일때는 quote 생략 가능 - 그래서 nameDic 이런식
   
   꺼낼때는 `me.name.key` or `me[name][key]`
   
   key와 value에 완전히 같은 단어를 쓸 때 축약할 수 있다.
   
   books: books -> books, , 
   
   * method
   
     object의 value에 함수를 할당한다
   
     ```javascript
     const me = {
     	name: 'yu',
     	greeting: function(message) {
     		return `${this.name}: ${message}`
     	}
     }
     me.greeting('hi') // yu: hi
     me.name = 'lim'
     me.greeting('hello') // lim: hello
     ```
   
   * 함수도 선언 가능
   
     ```
     const you = {
     	name: 'Yu', 
     	greeting, 
     	bye() {
     		return 'bye'
     	}
     }
     ```
   
   * method 정의 시, arrow function 사용 불가



6. JSON

   key - value 형태의 자료구조를 JS Object와 유사한 모습으로 표현하는 표기법. 모습만 비슷할 뿐 실제로 Object 처럼 사용하려면 다른 언어들처럼 JS에서도 Parsing(구문분석) 작업이 필요하다.
   
   JSON으로 표현된 데이터의 타입은 무조건 string ( 모든 언어에서 )
   
   ```javascript
   // parsing : 구문 분석
   const parseData = JSON.parse(rawJson);
   // serializing : 공용어로 번역 (직렬화)
   const backToJSON = JSON.stringify(parseData);
   ```
   
   ​		

7. 함수

   ```javascript
   function adder1(x, y){  // 선언형
   	return x + y;
   }
   
   const adder2 = function(x, y){  // 할당형
       return x + y;
   }
   
   const adder3 = (x, y) => {  // 할당형
       return x + y;
   }
   
   const a = (x, y) => x + y;
   // arrow function에서 return문이 한줄이면 {}+return 생략
   
   const b = x => x ** 2;
   // 함수의 인자가 단 하나일 때 () 생략
   
   // 인자가 없을 때
   const c = () => false;
   
   const d = _ => {
       return false
   }
   ```
   
   

8. Array Helper Methods

   * forEach

     return이 없다. 원래 원소의 값들을 활용해서 합이나 평균을 구하고자 하거나 원래 배열과는 길이가 다른 배열 결과를 받고 싶다면 사용

   * map

     return이 있다. 원소의 값들을 각각 가공해서 수정된/새로운 배열을 return받고자 한다면 사용

   * filter

     조건자함수. 원래 배열을 변화시키지 않는다.

   * reduce

     ???



## DOM(document object model)



