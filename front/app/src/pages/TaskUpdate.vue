<template>
  <div class="content">
    <div class="container-fluid">
      
      <task-info v-if="!isLoading" @send="onSend" :data="taskInfo" />
      <loader v-if="isLoading" />
     
    </div>
  </div>
</template>

<script>
import TaskInfo from '../components/TaskInfo.vue'
import Loader from '../components/loader.vue'

  export default {
    components: {
        TaskInfo,
        Loader
    },
    data() {
      return {
          isLoading: true,
          taskInfo: {}
      }
    },
    methods: {
      onSend(data) {
        this.isLoading = true
        this.$store.dispatch('updateTask', data)
          .then(() => {
            this.isLoading = false
          })
      }
    },
    mounted() {
      this.$store.dispatch('getTask', this.$route.params.id)
        .then((info) => {
          this.taskInfo = info
          this.isLoading = false
        })
    }
  }
</script>

<style>
  
</style>
