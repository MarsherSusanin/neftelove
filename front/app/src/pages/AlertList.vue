<template>
  <task-board />

</template>

<script>
import Card from "../components/Cards/Card.vue";
import StatsCard from "../components/Cards/StatsCard.vue";
import LTable from "../components/Table.vue";
import TaskBoard from "../components/Task-board.vue";
import "/src/assets/css/style.css";

export default {
  components: {
    LTable,
    StatsCard,
    Card,
    TaskBoard,
  },
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
  computed: {
    taskList() {
      return {
        columns: [
          { key: "id", value: "#" },
          { key: "name", value: "Название" },
          { key: "last_date", value: "Последнее обновление" },
          { key: "next_date", value: "Следующее обновление" },
        ],
        data: [
          {
            id: 1,
            name: "Сызрань",
            last_date: "02.12.2021 16:03",
            next_date: "04.12.2021 16:00",
          },
          {
            id: 2,
            name: "Нефтеюганск",
            last_date: "01.12.2021 12:01",
            next_date: "05.12.2021 12:00",
          },
          {
            id: 3,
            name: "Алапаевск",
            last_date: "02.12.2021 11:00",
            next_date: "04.12.2021 11:00",
          },
        ],
      };
    },
  },
  methods: {
    onShow(id) {
      console.log(`/tasks/${id}`);
      this.$router.push(`/admin/tasks/${id}`);
    },
    onAdd() {
      this.$router.push(`/admin/tasks/add`);
    },
  },
};
</script>
<style lang="scss" scoped>
</style>
