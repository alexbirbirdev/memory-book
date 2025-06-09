<script>
export default {
  name: "VSelect",

  props: {
    modelValue: {
      type: [String, Number],
      default: "",
    },
    label: {
      type: String,
      default: "",
    },
    placeholder: {
      type: String,
      default: "",
    },
    options: {
      type: Array,
      required: true,
    },
    optionValue: {
      type: String,
      default: "", // например: "id"
    },
    optionLabel: {
      type: String,
      default: "", // например: "name"
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
    return {
      isOpen: false, // Состояние открытия/закрытия списка
    };
  },

  emits: ["update:modelValue"],

  computed: {
    selectClasses() {
      return {
        "v-select--error": this.error,
        "v-select--disabled": this.disabled,
      };
    },
    arrowClasses() {
      return {
        "transform rotate-180": this.isOpen,
        "transition-all": true,
      };
    },
  },

  methods: {
    handleChange(event) {
      this.$emit("update:modelValue", event.target.value);
    },
    toggleDropdown() {
      //   if (!this.disabled) {
      //     this.isOpen = !this.isOpen;
      //   }
    },
  },
};
</script>

<template>
  <div class="relative w-full">
    <label>
      <div class="mb-2" v-if="label">{{ label }}</div>
      <div class="relative w-full">
        <select
          :value="modelValue"
          @change="handleChange"
          :disabled="disabled"
          :placeholder="placeholder"
          class="w-full px-4 py-2 border rounded-md duration-100 focus:outline-none focus:ring-2 appearance-none"
          :class="{
            'border-gray-300 focus:border-blue-500 focus:ring-blue-500': !error,
            'border-red-500 focus:border-red-500 focus:ring-red-200': error,
            'bg-gray-100 cursor-not-allowed': disabled,
          }"
          @click="toggleDropdown"
        >
          <option value="" disabled>{{ placeholder }}</option>
          <option
            v-for="(option, index) in options"
            :key="index"
            :value="optionValue && optionLabel ? option[optionValue] : option"
          >
            {{ optionValue && optionLabel ? option[optionLabel] : option }}
          </option>
        </select>
        <span
          class="absolute right-3 top-1/2 transform -translate-y-1/2 pointer-events-none"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            class="h-5 w-5 text-gray-500"
            :class="arrowClasses"
          >
            <path
              fill-rule="evenodd"
              d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
              clip-rule="evenodd"
            />
          </svg>
        </span>
      </div>
    </label>

    <p v-if="error" class="mt-1 text-sm text-red-500">
      {{ error }}
    </p>
  </div>
</template>

<style scoped>
.v-select--error select {
  border-color: #f87171;
}
.v-select--disabled select {
  cursor: not-allowed;
}
</style>
