<template>
  <div>
    <div class="row">

        <div class="col-md-4 info" style="display: flex;">
          <card>
            <template slot="header">
              <h3>{{ this.data ? 'Редактирование' : 'Создание'}} задания</h3>
            </template>

            <input type="text" placeholder="Название задания" v-model="info.name">

            <textarea placeholder="Описание задания" v-model="info.name"></textarea>

            <input type="number" placeholder="Переодичность обновления" v-model="info.pereodic">

            <button class="btn btn-success" @click="send">Сохранить</button>
          </card>
        </div>

        <div class="col-md-8">
          <card>
            <h4 slot="header" class="card-title">Область съемки</h4>
            <div class="row">
              <div class="col-md-12">
                <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3A3e8da3778c0d4821707b7a54d0f7d688d2cd4f34cfdd23517bc03fa71ada3255&amp;source=constructor" width="100%" height="464" frameborder="0"></iframe>
              </div>
            </div>
          </card>
        </div>

    </div>
    <div class="row">

      <div class="col-md-8" style="display: flex;">
        <card class="col-md-12">
          <h4 slot="header" class="card-title">Пресеты настроек</h4>

          <p>Выберете оптимальный набор настроек в зависимости от типа местности (рекомендуется)</p>
          
          <div class="row" style="margin-top: 150px">
            <div class="col-md-4">
              <button @click="function(){setPreset(this.PRESETS.LAND)}.bind(this)" :class="`btn ${this.preset == this.PRESETS.LAND ? 'btn-info' : 'btn-success'}`" style="width: 100%">Суша</button>
            </div>
            <div class="col-md-4">
              <button @click="function(){setPreset(this.PRESETS.RIVER)}.bind(this)" :class="`btn  ${this.preset == this.PRESETS.RIVER ? 'btn-info' : 'btn-success'}`" style="width: 100%">Река</button>
            </div>
            <div class="col-md-4">
              <button @click="function(){setPreset(this.PRESETS.SEA)}.bind(this)" :class="`btn  ${this.preset == this.PRESETS.SEA ? 'btn-info' : 'btn-success'}`" style="width: 100%">Море</button>
            </div>
          </div> 
        </card>
      </div>
      <div class="col-md-4" style="display: flex;">
        <card class="col-md-12">
          <h4 slot="header" class="card-title">Точные настройки</h4>

          <p>Или установите собственные настройки вручную</p>

          <fieldset>
            <h4>Спутник</h4>
            <label style="display: flex; justify-content: left"><input type="radio" @click="function(){this.info.name_sputnik = this.SATELLITES.SENTINEL_1}.bind(this)" :checked="this.info.name_sputnik == this.SATELLITES.SENTINEL_1"> <span> - {{ this.SATELLITES.SENTINEL_1 }}</span></label>
            <label style="display: flex; justify-content: left"><input type="radio" @click="function(){this.info.name_sputnik = this.SATELLITES.SENTINEL_2}.bind(this)" :checked="this.info.name_sputnik == this.SATELLITES.SENTINEL_2"> <span> - {{ this.SATELLITES.SENTINEL_2 }}</span></label>
          </fieldset>

          <fieldset>
            <h4>Sensitivity</h4>
            <input type="text" v-model="this.info.sensitivity">
          </fieldset>

          <fieldset>
            <h4>Maxcc</h4>
            <input type="text" v-model="this.info.maxcc">
          </fieldset>
        </card>
      </div>
    </div>

  </div>
</template>

<script>
import SATELLITES from '../enums/satellites'
import PRESETS from '../enums/task_config_presets'

import Card from '../components/Cards/Card.vue'

export default {
  name: 'TaskInfo',
  components: {
    Card
  },
  props: {
    data: {
      type: Object,
    }
  },
  data() {
    return {
      SATELLITES,
      PRESETS,
      info: {},
      preset: null,
      coord: {
        lat: null,
        long: null,
        iLeng: null
      }
    }
  },
  methods: {
    send() {
      this.$emit('send', Object.assign({}, this.info, this.coord))
    },

    setPreset(preset) {
      this.preset = preset
      Object.assign(this.info, preset)
    }
  },
  mounted() {
    if (this.data) {
      this.info = this.data
    } else {
      this.preset = PRESETS.LAND
      this.info = Object.assign({}, { name: '', desc: '', pereodic: null }, PRESETS.LAND)
    }
  }
}
</script>

<style lang="scss" scoped>
  .info input, .info textarea {
    width: 100%;
    margin-bottom: 20px;
  }
</style>