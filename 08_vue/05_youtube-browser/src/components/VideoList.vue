<template>
    <ul class="col-lg-4 list-group">
        <VideoListItem 
            v-for="video in videos" 
            :key="video.etag"
            :video="video"
            @videoSelect="onvideoSelect"
        >
        </VideoListItem>
    </ul>
        <!-- <li v-for="video in videos" :key="video.etag">
            {{ video.snippet.title }}
        </li> -->
</template>

<script>
import VideoListItem from './VideoListItem';

export default {
    name: 'VideoList',
    // props 사용: 1. props가 넘어온다고 명시한다. 여러 개 넘어올 수 있음 [] {}
    // props 는 data랑 똑같이 쓸 수 있음. props === 물려받은 data, 그냥 바로 쓰면 된다
    props: {  // 배열로 써도 되지만, 객체를 매우 권장
        videos: Array,  // Validation. videos가 Array인지 먼저 확인
    },
    /* 아래 예시처럼 하면 안됨
    data() {
        return {
            videos: this.videos
        }
    } */
    components: {
        VideoListItem,
    },
    methods: {
        onvideoSelect (video) {
            this.$emit('videoSelect', video)
        }
    },
}
</script>

<style>
</style>