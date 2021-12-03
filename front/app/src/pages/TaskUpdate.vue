<template>
  <div class="content">
    <div class="container-fluid">
      
      <task-info @send="onSend" :data="info" />

     
    </div>
  </div>
</template>

<script>
import TaskInfo from '../components/TaskInfo.vue'

  export default {
    components: {
        TaskInfo
    },
    computed: {
      info() {
        return {
          name: 'Алапаевск',
          desc: 'короткое описание задачи',
          name_sputnik: SATELLITES.SENTINEL_1,
          contour_line_width: 2,
          sensitivity: 70,
          maxcc: 20,
        }
      }
    },
    methods: {
      onSend(data) {

      }
    }
  }
</script>

<style>
  
</style>
