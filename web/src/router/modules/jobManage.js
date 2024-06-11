import Layout from "@/uni/layouts";


const jobRouter = {
  path: "/job",
  name: "job",
  component: Layout,
  meta: {
    title: "工种管理",
    levelHidden: true,
  },
  children: [
    {
      path: "JobManage",
      name: "JobManage",
      component: () => import("@/views/jobManage/jobSetting"),
      meta: {
        title: "工种管理"
      }
    }
  ]
}

export default jobRouter