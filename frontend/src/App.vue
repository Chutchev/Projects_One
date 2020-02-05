<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>Project One</v-toolbar-title>
      <v-spacer></v-spacer>
      <div v-if="user">
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn text v-on="on">{{ user.username }}</v-btn>
          </template>
          <v-list>
            <v-list-item v-for="(item, index) in items" :key="index" :to="item.link" link>
              <v-list-item-title>{{ item.key }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
      <v-btn outlined text v-else>Войти</v-btn>
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
    items: [{ key: "Настройки", link: '/settings' }, { key: "Выход", link: '/logout' }]
  }),
  computed: {
    ...mapState(["user", "isLoading"])
  },
  methods: {
    ...mapActions(["getUser"])
  },
  created() {
    this.getUser();
    console.log(this);
  }
};
</script>
