<script>
export default {
  name: "VInput",

  components: {},

  props: {
    modelValue: {
      type: [String, Number],
      default: "",
    },
    type: {
      type: String,
      default: "text",
      validator: (value) =>
        ["text", "password", "date", "email", "number", "tel", "url"].includes(value),
    },
    label: {
      type: String,
      default: "",
    },
    placeholder: {
      type: String,
      default: "",
    },
    error: {
      type: String,
      default: "",
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    required: {
      type: Boolean,
      default: false,
    },
  },

  data() {
    return {};
  },

  emits: ["update:modelValue"],
  computed: {
    inputClasses() {
      return {
        "v-input--error": this.error,
        "v-input--disabled": this.disabled,
      };
    },
  },

  methods: {
    handleInput(event) {
      this.$emit("update:modelValue", event.target.value);
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
  <div class="w-full">
    <label>
      <div class="mb-2" v-if="label">{{ label }}</div>
      <input
        class="w-full px-4 py-2 border rounded-md duration-100 focus:outline-none focus:ring-2 transition-all"
        :class="{
          'border-gray-300 focus:border-blue-500 focus:ring-blue-500': !error,
          'border-red-500 focus:border-red-500 focus:ring-red-200': error,
          'bg-gray-100 cursor-not-allowed': disabled,
        }"
        :type="type"
        :value="modelValue"
        :placeholder="placeholder"
        :disabled="disabled"
        @input="handleInput"
      />
    </label>

    <p v-if="error" class="mt-1 text-sm text-red-500">
      {{ error }}
    </p>
  </div>
</template>

<style scoped></style>
