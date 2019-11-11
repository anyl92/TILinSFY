import Vue from 'vue';
import App from './App';  // App.vue 를 알아서 확장자 버리고 읽음 (써도 됨)

new Vue({
    // el: '#app',  // vue instance를 마운트할 대상을 찾는다 or 함수 끝에 .$mount('#app') 사용
    // render 는 유일하게 method 인데 arrow function 사용이 가능함
    render: h => h(App), 
}).$mount('#app')