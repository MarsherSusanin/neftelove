import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


const API = "http://api.neftelove.pena.marketing/"


Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    yamapSettings: {
      apiKey: '8b947c34-afb2-44d8-b610-da8972b2976c',
      lang: 'ru_RU',
      coordorder: 'latlong',
      enterprise: false,
      version: '2.1'
    }
  },
  getters: {
    yamap_settings: (state) => state.yamapSettings
  },
  mutations: {

  },
  actions: {
    getAlerts () {
      return axios({
        method: 'get',
        url: `${API}alerts`,
      })
      .then(response => response.data)
    },
    getAlert ({}, id) {
      return axios({
        method: 'get',
        url: `${API}alerts/${id}`,
      })
      .then(response => response.data)
    },
    updateAlert ({}, data) {
      return axios({
        method: 'patch',
        url: `${API}alerts/${data.id}`,
        data: JSON.stringify(data)
      })
      .then(response => response.data)
    },
    getTasks () {
      return axios({
        method: 'get',
        url: `${API}tasks`,
      })
      .then(response => response.data)
    },
    getTask ({}, id) {
      return axios({
        method: 'get',
        url: `${API}tasks/${id}`,
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
    updateTask ({}, data) {
      return axios({
        method: 'patch',
        url: `${API}tasks/${data.id}`,
        data: JSON.stringify(data)
      })
      .then(response => response.data)
    },
    deleteTask ({}, id) {
      return axios({
        method: 'delete',
        url: `${API}tasks/${id}`,
      })
      .then(response => response.data)
    },
  }
})
