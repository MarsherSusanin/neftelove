<template>
  <!-- // верстка для 3х столбца - новые, действия, архив, 
// img, картика с границ, площадь, когда, где, статус -->

  <section class="taskboard">
    <h2 class="visually-hidden">Ваши задачи:</h2>
    <article class="taskboard__group taskboard__group--backlog">
      <h3 class="taskboard__group-heading taskboard__group-heading--backlog">
        Бэклог
      </h3>
      <div class="taskboard__list">
        <div class="taskboard__item task task--active">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="taskboard__item task">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="taskboard__item task">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="taskboard__item task">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="taskboard__item task">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
      </div>
    </article>
    <article class="taskboard__group taskboard__group--processing">
      <h3 class="taskboard__group-heading taskboard__group-heading--processing">
        В процессе
      </h3>
      <div class="taskboard__list taskboard__list--sorted">
        <div class="taskboard__item task task--empty">
          <p>Перетащите карточку</p>
        </div>
        <div class="taskboard__item task task--processing task--active">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="taskboard__item task task--processing">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="taskboard__item task task--processing">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
      </div>
      <div class="taskboard__item task task--processing">
        <div class="task__body">
          <p class="task__view">Название первой задачи</p>
          <input
            class="task__input"
            type="text"
            value="Название первой задачи"
          />
        </div>
        <button class="task__edit" type="button" aria-label="Изменить"></button>
      </div>
    </article>
    <article class="taskboard__group taskboard__group--done">
      <h3 class="taskboard__group-heading taskboard__group-heading--done">
        Готово
      </h3>
      <div class="taskboard__list taskboard__list--sorted">
        <div class="taskboard__item task task--empty">
          <p>Перетащите карточку</p>
        </div>
        <div class="taskboard__item task task--done task--active">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="taskboard__item task task--processing">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
      </div>
    </article>
    <article class="taskboard__group taskboard__group--basket">
      <h3 class="taskboard__group-heading taskboard__group-heading--basket">
        Корзина
      </h3>
      <div class="taskboard__list taskboard__list--trash">
        <div class="taskboard__item task task--basket task--active">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="taskboard__item task task--basket">
          <div class="task__body">
            <p class="task__view">Название первой задачи</p>
            <input
              class="task__input"
              type="text"
              value="Название первой задачи"
            />
          </div>
          <button
            class="task__edit"
            type="button"
            aria-label="Изменить"
          ></button>
        </div>
        <div class="task--empty task task--empty-trash">
          <p>Корзина пуста</p>
        </div>
      </div>
      <button class="taskboard__button button button--clear" type="button">
        <svg
          width="22"
          height="22"
          viewBox="0 0 22 22"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <rect
            x="15.5374"
            y="5.16638"
            width="1.83333"
            height="14.6667"
            transform="rotate(45 15.5374 5.16638)"
            fill="white"
          />
          <rect
            x="16.8337"
            y="15.5372"
            width="1.83333"
            height="14.6667"
            transform="rotate(135 16.8337 15.5372)"
            fill="white"
          />
        </svg>
        <span>Очистить</span>
      </button>
    </article>
  </section>
</template>

<script>
import Card from "../components/Cards/Card.vue";
import StatsCard from "../components/Cards/StatsCard.vue";
import LTable from "../components/Table.vue";
import "/src/assets/css/style.css";

export default {
  components: {
    LTable,
    StatsCard,
    Card,
  },
  data() {
    return {
      Status: {
        BACKLOG: `backlog`,
        PROCESSING: `processing`,
        DONE: `done`,
        BASKET: `basket`,
      },
    };
  },
  computed: {
    taskList() {
      return {
        columns: [
          { key: "id", value: "#" },
          { key: "name", value: "Название" },
          { key: "last_date", value: "Последнее обновление" },
          { key: "next_date", value: "Следующее обновление" },
        ],
        data: [
          {
            id: 1,
            name: "Сызрань",
            last_date: "02.12.2021 16:03",
            next_date: "04.12.2021 16:00",
          },
          {
            id: 2,
            name: "Нефтеюганск",
            last_date: "01.12.2021 12:01",
            next_date: "05.12.2021 12:00",
          },
          {
            id: 3,
            name: "Алапаевск",
            last_date: "02.12.2021 11:00",
            next_date: "04.12.2021 11:00",
          },
        ],
      };
    },
  },
  methods: {
    onShow(id) {
      console.log(`/tasks/${id}`);
      this.$router.push(`/admin/tasks/${id}`);
    },
    onAdd() {
      this.$router.push(`/admin/tasks/add`);
    },
  },
};
</script>
<style lang="scss" scoped>
</style>
