<template>
  <div class="taskboard__list">
    <div class="taskboard__item task">
      <div class="task__body">
        <p class="task__view">Название первой задачи</p>
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
    group: String,
  },
};
</script>