<script>
import VLoader from "./VLoader.vue";

export default {
  name: "VHeroItemLoader",

  components: {
    VLoader,
  },

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
    class="bg-white rounded-lg overflow-hidden shadow flex flex-col duration-200 hover:shadow-xl"
  >
    <VLoader class="w-full aspect-[3/4] mb-3" />
    <div class="p-4">
      <h3
        class="text-xl flex gap-2 items-center justify-start flex-wrap font-bold mb-2"
      >
        <VLoader class="w-20 mb-7" />
        <VLoader class="w-20 mb-7" />
        <VLoader class="w-20 mb-7" />
      </h3>
      <VLoader class="w-1/2 h-6 mb-1" />
      <VLoader class="w-2/3 h-6 mb-1" />
      <VLoader class="w-1/2 h-6 mb-1" />
      <VLoader class="w-2/3 h-6 mb-1" />
      <VLoader class="w-1/2 h-6 mb-1" />
      <VLoader class="w-2/3 h-6 mb-1" />

      <div class="mt-3">
        <VLoader class="w-1/2 h-6 mb-1" />
        <div class="flex med overflow-x-auto custom-scrollbar space-x-2">
          <div
            v-for="val in 3"
            :key="val"
            class="py-1 rounded whitespace-nowrap"
          >
            <VLoader class="w-20 h-8" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
