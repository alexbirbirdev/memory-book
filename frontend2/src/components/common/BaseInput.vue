<template>
  <div class="base-input">
    <label v-if="label" :for="id">{{ label }}</label>
    <component
      :is="isTextarea ? 'textarea' : 'input'"
      :id="id"
      :type="type"
      :placeholder="placeholder"
      :rows="isTextarea ? rows : null"
      :value="modelValue"
      @input="updateInput"
      :class="{ error: error }"
    />
    <small v-if="error" class="error-message">{{ error }}</small>
  </div>
</template>

<script>
export default {
  name: "base-input",
  props: {
    modelValue: String,
    label: String,
    placeholder: String,
    id: String,
    type: {
      type: String,
      default: "text",
    },
    error: String,
    isTextarea: {
      type: Boolean,
      default: false,
    },
    rows: {
      type: Number,
      default: 4,
    },
  },
  methods: {
    updateInput(event) {
      this.$emit("update:modelValue", event.target.value);
    },
  },
};
</script>

<style scoped>
.base-input {
  display: flex;
  flex-direction: column;
  margin-bottom: 20px;
}
label {
  font-weight: bold;
  margin-bottom: 5px;
}
input,
textarea {
  padding: 10px;
  border-radius: 4px;
  border: 1px solid #ccc;
  font-size: 14px;
  resize: vertical;
}
input.error,
textarea.error {
  border-color: #e53935;
}
.error-message {
  color: #e53935;
  font-size: 12px;
  margin-top: 4px;
}
</style>
