<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">

        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-success">
              <i class="nc-icon nc-spaceship text-success"></i>
            </div>
            <div slot="content">
              <p class="card-category">Активные задания</p>
              <h4 class="card-title">5</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-info">
              <i class="nc-icon nc-spaceship text-info"></i>
            </div>
            <div slot="content">
              <p class="card-category">Выполненные задания</p>
              <h4 class="card-title">5</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-secondary">
              <i class="nc-icon nc-spaceship text-secondary"></i>
            </div>
            <div slot="content">
              <p class="card-category">Архив заданий</p>
              <h4 class="card-title">5</h4>
            </div>
          </stats-card>
        </div>

      </div>

      <div class="row">
        <div class="col-md-12">
          <card>
            <template slot="header">
              <h3>Задания</h3>

              <button class="btn btn-success" @click="onAdd"><i class="fa fa-plus"></i> Создать задание</button>
            </template>

            <l-table class="table-hover table-striped"
                     :columns="taskList.columns"
                     :data="taskList.data"
                     @show="onShow">
            </l-table>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Card from '../components/Cards/Card.vue'
  import StatsCard from '../components/Cards/StatsCard.vue'
  import LTable from '../components/Table.vue'

  export default {
    components: {
      LTable,
      StatsCard,
      Card
    },
    data () {
      return {
        taskList: {
          columns: [{key:'id', value:'#'}, {key:'name', value:'Название'}, {key:'last_date', value:'Последнее обновление'}, {key:'next_date', value:'Следующее обновление'}],
          data: []
        }
      }
    },
    methods: {
      onShow(id) {
        console.log(`/tasks/${id}`)
        this.$router.push(`/admin/tasks/${id}`)
      },
      onAdd() {
        this.$router.push(`/admin/tasks/add`)
      }
    },
    mounted() {
      this.$store.dispatch('getTasks')
        .then((list) => {
          this.taskList.data = list
        })
    }
  }
</script>
<style lang="scss" scoped>
  
</style>
