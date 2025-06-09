<script>
import axios from "axios";
import NewsCard from "@/components/common/NewsCard.vue";
import VButton from "@/components/form/VButton.vue";
import VNewsItemLoader from "@/components/loaders/VNewsItemLoader.vue";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";
export default {
  name: "NewsListView",

  components: {
    NewsCard,
    VBreadcrumds,
    VButton,
    VNewsItemLoader,
  },

  props: {},

  data() {
    return {
      visibleCount: 10,
      newsList: [],
      isLoading: false,
    };
  },

  computed: {
    sortedNews() {
      return [...this.newsList].sort(
        (a, b) => new Date(b.date) - new Date(a.date)
      );
    },
    visibleNews() {
      return this.sortedNews.slice(0, this.visibleCount);
    },
  },

  methods: {
    loadMore() {
      this.visibleCount += 10;
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleString("ru-RU", {
        hour: "2-digit",
        minute: "2-digit",
        day: "2-digit",
        month: "long",
        year: "numeric",
      });
    },
    async getNews() {
      try {
        this.isLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/news/`);

        this.newsList = response.data.results;
        // console.log(response.data.results);
      } catch (error) {
        console.log(error);
      } finally {
        this.isLoading = false;
      }
    },
  },

  watch: {},

  created() {
    this.getNews();
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
    <h1 class="text-3xl font-bold mb-6">Новости</h1>

    <div
      v-if="!isLoading"
      class="grid gap-4 sm:gap-6 sm:grid-cols-2 lg:grid-cols-3"
    >
      <NewsCard
        v-for="news in newsList"
        :key="news.id"
        :news="news"
        :link="`/news/${news.id}`"
      />
    </div>

    <div
      v-if="isLoading"
      class="grid gap-4 sm:gap-6 sm:grid-cols-2 lg:grid-cols-3"
    >
      <VNewsItemLoader v-for="news in 6" :key="news" />
    </div>
    <div v-if="!isLoading && !newsList.length">Список новостей пуст!</div>

    <div
      class="text-center mt-8"
      v-if="visibleCount < newsList.length && !isLoading"
    >
      <VButton @click="loadMore">Показать ещё</VButton>
    </div>
  </div>
</template>

<style scoped></style>
