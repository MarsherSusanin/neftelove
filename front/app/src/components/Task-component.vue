<template>
  <div class="taskboard__list">
    <div class="taskboard__item task" v-on:click="show()">
      <div class="task__body">
        <p class="task__view"><i class="nc-icon nc-spaceship"></i><strong> Задача:</strong> {{data.task.name}} <br /> <i class="nc-icon nc-alien-33"></i> <strong> Найдено:</strong> {{JSON.parse(JSON.parse(data.contours)).length}}</p>
        <input class="task__input" type="text" value="Название первой задачи" />
      </div>
      <button class="task__edit" type="button" aria-label="Изменить"></button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      todos: [],
    };
  },
  props: {
    data: Object,
  },
  methods: {
    show() {
        this.$router.push(`/admin/alerts/${this.data.id}`)
      },
  }
};
</script>