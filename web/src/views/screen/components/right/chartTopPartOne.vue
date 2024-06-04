<template>
  <div id="part-one" :style="{ height: chartHeight + 'px', padding: chartPaddingFourteen + 'px' }">
    <div class="first" :style="{ fontSize: chartFontSixteen + 'px' }">
      质量检测(全年)
    </div>
    <div class="container">
      <div class="column-left">
        <div
          class="column"
          v-for="(item, index) in leftColumnData"
          :key="index"
          :style="{paddingBottom: chartPaddingEight + 'px'}"
        >
          <img src="@/assets/bg_image/icon.png" alt="描述文字" :style="{ width: chartImgWidth + 'px', height: chartImgWidth + 'px'}" />
          <div
            class="desc"
            :style="{ paddingLeft: chartPaddingEight + 'px'}"
          >
            <div :style="{ fontSize: chartFontTwelve + 'px'}">{{ item.name }}</div>
            <div class="info">
              <span
                class="count"
                :style="{ fontSize: chartFontEighteen + 'px'}"
              > {{ item.value }} </span>
              <span :style="{ fontSize: chartFontTwelve + 'px'}">人次</span>
            </div>
          </div>
        </div>
      </div>
      <div class="column-right">
        <div
          class="column"
          v-for="(item, index) in rightColumnData"
          :key="index"
          :style="{paddingBottom: chartPaddingEight + 'px'}"
        >
          <img src="@/assets/bg_image/icon.png" alt="描述文字" :style="{ width: chartImgWidth + 'px', height: chartImgWidth + 'px'}" />
          <div
            class="desc"
            :style="{ paddingLeft: chartPaddingEight + 'px'}"
          >
            <div :style="{ fontSize: chartFontTwelve + 'px'}">{{ item.name }}</div>
            <div class="info">
              <span 
                class="count"
                :style="{ fontSize: chartFontEighteen + 'px'}"
              > {{ item.value }} </span>
              <span :style="{ fontSize: chartFontTwelve + 'px'}">人次</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { chartRightTopOne } from "@/api/screen/home";

export default {
  data() {
    return {
      datas: [],
      leftColumnData: [],
      rightColumnData: [],
      // 页面宽高
      screenHeight:
        window.innerHeight ||
        document.documentElement.clientHeight ||
        document.body.clientHeight,
      screenWidth:
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth,

      chartTime: null,
      chartWidth: 0,
      chartHeight: 0,
      chartFontTwelve: 0,
      chartFontSixteen: 0,
      chartFontEighteen: 0,
      chartPaddingEight: 0,
      chartPaddingFourteen: 0,
      chartImgWidth: 0,

    };
  },
  beforeMount() {
    this.chartHeight = Math.round(this.screenHeight * 0.24);
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
    getData() {
      chartRightTopOne().then((res) => {
        if (res.code === 200) {
          this.datas = res.datas;
          this.leftColumnData = res.datas.slice(0, 3);
          this.rightColumnData = res.datas.slice(3)
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
      // 四舍五入取整数
      this.chartHeight = Math.round(this.screenHeight * 0.24);
    },
    // 字体大小根据宽度自适应
    getScreenWidth() {
      this.screenWidth =
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth;
      this.chartFontTwelve = Math.round(this.screenWidth / 133);
      this.chartFontSixteen = Math.round(this.screenWidth / 100);
      this.chartFontEighteen = Math.round(this.screenWidth / 89);
      this.chartPaddingEight = Math.round(this.screenWidth / 200);
      this.chartPaddingFourteen = Math.round(this.screenWidth / 114);
      this.chartImgWidth = Math.round(this.screenWidth / 50);
      
    },
  },
};
</script>

<style lang="scss" scoped>
#part-one {
  .first {
    height: 20%;
    font-weight: 700;
    color: #0dc1ff;
  }
  .container {
    height: 80%;
    display: flex;
    justify-content: space-between;
    color: white;
  }
  .column-left,
  .column-right {
    width: 50%;
  }
  .column {
    display: flex;
  }
  
  .desc {
    display: flex;
    flex-direction: column;
  }
  .info {
    color: #0dc1ff;
  }
  .count {
    font-weight: 700;
  }
  
}
</style>