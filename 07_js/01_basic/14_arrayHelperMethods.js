// 14_ARRAYhELPERmETHOD.JS
// ess
var colors = ['red', 'blue', 'green'];

for (var i=0; i<colors.length; i++) {
    console.log(colors[1]);
}

// ES6+
// function logger(x) {
//     console.log(x);
// }

colors.forEach(function (x) {  // return 값 없어
    console.log(x)
});


// ESS
const numbers = [1, 2, 3];
const doubledNumbers = [];

for (let i=0; i < numbers.length; i++) {
    doubledNumbers.push(numbers[i]*2);
}
console.log(doubledNumbers);


// ES6+
const tripleNumbers = numbers.map(function(number) {
    return number * 3;
})
console.log(tripleNumbers);


// ESS
const products = [
    {name: 'apple', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'tomato', type: 'fruit'},
    {name: 'cucumber', type: 'vegetable'},
];

const fruits = []

for (const product of products) {
    if (product.type === 'fruit') {
        fruits.push(product);
    }
}
console.log(fruits);

// ES6+
const vegetables = products.filter((product) => {
    return product.type === 'vegetable';
})
console.log(vegetables);