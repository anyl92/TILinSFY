<template>
  <div class="login">
      <h1>Log in</h1>
      <LoginForm />
  </div>
</template>

<script>
import LoginForm from '../components/LoginForm.vue';
// import router from '../router'

export default {
    name: 'Login',
    components: {
      LoginForm,
    },
    // methods: {  // 내가 실행할 함수들
    //   isLoggedIn() {
    //     this.$session.start();
    //     if (this.$session.has('jwt')) {  // jwt 있으면 === login 했으면!
    //       router.push('/');
    //     }
    //   }
    // },
    // created() { 
    //   this.isLoggedIn()
    // },
}
</script>

<style>

</style>