<template>
  <div class="home">
    <MessageNew v-if="loggedIn" @added="getMessages()" />
    <Message v-for="message in messages" v-bind:key="message.id" v-bind:message="message" />
  </div>
</template>

<script>
import axios from "axios";
import MessageNew from "@/components/messageNew";
import Message from "@/components/message";
import { mapGetters } from "vuex";

export default {
  name: "home",
  computed: {
    ...mapGetters([
      "loggedIn",
    ])
  },
  data() {
    return {
      messages: "",
    };
  },
  components: {
    MessageNew, Message
  },
  methods: {
    getMessages() {
      axios.get("/api/messages/").then(response => this.messages = response.data);
    },
  },
  mounted() {
    this.getMessages();
  },
};
</script>
