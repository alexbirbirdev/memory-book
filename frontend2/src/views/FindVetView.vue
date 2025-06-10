<script>
import axios from "axios";
import VHeroItem from "@/components/common/VHeroItem.vue";
import VButton from "@/components/form/VButton.vue";
import VInput from "@/components/form/VInput.vue";
import VSelect from "@/components/form/VSelect.vue";
import VHeroItemLoader from "@/components/loaders/VHeroItemLoader.vue";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";

export default {
  name: "FindVetView",

  components: {
    VBreadcrumds,
    VButton,
    VInput,
    VSelect,
    VHeroItem,
    VHeroItemLoader,
  },

  props: {},

  data() {
    return {
      allVeterans: [], // ВСЕ ветераны с бэка
      filteredVeterans: [], // Отфильтрованные
      resultsLimit: 10,
      listTotal: 0,
      isListLoading: false,
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

      showMoreFilters: false,

      filtersSelects: {
        conflict: {
          label: "Выберите конфликт",
          placeholder: "Выберите конфликт",
          options: ["СВО", "Великая отечественная война"],
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
        servicePlace: {
          label: "Место службы",
          placeholder: "Введите место службы",
          options: [], // Это поле можно либо оставить пустым, либо заменить на обычный `VInput`, если оно не предполагает выбор
        },
      },
      // veterans: [],
      listTotal: null,
      // resultsLimit: 8,

      displayedVeterans: [],
      isFiltersLoading: false,
    };
  },

  computed: {},

  methods: {
    async getVeterans() {
      try {
        this.isListLoading = true;
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/veterans/`);

        console.log(response.data);
        this.allVeterans = response.data.results;
        this.filteredVeterans = this.allVeterans.slice();
        this.listTotal = this.filteredVeterans.length;
        this.resultsLimit = 10;

        // При первой загрузке показываем первые 10
        this.resultsLimit = 10;
        // this.allVeterans = response.data.results.map((item) => item._custom.value);
        // this.filteredVeterans = this.allVeterans;
        // this.displayedVeterans = this.filteredVeterans.slice(0, this.resultsLimit);

        this.listTotal = response.data.count;
        // this.veterans = response.data.results;
      } catch (error) {
        console.log(error);
      } finally {
        this.isListLoading = false;
      }
    },

    applyFilters() {
      // Фильтруем this.allVeterans по текущим this.filters
      this.filteredVeterans = this.allVeterans.filter((vet) => {
        // Пример простой фильтрации по lastName, firstName, middleName
        const matchLastName = this.filters.lastName
          ? vet.last_name
              .toLowerCase()
              .includes(this.filters.lastName.toLowerCase())
          : true;

        const matchFirstName = this.filters.firstName
          ? vet.first_name
              .toLowerCase()
              .includes(this.filters.firstName.toLowerCase())
          : true;

        const matchMiddleName = this.filters.middleName
          ? vet.middle_name
              .toLowerCase()
              .includes(this.filters.middleName.toLowerCase())
          : true;

        // Фильтрация по датам рождения (если указаны)
        const birthDateFrom = this.filters.birthDateFrom
          ? new Date(this.filters.birthDateFrom)
          : null;
        const birthDateTo = this.filters.birthDateTo
          ? new Date(this.filters.birthDateTo)
          : null;
        const vetBirthDate = new Date(vet.birth_date);

        const matchBirthDateFrom = birthDateFrom
          ? vetBirthDate >= birthDateFrom
          : true;
        const matchBirthDateTo = birthDateTo
          ? vetBirthDate <= birthDateTo
          : true;

        // Фильтрация по конфликту
        const matchConflict = this.filters.conflict
          ? vet.conflict?.name === this.filters.conflict
          : true;

        // Фильтрация по званию
        const matchRank = this.filters.rank
          ? vet.military_rank?.name === this.filters.rank
          : true;

        // Фильтрация по виду ВС
        const matchArmyType = this.filters.armyType
          ? vet.branch_of_service?.name === this.filters.armyType
          : true;

        // Фильтрация по роду войск
        const matchArmyBranch = this.filters.armyBranch
          ? vet.military_unit === this.filters.armyBranch
          : true;

        // Фильтрация по месту службы (поиск подстроки)
        const matchServicePlace = this.filters.servicePlace
          ? vet.service_place
              .toLowerCase()
              .includes(this.filters.servicePlace.toLowerCase())
          : true;

        return (
          matchLastName &&
          matchFirstName &&
          matchMiddleName &&
          matchBirthDateFrom &&
          matchBirthDateTo &&
          matchConflict &&
          matchRank &&
          matchArmyType &&
          matchArmyBranch &&
          matchServicePlace
        );
      });

      this.listTotal = this.filteredVeterans.length;
    },

    toggleFilterList() {
      this.showMoreFilters = !this.showMoreFilters;
    },

    onSearch() {
      // При клике на "Найти" применяем фильтры и сбрасываем количество видимых результатов
      this.resultsLimit = 10;
      this.applyFilters();
    },

    loadMore() {
      // Добавляем ещё 10 элементов в список видимых
      this.resultsLimit += 10;
    },

    clearFilters() {
      this.filters = {
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
      };
      this.onSearch();
    },
    submitFilters() {
      this.applyFilters();
    },
  },

  watch: {},

  created() {
    this.getVeterans();
  },
  mounted() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<template>
  <div class="container mx-auto px-4 md:px-2">
    <VBreadcrumds />
    <div class="space-y-10">
      <!-- Заголовок -->
      <h1 class="text-3xl font-bold mb-6">Найти ветерана</h1>

      <!-- Форма поиска -->
      <form
        @submit.prevent="onSearch"
        class="bg-white p-4 md:p-6 rounded-xl shadow space-y-6"
      >
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 xl:gap-6">
          <VInput
            label="Фамилия"
            placeholder="Фамилия"
            v-model="filters.lastName"
          />
          <VInput label="Имя" placeholder="Имя" v-model="filters.firstName" />
          <VInput
            label="Отчество"
            placeholder="Отчество"
            v-model="filters.middleName"
          />
          <div
            class="grid md:col-span-3 md:grid-cols-3 gap-3 xl:gap-6"
            v-if="showMoreFilters"
          >
            <VInput
              label="Дата рождения от"
              placeholder="Дата рождения от"
              type="date"
              v-model="filters.birthDateFrom"
            />
            <VInput
              label="Дата рождения до"
              placeholder="Дата рождения до"
              type="date"
              v-model="filters.birthDateTo"
            />
            <VSelect
              v-model="filters.conflict"
              :label="filtersSelects.conflict.label"
              :placeholder="filtersSelects.conflict.placeholder"
              :options="filtersSelects.conflict.options"
            />
            <VSelect
              v-model="filters.rank"
              :label="filtersSelects.rank.label"
              :placeholder="filtersSelects.rank.placeholder"
              :options="filtersSelects.rank.options"
            />
            <VSelect
              v-model="filters.armyType"
              :label="filtersSelects.armyType.label"
              :placeholder="filtersSelects.armyType.placeholder"
              :options="filtersSelects.armyType.options"
            />
            <VSelect
              v-model="filters.armyBranch"
              :label="filtersSelects.armyBranch.label"
              :placeholder="filtersSelects.armyBranch.placeholder"
              :options="filtersSelects.armyBranch.options"
            />
            <VInput
              v-model="filters.servicePlace"
              :label="filtersSelects.servicePlace.label"
              :placeholder="filtersSelects.servicePlace.placeholder"
            />
          </div>
          <div class="col-start-1 cols-span-3">
            <div class="">
              <VButton
                class="max-md:w-full max-md:flex justify-center max-md:!text-xs"
                @click.prevent.stop="toggleFilterList"
                >{{
                  !showMoreFilters
                    ? "Показать больше фильтров"
                    : "Скрыть дополнительные фильтры"
                }}</VButton
              >
            </div>
          </div>
        </div>

        <div class="flex gap-4">
          <VButton
            @click.prevent.stop="submitFilters"
            type="submit"
            class="!text-base"
          >
            <span v-if="isListLoading" class="animate-spin"
              ><svg
                width="24"
                height="24"
                class="*:fill-white"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M12 2.25C17.3848 2.25 21.75 6.61522 21.75 12C21.75 17.3848 17.3848 21.75 12 21.75C6.61522 21.75 2.25 17.3848 2.25 12C2.25 10.4448 2.61447 8.97237 3.26367 7.66602C3.44804 7.29514 3.89863 7.1438 4.26953 7.32812C4.6404 7.51249 4.79174 7.96308 4.60742 8.33398C4.05901 9.43754 3.75 10.6816 3.75 12C3.75 16.5563 7.44365 20.25 12 20.25C16.5563 20.25 20.25 16.5563 20.25 12C20.25 7.44365 16.5563 3.75 12 3.75C11.5858 3.75 11.25 3.41421 11.25 3C11.25 2.58579 11.5858 2.25 12 2.25Z"
                  fill="black"
                />
              </svg>
            </span>
            <span v-else>Найти</span>
          </VButton>
          <VButton
            class="bg-gray-400 text-white px-6 py-2 rounded hover:bg-gray-500 transition"
            @click="clearFilters"
          >
            <span v-if="isListLoading" class="animate-spin"
              ><svg
                width="24"
                height="24"
                class="*:fill-white"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M12 2.25C17.3848 2.25 21.75 6.61522 21.75 12C21.75 17.3848 17.3848 21.75 12 21.75C6.61522 21.75 2.25 17.3848 2.25 12C2.25 10.4448 2.61447 8.97237 3.26367 7.66602C3.44804 7.29514 3.89863 7.1438 4.26953 7.32812C4.6404 7.51249 4.79174 7.96308 4.60742 8.33398C4.05901 9.43754 3.75 10.6816 3.75 12C3.75 16.5563 7.44365 20.25 12 20.25C16.5563 20.25 20.25 16.5563 20.25 12C20.25 7.44365 16.5563 3.75 12 3.75C11.5858 3.75 11.25 3.41421 11.25 3C11.25 2.58579 11.5858 2.25 12 2.25Z"
                  fill="black"
                />
              </svg>
            </span>
            <span v-else>Очистить фильтры</span>
          </VButton>
        </div>
      </form>

      <!-- Результаты поиска -->
      <section>
        <h2 class="text-xl font-semibold mb-4">Найдено: {{ listTotal }}</h2>

        <div
          v-if="filteredVeterans.length != 0 && !isListLoading"
          class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 xl:gap-6"
        >
          <VHeroItem
            v-for="vet in filteredVeterans.slice(0, resultsLimit)"
            :key="vet"
            :vet="vet"
          />
        </div>
        <div
          v-else-if="filteredVeterans.length == 0 && !isListLoading"
          class="text-gray-600"
        >
          Нет подходящих результатов поиска. Измените поисковый запрос или
          параметры фильтрации.
        </div>
        <div
          class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4 xl:gap-6"
          v-else
        >
          <VHeroItemLoader v-for="vet in 6" :key="vet" />
        </div>

        <div class="text-center mt-6">
          <VButton @click="loadMore">
            <span v-if="isListLoading" class="animate-spin"
              ><svg
                width="24"
                height="24"
                class="*:fill-white"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M12 2.25C17.3848 2.25 21.75 6.61522 21.75 12C21.75 17.3848 17.3848 21.75 12 21.75C6.61522 21.75 2.25 17.3848 2.25 12C2.25 10.4448 2.61447 8.97237 3.26367 7.66602C3.44804 7.29514 3.89863 7.1438 4.26953 7.32812C4.6404 7.51249 4.79174 7.96308 4.60742 8.33398C4.05901 9.43754 3.75 10.6816 3.75 12C3.75 16.5563 7.44365 20.25 12 20.25C16.5563 20.25 20.25 16.5563 20.25 12C20.25 7.44365 16.5563 3.75 12 3.75C11.5858 3.75 11.25 3.41421 11.25 3C11.25 2.58579 11.5858 2.25 12 2.25Z"
                  fill="black"
                />
              </svg>
            </span>
            <span v-else>Показать больше</span>
          </VButton>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.med::-webkit-scrollbar {
  height: 6px;
}
.med::-webkit-scrollbar-thumb {
  background-color: #fbbf24; /* amber-400 */
  border-radius: 3px;
}
</style>
