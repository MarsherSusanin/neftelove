<template>
  <div class="content">
    <div class="container-fluid">
      
      <alert-info v-if="!isLoading" @send="onSend" :data="alertInfo" />
      <loader v-if="isLoading" />
     
    </div>
  </div>
</template>

<script>
import AlertInfo from '../components/AlertInfo.vue'
import Loader from '../components/loader.vue'

  export default {
    components: {
        AlertInfo,
        Loader
    },
    data() {
      return {
          isLoading: true,
          alertInfo: {}
      }
    },
    methods: {
      onSend(data) {
        this.isLoading = true
        this.$store.dispatch('updateAlert', data)
          .then(() => {
            this.isLoading = false
          })
      }
    },
    mounted() {
      this.$store.dispatch('getAlert', this.$route.params.id)
        .then((info) => {
          this.alertInfo = info
          this.isLoading = false
        })
    }
  }
</script>

<style>
  
</style>
