# Web

### 웹 서비스

웹 서비스 - 서버 컴퓨터에서 제공하는 무언가

url로 요청을 보내고, 정보를 얻음 ex) requests 모듈, postman

* 요청의 종류
  1. 줘라 (HTML 문서)
     - server - 요청을 받고 분석하여 일을 하고, 해당하는 것을 준다.
  2. 받아라 (로그인, 회원가입 등)
     * 사람이 처리요청 데이터를 넘기고, 자동화된 프로그램이 응답해준다.
     * url 요청이 들어오면 일을 끝내고 html을 보낸다.

**<u>우리는 서버컴퓨터에서 요청과 응답을 처리할 프로그램을 개발한다.</u>** 

탐색기와 browser는 같은 일을 한다.

* 탐색기 -> file:// (내컴퓨터) 위치

* Browser -> http:// (남의 컴퓨터) 주소

Web의 변화

* Static web - Sever는 file을 들고 있고, 정확한 요청을 해야 file을 줌(도서관과 같음). 단순하다는 장점이 있다.

* Dynamic web web application program (Web APP) - Program이 돌아 분석하고, 일해서 문서(html)를 보냄.

URI -> URL(Uniform Resource Locator, 파일 식별자)는 네트워크 상에서 자원이 어디 있는 지를 알려주기 위한 고유 규약이다.

### HTML

HTML(hyper text markup language) 

: (링크들로 이루어진 글) 웹 페이지를 작성하기 위해 쓴 역할 표시 / 언어 최종적으로 나가게 되는 정보

HTTP(hyper text transfer protocol)(s - secure)

`<meta>` : 정보의 정보

h1 : 가장 중요한 제목. 따라서, 여러 개를 쓸 수 없다. 글씨를 조절하고 싶다면 CSS에서 조절하는 것

-> 글을 구조화할 때 content가 갖고 있는 역할 지정만 생각하고, 스타일은 나중에 함.

