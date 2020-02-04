<template>
  <v-container fill-height fluid>
    <v-col md="12" sm="12">
      <v-row justify="space-around">
        <div class="display-4 d-flex align-center">
          <p>Доска объявлений</p>
        </div>
        <v-card tile class="pa-6" max-width="500" width="500">
          <v-card-title>Авторизация</v-card-title>
          <v-card-text>
            <v-text-field v-model="username" label="Логин" />
            <v-text-field v-model="password" type="password" label="Пароль" />
            <v-btn color="success" block @click="login({username, password})">Войти</v-btn>
          </v-card-text>
        </v-card>
      </v-row>
    </v-col>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "login",
  data: () => ({
    username: "",
    password: ""
  }),
  methods: {
    ...mapActions(['login'])
  }
};
</script>
