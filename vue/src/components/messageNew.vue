<template>
  <div class="column is-10 is-offset-1">
    <div class="box">
      <article class="media">
        <div class="media-content">
          <div class="content">
            <div class="field has-addons has-addons-centered">
              <div class="control is-expanded">
                <input class="input" type="text" v-model="text" placeholder="Add new message" />
              </div>
              <div class="control">
                <button class="button is-link" @click="submit">Add</button>
              </div>
            </div>
          </div>
        </div>
      </article>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "newMessage",
  data() {
    return {
      text: null,
    };
  },
  methods: {
    submit() {
      axios.post("/api/messages/add", {text: this.text}).then(() => {
        this.text = null;
        this.$emit('added');
      });
    }
  }
};
</script>
