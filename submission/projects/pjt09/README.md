### 09 - Vue

1. db.json에 데이터를 저장

```
{
  "genres": [
    {
      "id": 1,
      "name": "드라마"
    },
...
  ],
  "movies": [
    {
      "id": 1,
      "name": "82년생 김지영",
      "rating": "12세이상관람가",
      "genre_id": 1,
      "director": "김도영",
      "user_rating": 6.61,
      "poster_url": "https://movie-phinf.pstatic.net/20191024_215/1571900079078PNazL_JPEG/movie_image.jpg",
      "description": "1982년 봄에 태어나 누군가의 딸이자 아내, 동료이자 엄마로 2019년 오늘을 살아가는 ‘지영’(정유미). 때론 어딘가 갇힌 듯 답답하기도 하지만 남편 ‘대현’(공유)과 사랑스러운 딸, 그리고 자주 만나지 못해도 항상 든든한 가족들이 ‘지영’에겐 큰 힘이다.  하지만 언젠가부터 마치 다른 사람이 된 것처럼 말하는 ‘지영’. ‘대현’은 아내가 상처 입을까 두려워 그 사실을 털어놓지 못하고 ‘지영’은 이런 ‘대현’에게 언제나 “괜찮다”라며 웃어 보이기만 하는데…  모두가 알지만 아무도 몰랐던 당신과 나의 이야기"
    },
...
  ]
}
```



2. App.vue

```js
<script>
const axios = require('axios');
import MovieList from './components/movies/MovieList';
const HOST = 'http://localhost:3000/';
// 경로에 있는 MovieList 컴포넌트를 불러오고 url주소도 host에 저장한다

export default {
  name: 'app',
  // 불러온 컴포넌트를 사용하기 위해 등록한다
  components: {
    MovieList,
  },
  data() {
    return {
      movies: [],
      genres: [],
    }
  },
  mounted() {
    // 제시된 URL로 요청해 data의 movies 배열에 해당 하는 데이터를 넣는다
    axios.get(HOST + 'movies')
      .then(res => this.movies = res.data);
    // 제시된 URL로 요청해 data의 genres 배열에 해당 하는 데이터를 넣는다
    axios.get(HOST + 'genres')
      .then(res => this.genres = res.data);
  },
}
</script>
```

```html
<template>
  <div id="app">
    <div class="container">
        <!-- movie와 genres를 호출하여 props -->
        <MovieList :movies="movies" :genres="genres" />
    </div>
  </div>
</template>
```



3. MovieList.vue

```js
<script>
import MovieListItem from './MovieListItem'
export default {
  name: 'MovieList',
  components: {
    MovieListItem
  },
  data () {
    return {
      showGenreNum: 0,
    } // 보여줄 장르의 넘버값을 저장할 변수를 생성해둔다
  },
  computed: {
    genresChange () {
      if (this.showGenreNum === 0) {  // 기본값인 경우 전체 리스트를 보여준다
        return this.movies;
      } else {
        return this.movies.filter(movie => movie.genre_id === this.showGenreNum)
      }  // 현재 영화의 장르id값과 보여줄 장르의 넘버값이 같은 것만을 골라 보여준다
    }
  },
  // App.vue의 props 데이터를 받기 위한 입력
  props: {
    movies: Array,
    genres: Array,
  }
}
</script>
```

```html
<template>
  <div>
    <h1>영화 목록</h1>
    <h2>장르 선택</h2>
      
    <!-- select 태그를 showGenreNum와 양방향 바인딩 한다 -->  
    <select class="form-control" v-model="showGenreNum">
      <option :value="0">전체보기</option>
      <option v-for="genre in genres" :key="genre.id" :value="genre.id">
        {{ genre.name }}</option>
    </select>
      
    <!-- genresChange의 리턴배열을 for로 돌면서 출력한다 -->  
    <div class="row">
      <MovieListItem v-for="movie in genresChange" :key="movie.id" :movie="movie"/>
    </div>
  </div>
</template>
```



4. MovieListItem.vue

```js
<script>
import MovieListItemModal from './MovieListItemModal';
export default {
  name: 'MovieListItem',
  components: {
    MovieListItemModal,
  },
  props: {
    movie: Object,
  },
  data () {
    return {
    }
  }
}
</script>
```

```html
<template>
  <div class="col-3 my-3">
    <img class="movie--poster my-3" :src="movie.poster_url" :alt="movie.name">
    <h3>{{ movie.name }}</h3>
    <!-- 모달을 활용하기 위해서는 data-taget에 모달에서 정의된 id값을 넣어야 한다. -->
    <button class="btn btn-primary" data-toggle="modal" :data-target="`#movie-${movie.id}`">영화 정보 상세보기</button>
    <MovieListItemModal :movie="movie" />
  </div>
</template>
```



5. MovieListItemModal.vue

```js
<script>
export default {
  name: 'MovieListItemModal', 
  props: {
    movie: Object,
  },
}
</script>
```

```html
<template>
<div class="modal fade" tabindex="-1" role="dialog" :id="`movie-${movie.id}`">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">{{ movie.name }}</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <img class="modal-image-size" :src="movie.poster_url" :alt="movie.name">
        <p>{{ movie.rating }}</p>
        <p>{{ movie.description }}</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>
</template>
```

```css
<style>
    .modal-image-size {
      width: 200px;
    }
</style>
```



6. result

![결과화면](C:\Users\student\submission\projects\pjt09\결과화면.PNG)

![모달화면](C:\Users\student\submission\projects\pjt09\모달화면.PNG)

