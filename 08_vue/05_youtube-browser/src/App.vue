<template>
    <div class="container">
        <!-- 3. template에 보여주기 -->
        <SearchBar @inputChange="oninputChange"></SearchBar>
        <!-- v-on:[자식cmpnt에서 emit하는 이벤트 이름] -->
        
        <div class="row">
            <VideoDetail :video="selectedVideo"></VideoDetail>

            <!-- v-bind: 는 줄여서 : -->
            <!-- props 사용: 0. bind로 데이터를 넘긴다 -->
            <!-- 부모랑 자식간 이름 중복은 상관없다 -->
            <VideoList 
                :videos="videos"
                @videoSelect="onVideoSelect"
            >
            </VideoList>
        </div>
    </div>
</template>

<script>
// 1. import
import SearchBar from './components/SearchBar';  
import VideoList from './components/VideoList';
import VideoDetail from './components/VideoDetail';

import axios from 'axios';

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY;

export default {
    // 컴포넌트 생성하면 해야될 일 컴포넌트는 재사용이가능
    // 0. 이름 적기
    name: 'App',

    // 2. 부모에게 자식들 등록하기
    components: {
        SearchBar,
        VideoList,
        VideoDetail,
    },
    // 원래처럼 data: {} 하면 함수 쓰라고 에러 난다..
    data() {
        return {  // 값이 없을 때 null이라도 써줘야 한다
            videos: [],
            selectedVideo: null,
        }
    },
    methods: {
        oninputChange (inputValue) {
            axios.get('https://www.googleapis.com/youtube/v3/search', {
                params: {
                    key: API_KEY,
                    type: 'video',
                    part: 'snippet',
                    q: inputValue,
                }
            })
            .then(res => this.videos = res.data.items)
        },
        onVideoSelect (video) {
            this.selectedVideo = video;
        }
    },
}
</script>

<style>
</style>