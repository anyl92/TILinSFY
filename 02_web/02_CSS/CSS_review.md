### CSS

p {

​    <Property>: <Value>

}



(0, 1, 0) >우선순위가 더 높음  (0, 0, 1)   *순차적인 순서가 아님

!important > inline css > [#id > .class] > tag > * > browser기본세팅

* !important는 웬만하면 쓰지 말 것
* id / class 는 selecting을 위한 존재 . class가 가장 많이 쓰임 그다음 tag



우선순위가 같으면 순차적으로 진행?



p:first-child {}    - 핵심은 p, 그러나 첫째인 p/ 첫번째 자식인데 까고보니 p

p:last-child P{}   - 마지막 자식인데 까고보니 p

p:nth-child(2) {}   - 부모는 모르겠고 어쨌든 2번째 p



---

190731

font-size: 100%  브라우저의 기본값 px/100 에서 100%

rem 브라우저 기본 폰트 사이즈 == 1rem

상속받은 100 % 값이 1em (부모의 )



RGB의 채도. 각각의 range(256) 16진수로 표현하면 0-f이라서 0f0f0f, ffffff



div, p 등의 box는 가로를 다 먹음

box  :  div + 6개 시맨틱 태그 

* 내용물이 없으면 안나옴



Lorem탭 - 문자열 줌



width가 지정한 건 콘텐트 영역뿐

박스 모델의 크기는 width + padding + border



-block 속성의 특징

[ div / h1 ~ h6 / p  / op, ul, li / hr / table / form ]

* 항상 새로운 line에서 시작
* 기본으로 width 100%
* width height margin padding 속성 지정 가능
* block 요소 안에 inline 요소를 포함 가능



-inline 속성의 특징

[ span / a / strong, em, del / img / br / input, select / textarea / button ]

* 새로운 라인에서 시작하지 않으며, 문장 중간에 쓸 수 있다
* content 너비만큼 가로폭을 차지한다
* width height margin padding 속성 지정 불가능, line-height(행간)으로 지정
* inline 요소 뒤에 공백(\n, space)이 있으면, 자동으로 space(4px)이 들어감
* inline 요소 안에 block 요소 포함 불가능



-inline-block 속성의 특징

* inline의 한줄표시 + block의 margin, padding, width, height
* content 너비만큼 가로폭을 차지
* display: inline-block인 요소들 뒤에 공백은 space(4px)
* 상하 여백: margin과 line height로 가능



* visibility

visible - 안보이게 상속받았을 때 보이게 해줘야 한다면

hidden - content만 화면에 안나옴 (margin, padding 있음)

collapse - table에서 안보이게 해주는것

* display

None - 아무것도 안나옴 공간도, 컨텐트도 (margin, padding 없음)



position의 default

* 위 => 아래, 왼 => 오
* 부모요소 <=> 자식요소 부모의 위치가 기준
* 좌표값을 줘도 안먹음



width, height는 상속이 안됨

relative - 상대적  

absolute - 부모(조상)가 static이면 body기준으로움직임 절대적으로 0,0)                                                   - 부모가 relative면 부모기준으로 움직임



지금보고있는화면에서의 100%  - 100vw 화면전체의비율

letterspacing? 자간

font-style: (normal, italic, oblique)

font-weight: (bold)



justify - 텍스트 늘여서 빈공간 없애줌

inline애들은 정렬안됨