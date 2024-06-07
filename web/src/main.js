import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import * as echarts from 'echarts'
import "./assets/icons/iconfont.css";
import "./assets/icons/iconfont.svg";
import "./icons";
import "./uni/index"
import "./assets/css/reset.css"
import "./assets/css/screen.scss"
import MyButton from './uni/components/UniButton'; // 调整为你的组件路径

// 全局注册组件
Vue.component('my-button', MyButton);

// 引入DataV,将自动注册所有组件为全局组件
import dataV from '@jiaminghi/data-view';
Vue.use(dataV)

Vue.config.productionTip = false;

Vue.prototype.$echarts = echarts

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
