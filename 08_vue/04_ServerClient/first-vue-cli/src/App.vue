<template>
    <!-- 반드시 template 안에는 단 한개의 최상단 태그/노드-->
    <div>
        <h1>나쁜말 거름종이</h1>
        <input type="text" v-model="input">
        <p>{{ filteredInput }}</p>

        <!-- <div class="static" v-bind:class= "{ active: isActive, error: hasError }">Hi</div> -->
        <!-- <div v-bind:style= "{ color: activeColor, fontsize: fontSize + 'px' }">Hi</div> -->
    </div>
</template>

<script>
/* eslint-disable no-console */
// 컴포넌트 이름부터 쓰고 시작함
export default {
    name: 'App',
    // data를 function으로 만들어야함
    data: function () {
        return {
            input: 'type something',
        }
    },
    // data: function () {
    //     return {
    //         activeColor: 'red',
    //         fontsize: 30
    //     }
    // },
    
    methods: {
        
    },

    computed: {
        filteredInput: function () {
            // return `Filtered: ${this.input.replace('바보', '**')}`;
            // 한번밖에안돼

            return this.input.replace(/바보|멍청이|똥개/g, '**');
            // g, 전체 다 찾아라  i, 대소문자구분X
        }
    },
}
</script>

<style></style>