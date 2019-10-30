// 1. 선언형
function a (x, y) {
    return x + y;
}

// 2. 할당형
const b = function (x, y) {
    return x + y;
};

// 3. arrow function (할당형)
const c = (x, y) => {
    return x + y;
};

// 3-1. 짧게 (함수 블록에 코드가 return 문 한줄이라면 {}+return 생략)
const d = (x, y) => x + y;

// 3-2. 함수의 인자가 단 하나일때 () 생략
const e = x => x ** 2;

// 3=3. 인자가 없으면?
const e = () => false;

const f = _ => { 
    return false
}

// 3
const square = x => x ** 2;

