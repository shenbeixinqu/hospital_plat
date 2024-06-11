import Layout from "@/uni/layouts";


const departRouter = {
  path: "/departManage",
  name: "departManage",
  component: Layout,
  meta: {
    title: "组织管理"
  },
  children: [
    {
      path: "departSetting",
      name: "departSetting",
      component: () => import("@/views/departManage"),
      meta: {
        title: "组织管理"
      }
    }
  ]
}

export default departRouter