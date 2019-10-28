typeof(1)  // number
typeof(1/0)  // Infinity
typeof(Infinity)  // number
typeof(NaN)  // Not A Number : number 어쨌든 숫자 연산에 관련돼서
// number 연산이 이상할 경우 에러가 아니라 NaN 이라는 값을 return

Infinity - Infinity // NaN
'asdf' + 1 // 덧셈이 아니라 string concat: 'asdf1'
'asdf' - 1 // NaN
'asdf' * 1 // NaN


typeof(alert)  // function
// typeof 는 함수가 아님. 연산자임. (특수연산자) 다른 거(문자)랑 붙이면 안됨