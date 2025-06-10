<script>
export default {
  name: "BaseArticle",

  components: {},

  props: {
    article: {
      type: Object,
      required: true,
    },
  },

  data() {
    return {};
  },

  computed: {},

  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      const options = {
        hour: "2-digit",
        minute: "2-digit",
        day: "2-digit",
        month: "long",
        year: "numeric",
      };
      return date.toLocaleString("ru-RU", options);
    },

    formatImageUrl(url) {
      if (!url) return "";
      try {
        // Добавим схему, если её нет (на всякий случай)
        const hasProtocol =
          url.startsWith("http://") || url.startsWith("https://");
        const fullUrl = hasProtocol ? url : "http://" + url;

        const parsed = new URL(fullUrl);

        // Пропустим, если порт уже есть
        if (parsed.port) return parsed.toString();

        // Вставим порт 8100
        parsed.port = "8100";
        return parsed.toString();
      } catch (e) {
        // Если что-то пошло не так — вернём оригинал
        return url;
      }
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
    :to="'/articles/' + article.id"
    class="bg-white block rounded-2xl shadow hover:shadow-lg transition cursor-pointer overflow-hidden"
  >
    <!-- <img :src="article.image" alt="Превью" class="w-full h-48 object-cover" /> -->
    <div
      class="w-full aspect-video bg-cover bg-center"
      :style="{ backgroundImage: `url('${formatImageUrl(article.preview_image)}')` }"
    ></div>
    <div class="p-4 space-y-2">
      <p class="text-sm text-gray-500">
        {{ formatDate(article.publish_date) || "Дата не добавлена" }}
      </p>
      <h2 class="text-xl font-semibold line-clamp-2">
        {{ article.title || "Название не добавлено" }}
      </h2>
      <p class="text-gray-600 text-sm line-clamp-3">
        {{ article.short_description || "Описание не добавлено" }}
      </p>
    </div>
  </router-link>
</template>

<style scoped></style>
