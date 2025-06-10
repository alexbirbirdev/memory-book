<script>
import axios from "axios";
import VButton from "@/components/form/VButton.vue";
import VLoader from "@/components/loaders/VLoader.vue";
import VBreadcrumds from "@/components/UI/VBreadcrumds.vue";

export default {
  name: "HeroesItemView",

  components: {
    VBreadcrumds,
    VButton,
    VLoader,
  },

  props: {},

  data() {
    return {
      vet: {
        id: 1,
        image: "https://placehold.co/90x160",
        lastName: "Иванов",
        firstName: "Пётр",
        middleName: "Александрович",
        birthDate: "1925-06-15",
        armyType: "Сухопутные войска",
        armyBranch: "Пехота",
        rank: "Сержант",
        militaryUnit: "101-й стрелковый полк",
        battle: "ВОВ",
        awards: ["Орден Славы", "Медаль За отвагу"],
      },
      veteran: null,
      biography: [
        {
          title: "1941 – Начало службы",
          description: "Призван в армию в июне 1941 года.",
        },
        {
          title: "1943 – Награда",
          description: 'Награждён медалью "За отвагу".',
        },
        // ...
      ],
      documents: [
        {
          name: "Удостоверение ветерана",
          format: "PDF",
          size: "1.2 MB",
          url: "/files/doc1.pdf",
        },
        {
          name: "Фотография",
          format: "JPG",
          size: "800 KB",
          url: "/files/photo.jpg",
        },
        // ...
      ],
      recommended: [
        {
          url: "1",
          image: "https://placehold.co/160x90",
          title: "История полка",
          description: "Краткий обзор истории полка, в котором служил ветеран.",
        },
        {
          url: "2",
          image: "https://placehold.co/160x90",
          title: "Архивные документы",
          description: "Сборник архивных материалов времён войны.",
        },
        // до 3-х
      ],
      isLoading: false,
    };
  },

  computed: {},

  methods: {
    download(url) {
      const a = document.createElement("a");
      a.href = url;
      a.download = "";
      a.click();
    },
    formatDate(dateStr) {
      if (!dateStr) return "";
      const d = new Date(dateStr);
      return d.toLocaleDateString("ru-RU");
    },
    async getVeteran() {
      try {
        this.isLoading = true;
        const response = await axios.get(
          `${import.meta.env.VITE_API_URL}/veterans/` + this.$route.params.id
        );

        console.log(response.data);
        this.veteran = response.data;
        this.$route.meta.title = response.data.full_name;
        // this.newsTitle = response.data.title;
      } catch (error) {
        console.log(error.response.data);
        this.$router.push("/heroes/");
      } finally {
        this.isLoading = false;
      }
    },
  },

  watch: {},

  created() {
    this.getVeteran();
  },
  mounted() {},
  updated() {},
  beforeUnmount() {},
  unmounted() {},
};
</script>

<template>
  <div class="container mx-auto px-4">
    <VBreadcrumds v-if="!isLoading" />
    <div class="grid lg:grid-cols-2 xl:grid-cols-3 gap-4">
      <!-- Основная информация -->
      <div class="flex flex-col gap-4">
        <div
          v-if="!isLoading"
          class="max-lg:hidden aspect-[3/4] shadow rounded-2xl bg-center bg-cover"
          :style="'background-image: url(' + $formatImageUrl(veteran.photo) + ')'"
        ></div>
        <VLoader v-else class="w-full aspect-[3/4]" />

        <section
          v-if="!isLoading"
          class="bg-white p-4 sm:p-6 rounded-2xl shadow"
        >
          <h2 class="text-2xl font-bold mb-4">Документы</h2>
          <ul class="space-y-4">
            <li
              v-for="(doc, index) in documents"
              :key="index"
              class="flex items-center justify-between bg-gray-100 p-4 gap-2 rounded-xl hover:bg-gray-200 cursor-pointer"
              @click="download(doc.url)"
            >
              <div class="flex items-center gap-3">
                <!-- <img src="/icons/file-icon.svg" class="w-6 h-6" alt="file icon" /> -->
                <div>
                  <p class="font-semibold">{{ doc.name }}</p>
                  <p class="text-sm text-gray-500">
                    {{ doc.format }} • {{ doc.size }}
                  </p>
                </div>
              </div>
              <button class="text-blue-600 underline">Скачать</button>
            </li>
          </ul>
        </section>
        <section v-else class="bg-white p-4 sm:p-6 rounded-2xl shadow">
          <VLoader class="h-8 w-7/10 mb-4" />
          <ul class="space-y-4">
            <VLoader class="h-19 w-full" v-for="el in 2" :key="el" />
          </ul>
        </section>
      </div>

      <div class="xl:col-span-2 flex flex-col gap-4 max-lg:row-start-1">
        <div
          v-if="!isLoading"
          class="lg:hidden aspect-[3/4] shadow rounded-2xl bg-center bg-cover"
          :style="'background-image: url(' + veteran.photo + ')'"
        ></div>
        <VLoader v-else class="w-full aspect-[3/4]" />
        <div v-if="!isLoading" class="bg-white p-4 sm:p-6 rounded-2xl shadow">
          <h2
            class="text-2xl mb-4 flex gap-2 items-center justify-start flex-wrap font-bold"
          >
            <span v-if="veteran.full_name">{{ veteran.full_name }}</span>
          </h2>
          <div class="space-y-2 text-gray-700">
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.birth_date"
            >
              <div class="text-sm">Дата рождения:</div>
              <div class="font-bold">{{ formatDate(veteran.birth_date) }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.death_date"
            >
              <div class="text-sm">Дата смерти:</div>
              <div class="font-bold">{{ formatDate(veteran.death_date) }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.veteran_type_display"
            >
              <div class="text-sm">Дата смерти:</div>
              <div class="font-bold">{{ veteran.veteran_type_display }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.branch_of_service"
            >
              <div class="text-sm">Вид вооруженных сил:</div>
              <div class="font-bold">{{ veteran.branch_of_service.name }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="vet.armyBranch"
            >
              <div class="text-sm">Род войск:</div>
              <div class="font-bold">{{ vet.armyBranch }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.military_rank"
            >
              <div class="text-sm">Звание:</div>
              <div class="font-bold">{{ veteran.military_rank.name }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.military_unit"
            >
              <div class="text-sm">Воинское формирование:</div>
              <div class="font-bold">{{ veteran.military_unit }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.conflict"
            >
              <div class="text-sm">Сражение:</div>
              <div class="font-bold">{{ veteran.conflict.name }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.service_place"
            >
              <div class="text-sm">Место службы:</div>
              <div class="font-bold">{{ veteran.service_place }}</div>
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center lg:gap-4"
              v-if="veteran.call_place"
            >
              <div class="text-sm">Место призыва:</div>
              <div class="font-bold">{{ veteran.call_place }}</div>
            </div>

            <!-- Кнопки действий -->
            <div class="flex flex-wrap gap-3 mt-6">
              <VButton>Поделиться</VButton>
              <VButton>Связаться с автором</VButton>
              <VButton v-if="vet.image">Распечатать фото</VButton>
              <VButton>Заявка на шествие</VButton>
            </div>
          </div>
        </div>
        <div v-else class="bg-white p-4 sm:p-6 rounded-2xl shadow">
          <VLoader class="h-8 w-1/2 mb-4" />
          <div class="space-y-2 text-gray-700">
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center gap-1 lg:gap-4"
            >
              <VLoader class="h-5 w-14" />
              <VLoader class="h-5 w-30" />
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center gap-1 lg:gap-4"
            >
              <VLoader class="h-5 w-14" />
              <VLoader class="h-5 w-30" />
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center gap-1 lg:gap-4"
            >
              <VLoader class="h-5 w-14" />
              <VLoader class="h-5 w-30" />
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center gap-1 lg:gap-4"
            >
              <VLoader class="h-5 w-14" />
              <VLoader class="h-5 w-30" />
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center gap-1 lg:gap-4"
            >
              <VLoader class="h-5 w-14" />
              <VLoader class="h-5 w-30" />
            </div>
            <div
              class="flex max-lg:flex-col max-lg:items-start justify-start items-center gap-1 lg:gap-4"
            >
              <VLoader class="h-5 w-14" />
              <VLoader class="h-5 w-30" />
            </div>
            <div class="flex flex-col gap-1" v-if="vet.awards != 0">
              <VLoader class="h-5 w-20" />
              <div class="flex items-center justify-start flex-wrap gap-2">
                <VLoader class="h-8 w-35" v-for="el in 5" :key="el" />
              </div>
            </div>

            <!-- Кнопки действий -->
            <div class="flex flex-wrap gap-3 mt-6">
              <VLoader class="h-9 w-25" />
              <VLoader class="h-9 w-25" />
              <VLoader class="h-9 w-25" />
              <VLoader class="h-9 w-25" />
            </div>
          </div>
        </div>
        <section
          v-if="!isLoading && veteran.biography"
          class="bg-white p-4 sm:p-6 rounded-2xl shadow"
        >
          <h2 class="text-2xl font-bold mb-4">Биография</h2>
          <div class="">{{ veteran.biography }}</div>
          <!-- <ul class="space-y-4">
            <li
              v-for="(item, index) in biography"
              :key="index"
              class="border-l-4 border-blue-500 pl-4 duration-200 hover:bg-sky-50 py-1 rounded-r-2xl"
            >
              <h3 class="font-semibold text-base md:text-lg">
                {{ item.title }}
              </h3>
              <p class="text-gray-700 max-md:text-xs">{{ item.description }}</p>
            </li>
          </ul> -->
        </section>
        <section v-else class="bg-white p-4 sm:p-6 rounded-2xl shadow">
          <VLoader class="h-8 w-1/2 mb-4" />
          <ul class="space-y-4">
            <li v-for="el in 2" :key="el">
              <VLoader class="h-6 w-1/3 mb-1" />
              <VLoader class="h-6 w-2/3" />
            </li>
          </ul>
        </section>

        <section
          v-if="!isLoading && veteran.rewards.length"
          class="bg-white p-4 sm:p-6 rounded-2xl shadow"
        >
          <h2 class="text-2xl font-bold mb-4">Награды</h2>
          <ul class="space-y-4">
            <li
              v-for="(item, index) in veteran.rewards"
              :key="index"
              class="border-l-4 border-blue-500 pl-4 duration-200 hover:bg-sky-50 py-1 rounded-r-2xl"
            >
              <h3 class="font-semibold text-base md:text-lg">
                {{ item.reward.name }}
              </h3>
              <p class="text-gray-700 max-md:text-xs">{{ item.reward.description }}</p>
              <p class="text-gray-600 text-xs mt-1">{{ item.award_date }} {{ item.document_number }} </p>
            </li>
          </ul>
        </section>
        <section v-if="isLoading" class="bg-white p-4 sm:p-6 rounded-2xl shadow">
          <VLoader class="h-8 w-1/2 mb-4" />
          <ul class="space-y-4">
            <li v-for="el in 2" :key="el">
              <VLoader class="h-6 w-1/3 mb-1" />
              <VLoader class="h-6 w-2/3" />
            </li>
          </ul>
        </section>
      </div>

      <!-- Документы -->

      <!-- Биография -->

      <!-- Рекомендованные материалы -->
      <section
        class="bg-white p-4 sm:p-6 rounded-2xl shadow lg:col-span-2 xl:col-span-3"
      >
        <h2 class="text-2xl font-bold mb-4">Рекомендованные материалы</h2>
        <div
          v-if="!isLoading"
          class="grid sm:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-4 gap-6"
        >
          <router-link
            v-for="(material, index) in recommended"
            :key="index"
            :to="'/articles/' + material.url"
            class="bg-gray-50 rounded-xl overflow-hidden shadow hover:shadow-md transition rec-item"
          >
            <img
              :src="$formatImageUrl(material.image)"
              alt="Материал"
              class="w-full aspect-video object-cover"
            />
            <div class="p-4">
              <h3 class="font-semibold text-lg duration-200">
                {{ material.title }}
              </h3>
              <p class="text-gray-600 text-sm mt-2">
                {{ material.description }}
              </p>
            </div>
          </router-link>
        </div>
        <div
          v-else
          class="grid sm:grid-cols-2 lg:grid-cols-3 2xl:grid-cols-4 gap-6"
        >
          <div
            v-for="el in 4"
            class="bg-gray-50 rounded-xl overflow-hidden shadow hover:shadow-md transition rec-item"
          >
            <VLoader class="w-full aspect-video" />
            <div class="p-4">
              <VLoader class="w-2/3 h-7" />
              <VLoader class="w-full h-5 mt-2" />
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<style scoped>
.rec-item:hover h3 {
  color: #1d4ed8;
}
</style>
