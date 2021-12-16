<template>
  <section class="taskboard">
    <h2 class="visually-hidden">Ваши задачи:</h2>
    <taskBoard-group
      v-for="(group, i) of this.stacks"
      v-bind:index="i"
      :key="i"
      :group="group.title"
      :list="list.filter((item) => item.status == group.status)"
    />
  </section>
</template>

<script>
import TaskBoardGroup from "./TaskBoard-group.vue";
export default {
  components: { TaskBoardGroup },
  props: ['list'],
  data() {
    return {
      stacks: {
        BACKLOG: {
          title: `Не обработанные`,
          status: 'pending'
        },
        APPROVED: {
          title: `Подтвержденные`,
          status: 'resolved'
        },
        BASKET: {
          title: `Не подтвержденные`,
          status: 'rejected'
        }
      },
    };
  },
 
};
</script>