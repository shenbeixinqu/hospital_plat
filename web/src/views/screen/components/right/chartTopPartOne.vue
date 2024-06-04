<template>
  <div id="part-one" :style="{ height: chartHeight + 'px' }">
    <div class="first" :style="{ fontSize: chartFontSixteen + 'px' }">
      质量检测(全年)
    </div>
    <div class="container">
      <div class="column-left">
        <div class="column">
          <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          <div class="desc">
            <div class="title">接诊后无诊断</div>
            <div class="info">
              <span class="count"> {{ datas.data_one }} </span>人次
            </div>
          </div>
        </div>
        <div class="column">
          <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          <div class="desc">
            <div class="title">医生拒诊</div>
            <div class="info">
              <span class="count"> {{ datas.data_two }} </span>人次
            </div>
          </div>
        </div>
        <div class="column">
          <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          <div class="desc">
            <div class="title">投诉(无方案)</div>
            <div class="info">
              <span class="count"> {{ datas.data_three }} </span>人次
            </div>
          </div>
        </div>
      </div>
      <div class="column-right">
        <div class="column">
          <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          <div class="desc">
            <div class="title">无电子病历</div>
            <div class="info">
              <span class="count"> {{ datas.data_four }} </span>人次
            </div>
          </div>
        </div>
        <div class="column">
          <div>
            <img
              src="@/assets/bg_image/icon.png"
              alt="描述文字"
              class="image"
            />
          </div>
          <div class="desc">
            <div class="title">超时拒诊</div>
            <div class="info">
              <span class="count"> {{ datas.data_five }} </span>人次
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
      datas: {},

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
      chartFontSixteen: 0,
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
          console.log("Res123456", res);
          console.log("datas", this.datas);
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
      this.chartFontSixteen = Math.round(this.screenWidth / 100);
    },
  },
};
</script>

<style lang="scss" scoped>
#part-one {
  padding: 14px;
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
    padding-bottom: 8px;
  }
  .title {
    font-size: 12px;
  }
  .desc {
    display: flex;
    flex-direction: column;
    padding-left: 4px;
  }
  .info {
    color: #0dc1ff;
  }
  .count {
    font-weight: 700;
    font-size: 18px;
  }
  .image {
    width: 34px;
    height: 34px;
  }
}
</style>