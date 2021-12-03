<template>
  <section class="taskboard">
    <h2 class="visually-hidden">Ваши задачи:</h2>
    <taskBoard-group
      v-for="(group, i) of this.Status"
      v-bind:index="i"
      :key="i"
      :group="group"
    />
  </section>
</template>

<script>
import TaskBoardGroup from "./TaskBoard-group.vue";
export default {
  components: { TaskBoardGroup },
  data() {
    return {
      Status: {
        BACKLOG: `backlog`,
        PROCESSING: `processing`,
        DONE: `done`,
        BASKET: `basket`,
      },
    };
  },
 
};
</script>