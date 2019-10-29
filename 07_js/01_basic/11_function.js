/* python

def adder_1(x, y):
    return x+y
*/

function adder1(x, y) {  // 선언식
    return x + y;
}

/* python 에서는 안됨!
    adder2 = (x, y): return x + y
*/

const adder2 = function(x, y) {  // 할당식
    return x + y;
};

/* python lambda 표현식
    adder3 = lambda x, y: x + y
*/

// ES6+  Arrow function
// 1. function 을 지운다.
// 2. () 와 {} 사이에 => 를 넣는다.
const adder3 = (x, y) => {
    return x + y;
};