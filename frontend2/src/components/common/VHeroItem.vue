<script>
export default {
  name: "VHeroItem",

  components: {},

  props: {
    vet: Object,
    require: true,
  },

  data() {
    return {};
  },

  computed: {},

  methods: {
    formatDate(dateStr) {
      if (!dateStr) return "";
      const d = new Date(dateStr);
      return d.toLocaleDateString("ru-RU");
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
  <router-link
    :to="'/heroes/' + vet.id"
    class="bg-white rounded-lg overflow-hidden shadow flex flex-col duration-200 hover:shadow-xl"
  >
    <img
      :src="vet.photo"
      alt="Фото ветерана"
      class="w-full aspect-[3/4] object-cover mb-3"
      loading="lazy"
    />
    <div class="p-4">
      <h3
        class="text-xl flex gap-2 items-center justify-start flex-wrap font-bold mb-2"
      >
        <span v-if="vet.full_name">{{ vet.full_name }}</span>
      </h3>
      <p v-if="vet.birth_date">
        <strong>Дата рождения:</strong> {{ formatDate(vet.birth_date) }}
      </p>
      <p v-if="vet.death_date">
        <strong>Дата смерти:</strong> {{ formatDate(vet.death_date) }}
      </p>
      <p v-if="vet.branch_of_service">
        <strong>Род войск:</strong> {{ vet.branch_of_service.name }}
      </p>
      <p v-if="vet.military_rank"><strong>Звание:</strong> {{ vet.military_rank.name }}</p>
      <p v-if="vet.military_unit">
        <strong>Воинское формирование:</strong> {{ vet.military_unit }}
      </p>
      <p v-if="vet.conflict"><strong>Сражение:</strong> {{ vet.conflict.name }}</p>

      <div v-if="vet.rewards.length > 0" class="mt-3">
        <p class="font-semibold mb-1">Награды:</p>
        <div class="flex med overflow-x-auto custom-scrollbar space-x-2">
          <div
            v-for="(award, i) in vet.rewards"
            :key="i"
            class="flex-shrink-0 bg-yellow-200 px-3 py-1 rounded whitespace-nowrap"
          >
            {{ award.reward.name }}
          </div>
        </div>
      </div>

    </div>
  </router-link>
</template>

<style scoped>
.custom-scrollbar {
  &::-webkit-scrollbar {
    height: 0;
  }
  /* &::-webkit-scrollbar-track {
  }
  &::-webkit-scrollbar-thumb {
  } */
}
</style>
