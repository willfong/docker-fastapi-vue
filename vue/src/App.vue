<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/navbar";

export default {
  name: "appMain",
  components: {
    NavBar,
  },
  mounted() {
    // This should be handled elsewhere?
    if (window.location.pathname == '/oauth/github') {
      window.location.href = `/#/login?oauth=github&code=${window.location.search.substring(6)}`;
    }
  }
};
</script>
