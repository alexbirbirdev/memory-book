<script>
import axios from "axios";
import EventView from "@/components/common/EventItem.vue";
import VNewsItemLoader from "@/components/loaders/VNewsItemLoader.vue";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";
export default {
  name: "EventsView",

  components: { EventView, VBreadcrumds, VNewsItemLoader },

  props: {},

  data() {
    return {
      description:
        "Добро пожаловать в раздел мероприятий! Здесь вы можете найти анонсы будущих событий и узнать подробности о прошедших мероприятиях.",
      visibleCount: 10,
      events: [],
      isLoading: false,
    };
  },

  computed: {},

  methods: {
    async getEvents() {
      try {
        this.isLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/events/`);

        this.events = response.data.results;
      } catch (error) {
        console.log(error);
      } finally {
        this.isLoading = false;
      }
    },
  },

  watch: {},

  created() {
    this.getEvents();
  },
  mounted() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<template>
  <div class="container mx-auto px-4">
    <VBreadcrumds />
    <div class="space-y-6">
      <!-- Заголовок -->
      <h1 class="text-3xl font-bold">Мероприятия</h1>

      <!-- Блок описания (редактируемый из админки) -->
      <div class="text-gray-700 text-base">
        {{ description }}
      </div>

      <!-- Список карточек мероприятий -->
      <div
        v-if="!isLoading && events.length"
        class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3"
      >
        <EventView v-for="event in events" :key="event" :event="event" />
      </div>
      <div
        v-if="isLoading"
        class="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3"
      >
        <VNewsItemLoader v-for="el in 6" :key="el" />
      </div>
      <div v-if="!isLoading && events.length == 0">
        Нет доступных мероприятий
      </div>

      <!-- Показать ещё -->
      <div
        v-if="visibleCount < events.length && !isLoading"
        class="text-center mt-6"
      >
        <button
          @click="loadMore"
          class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
        >
          Показать больше
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
