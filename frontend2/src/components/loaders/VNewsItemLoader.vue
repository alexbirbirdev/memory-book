<script>
import VLoader from "./VLoader.vue";
export default {
  name: "VNewsItemLoader",

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
  <div class="rounded-lg overflow-hidden shadow transition">
    <VLoader class="w-full aspect-video rounded-none" />
    <div class="p-4">
      <VLoader class="w-1/2 h-5 mb-1" />
      <VLoader class="w-full h-7 mb-2" />
      <VLoader class="w-full h-6" />
    </div>
  </div>
</template>

<style scoped></style>
