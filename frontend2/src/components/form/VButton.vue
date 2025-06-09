<script>
export default {
  name: "VButton",

  components: {},

  props: {
    to: {
      type: String,
      default: null,
    },
    href: {
      type: String,
      default: null,
    },
    type: {
      type: String,
      default: "button",
    },
    variant: {
      type: String,
      default: "default", // 'default' | 'danger'
      validator: (value) => ["default", "danger"].includes(value),
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },

  data() {
    return {};
  },

  computed: {
    classes() {
      const base =
        "inline-flex items-center px-4 cursor-pointer py-2 rounded-lg text-sm font-medium transition focus:outline-none";
      const variants = {
        default:
          "bg-blue-600 text-white hover:bg-blue-700 disabled:bg-blue-300",
        danger: "bg-red-600 text-white hover:bg-red-700 disabled:bg-red-300",
      };

      const disabledClass = this.disabled ? "cursor-not-allowed" : "";

      return `${base} ${variants[this.variant]} ${disabledClass}`;
    },
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
  <!-- Если используется router-link -->
  <router-link
    v-if="to"
    :to="to"
    custom
    v-slot="{ navigate, href: routerHref }"
  >
    <a
      :href="routerHref"
      @click.prevent="!disabled && navigate()"
      :class="classes"
      :aria-disabled="disabled"
    >
      <slot></slot>
    </a>
  </router-link>

  <!-- Если обычная ссылка -->
  <a
    v-else-if="href"
    :href="href"
    :class="classes"
    :aria-disabled="disabled"
    @click.prevent="disabled && $event.preventDefault()"
  >
    <slot></slot>
  </a>

  <!-- Если обычная кнопка -->
  <button v-else :type="type" :disabled="disabled" :class="classes">
    <slot></slot>
  </button>
</template>

<style scoped></style>
