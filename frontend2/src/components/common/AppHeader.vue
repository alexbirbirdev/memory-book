<script>
import VButton from "../form/VButton.vue";
import VInput from "../form/VInput.vue";
import VBurger from "../UI/VBurger.vue";

export default {
  name: "AppHeader",

  components: { VButton, VBurger, VInput },

  props: {},

  data() {
    return {
      navLinks: [
        { name: "Найти ветерана", link: "/heroes/" },
        { name: "Статьи", link: "/articles/" },
        { name: "Документы", link: "/documents/" },
        { name: "Новости", link: "/news/" },
        { name: "Анонсы мероприятий", link: "/events/" },
      ],

      isSearch: false,
      searchInput: "",
      showFixedHeader: false,
      showMobile: false,
    };
  },

  computed: {},

  methods: {
    handleSearch() {
      this.isSearch = !this.isSearch;
      if (this.isSearch) {
        document.body.classList.add("search-active");
      } else {
        document.body.classList.remove("search-active");
        this.searchInput = "";
      }
    },
    handleSearchForm() {
      if (this.searchInput) {
        console.log("form handled: ", this.searchInput);
        this.$router.push("/search");
        this.toggleBurger();
        this.searchInput = "";
        this.handleSearch()
      }
    },
    mobileHandleSearchForm() {
      if (this.searchInput) {
        console.log("form handled: ", this.searchInput);
        this.$router.push("/search");
        this.toggleBurger();
        this.searchInput = "";
        // this.handleSearch()
      }
    },
    checkHeaderScroll() {
      const header = this.$refs.mainHeader;
      if (!header) return;

      const headerBottom = header.getBoundingClientRect().bottom;
      this.showFixedHeader = headerBottom < 0;
    },
    toggleBurger() {
      this.showMobile = !this.showMobile;
      if (this.showMobile) {
        document.body.classList.add("search-active");
      } else {
        document.body.classList.remove("search-active");
      }
    },
  },

  watch: {},

  created() {},
  mounted() {
    window.addEventListener("scroll", this.checkHeaderScroll);
  },
  updated() {},
  beforeUnmount() {
    window.removeEventListener("scroll", this.checkHeaderScroll);
  },
  unmounted() {},
};
</script>

<template>
  <div
    v-if="showMobile"
    class="md:hidden w-full bg-white bottom-0 left-0 fixed z-20 flex justify-center"
    :class="{
      'h-[calc(100%_-_76px)]': showFixedHeader,
      'xs:h-[calc(100%_-_92px)] h-[calc(100%_-_76px)]': !showFixedHeader,
    }"
  >
    <div class="container p-4 flex flex-col items-start gap-7">
      <form @submit.prevent.stop="mobileHandleSearchForm" class="grid gap-2 w-full">
        <div class="text-xl font-bold">Поиск по портелу</div>
        <VInput
          v-model="searchInput"
          :placeholder="'Введите поисковый запрос'"
          :required="true"
        ></VInput>
        <VButton
          class="text-xl flex justify-center text-center"
          type="submit"
          :disabled="!searchInput.length"
          >Найти</VButton
        >
      </form>
      <div class="grid gap-2">
        <div class="text-xl font-bold">Поиск по портелу</div>
        <div class="gap-2 lg:gap-4 text-black flex flex-col items-start">
          <router-link
            exact-active-class="text-[#0A2E5E] before:opacity-100 cursor-default"
            class="hover:text-[#0A2E5E] text-base w-auto duration-200 inline-block relative before:w-full before:h-[2px] before:absolute before:top-full before:left-0 before:opacity-0 before:duration-200 before:bg-[#0A2E5E]"
            :to="link.link"
            v-for="link in navLinks"
            :key="link"
            @click="toggleBurger"
            >{{ link.name }}</router-link
          >
        </div>
      </div>
      <a
        class="hover:text-[#0A2E5E] text-base duration-200 inline-block relative before:w-full before:h-[2px] before:absolute before:top-full before:left-0 before:opacity-0 before:duration-200 before:bg-[#0A2E5E]"
        href="http://memory-book.bybirukov.ru:8100/admin"
        >Профиль</a
      >
    </div>
  </div>

  <!-- Выезжающий fixed-хедер -->
  <div
    class="fixed top-0 left-0 w-full bg-[#0A2E5E] z-50 transition-transform duration-300 flex justify-center"
    :class="{
      'translate-y-0': showFixedHeader,
      '-translate-y-full': !showFixedHeader,
      'min-[1024px]:pr-4': showFixedHeader && isSearch,
    }"
  >
    <div
      class="container flex justify-between items-center px-4 p-2 text-white relative"
    >
      <div class="flex flex-1 justify-start items-center gap-2 md:gap-4">
        <router-link to="/" class="flex items-center gap-2">
          <img src="/images/LOGO1.png" class="h-15" />
          <span
            class="text-base max-xs:leading-[120%] md:hidden xs:text-xl md:text-3xl font-bold"
            >Книга памяти <br class="md:hidden" />
            Красноярского края</span
          >
        </router-link>
        <div class="hidden gap-3 lg:gap-4 text-white md:flex">
          <router-link
            exact-active-class="text-[#FFD700] before:opacity-100 cursor-default"
            class="hover:text-[#FFD700] text-base lg:text-lg duration-200 relative before:w-full before:h-[2px] before:absolute before:top-full before:left-0 before:opacity-0 before:duration-200 before:bg-[#FFD700]"
            :to="link.link"
            v-for="link in navLinks"
            :key="link"
            >{{ link.name }}</router-link
          >
        </div>
      </div>
      <div class="hidden md:block">
        <div
          @click="handleSearch"
          class="p-2 bg-white duration-200 hover:bg-blue-100 hover:scale-105 cursor-pointer rounded-xl flex items-center justify-center"
        >
          <svg
            class="w-5"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M11 2.25C15.8325 2.25 19.75 6.16751 19.75 11C19.75 13.1462 18.9757 15.1106 17.6934 16.6328L20.5303 19.4697L20.582 19.5264C20.8223 19.8209 20.8049 20.2557 20.5303 20.5303C20.2557 20.8049 19.8209 20.8223 19.5264 20.582L19.4697 20.5303L16.6328 17.6934C15.1106 18.9757 13.1462 19.75 11 19.75C6.16751 19.75 2.25 15.8325 2.25 11C2.25 6.16751 6.16751 2.25 11 2.25ZM11 3.75C6.99594 3.75 3.75 6.99594 3.75 11C3.75 15.0041 6.99594 18.25 11 18.25C15.0041 18.25 18.25 15.0041 18.25 11C18.25 6.99594 15.0041 3.75 11 3.75Z"
              fill="black"
            />
          </svg>
        </div>

        <form
          class="duration-200 absolute bottom-2 right-0 bg-white h-[calc(100%_-_16px)] rounded-xl flex items-center justify-between gap-2"
          :class="
            isSearch
              ? 'w-full opacity-100 pr-2 pl-5 z-30'
              : 'opacity-0 w-40 overflow-hidden z-[-1]'
          "
          @submit.prevent.stop="handleSearchForm"
        >
          <input
            class="flex-1 text-black block h-[calc(100%_-_16px)] text-2xl !outline-0"
            placeholder="Введите поисковый запрос"
            type="text"
            id="formSearch"
            v-model="searchInput"
          />
          <VButton
            :disabled="!searchInput.length"
            type="submit"
            class="text-xl select-none"
            >Найти</VButton
          >
          <div
            @click="handleSearch"
            class="p-2 bg-white duration-200 hover:bg-neutral-200 cursor-pointer rounded-xl flex items-center justify-center"
          >
            <svg
              class="w-5"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M17.4698 5.46984C17.7627 5.17695 18.2375 5.17695 18.5304 5.46984C18.8233 5.76274 18.8233 6.2375 18.5304 6.53039L13.0607 12.0001L18.5304 17.4698L18.5821 17.5265C18.8225 17.8211 18.805 18.2558 18.5304 18.5304C18.2558 18.805 17.8211 18.8225 17.5265 18.5821L17.4698 18.5304L12.0001 13.0607L6.53039 18.5304C6.2375 18.8233 5.76274 18.8233 5.46984 18.5304C5.17695 18.2375 5.17695 17.7627 5.46984 17.4698L10.9396 12.0001L5.46984 6.53039L5.41809 6.47375C5.17778 6.17917 5.19524 5.74445 5.46984 5.46984C5.74445 5.19524 6.17917 5.17778 6.47375 5.41809L6.53039 5.46984L12.0001 10.9396L17.4698 5.46984Z"
                fill="black"
              />
            </svg>
          </div>
        </form>
      </div>
      <VBurger
        :isActive="showMobile"
        @toggle="toggleBurger"
        class="md:hidden"
      />
    </div>
  </div>

  <header
    ref="mainHeader"
    class="flex justify-center bg-[#0A2E5E] py-2 xs:py-4"
  >
    <div
      class="fixed w-full h-screen bg-[#0A2E5E]/40 top-0 left-0 duration-200"
      :class="isSearch ? 'opacity-100 z-20' : 'opacity-0 z-[-2]'"
    ></div>
    <div class="container px-4 md:px-2">
      <div class="flex justify-between items-center relative pr-2 gap-2">
        <router-link
          to="/"
          class="flex items-center justify-start gap-2 xs:gap-4 text-white"
        >
          <img src="/images/LOGO1.png" class="h-15" />
          <span
            class="text-base max-xs:leading-[120%] xs:text-xl md:text-3xl font-bold"
            >Книга памяти <br class="md:hidden" />
            Красноярского края</span
          >
        </router-link>

        <VBurger
          :isActive="showMobile"
          @toggle="toggleBurger"
          class="md:hidden"
        />

        <div class="hidden md:block">
          <div
            @click="handleSearch"
            class="p-2 bg-white duration-200 hover:bg-blue-100 hover:scale-105 cursor-pointer rounded-xl flex items-center justify-center"
          >
            <svg
              class="w-5"
              viewBox="0 0 24 24"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M11 2.25C15.8325 2.25 19.75 6.16751 19.75 11C19.75 13.1462 18.9757 15.1106 17.6934 16.6328L20.5303 19.4697L20.582 19.5264C20.8223 19.8209 20.8049 20.2557 20.5303 20.5303C20.2557 20.8049 19.8209 20.8223 19.5264 20.582L19.4697 20.5303L16.6328 17.6934C15.1106 18.9757 13.1462 19.75 11 19.75C6.16751 19.75 2.25 15.8325 2.25 11C2.25 6.16751 6.16751 2.25 11 2.25ZM11 3.75C6.99594 3.75 3.75 6.99594 3.75 11C3.75 15.0041 6.99594 18.25 11 18.25C15.0041 18.25 18.25 15.0041 18.25 11C18.25 6.99594 15.0041 3.75 11 3.75Z"
                fill="black"
              />
            </svg>
          </div>

          <form
            class="duration-200 absolute bottom-0 right-0 bg-white h-full rounded-xl flex items-center justify-between gap-2"
            :class="
              isSearch
                ? 'w-full opacity-100 pr-2 pl-5 z-30'
                : 'opacity-0 w-50 overflow-hidden z-[-1]'
            "
            @submit.prevent.stop="handleSearchForm"
          >
            <input
              class="flex-1 block h-[calc(100%_-_16px)] text-2xl !outline-0"
              placeholder="Введите поисковый запрос"
              type="text"
              id="formSearch"
              v-model="searchInput"
            />
            <VButton
              :disabled="!searchInput.length"
              type="submit"
              class="text-xl select-none"
              >Найти</VButton
            >
            <div
              @click="handleSearch"
              class="p-2 bg-white duration-200 hover:bg-neutral-200 cursor-pointer rounded-xl flex items-center justify-center"
            >
              <svg
                class="w-5"
                viewBox="0 0 24 24"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M17.4698 5.46984C17.7627 5.17695 18.2375 5.17695 18.5304 5.46984C18.8233 5.76274 18.8233 6.2375 18.5304 6.53039L13.0607 12.0001L18.5304 17.4698L18.5821 17.5265C18.8225 17.8211 18.805 18.2558 18.5304 18.5304C18.2558 18.805 17.8211 18.8225 17.5265 18.5821L17.4698 18.5304L12.0001 13.0607L6.53039 18.5304C6.2375 18.8233 5.76274 18.8233 5.46984 18.5304C5.17695 18.2375 5.17695 17.7627 5.46984 17.4698L10.9396 12.0001L5.46984 6.53039L5.41809 6.47375C5.17778 6.17917 5.19524 5.74445 5.46984 5.46984C5.74445 5.19524 6.17917 5.17778 6.47375 5.41809L6.53039 5.46984L12.0001 10.9396L17.4698 5.46984Z"
                  fill="black"
                />
              </svg>
            </div>
          </form>
        </div>
      </div>
      <div class="mt-4 md:flex justify-between items-center hidden">
        <div class="flex gap-4 text-white">
          <router-link
            exact-active-class="text-[#FFD700] before:opacity-100 cursor-default"
            class="hover:text-[#FFD700] text-lg duration-200 relative before:w-full before:h-[2px] before:absolute before:top-full before:left-0 before:opacity-0 before:duration-200 before:bg-[#FFD700]"
            :to="link.link"
            v-for="link in navLinks"
            :key="link"
            >{{ link.name }}</router-link
          >
        </div>
        <a
          href="http://memory-book.bybirukov.ru:8100/admin"
          class="flex items-center duration-200 hover:bg-blue-100 hover:scale-105 justify-center rounded-xl bg-white p-2 mr-2"
        >
          <svg
            class="w-6 *:fill-black"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M15.2441 14.2559C17.754 14.3829 19.75 16.4585 19.75 19C19.75 20.5188 18.5188 21.75 17 21.75H7C5.48122 21.75 4.25 20.5188 4.25 19C4.25 16.3766 6.37665 14.25 9 14.25H15L15.2441 14.2559ZM9 15.75C7.20507 15.75 5.75 17.2051 5.75 19C5.75 19.6904 6.30964 20.25 7 20.25H17C17.6904 20.25 18.25 19.6904 18.25 19C18.25 17.2611 16.8843 15.8408 15.167 15.7539L15 15.75H9ZM12 2.25C14.6234 2.25 16.75 4.37665 16.75 7C16.75 9.62335 14.6234 11.75 12 11.75C9.37665 11.75 7.25 9.62335 7.25 7C7.25 4.37665 9.37665 2.25 12 2.25ZM12 3.75C10.2051 3.75 8.75 5.20507 8.75 7C8.75 8.79493 10.2051 10.25 12 10.25C13.7949 10.25 15.25 8.79493 15.25 7C15.25 5.20507 13.7949 3.75 12 3.75Z"
              fill="black"
            />
          </svg>
        </a>
      </div>
    </div>
  </header>
</template>

<style scoped></style>
