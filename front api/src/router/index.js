import { createRouter, createWebHistory } from "vue-router";
import Searchlist from "../views/Searchlist.vue";
import Storageview from "../views/Storageview.vue";
const routes = [
  {
    path: "/",
    name: "Searchlist",
    component: Searchlist,
  },
  {
    path: "/storageview",
    name: "Storageview",
    component: Storageview,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
