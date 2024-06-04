<template>
  <div ref="chart-main" :style="{ height: chartHeight + 'px' }"></div>
</template>

<script>
import { chartCenterTop } from "@/api/screen/home";

export default {
  data() {
    return {
      mapData: [],

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
            geoIndex: 1,
            showLegendSymbol: false, // 存在legend时显示
            roam: false,
          },
        ],
      };
      this.chart.setOption(option);
    },
    getChartData() {
      chartCenterTop().then((res) => {
        if (res.code === 200) {
          this.mapData = res.datas;
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
            data:  this.mapData
          }
        ]
      }
      this.chart.setOption(dataOption)
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
      this.chart.resize();
    },
    // 字体大小根据宽度自适应
    getScreenWidth() {
      this.screenWidth =
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth;
      this.chartWidth = Math.round(this.screenWidth * 0.18);
      this.chart.resize();
    },
  },
};
</script>

<style>
</style>