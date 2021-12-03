<template>
  <div class="content">
    <div class="container-fluid">
      
      <task-info @send="onSend" />

     
    </div>
  </div>
</template>

<script>
import TaskInfo from '../components/TaskInfo.vue'

  export default {
    components: {
        TaskInfo
    },
    methods: {
      onSend(data) {

      }
    }
  }
</script>

<style>
  
</style>
