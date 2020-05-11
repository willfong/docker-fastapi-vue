<template>
  <div>
    <button class="button" v-on:click="testAccountLogin">Test Account Login</button>
  </div>
</template>




<script>
import axios from "axios";

export default {
  name: "navbar",
  data() {
    return {
    }
  },

  methods: {
    loginSuccess() {
      this.$router.push("/");
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
        this.loginSuccess();
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