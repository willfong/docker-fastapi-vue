<template>
  <div class="column is-8 is-offset-2">
    <div class="card">
      <div class="card-content">
        <h3 class="title is-3">“{{message.message}}”</h3>
        <p class="subtitle">{{message.name}}</p>
      </div>
      <footer class="card-footer">
        <p class="card-footer-item">
          <span>
            {{moment(fmtDate).fromNow()}}
          </span>
        </p>
        <p class="card-footer-item">
          <span>
            {{message}}
          </span>
        </p>
      </footer>
    </div>
  </div>
</template>

<script>
import moment from 'moment/moment';

export default {
  name: "Message",
  props: ["message"],
  computed: {
    fmtDate: function() {
      return moment.utc(this.message.created_at).fromNow();
    }
  },
};
</script>
