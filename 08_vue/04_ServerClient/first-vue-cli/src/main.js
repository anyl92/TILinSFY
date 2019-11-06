import Vue from 'vue';
import App from './App.vue';  // .vue는 안써도 동작함

new Vue({
    // el: '#app',
    // method (함수 in 객체) 정의할 때, () => {} 금지이지만, 여기서만 쓴다
    render: h => h(App),
    },
).$mount('#app')  // 위 주석과 같은데 보통 이렇게 사용



