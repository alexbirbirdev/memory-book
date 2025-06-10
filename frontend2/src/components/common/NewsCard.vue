<script>
export default {
  name: "NewsCard",

  components: {},

  props: {
    news: {
      type: Object,
      required: true,
    },
    link: {
      type: String,
      required: true,
    },
  },

  data() {
    return {};
  },

  computed: {
    formattedDate() {
      const date = new Date(this.news.publish_date);
      return date.toLocaleString("ru-RU", {
        hour: "2-digit",
        minute: "2-digit",
        day: "2-digit",
        month: "long",
        year: "numeric",
      });
    },
  },

  methods: {},

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
    :to="link"
    class="cursor-pointer rounded-lg overflow-hidden shadow hover:shadow-lg transition"
  >
    <div
      class="w-full aspect-video bg-cover bg-center"
      :style="'background-image: url(' + $formatImageUrl(news.preview_image) + ');'"
    ></div>
    <div class="p-4">
      <p class="text-sm text-gray-500">{{ formattedDate || "Дата не добавлена" }}</p>
      <h2 class="text-xl font-semibold line-clamp-2">{{ news.title || "Название не добавлено" }}</h2>
      <p class="text-gray-600 text-sm line-clamp-3">{{ news.short_description || "Описание не добавлено" }}</p>
    </div>
  </router-link>
</template>

<style scoped></style>
