import Vue from "vue";
import VueRouter from "vue-router";
import Layout from "@/uni/layouts";
import systemRouter from './modules/systemManage'
import screenRouter from "./modules/screen";
import roleRouter from './modules/roleManage'
import { publicPath, routerMode } from "@/config";
Vue.use(VueRouter);

export const constantRoutes = [
  {
    path: "/login",
    component: () => import("@/views/login"),
    meta: {
      hidden: true,
    },
  },
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
    path: "/",
    component: Layout,
    redirect: "/index",
    meta: {
      title: "系统首页",
      levelHidden: true,
    },
    children: [
      {
        path: "index",
        name: "Index",
        component: () => import("@/views/index"),
        meta: {
          title: "系统首页"
        },
      },
    ],
  },
  systemRouter,
  roleRouter,
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

function createRouter(routes = constantRoutes) {
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
