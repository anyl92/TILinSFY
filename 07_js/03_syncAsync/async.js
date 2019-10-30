// JS: Non-Blocking

// function nothing () {
//     console.log('end');
// }

// console.log('start');
// setTimeout(nothing, 3000)


// function sleep_3s() {
//     setTimeout(() => {console.log('Wake Up!')}, 3000);
// }

// console.log('Start sleeping');
// sleep_3s()
// console.log('End of program');

/* 그럼 어떤 함수/작업들이 Non blocking 한가용?  
지금 당장 해결할 수 없고 결과도 확신할 수 없는 모든일 
*/

function complexTask() {
    console.log('시작');
    for (let i=0; i<10000000000; i++) {}
    console.log('오래걸림');
}

setTimeout(() => {console.log('짱빨리끝남!')}, 1)
complexTask()

// 자바스크립트 한계 - 이벤트 큐에 settimeout 이 들어가버림 빨리끝날줄알고

