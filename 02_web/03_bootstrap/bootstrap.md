## Bootstrap

1. Bootstrap은 무엇인가?

   - Bootstrap은 빠르고 간편한 반응형 웹 디자인(responsive web design)을 위한 open-source front-end framework이다.

   

2. Spacing (m-\*, p-\*, mx-\*, my-\* 등)

   - 작성 형태 : {property}{sides} - {size}

   - {property} : m(margin), p(padding)

   - {sides}:  t(top), b(bottom), l(left), r(right), x(좌우), y(상하) 

     m,p 뒤에 아무것도 안적고 단독 사용시 상하좌우 모두를 의미

   - size 

     - 0  => 0
     - 1 => 0.25 rem
     - 2 => 0.5 rem
     - 3 => 1 rem
     - 4 => 1.5 rem
     - 5 => 3 rem

   - Examples

     ```html
         <div class="mt-3 text-right">margin top3(1rem) + Text right</div>
         <div class="mt-2 text-center">mt2(0.5rem) + Text center</div>
         <div class="mt-1 text-left">mt1(0.25rem) + Text left</div>
     
         <div class="mx-5 my-3">TEST</div>
         <div class="py-3 mx-3">TEST</div>
     ```

     

3. Colors (primary, secondary 등)

   primary - 파란색

   secondary - 회색

   success - 초록색

   danger- 빨간색

   warning - 노란색

   info -  회색 섞인 파란색

   light - 옅은 회색

   dark - 검정색

   white - 흰색

   

4. 그리드 시스템 (Grid System)

   - 그리드 시스템은 열을 나누어 콘텐츠를 원하는 위치에 배치하는 방법을 말한다.

   - Bootstrap은 반응형 12열 그리드 시스템을 제공.

   - 그리드 레이아웃을 구성 시에는 반드시 `.row`(행)를 먼저 배치하고 행 안에 `.col-*-*`(열)을 필요한 갯수만큼 배치한다. 

     즉, container 내에 .row(행)을 먼저 배치하고 그 안에 `.col-*-*`(열)을 배치한다. 그리고 콘텐츠는 `.col-*-*` 내에 배치한다.

   - ```html
     <div class="container bg-success p-3">
             <div class="row bg-danger"> <!-- row 먼저 배치 -->
                 <div class="col-4 border border-dark">1/3</div> <!-- col -->
                 <div class="col-4 border border-dark">1/3</div>
                 <div class="col-4 border border-dark">1/3</div>
             </div>
             <div class="row bg-primary">
                 <div class="col-9 border border-dark">
                     <div class="row">
                 <!-- 중첩하는 법 / col-9으로 3/4차지 후, 3/4를 1/3씩 배치 -->
                         <div class="col-4 border border-dark">1/3</div>
                         <div class="col-4 border border-dark">1/3</div>
                         <div class="col-4 border border-dark">1/3</div>
                     </div>
                 </div>
                 <div class="col-3 border border-dark">1/4</div>
             </div>
             <div class="row bg-warning">
                 <div class="col-9 border border-dark">3/4</div>
                 <div class="col-4 border border-dark">???</div>
                 <div class="col-6 border border-dark">???</div>
             </div>
         </div>
     ```

   - 화면의 크기에 따른 클래스 이름 및 배치

     ```html
     <article class="col-12 col-sm-6 col-md-4 col-lg-3 col-xl-2 border border-light text-white">
              <p>This is Article</p>
     </article> 
     ```

     

   - |                     | Extra small <576px | Small ≥576px | Medium ≥768px | Large ≥992px | Extra large ≥1200px |
     | ------------------- | ------------------ | ------------ | ------------- | ------------ | ------------------- |
     | Max container width | None (auto)        | 540px        | 720px         | 960px        | 1140px              |
     | Class prefix        | `.col-`            | `.col-sm-`   | `.col-md-`    | `.col-lg-`   | `.col-xl-`          |
     | # of columns        | 12                 |              |               |              |                     |

   - col offset

     : offset은 중앙정렬시 또는 비우고 시작하고 싶을 때 사용한다.

     ```html
     <section class="row bg-secondary">
                 <article class="col-6 offset-3 border border-white">
                     <p>This is Article</p>
                 </article>
                 <article class="col-4 offset-4 border border-white">
                     <p>This is Article</p>
                 </article>
             </section>
     ```

     

- 사용 가능한 클래스
  - nav : nav bar 만드는것
  - nav-item : 네비의 요소 / link : 링크 검
  - justify-content-end : 컨텐트를 오른쪽정렬
  - col-12 col-md-6 : 그리드 분할 12 넘어가면 밑으로 흐름
  - border
  - text
  - d-inline 디스플레이 인라인으로
  - d-block 디스플레이 블록으로
  - d-lg-none 라지일때 안보여 
  - d-lg-block 라지일때 블록
  - text-left : 텍스트 왼쪽정렬
  - text-lowercase : 소문자 <-> uppercase
  - font-weight-bold/normar/light
  - font-italic
  - 
  
- 사용 가능한 컴포넌트 (Components) 
  
  - container : 좌우 마진이 있는... -fluid 꽉채움
  
  - jumbotron : 텍스트 박스?
  
  - nav
  
  - card
  
  - carousel : 회전목마? 
  
    slide : 그림슬라이드
  
    carousel-fade 사라지듯이
  
  - alert alert-primary role="alert" 경보?
  
  - btn ( button )



sr-only 시각장애인을 위한