<template>
  <div class="content">
    <loader v-if="isLoading" />
    <task-board v-if="!isLoading" v-bind:list="alertList" />
  </div>
</template>

<script>
import Card from "../components/Cards/Card.vue";
import StatsCard from "../components/Cards/StatsCard.vue";
import LTable from "../components/Table.vue";
import TaskBoard from "../components/Task-board.vue";
import Loader from '../components/loader.vue'
import "/src/assets/css/style.css";

export default {
  components: {
    LTable,
    StatsCard,
    Card,
    TaskBoard,
    Loader
  },
  data() {
    return {
     alertList: [],
     isLoading: true
    };
  },
  computed: {
    
    
  },
  methods: {
    
  },
  mounted() {
    this.$store.dispatch('getAlerts')
        .then((list) => {
          this.alertList = list
          this.isLoading = false
        })
  }
};
</script>
<style lang="scss" scoped>
</style>
