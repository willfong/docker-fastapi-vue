import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bulma/css/bulma.css'
import GSignInButton from 'vue-google-signin-button'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import moment from 'moment';


// See: https://github.com/FortAwesome/vue-fontawesome
library.add(faUserSecret)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.config.productionTip = false
Vue.config.devtools = true
Vue.use(GSignInButton)

Vue.prototype.moment = moment;


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
