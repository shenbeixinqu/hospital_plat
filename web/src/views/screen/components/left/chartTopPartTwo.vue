<template>
  <div
    id="part-two">
    <div
      class="title"
      style="color: #0dc1ff"
      :style="{ fontSize: chartFontSixteen + 'px', paddingTop: chartPaddingSixteen + 'px', paddingBottom: chartPaddingFour + 'px'}"
    >
      智慧医院好评率最高医生
    </div>
    <div class="container" :style="{ fontSize: chartFontFourteen + 'px'}">
      <div class="column-left" :style="{ padding: chartPaddingTwelve + 'px'}">
        <ul v-for="(item, index) in batchOneData" :key="index">
          <li class="column" :style="{ paddingBottom: chartPaddingFour + 'px'}">
            <div
              class="iconfont"
              :class="rankIconClass(index, '1')"
              :style="{ fontSize: chartFontFourteen + 'px'}"
            ></div>
            <div>{{ item.name }}</div>
            <div>{{ item.radio }}%</div>
          </li>
        </ul>
      </div>

      <div class="column-right" :style="{ padding: chartPaddingTwelve + 'px'}">
        <ul v-for="(item, index) in batchTwoData" :key="index">
          <li class="column" :style="{ paddingBottom: chartPaddingFour + 'px'}">
            <div
              class="iconfont"
              :class="rankIconClass(index, '2')"
              :style="{ fontSize: chartFontFourteen + 'px'}"
            ></div>
            <div>{{ item.name }}</div>
            <div>{{ item.radio }}%</div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>


<script>
import { chartLeftTopThree } from "@/api/screen/home";

export default {
  data() {
    return {
      rankData: [],
      batchOneData: [],
      batchTwoData: [],

      chartFontFourteen: 0,
      chartFontSixteen: 0,
      chartPaddingFour: 0,
      chartPaddingTwelve: 0,
      chartPaddingSixteen: 0,

      chartTime: null,
      // 页面宽高
      screenHeight:
        window.innerHeight ||
        document.documentElement.clientHeight ||
        document.body.clientHeight,
      screenWidth:
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth,
    };
  },
  mounted() {
    this.getData();
    // 页面大小改变时触发
    window.addEventListener("resize", this.getScreenHeight, false);
    // 页面大小改变时触发
    window.addEventListener("resize", this.getScreenWidth, false);
    // 自适应浏览器获取宽高大小定时器
    this.resizeScreen();
  },
  destroyed() {
    // 清除自适应定时器
    clearInterval(this.chartTime);
    this.chartTime = null;
    // 页面大小改变时触发销毁
    window.removeEventListener("resize", this.getScreenHeight, false);
    // 页面大小改变时触发销毁
    window.removeEventListener("resize", this.getScreenWidth, false);
  },
  methods: {
    rankIconClass(val, type) {
      if (type === "1") {
        if (val === 0) {
          return "icon-jinpai";
        } else if (val === 1) {
          return "icon-yinpai";
        } else if (val === 2) {
          return "icon-tongpai";
        }
      } else {
        if (val === 0) {
          return "icon-icon-test6";
        } else if (val === 1) {
          return "icon-icon-test4";
        } else if (val === 2) {
          return "icon-icon-test";
        }
      }
    },
    getData() {
      chartLeftTopThree().then((res) => {
        if (res.code === 200) {
          this.rankData = res.datas;
          this.batchOneData = res.datas.slice(0, 3);
          this.batchTwoData = res.datas.slice(3);
        } else {
          this.$message({
            type: "error",
            message: res,
          });
        }
      });
    },
    resizeScreen() {
      this.chartTime = setInterval(() => {
        this.getScreenHeight();
        this.getScreenWidth();
      }, 200);
    },
    // 获取浏览器高度进行自适应
    getScreenHeight() {
    this.screenHeight =
      window.innerHeight ||
      document.documentElement.innerHeight ||
      document.body.clientHeight;
    },
    // 字体大小根据宽度自适应
    getScreenWidth() {
    this.screenWidth =
      window.innerWidth ||
      document.documentElement.clientWidth ||
      document.body.clientWidth;
      this.chartFontFourteen = Math.round(this.screenWidth / 114);
      this.chartFontSixteen = Math.round(this.screenWidth / 100);
      this.chartPaddingFour = Math.round(this.screenWidth / 400);
      this.chartPaddingSix = Math.round(this.screenWidth / 267);
      this.chartPaddingEight = Math.round(this.screenWidth / 200);
      this.chartPaddingTwelve = Math.round(this.screenWidth / 133);
      this.chartPaddingSixteen = Math.round(this.screenWidth / 100);
    },
  },
};
</script>

<style lang="scss" scoped>
#part-two {
  .title {
    text-align: center;
  }
  .container {
    display: flex;
    justify-content: space-between;
    color: white;
  }
  .column-left,
  .column-right {
    width: 50%;
  }
  .column {
    display: flex; /* 启用Flex布局 */
    justify-content: space-between;
  }
}
</style>