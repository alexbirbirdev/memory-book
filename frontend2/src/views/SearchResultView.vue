<script>
import VButton from "@/components/form/VButton.vue";
import VLoader from "@/components/loaders/VLoader.vue";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";

export default {
  name: "SearchResult",

  components: { VBreadcrumds, VLoader, VButton },

  props: {},

  data() {
    return {
      results: [
        // Пример данных. В реальном проекте — заменяется результатами поиска.
        {
          id: 1,
          title: "Название статьи 1",
          description: "Краткое описание материала 1",
          date: "2024-01-10",
        },
        {
          id: 2,
          title: "Название статьи 2",
          description: "Краткое описание материала 2",
          date: "2024-03-15",
        },
        {
          id: 3,
          title: "Название статьи 3",
          description: "Краткое описание материала 3",
          date: "2024-05-20",
        },
        {
          id: 4,
          title: "Название статьи 4",
          description: "Краткое описание материала 4",
          date: "2024-06-01",
        },
        {
          id: 5,
          title: "Название статьи 5",
          description: "Краткое описание материала 5",
          date: "2024-06-05",
        },
      ],
      visibleCount: 4,
      isLoading: false,

      searchForm: "",
    };
  },

  computed: {
    total() {
      return this.results.length;
    },
    visibleResults() {
      return this.results.slice(0, this.visibleCount);
    },
  },

  methods: {
    showMore() {
      this.visibleCount += 4;
    },
    formatDate(dateStr) {
      const date = new Date(dateStr);
      return date.toLocaleDateString("ru-RU", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    },
    handleSearchForm() {
        console.log(234234234)
    }
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
  <div class="container mx-auto px-4">
    <VBreadcrumds />
    <!-- Количество найденных результатов -->
    <div class=" mb-6">
      <form
        class="duration-200 p-4 bg-white h-full shadow rounded-xl flex justify-between gap-2 w-full"
        @submit.prevent.stop="handleSearchForm"
      >
        <input
          class="flex-1 block text-base sm:text-2xl !outline-0"
          placeholder="Введите поисковый запрос"
          type="text"
          id="formSearch"
          v-model="searchForm"
        />
        <VButton
          :disabled="!searchForm.length"
          type="submit"
          class="sm:text-xl select-none"
          >Найти</VButton
        >
      </form>
    </div>
    <div
      v-if="results.length > 0"
      class="text-2xl sm:text-3xl font-semibold mb-6"
    >
      Найдено результатов: {{ total }}
    </div>
    <div v-else class="text-gray-500">
      Нет подходящих результатов поиска. Измените поисковый запрос.
    </div>

    <!-- Список результатов -->
    <ul class="space-y-4" v-if="!isLoading">
      <li
        v-for="item in visibleResults"
        :key="item.id"
        class="border border-gray-200 p-4 rounded-lg shadow-sm hover:shadow transition"
      >
        <a
          :href="`/articles/${item.id}`"
          class="text-blue-600 text-xl font-bold hover:underline"
        >
          {{ item.title }}
        </a>
        <p class="text-gray-700 mt-2">{{ item.description }}</p>
        <p class="text-sm text-gray-400 mt-1">
          {{ formatDate(item.date) }}
        </p>
      </li>
    </ul>
    <ul class="space-y-4" v-if="isLoading">
      <div
        v-for="item in 4"
        :key="item"
        class="border border-gray-200 p-4 rounded-lg shadow-sm hover:shadow transition"
      >
        <VLoader class="h-6 w-1/2" />
        <VLoader class="h-6 w-2/3 mt-2" />
        <VLoader class="h-4 w-20 mt-1" />
      </div>
    </ul>

    <!-- Показать больше -->
    <div
      v-if="visibleCount < results.length && !isLoading"
      class="text-center mt-10"
    >
      <button
        @click="showMore"
        class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
      >
        Показать больше
      </button>
    </div>
  </div>
</template>

<style scoped></style>
