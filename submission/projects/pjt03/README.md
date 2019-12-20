## 03 - Web(HTML/CSS를 활용한 웹 사이트 구성)

1. Header

웹사이트의 헤더 부분에 로고 이미지와 네비게이션 바를 구성합니다.

2. title section

서비스를 소개하는 문구와 배경 이미지가 있는 섹션을 구성합니다.

3. aside

좌측 레이아웃에 장르 목록을 구성합니다.

4. move section

우측 레이아웃에 제공된 영화 포스터를 활용하여 실시간 영화 순위 목록을 구성합니다.

5. footer

연도와 이름이 작성된 푸터를 구성합니다.



* 기본 예시 작성 . css

```css
/* header */
header {
  /* 상단에 고정시키며(sticky) 다른 영역보다 우선하여 볼 수 있도록 작성하세요. */
  position: fixed;
  /* position: sticky;  마진이 생김 */
  top: 0;
  z-index: 1000;
}

/* nav */
nav {
  /* navigation 항목을 오른쪽으로 정렬 시키세요.*/
  float: right;
}

.nav-items > li {
  /* navigation 항목을 한 줄로 만들어 주세요. */
  display: inline-block;
  /* 좌우 여백을 지정하세요. */
  margin: 0 5px;
  /* li 태그의 bullet point를 제거 해주세요. */
  list-style: none;
}

.nav-items > li > a {
  /* a tag는 링크를 나타내며, 기본적으로 글자 색상이 파란색입니다. 원하는 색상으로 바꿔보세요. */
  color: #444444;
}

.nav-items > li > a:hover {
  /* hover는 마우스 오버시 모습입니다. 
  이때 하이라이트 되도록 다른 색상으로 바꿔보세요. */
  color: #7048e8;
  /* a tag를 마우스 오버하면 밑줄이 나타납니다.
  text를 꾸며주고 있는 밑줄을 없애보세요. */
  text-decoration: none;
}

/* title section */
#section-title {
  /* 배경 이미지를 적용 해보세요. (이미지는 images/background.jpg) */
  background-image: url(images/background.jpg);
  /* 텍스트를 가운데 정렬 해보세요. */
  text-align: center;
  /* 텍스트를 수직 가운데 정렬 해보세요. (section-title은 높이가 300px) */
  line-height: 300px;
}

.section-title-heading {
  /* font size를 적절하게 조정 해주세요. (h1 기본 2rem) */
  font-size: 2.5rem
}

/* aside */
aside {
  /* aside를 부모인 div#content의 영역에 위치시키세요.
  div#content는 position: relative 입니다.
  상위가 relative니까 position주면 잘 작동 할거다.
  top이 0인데 부모밖으로 나갈 수 없어 부모밑에딱붙는다.
  */
  position: absolute;
  top: 0;
  bottom: 0;
}

.aside-items {
  /* ul 태그의 자동으로 적용된 padding을 제거 해주세요. */
  padding: 0;
}

.aside-items > li {
  /* li 태그의 bullet point를 제거 해주세요. */
  list-style: none;
}

/* footer */
footer {
  /* footer는 항상 바닥에 위치하도록 position을 설정 해주세요. */
  position: fixed;
  bottom: 0;
  /* 텍스트를 가운데 정렬 해주세요. */
  text-align: center;
  /* 텍스트가 수직정렬 되도록 해주세요. (footer는 높이가 40px) */
  line-height: 40px
}
```



### Result

![result_cap](C:\Users\student\submission\projects\pjt03\result_cap.png)
