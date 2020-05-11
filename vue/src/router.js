import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home.vue'
import About from '@/views/About.vue'
import Login from '@/views/Login.vue'

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
]

export default new VueRouter({routes})
