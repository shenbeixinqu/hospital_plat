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
      path: "DepartSetting",
      name: "DepartSetting",
      component: () => import("@/views/departManage"),
      meta: {
        title: "组织管理"
      }
    },
    {
      path: "departTree",
      name: "departTree",
      component: () => import("@/views/departManage/departTree"),
      meta: {
        title: "组织架构图"
      }
    },
  ]
}

export default departRouter