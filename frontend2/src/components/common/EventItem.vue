<script>
export default {
  name: "EventItem",

  components: {},

  props: {
    event: Object,
    require: true,
  },

  data() {
    return {};
  },

  computed: {},

  methods: {
    formatDateTime(dateStr) {
      const options = {
        hour: "2-digit",
        minute: "2-digit",
        day: "2-digit",
        month: "long",
        year: "numeric",
      };
      return new Date(dateStr).toLocaleString("ru-RU", options);
    },
  },

  watch: {},

  created() {},
  mounted() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<template>
  <router-link
    :to="'/events/' + event.id"
    class="cursor-pointer rounded-lg overflow-hidden shadow hover:shadow-lg transition"
  >
    <!-- Картинка -->
    <img
      :src="event.preview_image"
      alt="Превью"
      class="w-full aspect-video object-cover"
    />

    <div class="p-4 space-y-2">
      <!-- Дата и время -->
      <div class="text-sm text-gray-500">
        <span class="block">С {{ formatDateTime(event.start_date) }}</span>
        <span class="block">По {{ formatDateTime(event.end_date) }}</span>
      </div>

      <!-- Статус и формат -->
      <div class="flex flex-wrap gap-2 text-xs">
        <span class="px-2 py-1 rounded bg-gray-200 text-gray-700">
          {{ event.status == "in_progress" ? "В процессе" : "" }}
          {{ event.status == "completed" ? "Завершено" : "" }}
          {{ event.status == "planned" ? "Запланировано" : "" }}
        </span>
        <span class="px-2 py-1 rounded bg-blue-100 text-blue-700">
          {{ event.format == "online" ? "Онлайн" : "" }}
          {{ event.format == "offline" ? "Оффлайн" : "" }}
          {{ event.format == "hybrid" ? "Гибридный" : "" }}
        </span>
      </div>

      <!-- Заголовок -->
      <h2 class="text-lg font-semibold line-clamp-1">
        {{ event.title }}
      </h2>

      <!-- Краткое описание -->
      <p class="text-sm text-gray-600 line-clamp-1">
        {{ event.short_description }}
      </p>
    </div>
  </router-link>
</template>

<style scoped></style>
