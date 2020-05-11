<template>
    <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
        <h1 class="title">Welcome To My App</h1>
        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" @click="showNav = !showNav" :class="{ 'is-active': showNav }">
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        <span aria-hidden="true"></span>
        </a>
    </div>

    <div id="navbarBasicExample" class="navbar-menu" :class="{ 'is-active': showNav }">
        <div class="navbar-start">
        <router-link to="/" class="navbar-item">Home</router-link>
        <router-link to="/about" class="navbar-item">About</router-link>
        </div>

        <div class="navbar-end">
        <div class="navbar-item">
            <div class="buttons">
                <v-facebook-login app-id="1841024232697094" v-on:login="fbLogin"></v-facebook-login>
                <button class="button" v-on:click="testAccountLogin">Test Account Login</button>
                <g-signin-button :params="googleSignInParams" @success="googleLogin" @error="onSignInError">Sign in with Google</g-signin-button>
            </div>
        </div>
        </div>
    </div>
    </nav>
</template>




<script>
import axios from "axios";
import "regenerator-runtime";
import VFacebookLogin from "vue-facebook-login-component";
import { mapGetters } from "vuex";

export default {
  name: "navbar",
  data() {
    return {
      showNav: false,
      googleSignInParams: {
        client_id: '483971467115-fqkbv161jul0hbcr8rj6lj9es15ghndu.apps.googleusercontent.com'
      },
    }
  },
  components: {
    VFacebookLogin,
  },
  computed: {
    ...mapGetters(["isConnected", "name", "email", "picture", "personalID"])
  },
  methods: {
    googleLogin (googleUser) {
      var gjwt = googleUser.getAuthResponse().id_token;
      console.log("Google Login: " + gjwt); // eslint-disable-line no-console
      axios.post('/api//users/google', {
        value: gjwt
      })
      .then(response => {
        this.$store.dispatch("jwtSet", response.data.token);
        // TODO: Save token locally so user won't have to log back in on refresh
      })
    },
    onSignInError (error) {
      console.log('OH NOES', error); // eslint-disable-line no-console
    },
    fbLogin(response) {
      console.log("Facebook Login: " + response.authResponse.accessToken); // eslint-disable-line no-console
      axios.post('/api//users/facebook', {
        value: response.authResponse.accessToken
      })
      .then(response => {
        this.$store.dispatch("jwtSet", response.data.token);
        // TODO: Save token locally so user won't have to log back in on refresh
      })
    },
    testAccountLogin() {
      var username = prompt("Please enter in a user name:");
      console.log("Logging in with test account: " + username); // eslint-disable-line no-console
      axios.post('/api/users/test-account', {
        value: username
      })
      .then(response => {
        console.log("Test Account JWT: " + response.data.token); // eslint-disable-line no-console
        this.$store.dispatch("jwtSet", response.data.token);
        // TODO: Save token locally so user won't have to log back in on refresh
      });
    },
  }
};
</script>
<style scoped>
.g-signin-button {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  background-color: #3c82f7;
  color: #fff;
  box-shadow: 0 3px 0 #0f69ff;
}
</style>