import Layout from "@/uni/layouts";

const roleRouter = {
  path: "/roleManage",
  name: "roleManage",
  component: Layout,
  meta: {
    title: "角色管理",
    levelHidden: true,
  },
  children: [
    {
      path: "RoleSetting",
      name: "RoleSetting",
      component: () => import("@/views/roleManage"),
      meta: {
        title: "角色管理"
      }
    }
  ]
}

export default roleRouter
