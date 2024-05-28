import Layout from "@/uni/layouts";

const systemRouter = {
  path: "/systemManage",
  name: "systemManage",
  component: Layout,
  meta: {
    title: "系统管理"
  },
  children: [
    {
      path: "ScreenSetting",
      name: "ScreenSetting",
      component: () => import("@/views/systemManage/ScreenSetting"),
      meta: {
        title: "大屏设置"
      }
    },
    {
      path: "SecurityManage",
      name: "SecurityManage",
      component: () => import("@/views/systemManage/SecurityManage"),
      meta: {
        title: "安全管理"
      }
    },
    {
      path: "AutomaticSetting",
      name: "AutomaticSetting",
      component: () => import("@/views/systemManage/AutomaticSetting"),
      meta: {
        title: "业务报告自动生成设置"
      }
    }
  ]
}

export default systemRouter