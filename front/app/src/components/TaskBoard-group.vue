<template>
  <article :class="`taskboard__group taskboard__group--${this.group}`">
    <h3
      :class="`taskboard__group-heading taskboard__group-heading--${this.group}`"
    >
      {{ group }}
    </h3>
    <task-component />
    <task-component />
    <task-component />
  </article>
</template>

<script>
import TaskComponent from "./Task-component.vue";
import tasks from "./data";

export default {
  components: { TaskComponent },
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