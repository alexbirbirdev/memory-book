<script>
import axios from "axios";
import VInput from "@/components/form/VInput.vue";
import VSelect from "@/components/form/VSelect.vue";
import VButton from "@/components/form/VButton.vue";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";
export default {
  name: "AddVeteranView",

  components: { VInput, VSelect, VButton, VBreadcrumds },

  props: {},

  data() {
    return {
      form: {
        last_name: "",
        first_name: "",
        middle_name: "",
        birth_date: "",
        death_date: "",
        biography: "",
        military_unit: "",
        service_place: "",
        call_place: "",
        // veteran_type: "",
        military_rank: "",
        branch_of_service: "",
        conflict: "",

        // servicePlace: "",
        // draftPlace: "",
        // armyType: "",
        // deathPlace: "",
        // hospital: "",
        // prisonCamp: "",
        // award: "",
        // awardDocNumber: "",
        // awardDate: "",
      },
      errors: {},

      filters: {
        lastName: "",
        firstName: "",
        middleName: "",
        birthDateFrom: "",
        birthDateTo: "",
        conflict: "",
        rank: "",
        armyType: "",
        armyBranch: "",
        servicePlace: "",
      },
      filtersSelects: {
        conflict: {
          label: "Выберите конфликт",
          placeholder: "Выберите конфликт",
          options: ["СВО", "ВОВ"],
        },
        rank: {
          label: "Воинское звание",
          placeholder: "Выберите звание",
          options: [
            "Рядовой",
            "Сержант",
            "Лейтенант",
            "Капитан",
            "Майор",
            "Подполковник",
            "Полковник",
          ],
        },
        armyType: {
          label: "Вид вооруженных сил",
          placeholder: "Выберите вид ВС",
          options: ["Сухопутные войска", "ВВС", "ВМФ", "Ракетные войска"],
        },
        armyBranch: {
          label: "Род войск",
          placeholder: "Выберите род войск",
          options: [
            "Пехота",
            "Танковые войска",
            "Артиллерия",
            "Связь",
            "Разведка",
          ],
        },
        badge: {
          label: "Тип ветерана",
          placeholder: "Выберите тип",
          options: ["ветеран боевых действий", "труженик тыла"],
        },
        prisoner: {
          label: "Лагерь военнопленных ",
          placeholder: "Лагерь военнопленных ",
          options: ["ветеран боевых действий", "труженик тыла"],
        },
        reward: {
          label: "Выбрать награду ",
          placeholder: "Выбрать награду ",
          options: ["ветеран боевых действий", "труженик тыла"],
        },
        servicePlace: {
          label: "Место службы",
          placeholder: "Введите место службы",
          options: [], // Это поле можно либо оставить пустым, либо заменить на обычный `VInput`, если оно не предполагает выбор
        },
      },

      isLoading: false,
      toast: {
        message: "",
        type: "", // 'success' или 'error'
        visible: false,
      },
    };
  },

  computed: {},

  methods: {
    showToast(message, type = "success") {
      this.toast.message = message;
      this.toast.type = type;
      this.toast.visible = true;

      setTimeout(() => {
        this.toast.visible = false;
      }, 3000);
    },
    sanitizeInput(input) {
      return String(input)
        .replace(/['"`;]/g, "")
        .replace(/<[^>]*>/g, "")
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
    },

    validateForm() {
      this.errors = {};

      const requiredFields = [
        "last_name",
        "first_name",
        "middle_name",
        "birth_date",
        "death_date",
        "biography",
        // "veteran_type",
        "military_rank",
        "branch_of_service",
        "conflict",
        "call_place",
        "military_unit",
        "service_place",
      ];
      for (const field of requiredFields) {
        if (!this.form[field]) {
          this.errors[field] = "Обязательное поле";
        }
      }

      return Object.keys(this.errors).length === 0;
    },

    handleForm() {
      if (!this.validateForm()) {
        return;
      }

      const sanitizedForm = {};
      for (const key in this.form) {
        sanitizedForm[key] = this.sanitizeInput(this.form[key]);
      }

      console.log("Отправка данных:", sanitizedForm);
      this.createVet();
    },

    async createVet() {
      try {
        this.isLoading = true;
        const response = await axios.post(`${import.meta.env.VITE_API_URL}/veterans/`, {
          last_name: this.form.last_name,
          first_name: this.form.first_name,
          middle_name: this.form.middle_name,
          birth_date: this.form.birth_date,
          death_date: this.form.death_date,
          biography: this.form.biography,
          military_unit: this.form.military_unit,
          service_place: this.form.service_place,
          call_place: this.form.call_place,
          // veteran_type: this.form.veteran_type,
          military_rank: this.form.military_rank,
          branch_of_service: this.form.branch_of_service,
          conflict: this.form.conflict,
        });
        console.log(response.data);
        this.clearForm();
        this.showToast("Ветеран успешно добавлен", "success");
      } catch (error) {
        console.log(error.response.data.detail);
        const message =
          error.response?.data?.detail || "Произошла ошибка при отправке формы";
        this.showToast(message, "error");
      } finally {
        this.isLoading = false;
      }
    },
    clearForm() {
      this.form.last_name = "";
      this.form.first_name = "";
      this.form.middle_name = "";
      this.form.birth_date = "";
      this.form.death_date = "";
      this.form.biography = "";
      this.form.military_unit = "";
      this.form.service_place = "";
      this.form.call_place = "";
      this.form.military_rank = "";
      this.form.branch_of_service = "";
      this.form.conflict = "";
    },
    async getConflicts() {
      try {
        this.isLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/conflicts/`);

        // console.log(response.data.results);
        this.filtersSelects.conflict.options = response.data.results;
      } catch (error) {
        console.log(error);
      } finally {
        this.isLoading = false;
      }
    },
    async getRanks() {
      try {
        this.isLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/military-ranks/`);

        // console.log(response.data.results);
        this.filtersSelects.rank.options = response.data.results;
      } catch (error) {
        console.log(error);
      } finally {
        this.isLoading = false;
      }
    },
    async getBranchServ() {
      try {
        this.isLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/branches-of-service/`);

        // console.log(response.data.results);
        this.filtersSelects.armyBranch.options = response.data.results;
      } catch (error) {
        console.log(error);
      } finally {
        this.isLoading = false;
      }
    },
  },

  watch: {},

  created() {
    this.getConflicts();
    this.getRanks();
    this.getBranchServ();
  },
  mounted() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<template>
  <div class="container mx-auto">
    <VBreadcrumds />
  </div>
  <div class="max-w-4xl mx-auto p-6 bg-white rounded shadow space-y-6">
    <h1 class="text-3xl font-bold mb-6">Добавить ветерана</h1>

    <form @submit.prevent="onSearch" class="flex flex-col gap-10">
      <div class="grid grid-cols-1 gap-3 xl:gap-6">
        <VInput
          label="Фамилия"
          placeholder="Фамилия"
          v-model="form.last_name"
          :required="true"
          :error="errors.last_name"
        />
        <VInput
          label="Имя"
          placeholder="Имя"
          v-model="form.first_name"
          :required="true"
          :error="errors.first_name"
        />
        <VInput
          label="Отчество"
          placeholder="Отчество"
          v-model="form.middle_name"
          :required="true"
          :error="errors.middle_name"
        />
        <VInput
          label="Дата рождения"
          placeholder="Дата рождения"
          type="date"
          v-model="form.birth_date"
          :required="true"
          :error="errors.birth_date"
        />
        <VInput
          label="Дата смерти"
          placeholder="Дата смерти"
          type="date"
          v-model="form.death_date"
          :required="true"
          :error="errors.death_date"
        />

        <VInput
          label="Биография"
          placeholder="Биография"
          v-model="form.biography"
          :required="true"
          :error="errors.biography"
        />

        <!-- <VSelect
          v-model="form.veteran_type"
          :label="filtersSelects.badge.label"
          :placeholder="filtersSelects.badge.placeholder"
          :options="filtersSelects.badge.options"
          :error="errors.veteran_type"
        /> -->
        <VSelect
          v-if="!isLoading"
          v-model="form.military_rank"
          :label="filtersSelects.rank.label"
          :placeholder="filtersSelects.rank.placeholder"
          :options="filtersSelects.rank.options"
          :error="errors.military_rank"
          option-value="id"
          option-label="name"
        />
        <VSelect
          v-if="!isLoading"
          v-model="form.branch_of_service"
          :label="filtersSelects.armyBranch.label"
          :placeholder="filtersSelects.armyBranch.placeholder"
          :options="filtersSelects.armyBranch.options"
          :error="errors.branch_of_service"
          option-value="id"
          option-label="name"
        />
        <VSelect
          v-if="!isLoading"
          v-model="form.conflict"
          :label="filtersSelects.conflict.label"
          :placeholder="filtersSelects.conflict.placeholder"
          :options="filtersSelects.conflict.options"
          option-value="id"
          option-label="name"
          :error="errors.conflict"
        />
        <VInput
          v-model="form.call_place"
          label="Место призыва"
          placeholder="Место призыва"
          :required="true"
          :error="errors.call_place"
        />
        <VInput
          v-model="form.military_unit"
          label="Воинское формирование"
          placeholder="Воинское формирование"
          :required="true"
          :error="errors.military_unit"
        />
        <VInput
          v-model="form.service_place"
          label="Место службы"
          placeholder="Место службы"
          :required="true"
          :error="errors.service_place"
        />

        <!-- <VSelect
          v-model="form.armyType"
          :label="filtersSelects.armyType.label"
          :placeholder="filtersSelects.armyType.placeholder"
          :options="filtersSelects.armyType.options"
        />
        <VInput
          v-model="form.servicePlace"
          :label="filtersSelects.servicePlace.label"
          :placeholder="filtersSelects.servicePlace.placeholder"
        /> -->
        <!-- <VInput
          label="Дата призыва"
          placeholder="Дата призыва"
          type="date"
          v-model="form.draftDate"
        /> -->
        <!-- <VInput
          label="Дата награждения"
          placeholder="Дата награждения"
          type="date"
          v-model="form.awardDate"
        /> -->
        <!-- <VInput
          v-model="form.deathPlace"
          label="Место выбытия/смерти"
          placeholder="Место выбытия/смерти"
        /> -->

        <!-- <VInput
          v-model="form.hospital"
          label="Госпиталь"
          placeholder="Госпиталь"
        />
        <VInput
          v-model="form.awardDocNumber"
          label="Номер наградного документа"
          placeholder="Номер наградного документа"
        /> -->

        <!-- <VSelect
          v-model="form.prisonCamp"
          :label="filtersSelects.prisoner.label"
          :placeholder="filtersSelects.prisoner.placeholder"
          :options="filtersSelects.prisoner.options"
        /> -->
        <!-- <VSelect
          v-model="form.award"
          :label="filtersSelects.reward.label"
          :placeholder="filtersSelects.reward.placeholder"
          :options="filtersSelects.reward.options"
        /> -->
      </div>

      <div>
        <VButton
          @click.prevent.stop="handleForm"
          class="max-sm:w-full max-sm:flex max-sm:justify-center"
        >
          Отправить форму
        </VButton>
      </div>
    </form>
  </div>

  <transition name="fade">
    <div
      v-if="toast.visible"
      :class="[
        'fixed bottom-6 right-6 px-4 py-3 rounded shadow-lg text-white z-50',
        toast.type === 'success' ? 'bg-green-500' : 'bg-red-500',
      ]"
    >
      {{ toast.message }}
    </div>
  </transition>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
