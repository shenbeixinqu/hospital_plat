import Vue from "vue";
import VueRouter from "vue-router";
import Layout from "@/uni/layouts";
import systemRouter from './modules/systemManage'
import screenRouter from "./modules/screen";
import { publicPath, routerMode } from "@/config";
Vue.use(VueRouter);

export const constantRoutes = [
  {
    path: "/403",
    name: "403",
    component: () => import("@/views/403"),
    meta: {
      hidden: true,
    },
  },
];

export const asyncRoutes = [
  {
    path: "/login",
    component: () => import("@/views/login"),
    meta: {
      hidden: true,
    },
  },
  {
    path: "/",
    name: "Root",
    component: Layout,
    redirect: "/index",
    meta: {
      title: "首页",
    },
    children: [
      {
        path: "index",
        name: "Index",
        component: () => import("@/views/index"),
        meta: {
          title: "首页",
        },
      },
    ],
  },
  systemRouter,
  screenRouter
];

const router = createRouter();

function fatteningRoutes(routes) {
  return routes.flatMap((route) => {
    return route.children ? fatteningRoutes(route.children) : route;
  });
}

export function resetRouter(routes = constantRoutes) {
  routes.map((route) => {
    if (route.children) {
      route.children = fatteningRoutes(route.children);
    }
  });
  router.matcher = createRouter(routes).matcher;
}

function createRouter(routes = asyncRoutes) {
  return new VueRouter({
    // base: process.env.BASE_URL,
    base: publicPath,
    mode: routerMode,
    scrollBehavior: () => ({
      y: 0,
    }),
    routes: routes,
  });
}

// const router = new VueRouter({
//   mode: "history",
//   base: process.env.BASE_URL,
//   routes,
// });

export default router;
