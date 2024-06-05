<template>
  <div class="main" :style="{ height: chartHeight + 'px', padding: chartPaddingFourteen + 'px' }">
    <div class="first">
      <div>
        <button
          class="button"
          :style="{
            fontSize: chartFontTwelve + 'px',
            paddingTop: chartPaddingTwo + 'px',
            paddingBottom: chartPaddingTwo + 'px',
            paddingLeft: chartPaddingSix + 'px',
            paddingRight: chartPaddingSix + 'px',
          }"
        >按月</button>
      </div>
      <div>
        <div class="desc" :style="{ fontSize: chartFontTwelve + 'px', paddingBottom: chartPaddingFour + 'px'}">当年总收入(万元)</div>
        <div class="count" :style="{ fontSize: chartFontSixteen + 'px'}">1213.25</div>
      </div>
    </div>
    <div ref="chart-main" style="height: 85%" />
  </div>
</template>

<script>
import { chartRightBottom } from "@/api/screen/home";

export default {
  data() {
    return {
      dataList: [],

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

      chartLabelText: 0,
      chartFontTwelve: 0,
      chartFontFourteen: 0,
      chartFontSixteen: 0,
      chartPaddingTwo: 0,
      chartPaddingFour: 0,
      chartPaddingSix: 0,
      chartPaddingEight: 0,
      chartPaddingFourteen: 0,
    };
  },
  beforeMount() {
    this.chartHeight = Math.round(this.screenHeight * 0.33);
  },
  mounted() {
    this.getChartData();
    // 页面大小改变时触发
    window.addEventListener("resize", this.getScreenHeight, false);
    // 页面大小改变时触发
    window.addEventListener("resize", this.getScreenWidth, false);
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
    window.removeEventListener("resize", this.getScreenHeight, false);
    // 页面大小改变时触发销毁
    window.removeEventListener("resize", this.getScreenWidth, false);
    // Echarts图表自适应销毁
    window.removeEventListener("resize", this.screenAdapter);
  },
  methods: {
    initChart() {
      var colors = ["#00ffff", "#00cfff", "#ffe000", "#ffa800", "#ff3000"];
      const pieData = [];
      this.dataList.forEach((item, index) => {
        pieData.push({
          name: item.name,
          value: item.value,
          itemStyle: {
            color: colors[index],
            borderColor: colors[index],
            shadowColor: colors[index],
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
          align: "auto",
          itemWidth: 5,
          itemHeight: 5,
          // orient: 'horizontal',
          orient: "vertical",
          left: "left",
          top: "bottom",
          textStyle: {
            color: "#fff",
          },
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
                  padding: [3, 0],
                },
              },
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
            fontSize: this.chartTitleText,
          },
        },
        legend: {
          textStyle: {
            fontSize: this.chartLabelText,
          },
        },
        series: [
          {
            label: {
              textStyle: {
                fontSize: this.chartLabelText,
              },
            },
          },
        ],
      };
      this.chart.setOption(adapterOption);
      this.chart.resize();
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
      this.chart.resize();
    },
    // 字体大小根据宽度自适应
    getScreenWidth() {
      this.screenWidth =
        window.innerWidth ||
        document.documentElement.clientWidth ||
        document.body.clientWidth;
      this.chartWidth = Math.round(this.screenWidth * 0.18);
      this.chartFontTwelve = Math.round(this.screenWidth / 133);
      this.chartFontFourteen = Math.round(this.screenWidth / 114);
      this.chartFontSixteen = Math.round(this.screenWidth / 100);
      this.chartPaddingTwo = Math.round(this.screenWidth / 800);
      this.chartPaddingFour = Math.round(this.screenWidth / 400);
      this.chartPaddingSix = Math.round(this.screenWidth / 267);
      this.chartPaddingEight = Math.round(this.screenWidth / 200);
      this.chartPaddingFourteen = Math.round(this.screenWidth / 114);
      this.chart.resize();
    },
  },
};
</script>

<style lang="scss" scoped>
.first {
  height: 15%;
  display: flex;
  justify-content: space-between;
}
.desc {
  color: #0dc1ff;
}
.count {
  text-align: right;
  color: #ffe000;
}
.button {
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