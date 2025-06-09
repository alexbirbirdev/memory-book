<script>
export default {
  name: "VBurger",

  components: {},

  props: {
    isActive: Boolean,
  },

  data() {
    return {};
  },

  computed: {},

  methods: {
    toggleBurger() {
      //   this.isActive = !this.isActive;
      this.$emit("toggle");
    },
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
  <div
    class="relative w-10 h-10 rounded-xl bg-white burger"
    @click="toggleBurger"
    :class="isActive ? 'active' : ''"
  >
    <div class=""></div>
    <div class=""></div>
    <div class=""></div>
    <div class=""></div>
  </div>
</template>

<style scoped>
.burger div {
  width: calc(100% - 16px);
  height: 3px;
  position: absolute;
  background: #000;
  left: 50%;
  transform: translateX(-50%);
  border-radius: 4px;
  transition: 0.2s;
  &:nth-child(1) {
    top: 12px;
  }
  &:nth-child(2) {
    top: 50%;
    transform: translate(-50%, -50%);
  }
  &:nth-child(3) {
    top: 50%;
    transform: translate(-50%, -50%);
    opacity: 0;
  }
  &:nth-child(4) {
    bottom: 12px;
  }
}
.burger.active div {
  &:nth-child(1) {
    top: 12px;
    opacity: 0;
  }
  &:nth-child(2) {
    top: 50%;
    transform: translate(-50%, -50%) rotate(45deg);
  }
  &:nth-child(3) {
    top: 50%;
    transform: translate(-50%, -50%) rotate(-45deg);
    opacity: 1;
  }
  &:nth-child(4) {
    opacity: 0;
  }
}
</style>
