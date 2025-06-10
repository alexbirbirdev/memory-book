<script>
import axios from "axios";
import ArticleCard from "@/components/common/BaseArticle.vue";
import VButton from "@/components/form/VButton.vue";
import VArticleLoader from "@/components/loaders/VArticleLoader.vue";
import VLoader from "@/components/loaders/VLoader.vue";
import VSearchInfoLoader from "@/components/loaders/VSearchInfoLoader.vue";
export default {
  name: "HomeView",

  components: {
    ArticleCard,
    VButton,
    VLoader,
    VArticleLoader,
    VSearchInfoLoader,
  },

  props: {},

  data() {
    return {
      // Слайды баннера
      bannerSlides: [],

      currentSlide: 0,
      // Блок «Найти информацию»
      findBlock: {
        text: "Узнайте, какие события произошли в этот день или найдите ветерана по базе.",
        dayEvent: { count: 5 }, // например, 5 событий
        veteransCount: 1240, // общее число ветеранов в базе
        image:
          "https://waralbum.ru/wp-content/uploads/2018/01/45-mm_Berlin_1945.jpg",
      },

      // последние 3 статьи
      article: [],

      responsiveOptions: [
        {
          breakpoint: "768px",
          numVisible: 1,
          numScroll: 1,
        },
      ],
      // Блок «Стать участником проекта»
      joinBlock: {
        title: "Стать участником проекта",
        text: "Если у Вас есть информация о ветеране, информация о котором отсутсвует на платформе, заполните форму, перейдя по ссылки ниже",
        link: {
          title: "Добавить ветерана",
          href: "/heroes/add",
        },
      },

      bannerLoading: true,
      findBlockLoading: false,
      latestarticleLoading: true,
      joinBlockLoading: false,
    };
  },

  computed: {
    latestarticle() {
      if (this.article.length) {
        return this.article.slice(0, 3);
      }
      return 0;
    },
  },

  methods: {
    async getBanners() {
      try {
        this.bannerLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/banners/`);
        console.log(response.data)
        this.bannerSlides = response.data.results;
      } catch (error) {
        console.log(error);
      } finally {
        this.bannerLoading = false;
      }
    },
    async getArticles() {
      try {
        this.latestarticleLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/articles/`);
        console.log(response.data)
        this.article = response.data.results;
      } catch (error) {
        console.log(error);
      } finally {
        this.latestarticleLoading = false;
      }
    },
  },

  watch: {},

  created() {
    this.getBanners();
    this.getArticles();
  },
  mounted() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<template>
  <div class="container mx-auto px-4 space-y-16">
    <section>
      <Carousel
        v-if="bannerSlides && bannerSlides.length > 0 && !bannerLoading"
        :value="bannerSlides"
        :numVisible="1"
        :numScroll="1"
        :circular="true"
        :autoplayInterval="10000"
        :responsiveOptions="responsiveOptions"
        :showNavigators="false"
        :showIndicators="false"
        :touchScroll="false"
        class="banner-carousel"
      >
        <template #item="{ data }">
          <div
            class="relative aspect-video md:aspect-[3/1] bg-cover bg-center flex items-center justify-center rounded-2xl overflow-hidden shadow"
            :style="'background-image: url(' + data.image_desktop + ')'"
          >
            <div class="absolute inset-0 bg-black opacity-50"></div>
            <div class="relative z-10 text-white text-center px-4 max-w-xl">
              <h2 class="text-3xl md:text-4xl font-bold mb-2">
                {{ data.title }}
              </h2>
              <p class="text-lg">{{ data.description }}</p>
            </div>
          </div>
        </template>
      </Carousel>
      <div class="" v-if="bannerLoading">
        <VLoader class="w-full aspect-[3/1]" />
      </div>
    </section>

    <section
      v-if="!findBlockLoading"
      class="bg-white rounded-2xl shadow-md overflow-hidden grid md:grid-cols-2 gap-2"
    >
      <div class="flex flex-col justify-center gap-4 md:gap-6 p-6">
        <h2 class="text-xl xl:text-2xl 2xl:text-3xl font-semibold">
          Найти информацию об участниках войны
        </h2>
        <p class="text-gray-700">{{ findBlock.text }}</p>
        <div
          class="flex flex-col-reverse lg:flex-row items-center xl:items-center gap-6"
        >
          <VButton to="/heroes" class="xl:text-xl">Найти ветерана</VButton>
          <div class="flex items-start justify-start gap-6 xl:gap-8">
            <div class="text-center leading-[120%]">
              <p class="text-2xl xl:text-4xl font-bold">
                {{ findBlock.dayEvent.count }}
              </p>
              <p class="text-gray-600">
                Важных событий <br />
                в этот день
              </p>
            </div>
            <div class="text-center leading-[120%]">
              <p class="text-2xl xl:text-4xl font-bold">
                {{ findBlock.veteransCount }}
              </p>
              <p class="text-gray-600">Всего ветеранов</p>
            </div>
          </div>
        </div>
      </div>
      <div
        class="bg-cover bg-center aspect-video md:h-full lg:aspect-[16/9]"
        :style="'background-image: url(' + findBlock.image + ')'"
      ></div>
    </section>
    <VSearchInfoLoader v-else />

    <section class="space-y-6">
      <div class="flex justify-between items-center">
        <h2 class="text-2xl font-semibold">Статьи</h2>
        <VButton to="/articles/">Читать все статьи</VButton>
      </div>
      <div
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
        v-if="latestarticle.length && !latestarticleLoading"
      >
        <ArticleCard
          v-for="(art, i) in latestarticle"
          :key="art.id"
          :article="art"
        />
      </div>
      <div
        class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6"
        v-if="latestarticleLoading"
      >
        <VArticleLoader v-for="article in 3" :key="article" />
      </div>
    </section>

    <section class="bg-white p-6 rounded-2xl shadow space-y-4 text-center">
      <h2 class="text-2xl font-semibold">{{ joinBlock.title }}</h2>
      <p v-if="!joinBlockLoading" class="text-gray-700">{{ joinBlock.text }}</p>
      <VLoader v-else class="h-6 w-1/2 mx-auto" />
      <VButton :to="joinBlock.link.href">{{ joinBlock.link.title }}</VButton>
    </section>
  </div>
</template>

<style scoped></style>
