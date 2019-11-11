<template>
    <div>
        <!-- method는 내가 인자를 넘긴다면 (ARG) 붙이고 아니면 안붙임 -->
        <!-- v-on: 을 줄여서 @ 으로 -->
        <!-- <input @input="onInput" type="text"> -->
        <input @keypress.enter="onInput" type="text"> 
    </div>
</template>

<script>
export default {
    name: 'SearchBar',  // new cmpnt: 0. 이름적기
    methods: {
        onInput (e) {  // function 생략
            // 이벤트를 계속 위로 발생시키겠다('Event이름', 전송할 값)
            // 자식 cmpnt => 부모 cmpnt 등 정보(데이터)를 올려보낼 때 사용
            this.$emit('inputChange', e.target.value);
        }
    }
}
</script>


<style scoped>
/* scoped: 해당 컴포넌트의 태그들만 영향을 받는다! */
    input {
        width: 75%;
    }

    div {
        text-align: center;
        margin: 20px;
    }
</style>