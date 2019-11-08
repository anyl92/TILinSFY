/* 
javascrips는 event-driven(이벤트 기반)
특정 이벤트(click, network, request ..) 가 발생하면
뭘 할 지 함수를 미리 등록해서 사용한다
button.addEventListener('click', function () {...})
 */

 // 함수의 실행 순서
 function a () {
     console.log('a');
 }

 function b () {
     a();
     console.log('b');
 }

 function c () {
     a();
     b();
     console.log('c');
 }