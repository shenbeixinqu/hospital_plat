import Layout from "@/uni/layouts";

const screenRouter = {
  path: "/compositeScreen",
  // component: Layout,
  component: () => import('@/views/screen'),
  name: "compositeScreen",
  meta: { 
    title: "医院当年综合数据",
    hidden: true,
  }
}

export default screenRouter