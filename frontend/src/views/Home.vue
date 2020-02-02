<template>
  <div class="home">
    <p>home</p>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "home",
  data: () => ({
    // ...mapState(['user', 'isLoading'])
  }),
  methods: {
    ...mapActions(["getUser"])
  },

};
</script>
