// ES5
var books = ['Learning JS', 'Eloquent JS'];
var comics = {
    dc: ['Joker', 'Batman'],
    marvel: ['Avengers', 'spiderman'],
};

var magazine = {}

var bookshop = {
    books: books,
    comics: comics,
    magazine: magazine,
}

// ES6+
const books = ['Learning JS', 'Eloquent JS'];
const comics = {
    dc: ['Joker', 'Batman'],
    marvel: ['Avengers', 'spiderman'],
};

const magazine = {}


const bookshop = {
    books, comics, magazine,
}  
// key - value 에 같은 단어를 쓸 때 축약할 수 있다
// js에서 키밸류가 완전히 같다면 이 문법을 허용