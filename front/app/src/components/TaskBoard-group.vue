<template>
  <article :class="`taskboard__group taskboard__group--${this.group}`">
    <card>
    <h3
      slot="header"
      :class="`taskboard__group-heading taskboard__group-heading--${this.group}`"
    >
      {{ group }}
    </h3>
    
      <task-component v-for="item of list" :key="item.id" :data="item" />
    </card>
  </article>
</template>

<script>
import Card from './Cards/Card.vue';
import TaskComponent from "./Task-component.vue";

export default {
  components: { TaskComponent, Card },
  data() {
    return {
      todos: [],
    };
  },
  props: {
    group: String,
    list: Array
  },
};
</script>