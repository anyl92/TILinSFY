<template>
    <li @click="onVideoClick" class="list-group-item">
        <img :src="thumbnailUrl" class="mr-3" :alt="video.snippet.title">
        <div class="media-body">
            <!-- {{ video.snippet.title }} 인코딩 안된 상태로 나옴 -> span -->
            <span v-html="video.snippet.title"></span>
        </div>
    </li>
</template>

<script>
export default {
    name: 'VideoListItem',
    props: {
        video: Object,
    },
    methods: {
        onVideoClick () {
            this.$emit('videoSelect', this.video)
        }
    },
    computed: {
        thumbnailUrl () {
            return this.video.snippet.thumbnails.default.url
        }
    },
}
</script>

<style scoped>
    li {
        display: flex;
        cursor: pointer;
    }

    li:hover {
        background-color: #eee;
    }
    
</style>