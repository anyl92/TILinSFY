<template>
    <div v-if="video" class="col-lg-8">
        <div class="embed-responsive embed-responsive-16by9">
            <iframe :src="videoUrl" frameborder="0" class="embed-responsive-item"></iframe>
        </div>

        <div class="details">
            <h4 v-html="video.snippet.title"></h4>
            <p>{{ video.snippet.description }}</p>
        </div>
        <!-- {{ video.snippet.title }} -->
    </div>
</template>

<script>
export default {
    name: 'VideoDetail',
    props: {
        video: Object,
    },
    computed: {
        videoUrl () {
            return `https://www.youtube.com/embed/${this.video.id.videoId}`
        }
    },
}
</script>

<style scoped>
    .details {
        margin-top: 10px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
    }
</style>