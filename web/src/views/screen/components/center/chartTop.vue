<template>
  <div class="line_parent" :style="{ height: chartHeight + 'px' }">
    <!-- 地图容器 -->
    <div>
      <img src="@/assets/bg_image/map_title.png" alt="" />
    </div>
    <div :style="{ paddingLeft: chartPaddingFourteen + 'px'}">
      <button
        class="button"
        :style="{
          fontSize: chartFontTwelve + 'px',
          paddingTop: chartPaddingTwo + 'px',
          paddingBottom: chartPaddingTwo + 'px',
          paddingLeft: chartPaddingSix + 'px',
          paddingRight: chartPaddingSix + 'px',
        }"
      >
        按时段
      </button>
    </div>

    <div ref="chart-main" :style="{ height: chartSubHeight + 'px' }" />
    <!-- 弹窗容器 -->
    <!-- 折线图容器 -->
    <div
      v-show="popupVisible"
      ref="lineChart"
      class="line_popup"
      @click="handlePopup"
    />
  </div>
</template>

<script>
import { chartCenterTop } from "@/api/screen/home";

export default {
  data() {
    return {
      popupVisible: false,
      mapData: [],

      clickDown: false,
      // 用于记录当前被选中的省份
      selectedProvince: null,
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
      chartSubHeight: 0,
      chartFontTwelve: 0,
      chartPaddingTwo: 0,
      chartPaddingSix: 0,
      chartFont: 0,
      chartTime: null,
      chart: null,
      lineChart: null, // 折线图实例
    };
  },
  beforeMount() {
    this.chartHeight = Math.round(this.screenHeight * 0.55);
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
    initChart() {
      let ChinaJSON = require("@/assets/china.json");
      this.$echarts.registerMap("china", ChinaJSON);

      let option = {
        tooltip: {
          trigger: "item",
          formatter: function (params) {
            if (params.value) {
              return params.name + " : " + params.value;
            } else {
              return params.name + " : " + 0;
            }
          },
        },
        visualMap: {
          show: true,
          type: "piecewise",
          calculable: true,
          showLabel: true,
          itemSymbol: "rect",
          left: 20,
          bottom: 30,
          itemWidth: 20,
          itemHeight: 6,
          inRange: {
            // color: ["#00ffff","#00cfff","#ffe000","#ffa800","#ff3000"]
            color: ["#B5CCFF", "#80A8FF", "#5C8FFF", "#2167FF", "#0051FF"],
          },
          padding: 0,
          pieces: [
            { min: 80, label: "80以上", symbol: "rect" }, // 不指定 max，表示 max 为无限大（Infinity）。
            { min: 60, max: 79, label: "60~79", symbol: "rect" }, // 不指定 max，表示 max 为无限大（Infinity）。
            { min: 40, max: 59, label: "40~59", symbol: "rect" },
            { min: 20, max: 39, label: "20~39", symbol: "rect" },
            { min: 0, max: 19, label: "0~19", symbol: "rect" },
          ],
          align: "left",
          itemGap: 5,
          textStyle: {
            color: "#fff",
          },
        },
        geo: {
          map: "china",
          label: {
            emphasis: {
              show: true,
              color: "#fff",
            },
          },
          roam: false,
          //   放大我们的地图
          zoom: 1,
          itemStyle: {
            normal: {
              areaColor: "#B5CCFF",
              borderColor: "rgba(43, 196, 243, 1)",
              borderWidth: 1,
            },
            emphasis: {
              areaColor: "#2B91B7",
            },
          },
        },
        series: [
          {
            type: "map",
            map: "china",
            selectedMode: false,
            geoIndex: 1,
            showLegendSymbol: false, // 存在legend时显示
            roam: false,
          },
        ],
      };
      this.chart.setOption(option);

      this.chart.on("click", (params) => {
        var lineData = this.mapData.find(
          (item) => item.name === params.name
        ).lineData;
        if (!this.clickDown) {
          this.showLineChart(lineData, params.name);
          this.clickDown = true;
          setTimeout(() => {
            this.clickDown = false;
          }, 1000);
        }
      });
    },
    getChartData() {
      chartCenterTop().then((res) => {
        if (res.code === 200) {
          this.mapData = res.datas;
          this.updataChartData();
        } else {
          this.$message({
            type: "error",
            message: res,
          });
        }
      });
    },
    updataChartData() {
      const dataOption = {
        series: [
          {
            data: this.mapData,
          },
        ],
      };
      this.chart.setOption(dataOption);
    },
    updateChartAreaData() {
      const dataOption = {
        series: [
          {
            emphasis: {
              itemStyle: {
                areaColor: "#f00",
              },
            },
          },
        ],
      };
      this.chart.setOption(dataOption);
    },
    updataLineChartData(data) {
      const dataOption = {
        series: [
          {
            silent: true,
            data: data,
          },
        ],
      };
      this.lineChart.setOption(dataOption);
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
      this.chartHeight = Math.round(this.screenHeight * 0.55);
      this.chartSubHeight = Math.round(this.chartHeight * 0.80);
      this.chart.resize();
    },
    // 字体大小根据宽度自适应
    getScreenWidth() {
      this.screenWidth =
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth;
      this.chartFontTwelve = Math.round(this.screenWidth / 133);
      this.chartPaddingTwo = Math.round(this.screenWidth / 800);
      this.chartPaddingSix = Math.round(this.screenWidth / 267);
      this.chartPaddingFourteen = Math.round(this.screenWidth / 114);
      this.chartWidth = Math.round(this.screenWidth * 0.18);
      this.chart.resize();
    },
    showLineChart(data, name) {
      this.popupVisible = true;
      const myLineChart = this.$echarts.init(this.$refs["lineChart"]);
      this.lineChart = myLineChart;
      const lineOption = {
        title: {
          text: name,
        },
        tooltip: {
          trigger: "axis",
        },
        xAxis: {
          type: "category",
          axisTick: {
            show: false,
          },
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
        },
        yAxis: {
          type: "value",
          splitLine: {
            show: false,
          },
          axisTick: {
            show: false,
          },
          axisLabel: {
            show: true,
          },
        },
        series: [
          {
            name: "单量",
            type: "line",
          },
        ],
      };
      this.lineChart.setOption(lineOption);
      this.updataLineChartData(data);
    },
    handlePopup() {
      this.popupVisible = false;
    },
  },
};
</script>

<style lang="scss" scoped>
.line_parent {
  position: relative;
}
.line_popup {
  background: rgba(255, 255, 255, 0.8);
  height: 200px;
  width: 300px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); /* 使用transform来偏移自身的50%宽度和高度 */
}
img {
  display: block;
  max-width: 100%;
}
.button {
  font-size: 12px;
  padding: 2px 6px;
  background: #03050c;
  color: #0dc1ff; /* 文字颜色 */
  border: 1px solid #0dc1ff; /* 边框颜色与宽度 */
  border-radius: 12px; /* 圆角边框半径 */
  cursor: pointer; /* 鼠标悬停时显示手形图标 */
  transition: all 0.3s ease; /* 平滑过渡效果 */
}
.button:hover {
  background-color: #0056b3; /* 鼠标悬停时的背景颜色 */
  border-color: #0056b3; /* 鼠标悬停时的边框颜色 */
}
</style>