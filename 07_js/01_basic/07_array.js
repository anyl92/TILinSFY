const numbers = [1, 2, 3, 4];

numbers[0];  // 1
numbers[-1]; // undefined: index 는 양의 정수
numbers.length;  // 4

// 원본 파괴 methods
numbers.reverse();
numbers.push('a');
numbers.pop();
numbers.unshift('a');
numbers.shift();

// 원본 그대로인 methods
numbers.includes('a')  // false
numbers.indexOf(1)  // 0

numbers.join()  // "1,2,3"
numbers.join('')  // 123
numbers.join('-')  // 1-2-3