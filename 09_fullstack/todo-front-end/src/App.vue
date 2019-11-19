<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/Login">Login</router-link>
    </div>
    <div class="container col-6">
      <router-view/>
      <!-- 다른 url이 들어오면 여기에서 보여주세염 -->
    </div>
  </div>
</template>

<style>
/*
  1. 컴포넌트마다 비슷한/같은 함수들을 정의해야함 + 정리가 안됨.
  2. 사용자 auth 정보 & todos 목록을 컴포넌트끼리 공유하지 못함.

   => Vuex(State Management System)
*/
</style>
