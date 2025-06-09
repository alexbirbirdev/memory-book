<script>
import VLoader from "./VLoader.vue";

export default {
  name: "VSearchInfoLoader",

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
    class="bg-white rounded-2xl shadow-md overflow-hidden grid md:grid-cols-2 gap-2"
  >
    <div class="flex flex-col justify-center gap-4 md:gap-6 p-6">
      <VLoader class="md:w-7/10 h-9" />
      <div
        class="flex flex-col-reverse lg:flex-row items-center xl:items-center gap-6"
      >
        <VLoader class="h-11 w-35" />
        <div class="flex items-center justify-start gap-6 xl:gap-8">
          <div
            class="text-center flex flex-col gap-1 items-center leading-[120%]"
          >
            <VLoader class="h-10 w-25" />
            <VLoader class="h-4 w-15" />
          </div>
          <div
            class="text-center flex flex-col gap-1 items-center leading-[120%]"
          >
            <VLoader class="h-10 w-25" />
            <VLoader class="h-4 w-15" />
          </div>
        </div>
      </div>
    </div>
    <VLoader class="w-full aspect-video md:h-full lg:aspect-[16/9] rounded-xl" />
  </div>
</template>

<style scoped></style>
