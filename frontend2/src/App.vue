<script>
export default {
  name: "App",

  components: {},

  props: {},

  data() {
    return {};
  },

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
  <div class="app-cont bg-neutral-50">
    <div class="">
      <app-header></app-header>
      <div class="py-10">
        <router-view></router-view>
      </div>
    </div>

    <app-footer></app-footer>
  </div>
</template>

<style scoped>
.app-cont {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;
  
}
</style>
