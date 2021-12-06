<template>
  <div class="content">
    <loader v-if="isLoading" />
    <div v-if="!isLoading" class="container-fluid">
      <h2>Активные задания:</h2>
      <div class="row">

        <div class="col-xl-4 col-md-6" style="display: flex">
            <div class="add" v-on:click="add">
              <i class="far fa-plus-square"></i>
            </div>
        </div>

        <div 
          class="col-xl-4 col-md-6"
          v-for="task of taskList"
          v-bind:key="task.id"
        >
          <card>
            <h4
              v-on:click="show(task.id)"
            >{{ task.name }}</h4>
            <hr>

            <i 
              class="far fa-minus-square delete"
              id="del"
              v-on:click="deleteTask(task.id)"
              ></i>

            <p class="desc">{{ task.description }}</p>

            <div class="map-container">
              <div class="map">
                <yandex-map 
                    :settings="yamapSettings"
                    :coords="[]"
                    :bounds="[[54.62896654088406, 39.731893822753904], [54.92896664088406, 40.231893832753904]]"
                    :controls="[]"
                    :scroll-zoom="false"
                    zoom="8"
                    style="width: 300px; height: 300px;"
                  ></yandex-map>
                </div>
            </div>

            <hr>
            <p class="card-footer" slot="footer"><i class="fa fa-satellite"></i> {{ task.name_sputnik }}</p>
          </card>
        </div>


        <div class="col-xl-4 col-md-6">
          
        </div>

      </div>

    </div>
  </div>
</template>

<script>
  import Card from '../components/Cards/Card.vue'
  import { yandexMap, ymapMarker } from 'vue-yandex-maps'
  import Loader from '../components/loader.vue'

  export default {
    components: {
      Card,
      yandexMap,
      ymapMarker,
        Loader
    },
    data () {
      return {
        taskList: [],
        isLoading: true
      }
    },
    methods: {
      show(id) {
        console.log(`/tasks/${id}`)
        this.$router.push(`/admin/tasks/${id}`)
      },
      add() {
        this.$router.push(`/admin/tasks/add`)
      },
      deleteTask(id) {
        this.isLoading = true;
        this.$store.dispatch('deleteTask', id)
        .then(() => {
          this.taskList = this.taskList.filter(item => item.id !== id)
          this.isLoading = false
        })
      }
    },
    computed: {
      yamapSettings() { return this.$store.getters.yamapSettings }
    },
    mounted() {
      this.$store.dispatch('getTasks')
        .then((list) => {
          this.taskList = list
          this.isLoading = false
        })
    }
  }
</script>

<style lang="scss" scoped>
  h2{
    margin-bottom: 30px;
  }

  .card {

    h4{
      cursor: pointer;
    }

    .desc{
      text-align: center;
      font-style: italic;
      color: rgba(0, 0, 0, 0.7);
      margin-bottom: 20px;
    }

    &:hover{
      //background-color: rgba(219, 239, 239, 0.06);
      box-shadow: 0 0 10px #ccc;
    }
  }

  .card-header{
    background-color: transparent;
  }

  .card-footer{
    color: #ccc;
    text-align: right;
    text-transform: uppercase;
  }

  .map-container{
    display: flex;
    justify-content: center;
    height: 300px;
  }

  .map{
    width: 300px;
    height: 300px;
    box-shadow: 0 0 10px #ccc;
  }

  .add{
    font-size: 120px;
    text-align: center;
    vertical-align: center;
    width: 100%;
    color: #87CB16;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    border: 1px solid #87CB16;
    border-radius: 3px;
    margin-bottom: 30px;
    padding: 100px 0;

    &:hover{
      opacity: 0.5;
      box-shadow: 0 0 10px #87CB16;
    }
  }

  .delete{
    position: absolute;
    top: 20px;
    right: 20px;
    color: #FF4A55;
    font-size: 23px;
    display: block;

    &:hover{
      opacity: 0.5;
    }
  }
</style>
