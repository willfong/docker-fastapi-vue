import Vue from 'vue'
import Vuex from 'vuex'
import axios from "axios";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    jwt: false,    
  },
  mutations: {
    JWT_SET(state, jwt) {
      state.jwt = jwt;
    },
  },
  actions: {
    jwtSet({commit}, jwt) {
      axios.defaults.headers.common['Authorization'] = jwt;
      commit('JWT_SET', jwt);
    },
  },
  getters: {
    loggedIn: state => state.jwt,
  }
})
