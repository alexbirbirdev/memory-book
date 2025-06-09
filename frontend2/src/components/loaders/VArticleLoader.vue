<script>
import VLoader from "./VLoader.vue";
export default {
  name: "VArticleLoader",

  components: { VLoader },

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
    class="bg-white rounded-2xl shadow hover:shadow-lg transition cursor-pointer overflow-hidden"
  >
    <VLoader class="w-full aspect-video" />
    <div class="p-4 space-y-2">
      <VLoader class="w-1/2 h-5" />
      <VLoader class="w-full h-7" />
      <VLoader class="w-full h-5" />
    </div>
  </div>
</template>

<style scoped></style>
