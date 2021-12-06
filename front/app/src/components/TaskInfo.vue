<template>
  <div>
    <div class="row">

        <div class="col-md-4 info" style="display: flex;">
          <card>
            <template slot="header">
              <h3>{{ this.data ? 'Редактирование' : 'Создание'}} задания</h3>
            </template>

            <h5>Название</h5>
            <input type="text" v-model="info.name">

            <h5>Описание</h5>
            <textarea placeholder="Описание задания" v-model="info.description"></textarea>

            <h5>Координаты</h5>
            <span class="subtext">Область сьемки задается координатами левого нижнего угла и длинной стороны квадрата в км</span>
            <div class="row">
              <div class="col-md-6">
                <input type="text" placeholder="lat" v-model="info.lat">
              </div>
              <div class="col-md-6">
                <input type="text" placeholder="long" v-model="info.long">
              </div>
            </div>

            <h5>Площадь съемки</h5>
            <input type="text" v-model="info.i_leng">

            <h5>Переодичность обновления (часов)</h5>
            <input type="number" v-model="info.pereodic">
            

            <button class="btn btn-success" @click="send">Сохранить</button>
          </card>
        </div>

        <div class="col-md-8">
          <card>
            <h4 slot="header" class="card-title">Область съемки</h4>
            <div class="row">
              <div class="col-md-12">

                <loader v-if="!isLoaded" />

                <yandex-map 
                  v-if="isLoaded"
                  :coords="coordMap"
                  :map-events="['click']"
                  zoom="8"
                  style="width: 100%; height: 400px;"
                  @boundschange="onMapMove"
                >

                    <ymap-marker 
                      marker-id="1"
                      marker-type="rectangle"
                      :coords="coordMarker"
                      :marker-fill="{color: '#049F0C', opacity: 0.2}"
                    ></ymap-marker>

                </yandex-map>

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
            <input type="text" v-model="this.info.sensetivity">
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
import { yandexMap, ymapMarker } from 'vue-yandex-maps'
import Loader from './loader.vue'

export default {
  name: 'TaskInfo',
  components: {
    Card,
    yandexMap, 
    ymapMarker,
    Loader
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
      mapInstance: null,
      isRect: false,
      info: {},
      preset: null,
      isLoaded: false,
    }
  },
  computed: {
    coordMap: {
      get() {
        return [
          +this.info.lat + ((this.info.i_leng / 2) / 110.574),
          +this.info.long + ((this.info.i_leng / 2) / (111.320 * Math.cos(this.info.lat)))
        ]
      },
      set([lat, long]) {
        console.log(lat, long)
        this.info.lat = lat - ((this.info.i_leng / 2) / 110.574)
        this.info.long = long - ((this.info.i_leng / 2) / (111.320 * Math.cos(this.info.lat)))
      }
    },
    coordMarker: {
      get: function() {
        return [
          [+this.info.lat, +this.info.long],
          [
            +this.info.lat + (this.info.i_leng / 110.574),
            +this.info.long + (this.info.i_leng / (111.320 * Math.cos(+this.info.lat)))
          ]
        ]
      },
      set: function([[lat, long]]) {
        this.info.lat = lat
        this.info.long = long
      }
    }
  },
  methods: {
    send() {
      this.$emit('send', Object.assign({}, this.info))
    },

    setPreset(preset) {
      this.preset = preset
      Object.assign(this.info, preset)
    },

    onMapMove(e) {
      this.coordMap = e.originalEvent.newCenter
    }
  },
  mounted() {
    if (this.data) {
      this.info = this.data
    } else {
      this.preset = PRESETS.LAND
      this.info = Object.assign({}, { name: '', description: '', pereodic: null, 
        lat: 54.62896654088406,
        long: 39.731893822753904,
        i_leng: 10
       }, PRESETS.LAND)
    }

    this.isLoaded = true
  }
}
</script>

<style lang="scss" scoped>
  input, textarea {
    border: 2px solid #87CB16;
    border-radius: 3px;
    padding: 5px 10px;
  }

  h5{
    margin-bottom: 10px;
  }

  textarea {
    padding: 10px;
  }

  .info input, .info textarea {
    width: 100%;
    margin-bottom: 20px;
  }

  .subtext{
    font-style: italic;
    opacity: 0.5;
    margin: 10px 0;
    display: block;
  }
</style>