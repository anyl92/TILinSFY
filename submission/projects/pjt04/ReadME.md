### 04 - Web(반응형 웹 사이트 구성)



부트스트랩을 사용하여 여러 기능을 써볼 수 있었다.

이번 프로젝트로 어떤 기능들이 있는지 숙지할 수 있었고 하나의 사이트의 한 페이지를 구성하는 데도 굉장히 번거롭다는 것을 깨달았다.



![1574122846351](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1574122846351.png)



01_layout.html

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <link rel="stylesheet" href="./01_layout.css">
    <title>영화추천시스템</title>
</head>

<body>
  <nav class="fixed-top">
      <span>영화추천시스템</span>
        <ul class="nav justify-content-end ">
          <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
          <li class="nav-item"><a href="#" class="nav-link">친구 평점 보러가기</a></li>
          <li class="nav-item"><a href="#" class="nav-link">Log in</a></li>
        </ul>
  </nav>

  <header>
    <img class="back" src="./images/background.jpg" alt="배경 이미지">
    <div class="sero">
      <h2 class="text-center card-img-overlay">당신에게 어울리는 영화를<br>추천해드립니다.</h2>
    </div>
  </header>

  <footer>
    <span class="footer-name">YULIM</span>
    <div class="footer-image float-right"><a href="#"><img class="up cut" src="./images/화살표.png" alt="화살표"></a></div>
    <!-- <img class="footer-name" src="./images/background.jpg" alt="푸터배경"> -->
  </footer>
```



02_movie.html

```html
<body>
  <nav class="fixed-top">
    <span>영화추천시스템</span>
    <ul class="nav justify-content-end ">
      <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
      <li class="nav-item"><a href="#" class="nav-link">친구 평점 보러가기</a></li>
      <li class="nav-item"><a href="#" class="nav-link">Log in</a></li>
    </ul>
  </nav>

  <header>
    <img class="back" src="./images/background.jpg" alt="배경 이미지">
    <div class="sero">
      <h2 class="text-center card-img-overlay">당신에게 어울리는 영화를<br>추천해드립니다.</h2>
    </div>
  </header>

  <div class="subtitle">
    <h3>영화 목록</h3>
    <hr class="hr-subtitle">
  </div>
  
  <div class="container mt-4">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <div class="card my_mg">
          <img class="card-img-top" src="./images/20183867.jpg" alt="알라딘">
          <div class="card-body">
            <h4 class="card-title">알라딘</h4>
            <p class="hscore rounded">9.45</p>
            <hr>
            <p>판타지</p>
            <p>개봉일 : 2019.05.23.</p>
            <a href="#" target="_blank" class="btn btn-info">영화정보 보러가기</a>
          </div>
        </div>
      </div>
```



03_detail_view.html

```html
<body>
  <nav class="fixed-top">
    <span>영화추천시스템</span>
    <ul class="nav justify-content-end ">
      <li class="nav-item"><a href="#" class="nav-link">Home</a></li>
      <li class="nav-item"><a href="#" class="nav-link">친구 평점 보러가기</a></li>
      <li class="nav-item"><a href="#" class="nav-link">Log in</a></li>
    </ul>
  </nav>

  <header>
    <img class="back" src="./images/background.jpg" alt="배경 이미지">
    <div class="sero">
      <h2 class="text-center card-img-overlay">당신에게 어울리는 영화를<br>추천해드립니다.</h2>
    </div>
  </header>

  <div class="subtitle">
    <h3>영화 목록</h3>
    <hr class="hr-subtitle">
  </div>
  
  <div class="container mt-4">
    <div class="row">
      <div class="col-12 col-sm-6 col-md-4 col-lg-3">
        <div class="card">
          <img class="card-img-top" src="./images/20183867.jpg" alt="알라딘" data-toggle="modal"
            data-target="#movie-1-modal">
          <div class="card-body">
            <h4 class="card-title">알라딘</h4>
            <p class="hscore">9.45</p>
            <hr>
            <p>판타지</p>
            <p>개봉일 : 2019.05.23.</p>
            <a href="#" target="_blank" class="btn btn-info">영화정보 보러가기</a>
          </div>
        </div>
      </div>
```

```html
<!-- Modal-1-aladin -->
  <div>
    <div class="modal fade" id="movie-1-modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalScrollableTitle"
      aria-hidden="true">
      <div class="modal-dialog modal-dialog-scrollable" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalScrollableTitle">알라딘, Aladin</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div id="carousel-1" class="carousel slide" data-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img class="image-size d-block w-100" src="./images/20183867-01.jpg" alt="알라딘상세1">
                </div>
                <div class="carousel-item">
                  <img class="image-size d-block w-100" src="./images/20183867-02.jpg" alt="알라딘상세2">
                </div>
                <div class="carousel-item">
                  <img class="image-size d-block w-100" src="./images/20183867-03.jpg" alt="알라딘상세3">
                </div>
              </div>
              <a class="carousel-control-prev" href="#carousel-1" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
              </a>
              <a class="carousel-control-next" href="#carousel-1" role="button" data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
              </a>
            </div>
            <div class="modal-c-m">
              <p>12세이상관람가</p>
              <p>누적 관객수 : 2,962,455</p>
              <hr>
              <p>"머나먼 사막 속 신비의 아그라바 왕국의 시대.   좀도둑 ‘알라딘’은 마법사 ‘자파’의 의뢰로 마법 램프를 찾아 나섰다가   주인에게 세 가지 소원을 들어주는 지니를 만나게 되고,   자스민 공주의 마음을 얻으려다 생각도 못했던 모험에 휘말리게 되는데…
                "
                </p>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>
  </div>
```

