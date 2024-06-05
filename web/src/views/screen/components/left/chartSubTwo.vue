<template>
  <div class="rank-main" :style="{ padding: chartPaddingTwelve + 'px' }">
    <div
      style="color: #0dc1ff"
      class="rank-title"
      :style="{ fontSize: chartFontSixteen + 'px', padding: chartPaddingFour + 'px' }"
    >
      全年接诊科室排名
    </div>
    <ul v-for="(item, index) in rankData" :key="index">
      <li class="rank-area" :style="{ padding: chartPaddingFour + 'px' }">
        <div class="rank-name" :style="{ fontSize: chartFontFourteen + 'px' }">
          <span
            class="iconfont rank-icon"
            :class="rankIconClass(index)"
            :style="{ paddingRight: chartPaddingEight + 'px', fontSize: chartFontFourteen + 'px' }"
          ></span>
          <span :style="{ fontSize: chartFontFourteen + 'px' }">{{ item.name }}</span>
        </div>
        <div class="rank-count">
          <span :style="{ fontSize: chartFontFourteen + 'px' }">{{ item.count }}次</span>
        </div>
      </li>
    </ul>
    <div
      class="rank-button-main"
      :style="{ paddingTop: chartPaddingSix + 'px' }"
    >
      <span
        class="rank-button"
        :style="{
          fontSize: chartFontTwelve + 'px',
          paddingTop: chartPaddingTwo + 'px',
          paddingBottom: chartPaddingTwo + 'px',
          paddingLeft: chartPaddingSix + 'px',
          paddingRight: chartPaddingSix + 'px',
        }"
        >显示所有</span
      >
    </div>
  </div>
</template>

<script>
import { chartLeftTopTwo } from "@/api/screen/home";

export default {
  data() {
    return {
      rankData: [],
      chartFontTwelve: 0,
      chartFontFourteen: 0,
      chartFontSixteen: 0,
      chartPaddingTwo: 0,
      chartPaddingFour: 0,
      chartPaddingSix: 0,
      chartPaddingEight: 0,
      chartPaddingTwelve: 0,

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
    // 排名图标(val) {
    rankIconClass(val) {
      if (val === 0) {
        return "icon-jinpai";
      } else if (val === 1) {
        return "icon-yinpai";
      } else if (val === 2) {
        return "icon-tongpai";
      } else if (val === 3) {
        return "icon-icon-test6";
      } else if (val === 4) {
        return "icon-icon-test4";
      } else if (val === 5) {
        return "icon-icon-test";
      } else if (val === 6) {
        return "icon-icon-test5";
      } else if (val === 7) {
        return "icon-icon-test2";
      } else if (val === 8) {
        return "icon-icon-test3";
      } else if (val === 9) {
        return "icon-icon-test1";
      }
    },
    getData() {
      chartLeftTopTwo().then((res) => {
        if (res.code === 200) {
          this.rankData = res.datas;
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
      this.chartFontTwelve = Math.round(this.screenWidth / 133);
      this.chartFontFourteen = Math.round(this.screenWidth / 114);
      this.chartFontSixteen = Math.round(this.screenWidth / 100);
      this.chartPaddingTwo = Math.round(this.screenWidth / 800);
      this.chartPaddingFour = Math.round(this.screenWidth / 400);
      this.chartPaddingSix = Math.round(this.screenWidth / 267);
      this.chartPaddingEight = Math.round(this.screenWidth / 200);
      this.chartPaddingTwelve = Math.round(this.screenWidth / 133);
    },
  },
};
</script>

<style lang="scss" scoped>
.rank-main {
  color: white;
  .rank-title {
    color: "#0dc1ff";
  }
}

.rank-area {
  display: flex;
  justify-content: space-between;
  align-items: center;
}


.rank-button-main {
  display: flex;
  justify-content: center;
}
.rank-button {
  color: #0dc1ff; /* 文字颜色 */
  border: 1px solid #0dc1ff; /* 边框颜色与宽度 */
  border-radius: 10px; /* 圆角边框半径 */
  cursor: pointer; /* 鼠标悬停时显示手形图标 */
  transition: all 0.3s ease; /* 平滑过渡效果 */
}

.rank-button:hover {
  background-color: #0056b3; /* 鼠标悬停时的背景颜色 */
  border-color: #0056b3; /* 鼠标悬停时的边框颜色 */
}
</style>