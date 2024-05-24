import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import * as echarts from 'echarts'
import "./assets/icons/iconfont.css";
import "./assets/icons/iconfont.svg";
import "@/icons";
import "@/uni";
import "@/assets/css/reset.css"

Vue.config.productionTip = false;

Vue.prototype.$echarts = echarts

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
