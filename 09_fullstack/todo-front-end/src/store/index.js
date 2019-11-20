import Vuex from 'vuex';
import Vue from 'vue';
import auth from './modules/auth'

Vue.use(Vuex);  // Vue 에 Vuex 미들웨어 등록


const store = new Vuex.Store({
    modules: {
        auth, 
    }

});

export default store;
