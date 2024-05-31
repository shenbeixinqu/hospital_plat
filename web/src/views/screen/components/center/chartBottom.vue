<template>
  <div ref="chart-main" :style="{ height: chartHeight + 'px' }"></div>
</template>

<script>
import { chartCenterBottom } from "@/api/screen/home";

export default {
  data() {
    return {
      visit_data: [],
      admission_data: [],

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

      option: {
        title: {
          text: "全院网上复诊&接诊趋势",
          subtext: "单位: (万人次)",
          textStyle: {
            align: "center",
            color: "#0dc1ff",
            fontSize: 16,
          },
          subtextStyle: {
            top: "6%",
            color: "#ebf8ac",
          },
          top: "3%",
          left: "10%",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "none",
          },
        },
        legend: {
          data: ["网上复诊", "网上接诊"],
          top: "12%",
          textStyle: {
            color: "#fff",
          },
        },
        xAxis: {
          data: [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "07",
            "08",
            "09",
            "10",
            "11",
            "12",
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
        yAxis: [
          {
            type: "value",
            splitLine: {
              show: true,
              lineStyle: {
                color: "rgba(192, 192, 192, 0.2)",
              },
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
          {
            type: "value",
            position: "right",
            splitLine: {
              show: false,
            },
            axisTick: {
              show: false,
            },
            axisLine: {
              show: false,
            },
            axisLabel: {
              show: true,
            },
          },
          {
            type: "value",
            gridIndex: 0,
            min: 10,
            max: 1000,
            splitNumber: 8,
            splitLine: {
              show: false,
            },
            axisLine: {
              show: false,
            },
            axisTick: {
              show: false,
            },
            axisLabel: {
              show: false,
            },
            splitArea: {
              show: true,
              areaStyle: {
                color: ["rgba(250,250,250,0.0)", "rgba(250,250,250,0.05)"],
              },
            },
          },
        ],
        series: [
          {
            name: "网上复诊",
            type: "line",
            yAxisIndex: 1, //使用的 y 轴的 index，在单个图表实例中存在多个 y轴的时候有用
            smooth: true, //平滑曲线显示
            showAllSymbol: true, //显示所有图形。
            symbol: "circle", //标记的图形为实心圆
            symbolSize: 10, //标记的大小
            itemStyle: {
              //折线拐点标志的样式
              color: "#058cff",
            },
            lineStyle: {
              color: "#058cff",
            },
            areaStyle: {
              color: "rgba(5,140,255, 0.2)",
            },
          },
          {
            name: "网上接诊",
            type: "bar",
            zlevel: 1,
            barWidth: 15,
            itemStyle: {
              normal: {
                color: this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    offset: 0,
                    color: "#00FFE3",
                  },
                  {
                    offset: 1,
                    color: "#4693EC",
                  },
                ]),
              },
            },
          },
        ],
      },
    };
  },
  beforeMount() {
    this.chartHeight = Math.round(this.screenHeight * 0.4);
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
      this.chart.setOption(this.option);
    },
    getChartData() {
      chartCenterBottom().then((res) => {
        if (res.code === 200) {
          this.visit_data = res.datas.visit_data;
          this.admission_data = res.datas.admission_data;
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
            data: this.visit_data,
          },
          {
            data: this.admission_data,
          },
        ],
      };
      this.chart.setOption(dataOption);
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
      this.chartHeight = Math.round(this.screenHeight * 0.38);
      this.chart.resize();
    },
    // 字体大小根据宽度自适应
    getScreenWidth() {
      this.screenWidth =
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth;
      this.chartWidth = Math.round(this.screenWidth * 0.18);
      this.chartFont = Math.round(this.screenWidth / 100);
      this.chart.resize();
    },
  },
};
</script>

<style>
</style>