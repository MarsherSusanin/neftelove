<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">

        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-success">
              <i class="nc-icon nc-explore-2 text-danger"></i>
            </div>
            <div slot="content">
              <p class="card-category">Активные происшествия</p>
              <h4 class="card-title">5</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-info">
              <i class="nc-icon nc-explore-2 text-success"></i>
            </div>
            <div slot="content">
              <p class="card-category">Устраненные происшествия</p>
              <h4 class="card-title">5</h4>
            </div>
          </stats-card>
        </div>

        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-secondary">
              <i class="nc-icon nc-explore-2 text-secondary"></i>
            </div>
            <div slot="content">
              <p class="card-category">Архив происшествий</p>
              <h4 class="card-title">5</h4>
            </div>
          </stats-card>
        </div>

      </div>

      <div class="row">
        <div class="col-md-12">
          <card>
            <template slot="header">
              <h3>Происшествия</h3>
            </template>

            <l-table class="table-hover table-striped"
                     :columns="materialList.columns"
                     :data="materialList.data"
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
        
      }
    },
    computed: {
      materialList() {
        return  {
          columns: [{key:'id', value:'#'}, {key:'name', value:'место'}, {key:'date', value:'Дата начала'}, {key:'danger', value:'Потенциальный ущерб'}, {key:'status', value:'Статус'}],
          data: [{
            id: 1,
            name: 'Нефтеюганск',
            date: '02.12.2021',
            danger: 'Высокий',
            status: 'Обнаружен'
          },
          {
            id: 2,
            date: '02.12.2021',
            name: 'Анадырь',
            danger: 'Очень высокий',
            status: 'Уточнение данных'
          },
          {
            id: 3,
            name: 'Урюпинск',
            date: '02.12.2021',
            danger: 'Средний',
            status: 'Устранение'
          }]
        }
      }
    },
    methods: {
      onShow(id) {
        this.$router.push(`/admin/materials/${id}`)
      }
    }
  }
</script>
<style lang="scss" scoped>
  
</style>
