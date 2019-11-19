import Vue from 'vue'
import App from './App.vue'
import router from './router'
// import VueRouter from 'vue-router'
import VueSession from 'vue-session'  // 발급받은 token을 sessionstorage에 저장하는걸 도와주는 플러그인


Vue.config.productionTip = false;
Vue.use(VueSession);  // Vue 에게 VueSession 이라는 Middleware 등록


new Vue({
  router,  // router ./ index.js에서 악수하고, 본격적으로 일을 시작
  render: h => h(App)
}).$mount('#app');
