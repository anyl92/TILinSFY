<template>
  <div class="home">
    <h1>This is Home</h1>
    <TodoList />
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import router from '../router';
import TodoList from '../components/TodoList'

export default {
  name: 'home',
  components: {
    TodoList,
  },
  methods: {  // 내가 실행할 함수들
    isLoggedIn() {
      this.$session.start();
      if (!this.$session.has('jwt')) {  // jwt 없으면 === login 안했으면!
        router.push('/Login');
      }
    }
  },
  // lifecycle 정의는 아래에
  // this.isLoggedIn이 언제 실행되냐에 따라 어떤 함수를 쓸 지는 달라진다
  created() {  // logout 이후에 확인하기
    this.isLoggedIn()
  },
}
</script>
