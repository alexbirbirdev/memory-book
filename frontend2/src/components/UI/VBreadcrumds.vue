<script>
export default {
  name: "Breadcrumbs",

  data() {
    return {
      dynamicTitle: null,
    };
  },

  computed: {
    breadcrumbs() {
      const route = this.$route;
      const crumbs = [];

      // Главная страница
      crumbs.push({ title: "Главная", link: "/" });

      // Родительский раздел из meta
      if (route.meta?.parent) {
        const parentRoute = this.findRouteByName(route.meta.parent);
        if (parentRoute) {
          crumbs.push({
            title: route.meta.parent,
            link: parentRoute.path,
          });
        }
      }

      // Текущая страница (используем динамический заголовок если есть)
      if (route.name !== "home") {
        crumbs.push({
          title: this.dynamicTitle || route.meta?.title || "Страница",
          link: "",
        });
      }

      return crumbs;
    },
  },

  methods: {
    findRouteByName(name) {
      return this.$router.options.routes.find((r) => r.meta?.title === name);
    },

    setDynamicTitle(title) {
      this.dynamicTitle = title;
    },
  },
  watch: {
    $route() {
      this.dynamicTitle = null; // Сбрасываем при смене маршрута
    },
  },
};
</script>

<template>
  <nav v-if="breadcrumbs.length > 1" class="text-sm py-2 px-2 md:px-0 mb-4 md:mb-6">
    <ol class="flex items-center flex-wrap gap-2">
      <li
        v-for="(item, index) in breadcrumbs"
        :key="index"
        class="flex items-center"
      >
        <router-link
          v-if="item.link"
          :to="item.link"
          class="text-blue-600 hover:text-blue-800 hover:underline transition-colors cursor-pointer"
        >
          {{ item.title }}
        </router-link>
        <span v-else class="text-gray-600 cursor-default">
          {{ item.title }}
        </span>

        <span v-if="index < breadcrumbs.length - 1" class="ml-2 text-gray-600 cursor-default">
          >
        </span>
      </li>
    </ol>
  </nav>
</template>
