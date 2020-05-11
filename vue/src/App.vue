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
};
</script>
