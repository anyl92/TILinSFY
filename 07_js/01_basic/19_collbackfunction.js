function a(x, y) {
    return x + y;
}

function b(n) {
    return n++;  // return 하고 나서 n += 1
}

function c(f1, f2) {
    return f1(10, 10) + f2(99);
}

console.log(c(b, a))