import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import router from "../router";

Vue.use(Vuex);
const api = axios.create({
  baseURL: "http://localhost:8000/api/"
});

export default new Vuex.Store({
  state: {
    token: "",
    isLoading: false,
    user: {}
  },
  mutations: {
    loading: (state, value) => {
      console.log(`isLoading: ${value}`);
      state.isLoading = value;
    }
  },
  actions: {
    async login({ state, commit }, payload) {
      commit("loading", true);
      let response = await api.post("/board/auth/", payload);
      commit("loading", false);
      const token = response.data.token;
      localStorage.setItem("token", token);
      router.push("/");
      return state;
    },
    async getUser({ state, commit }) {
      const token = localStorage.getItem("token");
      commit("loading", true);
      let response = await api.get("/me", {
        headers: {
          Authorization: `Token ${token}`
        }
      });
      commit("loading", false);
      state.user = { ...response.data };
    }
  },
  modules: {}
});
