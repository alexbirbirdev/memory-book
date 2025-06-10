<script>
import axios from "axios";
import VHeroItem from "@/components/common/VHeroItem.vue";
import VButton from "@/components/form/VButton.vue";
import VInput from "@/components/form/VInput.vue";
import VSelect from "@/components/form/VSelect.vue";
import VHeroItemLoader from "@/components/loaders/VHeroItemLoader.vue";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";
import VDocumentItem from "@/components/common/VDocumentItem.vue";

export default {
  name: "DocumentsView",

  components: {
    VBreadcrumds,
    VButton,
    VInput,
    VSelect,
    VHeroItem,
    VHeroItemLoader,
    VDocumentItem,
  },

  props: {},

  data() {
    return {
      showMoreFilters: false,

      form: {
        title: "",
        district: "", // Район/округ
        operation: "", // Боевая операция
        militaryUnit: "", // Воинская часть
        documentAuthor: "", // Автор документа
        dateStart: "", // Дата начала
        dateEnd: "", // Дата окончания
        documentNumber: "", // Номер документа
        archiveFund: "", // Фонд
        archiveInventory: "", // Опись
        archiveCase: "", // Дело
      },
      resultsLimit: 8,

      isListLoading: false,
      canShowMore: false,

      docs: [],
    };
  },

  computed: {},

  methods: {
    toggleFilterList() {
      this.showMoreFilters = !this.showMoreFilters;
    },
    onSearch() {
      // Просто сбрасываем лимит, чтобы показать первые результаты после фильтрации
      this.resultsLimit = 8;
    },

    loadMore() {
      this.resultsLimit += 8;
    },

    clearFilters() {
      this.form = {
        title: "",
        district: "", // Район/округ
        operation: "", // Боевая операция
        militaryUnit: "", // Воинская часть
        documentAuthor: "", // Автор документа
        dateStart: "", // Дата начала
        dateEnd: "", // Дата окончания
        documentNumber: "", // Номер документа
        archiveFund: "", // Фонд
        archiveInventory: "", // Опись
        archiveCase: "", // Дело
      };
      this.onSearch();
    },
    submitFilters() {
      console.log(this.filters);
    },

    async getDocs() {
      try {
        this.isListLoading = true;

        const response = await axios.get(`${import.meta.env.VITE_API_URL}/documents`);
        this.docs = response.data.results
        console.log(response.data);
      } catch (error) {
        console.log(error);
      } finally {
        this.isListLoading = false;
      }
    },
  },

  watch: {},

  created() {
    this.getDocs();
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
      <h1 class="text-3xl font-bold mb-6">Найти документ</h1>

      <!-- Форма поиска -->
      <form
        @submit.prevent="onSearch"
        class="bg-white p-4 md:p-6 rounded-xl shadow space-y-6"
      >
        <div class="grid grid-cols-1 md:grid-cols-3 gap-3 xl:gap-6">
          <VInput
            label="Название документа"
            placeholder="Название документа"
            v-model="form.title"
          />
          <VInput
            label="Район/округ"
            placeholder="Район/округ"
            v-model="form.district"
          />
          <VInput
            label="Боевая операция"
            placeholder="Боевая операция"
            v-model="form.operation"
          />

          <div
            class="grid md:col-span-3 md:grid-cols-3 gap-3 xl:gap-6"
            v-if="showMoreFilters"
          >
            <VInput
              label="Воинская часть"
              placeholder="Воинская часть"
              v-model="form.militaryUnit"
            />
            <VInput
              label="Автор документа"
              placeholder="Автор документа"
              v-model="form.documentAuthor"
            />
            <VInput
              label="Дата начала"
              placeholder="Дата начала"
              v-model="form.dateStart"
              type="date"
            />
            <VInput
              label="Дата окончания"
              placeholder="Дата окончания"
              v-model="form.dateEnd"
              type="date"
            />
            <VInput
              label="Номер документа"
              placeholder="Номер документа"
              v-model="form.documentNumber"
            />
            <VInput
              label="Фонд"
              placeholder="Фонд"
              v-model="form.archiveFund"
            />
            <VInput
              label="Опись"
              placeholder="Опись"
              v-model="form.archiveInventory"
            />
            <VInput
              label="Дело"
              placeholder="Дело"
              v-model="form.archiveCase"
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
        <h2 class="text-xl font-semibold mb-4">
          Найдено:
          {{ docs.length }}
        </h2>

        <div v-if="!isListLoading" class="flex flex-col gap-4">
          <VDocumentItem v-for="doc in docs" :key="doc" :doc="doc"  />
        </div>
        <div v-if="!isListLoading && !docs.length" class="flex flex-col gap-4">
          Документов нет
        </div>


        <div v-if="canShowMore" class="text-center mt-6">
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
