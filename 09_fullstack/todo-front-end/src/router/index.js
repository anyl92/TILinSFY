import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)  // 우리 같이 일해보자. 악수

const router = new VueRouter({
  mode: 'history',  // 원래의 브라우저 라우팅 방식, # 없애줌
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})

export default router
