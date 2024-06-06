import Layout from "@/uni/layouts";

const roleRouter = {
  path: "/roleManage",
  name: "roleManage",
  component: Layout,
  meta: {
    title: "角色管理"
  },
  children: [
    {
      path: "RoleSetting",
      name: "RoleSetting",
      component: () => import("@/views/roleManage/roleSetting"),
      meta: {
        title: "角色管理"
      }
    }
  ]
}

export default roleRouter
