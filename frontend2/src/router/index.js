import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ArticleListView from "@/views/ArticleListView.vue";
import FindVetView from "@/views/FindVetView.vue";
import AddVeteranView from "@/views/AddVeteranView.vue";
import HeroesItemView from "@/views/HeroesItemView.vue";
import NewsListView from "@/views/NewsListView.vue";
import NewsDetailView from "@/views/NewsDetailView.vue";
import ArticleDetailView from "@/views/ArticleDetailView.vue";
import DocumentsView from "@/views/DocumentsView.vue";
import SearchResultView from "@/views/SearchResultView.vue";
import EventsView from "@/views/EventsView.vue";
import EventItemView from "@/views/EventItemView.vue";
// import NotFoundView from "@/views/NotFoundView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      meta: {
        title: "Главная",
      },
    },

    {
      path: "/heroes/",
      name: "heroes",
      component: FindVetView,
      meta: {
        title: "Найти ветерана",
      },
    },
    {
      path: "/heroes/:id",
      name: "HeroDetail",
      component: HeroesItemView,
      meta: {
        parent: "Найти ветерана",
        title: "Ветераны",
      },
    },
    {
      path: "/heroes/add",
      name: "add-veteran",
      component: AddVeteranView,
      meta: {
        parent: "Найти ветерана",
        title: "Добавить ветерана",
      },
    },
    {
      path: "/news/",
      name: "NewsList",
      component: NewsListView,
      meta: {
        title: "Новости",
      },
    },
    {
      path: "/news/:id",
      name: "NewsDetail",
      component: NewsDetailView,
      meta: {
        parent: "Новости",
        title: "Новоcть",
      },
    },
    {
      path: "/articles/",
      name: "articles",
      component: ArticleListView,
      meta: {
        title: "Статьи",
      },
    },
    {
      path: "/articles/:id",
      name: "ArticleDetailView",
      component: ArticleDetailView,
      meta: {
        parent: "Статьи",
        title: "Название статьи",
      },
    },
    {
      path: "/documents/",
      name: "DocumentsView",
      component: DocumentsView,
      meta: {
        title: "Документы",
      },
    },
    {
      path: "/events/",
      name: "events",
      component: EventsView,
      meta: {
        title: "Анонсы мероприятий",
      },
    },
    {
      path: "/events/:id",
      name: "EventItemView",
      component: EventItemView,
      meta: {
        parent: "Анонсы мероприятий",
        title: "Название мероприятия",
      },
    },
    {
      path: "/search",
      name: "SearchResultView",
      component: SearchResultView,
      meta: {
        title: "Результат поиска",
      },
    },
    {
      path: "/profile",
      name: "profile",
      component: AddVeteranView,
      meta: {
        title: "Профиль",
      },
    },
    // {
    //   path: "/:pathMatch(.*)*",
    //   name: "NotFound",
    //   component: NotFoundView,
    //   meta: {
    //     title: "Страница не найдена",
    //   },
    // },
  ],
});

export default router;
