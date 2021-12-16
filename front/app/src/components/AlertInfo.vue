<template>
  <div>
    <div class="row">
      <div class="col-md-12 info" style="display: flex;">
          <card>
            <h3 slot="header">Результаты анализа спутникового снимка по заданию "{{ info.task.name }}"</h3>
            <ul>
              <li><strong>Дата проведения: </strong>{{ info.created_at }}</li>
              <li><strong>Количество потенциальных разливов: </strong>{{JSON.parse(JSON.parse(info.contours)).length + JSON.parse(JSON.parse(info.contours)).length}}</li>
            </ul>
          </card>
      </div>
    </div>
    <div class="row">

        <div class="col-md-6 info" style="display: flex;">
          <card>
            <img :src="`data:image/png;base64,${info.image}`" />
          </card>
        </div>

        <div class="col-md-6 info" style="display: flex;">
          <card>
            <img :src="`data:image/png;base64,${info.result_image}`" />
          </card>
        </div>

    </div>

  </div>
</template>

<script>
import Card from '../components/Cards/Card.vue'
import Loader from './loader.vue'

export default {
  name: 'AlertInfo',
  components: {
    Card,
    Loader
  },
  props: {
    data: {
      type: Object,
    }
  },
  data() {
    return {
      info: {}
    }
  },
  computed: {
    
  },
  methods: {
    send() {
      this.$emit('send', Object.assign({}, this.info))
    }
  },
  mounted() {
    this.info = this.data
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