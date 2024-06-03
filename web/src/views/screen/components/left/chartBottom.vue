<template>
  <div :style="{ height: chartHeight + 'px' }">
    <div style="height: 25%">
      <div
        class="desc"
        :style="{ fontSize: chartFontFourteen + 'px', paddingTop: chartPaddingFourteen + 'px' }"
      >
        <div>
          <div
            :style="{ paddingBottom: chartPaddingFour + 'px', paddingRight: chartPaddingTwenty + 'px'}"  
          >
            全年配送量
            <span style="color: #00ffff">{{ deliveryValue }}</span>
          </div>
          <div
            :style="{ paddingBottom: chartPaddingFour + 'px', paddingRight: chartPaddingTwenty + 'px'}"  
          >
            全年检查项
            <span style="color: #ffe000">{{ examineValue }}</span>
          </div>
        </div>
        <div>
          <div
            :style="{ paddingBottom: chartPaddingFour + 'px', paddingRight: chartPaddingTwenty + 'px'}"  
          >
            全年化验量
            <span style="color: #00cfff">{{ assayValue }}</span>
          </div>
          <div
            :style="{ paddingBottom: chartPaddingFour + 'px', paddingRight: chartPaddingTwenty + 'px'}"  
          >
            全年治疗量
            <span style="color: #ffa800">{{ treatValue }}</span>
          </div>
        </div>
      </div>
    </div>
    <div ref="chart-main" style="height: 75%" />
  </div>
</template>

<script>
import { chartLeftBottom } from "@/api/screen/home";

export default {
  data() {
    return {
      deliveryData: [],
      assayData: [],
      examineData: [],
      treatData: [],
      deliveryValue: "",
      assayValue: "",
      examineValue: "",
      treatValue: "",

      // 页面宽高
      screenHeight:
        window.innerHeight ||
        document.documentElement.clientHeight ||
        document.body.clientHeight,
      screenWidth:
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth,
      chartWidth: 0,
      chartHeight: 0,
      chartFont: 0,
      chartTime: null,
      chart: null,

      chartLabelText: 0,
      chartFontFourteen: 0,
      chartPaddingFour: 0,
      chartPaddingTwelve: 0,
      chartPaddingFourteen: 0,
      chartPaddingTwenty: 0,
    };
  },
  beforeMount() {
    this.chartHeight = Math.round(this.screenHeight * 0.33);
  },
  mounted() {
    // 获取接口数据
    this.getChartData();
    // 页面大小改变时触发
    window.addEventListener("resize", this.getScreenHeight, false);
    // 页面大小改变时触发
    window.addEventListener("resize", this.getScreenWidth, false);
    // 自适应浏览器获取宽高大小定时器
    this.resizeScreen();
    const myChart = this.$echarts.init(this.$refs["chart-main"]);
    this.chart = myChart;
    // 图表初始化
    this.initChart();
    // 调用Echarts图表自适应方法
    this.screenAdapter();    
    // Echarts图表自适应
    window.addEventListener("resize", this.screenAdapter);
  },
  destroyed() {
    // 清除自适应定时器
    clearInterval(this.chartTime);
    this.chartTime = null;
    // 页面大小改变时触发销毁
    window.removeEventListener("resize", this.getScreenHeight, false);
    // 页面大小改变时触发销毁
    window.removeEventListener("resize", this.getScreenWidth, false);
    // Echarts图表自适应销毁
    window.removeEventListener("resize", this.screenAdapter);
  },
  methods: {
    initChart() {
      const option = {
        tooltip: {
          trigger: "axis",
        },
        grid: {
          left: "5%",
          right: "6%",
          top: "15%",
          bottom: "8%",
          containLabel: true,
        },
        xAxis: {
          type: "category",
          boundaryGap: false,
          data: [
            "1月",
            "2月",
            "3月",
            "4月",
            "5月",
            "6月",
            "7月",
            "8月",
            "9月",
            "10月",
            "11月",
            "12月",
          ],
          axisLine: {
            show: true,
            lineStyle: {
              color: "#01fce3",
            },
          },
          axisTick: {
            show: false,
          },
          axisLabel: {
            show: true,
            textStyle: {
              color: "#ebf8ac",
            },
          },
        },
        yAxis: {
          name: "单位: 千人次",
          nameTextStyle: {
            color: "#ebf8ac",
          },
          type: "value",
          splitLine: {
            show: false
          },
          axisTick: {
            show: false,
          },
          axisLine: {
            show: true,
            lineStyle: {
              color: "#fff",
            },
          },
          axisLabel: {
            show: true,
          },
        },
        series: [
          {
            name: "配送量",
            type: "line",
            smooth: true,
            symbol: 'none',
            lineStyle: {
              color: "#00ffff"
            }
          },
          {
            name: "化验量",
            type: "line",
            smooth: true,
            symbol: 'none',
            lineStyle: {
              color: "#00cfff"
            }
          },
          {
            name: "检查项",
            type: "line",
            smooth: true,
            symbol: 'none',
            lineStyle: {
              color: "#ffe000"
            }
          },
          {
            name: "治疗量",
            type: "line",
            smooth: true,
            symbol: 'none',
            lineStyle: {
              color: "#ffa800"
            }
          },
        ],
      };

      this.chart.setOption(option);
    },
    // 获取接口数据
    getChartData() {
      chartLeftBottom().then((res) => {
        if (res.code === 200) {
          this.deliveryData = res.datas.deliveryData;
          this.deliveryValue = res.datas.deliveryValue;
          this.assayData = res.datas.assayData;
          this.assayValue = res.datas.assayValue;
          this.examineData = res.datas.examineData;
          this.examineValue = res.datas.examineValue;
          this.treatData = res.datas.treatData;
          this.treatValue = res.datas.treatValue;
          this.updateChartData();
        } else {
          this.$message({
            type: "error",
            message: res,
          });
        }
      });
    },
    updateChartData() {
      const dataOption = {
        series: [
          {
            data: this.deliveryData,
          },
          {
            data: this.assayData,
          },
          {
            data: this.examineData,
          },
          {
            data: this.treatData,
          },
        ],
      };
      this.chart.setOption(dataOption);
    },
    screenAdapter() {
      this.chartLabelText = Math.round(this.screenWidth / 133);
      const adapterOption = {
        xAxis: {
          axisLabel: {
            textStyle: {
              fontSize: this.chartLabelText
            }
          }
        },
        yAxis: {
          axisLabel: {
            textStyle: {
              fontSize: this.chartLabelText
            }
          },
          nameTextStyle: {
            fontSize: this.chartLabelText
          }
        }
      }
      this.chart.setOption(adapterOption)
      this.chart.resize()
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
      this.chartHeight = Math.round(this.screenHeight * 0.33);
      this.chart.resize()
    },
    // 字体大小根据宽度自适应
    getScreenWidth() {
      this.screenWidth =
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth;
      this.chartWidth = Math.round(this.screenWidth * 0.18);
      this.chartFontFourteen = Math.round(this.screenWidth / 114);
      this.chartPaddingFour = Math.round(this.screenWidth / 400);
      this.chartPaddingFourteen = Math.round(this.screenWidth / 114);
      this.chartPaddingTwelve = Math.round(this.screenWidth / 133);
      this.chartPaddingTwenty = Math.round(this.screenWidth / 80);
      this.chart.resize()
    },
  },
};
</script>

<style lang="scss" scoped>
  .desc {
    display: flex;
    justify-content: center;
    color: #fff;
  }
  .title {
    padding-bottom: 4px;
    padding-right: 20px;
  }
</style>