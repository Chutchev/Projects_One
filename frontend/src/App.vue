<template>
  <v-app v-if="isLoading">
    <v-content>
      <v-container fill-height fluid>
        <v-row align="center" justify="center">
          <v-col class="text-center">
            <v-progress-circular size="50" color="primary" indeterminate></v-progress-circular
          ></v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>

  <v-app v-else>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Project One</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn text v-on="on">{{ user.username }}</v-btn>
        </template>
        <v-list>
          <v-list-item v-for="item in items" :key="item.key" to="/settings">
            <v-list-item-title>{{ item.key }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <v-content>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "App",
  data: () => ({
    items: [{ key: "Настройки" }, { key: "Выход" }]
  }),
  computed: {
    ...mapState(["user", "isLoading"])
  },
  methods: {
    ...mapActions(["getUser"])
  },
  mounted() {
    this.getUser();
  }
};
</script>
