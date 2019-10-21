### CSS (Cascading style sheet)

* em과 rem
  * em : 상속받은 사이즈의 100%가 1em
  * rem : 브라우저의 기본 폰트 사이즈 1rem

```css
div > div {
    font-size: 0.8em;
}
```

```html
<div>
    <!-- 기본 폰트 사이즈 16px --> 
    aaaa  
    <div>
        <!-- 16 * 0.8 -->
        bbbb
        <div>
            <!-- 16 * 0.8 * 0.8 -->
            cccc
            <div>
                <!-- 16 * 0.8 * 0.8 * 0.8 -->
                dddd
            </div>
        </div>
    </div>
</div>
```



* RGBA 
  * #ffffff  256을 16진수로 표현한 것
  * (256,256,256,0)  A는 투명도



* 스타일 지정 우선순위 - 내림차순

  * !important
  * inline css (html 태그에 바로 스타일을 지정하는 것)
  * #id
  * .class  <-가장 많이 쓴다
  * tag  <- class 다음으로 많이 쓴다
  * *
  * browser 기본 셋팅

  

* HTML에서 스타일을 지정하는 방법 3가지

  1. 외부 스타일 시트(External Style Sheet)

     ```html
     <link rel="stylesheet" type="text/css" href="mystyle.css">
     ```

  2. 내부 스타일 시트(Internal Style Sheet)

     ```html
     <style type="text/css">
       body {font-size:9pt;}
      </style>
     ```

  3. HTML 태그 내에 스타일 지정(Inline Styles)

     ```html
     <p style="color:gray;">이 문단의 색상은 회색으로 지정됩니다.</p>
     ```

  

* 상속(selector) _ 02_selectors1을 참조하세욤,,,

```css
h1, p, a {  /* h1과 p와 a태그 모두 */
     color: red;
}

.pp {  /* class="pp" 인 것들 */
    color: orange;
}

a[href] {  /* a태그 내의 href attribute를 가진 것들 */
    color: green;
}

a[target="_blank"] {  /* a태그의 target이 "_blank"인 것들 */
    color: black;
}

h2[title~="greeting"] {  /* h2 중 title="greeting"을 가진 것들 */
    color: blueviolet;
}

div p {  /* 모든 div 안의 p 후손 요소 */
    color:chocolate;
}

div > p { /* 정확히 div 의 p 중 자식 요소 */
    color:cyan;
}

div.a {  /* div의 a클래스만 */
    
}
```



* 상속2 _ 03_selectors2를 찹조하세염

```css
body {  /* 바디 태그의 모든 요소에  */
    color: deeppink;
}

article:first-of-type {  /* article 중에 첫 번째에게 */
    background-color: red;
}

article:nth-of-type(2) {  /* article 중에 두 번째에게 */
    background-color: green;
}

article:nth-last-of-type(2) {  /* article의 마지막에서 두 번째에게 */
    background-color: blue;
}

article:last-of-type {  /* article 중의 마지막에게 */
    background-color: black
}

p:first-child {  /* 첫번째 자식인데 까고 보니 p */
    color: gold
}

p:last-child {  /* 막내인데 까고보니 p */
    color: violet;
}

p:nth-child(4) {  /* 부모는 모르겠고 아무튼 4째인데 p */
    color: white;
}
```



* 상태에 따라 클래스를 바꾸는 가상 클래스(pseudo class selector)

```css
a {
    text-decoration: none;
    color: black;
}

a:link {  /* 방문하지 않은 link */
    color: red;
}

a:hover {  /* 마우스를 갖다댔을 때 */
    color: orange;
}

a:visited {  /* 방문한 link */
    color: beige;
}

input:focus {  /* 인풋에 포커싱이 되었을 때 */
    background-color: black;
    color: white
}
```



* rounded

```css
div.rounded {
    border-radius: 30px;
    overflow: hidden;
}
```



* block 속성 < div / h1~6 / p / ol, ul, li / hr / table / form >

  * 항상 새로운 line에서 시작
  * 기본으로 width 100%를 가진다
  * width height margin padding 속성 지정이 가능하다
  * block 요소 안에 inline 요소를 포함 가능

* inline 속성 

  < span / a / strong, em, del / img / br / input, select / textarea / button >

  * 새로운 라인에서 시작하지 않음, 문장 중간에 쓸 수 있다
  * content 너비만큼 가로폭을 차지한다
  * width height margin padding 속성 지정이 불가능하다
  * line height(행간)으로 지정
  * inline 요소 뒤에 공백(\n, space)이 있으면, 자동으로 4px space가 삽입
  * inline 요소 안에 block 요소 포함이 불가능하다

* inline-block 속성

  * inline의 한줄표시 + block의 margin, padding, width, height 지정 가능
  * content 너비만큼 가로폭을 가짐
  * `display: inline-block` 인 요소들 뒤에 공백은 4px space
  * 상하 여백 : margin과 line height 사용 가능

```html
<p class="ib">p는 원래 블록</p>
<p class="ib">하지만 짜잔!</p>
```

```css
.ib {
    display: inline-block;
} 이렇게 하면 block 속성인 p태그가 inline-block 속성을 갖는다
```



* visible

```css
.visible {
    visibility: visible;
} 화면에 보인다
```

```css
.hidden {
    visibility: hidden;
} content만 화면에 안나온다 (공간은 차지하고 있다)
```

```css
.display-none {
    /* Display 속성이지만, 비교해보자. */
    display: none;
} content와 공간(margin, padding 등등)도 안나온다
```

*  collapse - 표(table)의 테두리와 셀(td)의 테두리 사이의 간격을 없앱니다. 겹치는 부분은 한 줄로 나타냅니다.?? // 그냥 table내에서의 hidden

```css
.collapse {  
    /* collapse 는 Table 에서만 사용 */
    visibility: collapse;
}  
```



* opacity - 투명도

```css
div, img {
    opacity: 0.5;
    transition: opacity 1s;
}  투명도를 0.5로 설정, 1초에 걸쳐 변화하도록

div:hover, img:hover {
    opacity: 1.0;
}  마우스를 갖다대면 투명도를 1로 설정
```



* position

  default는 위에서 아래로, 왼쪽에서 오른쪽으로

  부모요소와 자식요소간에는 부모요소의 위치가 기준점

  * static;

    부모고 뭐고 다무시함

    top, left 안먹고 - 초깃값을 위치로 지정하면 안됨

    앞에 설정한 position을 무시하려고 할 때

  * relative;

    상대적으로 부모에서 top, left 이동 가능

    static이 끝나는 지점을 top 0으로 생각함

  * absolute;

    부모가 static이면, body 기준으로 움직임

    부모가 relative면, 부모 기준으로 움직임



* vw vh

  뷰포트의 너비값, 뷰포트의 높이값

  각 브라우저 / 스크린의 너비에 맞춰서 변함

  

* font

```css
{font-family: ;}
{font-style: normal, italic, oblique;}
{font-weight: bold;}
{letter-spacing: 5px;}
{text-align: justify;}
```



* p태그는 기본 마진이 위아래 16
* div 기본 마진 없음
* 블럭 요소안에는 인라인 쓸 수 있음



* width와 height 프로퍼티를 비롯한 모든 박스모델 관련 프로퍼티(margin, padding, border, box-sizing 등)는 [상속](https://poiemaweb.com/css3-inheritance-cascading)되지 않는다.