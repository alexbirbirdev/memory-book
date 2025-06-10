<script>
import axios from "axios";
import Carousel from "primevue/carousel";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";
import VLoader from "@/components/loaders/VLoader.vue";
export default {
  name: "ArticleDetailView",

  components: {
    Carousel,
    VBreadcrumds,
    VLoader,
  },

  props: {},

  data() {
    return {
      newsTitle: "sdfsdf",
      // news: {
      //   title: "Заголовок новости",
      //   detailImage: "https://placehold.co/160x90",
      //   images: [
      //     {
      //       url: "https://placehold.co/600x400?text=1",
      //       title: "Первый слайд",
      //     },
      //     {
      //       url: "https://placehold.co/600x400?text=2",
      //       title: "Второй слайд",
      //     },
      //     {
      //       url: "https://placehold.co/600x400?text=3",
      //       title: "Третий слайд",
      //     },
      //   ],
      //   detailedDescription: `
      //     <p>Это подробное описание новости с возможностью форматирования текста.</p>
      //     <p>Можно вставлять <strong>жирный текст</strong>, <em>курсив</em>, ссылки и т.д.</p>
      //     <p><a href="https://example.com" target="_blank" class="text-blue-600 underline hover:text-blue-800 transition">Пример ссылки</a></p>
      //     <p><img src="https://placehold.co/600x400" alt="Фото в описании" class="my-6 rounded-lg shadow-md" /></p>
      //     <p>
      //       <iframe
      //         width="560"
      //         height="315"
      //         src="https://www.youtube.com/embed/dQw4w9WgXcQ"
      //         title="Видео"
      //         frameborder="0"
      //         allowfullscreen
      //         class="w-full aspect-video rounded-lg shadow-md"
      //       ></iframe>
      //     </p>
      //   `,
      // },
      article: null,
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

  computed: {
    // getNew() {
    //   this.newsTitle = this.news.title;
    // },
    formattedDate() {
      const date = new Date(this.article.publish_date);
      return date.toLocaleString("ru-RU", {
        hour: "2-digit",
        minute: "2-digit",
        day: "2-digit",
        month: "long",
        year: "numeric",
      });
    },
  },

  methods: {
    
    async getArticle() {
      try {
        this.isLoading = true;
        const response = await axios.get(
          `${import.meta.env.VITE_API_URL}/articles/` + this.$route.params.id
        );

        // this.articles = response.data;
        // console.log(response.data);
        this.article = response.data;
        this.$route.meta.title = response.data.title;
        this.newsTitle = response.data.title;
      } catch (error) {
        console.log(error.response.data.detail);
        this.$router.push("/articles/");
      } finally {
        this.isLoading = false;
      }
    },
  },

  watch: {},
  created() {
    this.getArticle();
  },
  mounted() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<template>
  <div class="container mx-auto px-4">
    <VBreadcrumds v-if="!isLoading" ref="breadcrumbs" />
  </div>
  <div class="container mx-auto px-4">
    <div
      v-if="!isLoading"
      class="max-w-5xl mx-auto p-6 bg-white rounded-2xl shadow-md"
    >
      <!-- Заголовок новости -->
      <h1
        v-if="article.title"
        class="text-2xl md:text-3xl font-extrabold mb-4 md:mb-10 text-gray-900 border-b pb-4"
      >
        {{ article.title }}
      </h1>

      <!-- Детальная картинка -->
      <img
        v-if="article.detail_image"
        :src="$formatImageUrl(article.detail_image)"
        alt="Детальная картинка новости"
        class="w-full rounded-lg shadow-lg mb-4 md:mb-12 object-cover"
      />

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
        v-if="article.content"
        class="prose prose-lg max-w-none text-gray-800"
        v-html="article.content"
      ></div>

      <div class="prose prose-lg max-w-none text-xs text-gray-500 mt-4">
        {{ formattedDate }}
      </div>
    </div>
    <div v-else class="max-w-5xl mx-auto p-6 bg-white rounded-2xl shadow-md">
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
  </div>
</template>

<style scoped></style>
