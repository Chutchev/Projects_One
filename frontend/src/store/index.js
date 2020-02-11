import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import router from "../router";

Vue.use(Vuex);
const api = axios.create({
  baseURL: "http://localhost:8000/api/"
});

const LOADING = "LOADING";
const AUTH_SUCCESS = "AUTH_SUCCESS";

export default new Vuex.Store({
  state: {
    token: localStorage.getItem("token") || "",
    isLoading: false,
    user: {}
  },
  mutations: {
    [LOADING]: (state, value) => {
      console.log(`[LOADING]: ${value}`);
      state.isLoading = value;
    },
    [AUTH_SUCCESS]: (state, value) => {
      console.log(`[AUTH_SUCCESS]: ${value}`);
      state.token = value;
    }
  },
  actions: {
    async login({ state, commit, dispatch }, payload) {
      commit(LOADING, true);
      const resp = await api.post("/board/auth/", payload);
      const token = resp.data.token;
      localStorage.setItem("token", token);
      commit(LOADING, false);
      commit(AUTH_SUCCESS, token);
      dispatch("getUser");
      router.push("/");
    },
    async getUser({ state, commit }) {
      commit(LOADING, true);
      const token = localStorage.getItem("token");
      if (token) {
        let response = await api.get("/me", {
          headers: {
            Authorization: `Token ${token}`
          }
        });
        commit(LOADING, false);
        state.user = { ...response.data };
      } else {
        router.push("/login");
      }
    },
    async updateUser({ state, commit, dispatch }, payload) {
      commit(LOADING, true);
      const token = localStorage.getItem("token");
      if (token) {
        await api.put("/me/", payload, {
          headers: {
            Authorization: `Token ${token}`
          }
        });
        dispatch("getUser");
        commit(LOADING, false);
      } else {
        router.push("/login");
      }
    }
  },
  modules: {}
});
