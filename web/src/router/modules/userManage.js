import Layout from "@/uni/layouts";

const userRouter = {
  path: "/users",
  name: "users",
  component: Layout,
  meta: {
    title: "用户管理",
    levelHidden: true
  },
  children: [
    {
      path: "UserManage",
      name: "UserManage",
      component: () => import("@/views/userManage"),
      meta: {
        title: "用户管理",
      },
    }
  ]
}

export default userRouter