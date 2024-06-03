<template>
  <div ref="chart-main" :style="{ height: chartHeight + 'px' }"></div>
</template>

<script>
import { chartRightBottom } from "@/api/screen/home";

export default {
  data() {
    return {
      dataList: [],

      screenHeight: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight,
      screenWidth: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
      chartWidth: 0,
      chartHeight: 0,
      chartFont: 0,
      chartTime: null,

      chartLabelText: 0,
    };
  },
  beforeMount(){
    this.chartHeight = Math.round(this.screenHeight * 0.33)
  },
  mounted() {
    this.getChartData();
    // 页面大小改变时触发
    window.addEventListener('resize',this.getScreenHeight, false);
    // 页面大小改变时触发
    window.addEventListener('resize',this.getScreenWidth, false);
    // 自适应浏览器获取宽高大小定时器
    this.resizeScreen();
    const myChart = this.$echarts.init(this.$refs["chart-main"]);
    this.chart = myChart;
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
    window.removeEventListener('resize',this.getScreenHeight, false);
    // 页面大小改变时触发销毁
    window.removeEventListener('resize',this.getScreenWidth, false);
    // Echarts图表自适应销毁
    window.removeEventListener("resize", this.screenAdapter);
  },
  methods: {
    initChart() {
      var colors = [
        "#00ffff",
        "#00cfff",
        "#ffe000",
        "#ffa800",
        "#ff3000"
      ];
      const pieData = [];
      this.dataList.forEach((item, index) => {
        pieData.push({
          name: item.name,
          value: item.value,
          itemStyle: {
            color: colors[index],
            borderColor: colors[index],
            shadowColor: colors[index]
          },
        });
      });
      const option = {
        title: {
          text: "营收占比",
          x: "center",
          y: "center",
          textStyle: {
            color: "#0dc1ff",
          },
        },
        tooltip: {
          trigger: "item",
          formatter: (params) => {
            var relVal = params.seriesName;
            relVal +=
              "<br/>" +
              params.marker +
              params.name +
              " : " +
              params.value +
              "单";
            return relVal;
          },
        },
        legend: {
          // align: "auto",
          itemWidth: 5,
          itemHeight: 5,
          // orient: 'horizontal',
          orient: "vertical",
          left: 'left',
          top: "bottom",
          textStyle: {
            color: "#fff",
          }
        },
        series: [
          {
            name: "新增订单",
            type: "pie",
            radius: ["60%", "65%"],
            avoidLabelOverlap: false,
            clockWise: true,
            label: {
              show: true,
              position: "outside",
              color: "#eee",
              formatter: (params) => {
                let percent = 0;
                let total = 0;
                for (let i = 0; i < this.dataList.length; i++) {
                  total += this.dataList[i].value;
                }
                percent = ((params.value / total) * 100).toFixed(1);
                if (params.name !== "") {
                  return params.name + "\n" + percent + "%";
                } else {
                  return "";
                }
              },
              rich: {
                white: {
                  color: "#ddd",
                  align: "center",
                  padding: [3, 0]
                }
              }
            },
            labelLine: {
              show: true,
              position: "outside",
              length: 10,
              length2: 30,
              color: "#00ffff",
            },
            itemStyle: {
              borderRadius: 2,
            },
            data: pieData,
          },
        ],
      };

      this.chart.setOption(option, true);
    },
    getChartData() {
      chartRightBottom().then((res) => {
        if (res.code === 200) {
          this.dataList = res.datas;
          this.initChart();
        } else {
          this.$message({
            type: "error",
            message: res,
          });
        }
      });
    },
    screenAdapter() {
      this.chartLabelText = Math.round(this.screenWidth / 133);
      this.chartTitleText = Math.round(this.screenWidth / 80);
      const adapterOption = {
        title: {
          textStyle: {
            fontSize: this.chartTitleText
          }
        },
        legend: {
          textStyle: {
            fontSize: this.chartLabelText
          }
        },
        series: [
          {
            label: {
              textStyle: {
                fontSize: this.chartLabelText
              },
            }
          }
        ]
      }
      this.chart.setOption(adapterOption)
      this.chart.resize()
    },
    resizeScreen() {
      this.chartTime = setInterval(() => {
        this.getScreenHeight();
        this.getScreenWidth();
      }, 200)
    },
    // 获取浏览器高度进行自适应
    getScreenHeight() {
      this.screenHeight = window.innerHeight || document.documentElement.innerHeight || document.body.clientHeight;
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
      this.chart.resize();
    },
  },
};
</script>

<style>
</style>