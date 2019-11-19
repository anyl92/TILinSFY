jwt.io - libraries

빨간색을 디코딩 하면 헤더가 됨

보라색을 디코드 하니까 데이터가 됨

하늘색은 일종의 인증서 파트.



api-token-auth 에 들어가서 superuser로 로그인 하면 token이 생성됨



$ npm i vue-session

토큰을 세션에 저장하는 것을 쉽게 해주는 플러그인 (미들웨어라고 할 수 있다)

vue-session 없어도 할 수 있긴 해   `window.sessionStorage.setItem()`



요청할 때 jwt 키는 headers에 value값에 JWT' ' 를 붙여서 토큰을 보내야 한다

