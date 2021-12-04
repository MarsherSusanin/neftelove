import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


const API = "http://api.holodec.loc/"


Vue.use(Vuex)

export default new Vuex.Store({
  state: {

  },
  mutations: {

  },
  actions: {
    getTasks () {
      return axios({
        method: 'get',
        url: `${API}tasks`,
      })
      .then(response => response.data)
    },
    setTask ({}, data) {
      return axios({
        method: 'post',
        url: `${API}tasks`,
        data: JSON.stringify(data)
      })
      .then(response => response.data)
    },
  }
})
