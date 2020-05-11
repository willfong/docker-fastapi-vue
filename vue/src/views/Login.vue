<template>
  <div class="container">
    <button class="button" v-on:click="testAccountLogin">Test Account Login</button>
    <a class="button" :href="`https://github.com/login/oauth/authorize?client_id=${gitHubToken}`">Login via GitHub</a>
  </div>
</template>




<script>
import axios from "axios";

export default {
  name: "navbar",
  data() {
    return {
      gitHubToken: "626687d69db48d6cf1d2",
    }
  },
  methods: {
    loginSuccess(token) {
      this.$store.dispatch("jwtSet", token);
      this.$router.push("/");
    },
    testAccountLogin() {
      var username = prompt("Please enter in a user name:");
      console.log("Logging in with test account: " + username); // eslint-disable-line no-console
      axios.post('/api/users/test-account', {
        value: username
      })
      .then(response => {
        //console.log("Test Account JWT: " + response.data.token); // eslint-disable-line no-console
        this.loginSuccess(response.data.token);
      });
    },
    oauthGitHub(code) {
      axios.post("/api/users/github",{value: code}).then(response => {
        //console.log(response.data); // eslint-disable-line no-console
        this.loginSuccess(response.data.token);
      });
    },
  },
  mounted() {
    if (this.$route.query.oauth) {
      this.oauthGitHub(this.$route.query.code);
    }
  },
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