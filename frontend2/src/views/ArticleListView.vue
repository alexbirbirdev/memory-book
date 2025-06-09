<script>
import axios from "axios";

import ArticleCard from "@/components/common/BaseArticle.vue";
import VButton from "@/components/form/VButton.vue";
import VNewsItemLoader from "@/components/loaders/VNewsItemLoader.vue";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";
export default {
  name: "ArticleListView",

  components: {
    ArticleCard,
    VBreadcrumds,
    VButton,
    VNewsItemLoader,
  },

  props: {},

  data() {
    return {
      articles: [],
      itemsPerPage: 6,
      currentPage: 1,

      isLoading: false,
    };
  },

  computed: {
    visiblearticle() {
      return this.articles.slice(0, this.currentPage * this.itemsPerPage);
    },
    canLoadMore() {
      return this.visiblearticle.length < this.articles.length;
    },
  },
  methods: {
    loadMore() {
      this.currentPage++;
    },
    async getArticles() {
      try {
        this.isLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/articles/`);

        this.articles = response.data.results
      } catch (error) {
        console.log(error);
      } finally {
        this.isLoading = false;
      }
    },
  },

  watch: {},

  created() {
    this.getArticles();
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

    <h1 class="text-3xl font-bold mb-6">Статьи</h1>
    <div
      v-if="!isLoading"
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
    >
      <ArticleCard
        v-for="article in visiblearticle"
        :key="article.id"
        :article="article"
      />
    </div>
    <div
      v-if="isLoading"
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
    >
      <VNewsItemLoader v-for="el in 6" :key="el" />
    </div>
    <div v-if="!isLoading && !articles.length">
      Список статей пуст!
    </div>

    <div v-if="canLoadMore" class="flex justify-center mt-10">
      <VButton @click="loadMore">Показать ещё</VButton>
    </div>
  </div>
</template>

<style scoped></style>
