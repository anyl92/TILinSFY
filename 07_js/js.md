#### INTRO

자바스크립트란? 브라우저 조작 언어



브라우저 f12 -> console 에서

```
window.print();
인쇄 창 나옴

window
Window {parent: Window, postMessage: ƒ, blur: ƒ, focus: ƒ, close: ƒ, …}

window.console.log('Hi');
Hi

window.document.write('Hi');
문서에 작성

window.alert('Wow');
알림창이 나옴

window.confirm('진짜?');
알림창 - 확인 : True / 취소 : False 반환 (함수)

window.document.title = "제목을 바꿔라";
"제목을 바꿔라" HTML의 헤더 타이틀 바꿔준다
= 뒤에 꺼 빼면 그냥 출력도 해줌
```

```
for (let i=1; i <= 10; i++) {
    if (i % 3 == '0') {
        window.document.write(clap);
    }
	else {
        window.document.write('<p>' + i + '</p>');
    }
}
숫자 0인데 '0'? 그러나 제대로 잘 나옴
왜냐면 js에는 === 와 == 가 있다

0 === 1
false
0 === '0'
false
0 == 1
false
0 == '0'
true

js에서는 === 를 쓰는 걸로.. '===' 가 맞음
```



BOM, DOM TREE 용어 알아만 두기.

window.를 꼭 붙이지 않아도 동작함



(싸피 게시판 댓글 더보기)새로고침은 네트워크가 0초부터 다시 시작하는데 더보기 버튼은 새로고침이 아님.

```
function fnAnswerMore() {
	// 실행하면, 댓글 로드
}
```

-> 자바스크립트로는 새로고침 하지 않고 문서를 변환시킬 수 있다





11.4 : django 과목

11.11 : js 과목 + 수업

11.12 ~ 11.15 : 알고리즘

11.18 : Vue 과목 ( 시험범위 3일어치 )

11.18 + 19 Vue 수업





node.js 설치

vs code에서 node -v 확인 후

f1 quokka.js new javascript file

저장하면 안됨 안하고 해야함