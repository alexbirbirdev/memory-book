<script>
import axios from "axios";
import Carousel from "primevue/carousel";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";
import VLoader from "@/components/loaders/VLoader.vue";
export default {
  name: "EventItemView",

  components: {
    Carousel,
    VBreadcrumds,
    VLoader,
  },

  props: {},

  data() {
    return {
      newsTitle: "sdfsdf",
      news: null,
      responsiveOptions: [
        {
          breakpoint: "768px",
          numVisible: 1,
          numScroll: 1,
        },
      ],
      isLoading: false,
    };
  },

  computed: {},

  methods: {
    async getEvent() {
      try {
        this.isLoading = true;
        const response = await axios.get(
          `${import.meta.env.VITE_API_URL}/events/` + this.$route.params.id
        );

        // console.log(response.data);
        this.news = response.data;
        this.$route.meta.title = response.data.title;
        this.newsTitle = response.data.title;
      } catch (error) {
        console.log(error.response);
        this.$router.push("/events/");
      } finally {
        this.isLoading = false;
      }
    },
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

  created() {
    this.getEvent();
  },
  mounted() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<template>
  <div class="container mx-auto px-4">
    <VBreadcrumds ref="breadcrumbs" v-if="!isLoading" />
  </div>
  <div v-if="!isLoading" class="px-4 max-w-5xl mx-auto">
    <div class="p-6 bg-white rounded-2xl shadow-md">
      <!-- Заголовок новости -->
      <h1
        class="text-2xl md:text-3xl font-extrabold mb-4 md:mb-10 text-gray-900 border-b pb-4"
      >
        {{ news.title }}
      </h1>
      <div class="text-sm text-gray-500 mb-3">
        <span class="block">С {{ formatDateTime(news.start_date) }}</span>
        <span class="block">По {{ formatDateTime(news.end_date) }}</span>
      </div>
      <!-- Детальная картинка -->

      <img
        v-if="news.detail_image"
        :src="$formatImageUrl(news.detail_image)"
        alt="Детальная картинка новости"
        class="w-full rounded-lg shadow-lg mb-4 md:mb-12 object-cover max-h-96"
      />
      <div class="flex flex-wrap gap-2 text-xs">
        <span class="px-2 py-1 rounded bg-gray-200 text-gray-700">
          {{ news.status == "in_progress" ? "В процессе" : "" }}
          {{ news.status == "completed" ? "Завершено" : "" }}
          {{ news.status == "planned" ? "Запланировано" : "" }}
        </span>
        <span class="px-2 py-1 rounded bg-blue-100 text-blue-700">
          {{ news.format == "online" ? "Онлайн" : "" }}
          {{ news.format == "offline" ? "Оффлайн" : "" }}
          {{ news.format == "hybrid" ? "Гибридный" : "" }}
        </span>
      </div>

      <div class="flex flex-col gap-1 mt-6" v-if="news.location">
        <div class="text-sm text-gray-500">Где проходит</div>
        <div class="bg-neutral-100 text-neutral-900 rounded-xl px-4 py-2">
          {{ news.location }}
        </div>
      </div>

      <!-- Слайдер фото -->

      <!-- <Carousel
      v-if="news && news.images.length > 0 && !isLoading"
      :value="news.images"
      :numVisible="1"
      :numScroll="1"
      :circular="true"
      :autoplayInterval="7000"
      class="mb-4 md:mb-12 rounded-lg shadow-lg"
      :showIndicators="true"
      :showNavigators="false"
      :responsiveOptions="responsiveOptions"
    >
      <template #item="{ data }">
        <img
          :src="data.url"
          alt="Слайд фото"
          class="w-full object-cover rounded-lg max-h-80"
          loading="lazy"
        />
      </template>
    </Carousel> -->

      <!-- Детальное описание -->
      <div
        class="prose prose-lg max-w-none text-gray-800 mt-5"
        v-html="news.content"
      ></div>
    </div>
  </div>
  <div
    v-if="isLoading"
    class="max-w-5xl mx-auto p-6 bg-white rounded-2xl shadow-md"
  >
    <!-- Заголовок новости -->
    <VLoader class="w-2/3 h-16 mb-10" />

    <!-- Детальная картинка -->
    <VLoader class="w-full aspect-video shadow-lg mb-12" />

    <div class="flex flex-col items-start gap-2">
      <VLoader class="w-1/2 h-3" />
      <VLoader class="w-2/3 h-3" />
      <VLoader class="w-3/4 h-3" />
      <VLoader class="w-1/2 h-3" />
      <VLoader class="w-2/3 h-3" />
      <VLoader class="w-3/4 h-3" />
      <VLoader class="w-1/2 h-3" />
      <VLoader class="w-2/3 h-3" />
      <VLoader class="w-3/4 h-3" />
    </div>
  </div>
</template>

<style scoped></style>
