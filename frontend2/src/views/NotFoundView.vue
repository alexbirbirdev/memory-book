<script>
export default {
  name: "NotFoundView",

  components: {},

  props: {},

  data() {
    return {};
  },

  computed: {},

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
  <div
    class="min-h-[50vh] flex flex-col justify-center items-center text-center p-6"
  >
    <div class="text-[160px] sm:text-[200px] leading-[80%] font-bold mb-4">404</div>
    <h1 class="text-4xl font-bold mb-4">Страница не найдена</h1>
    <p class="text-lg text-gray-600 mb-6">
      Извините, такой страницы не существует.
    </p>
    <router-link to="/" class="text-blue-600 underline">На главную</router-link>
  </div>
</template>

<style scoped></style>
