<template>
  <div class="content">
    <div class="container-fluid">
      <div class="row">
        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-primary">
              <i class="nc-icon nc-spaceship text-success"></i>
            </div>
            <div slot="content">
              <p class="card-category">Активные задания</p>
              <h4 class="card-title">5</h4>
            </div>
            <div slot="footer">
              <i class="fa fa-external-link"></i> Управление заданиями
            </div>
          </stats-card>
        </div>
        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-warning">
              <i class="nc-icon nc-alien-33 text-warning"></i>
            </div>
            <div slot="content">
              <p class="card-category">Новые события</p>
              <h4 class="card-title">43</h4>
            </div>
            <div slot="footer">
              <i class="fa fa-eye"></i> Просмотреть
            </div>
          </stats-card>
        </div>
        <div class="col-xl-4 col-md-6">
          <stats-card>
            <div slot="header" class="icon-danger">
              <i class="nc-icon nc-explore-2 text-danger"></i>
            </div>
            <div slot="content">
              <p class="card-category">Происшествия</p>
              <h4 class="card-title">1</h4>
            </div>
            <div slot="footer">
              <i class="fa fa-eye"></i> Просмотреть
            </div>
          </stats-card>
        </div>
      </div>

      <div class="row">
        <div class="col-md-12">
          <card>
            <h4 slot="header" class="card-title">Карта событий</h4>
            <div class="row">
              <div class="col-md-12">
                <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A3e8da3778c0d4821707b7a54d0f7d688d2cd4f34cfdd23517bc03fa71ada3255&amp;source=constructor" width="100%" height="464" frameborder="0"></iframe>
              </div>
            </div>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import StatsCard from '../components/Cards/StatsCard.vue'

  export default {
    components: {
      StatsCard
    },
    data () {
      return {
        
      }
    }
  }
</script>
<style>

</style>
