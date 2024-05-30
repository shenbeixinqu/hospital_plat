<template>
  <div
    class="test"
    ref="right-main"
    :style="{ height: chartHeight + 'px' }"
  ></div>
</template>

<script>
import uniChart from "@/extra/index";
import { chartRightTopTwo } from '@/api/screen/home'
export default {
  components: {
    uniChart
  },
  data() {
    return {
      disease_name: [],
      disease_count: [],
      disease_max: [],

      // 页面宽高
      screenHeight: window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight,
      screenWidth: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
      chartInstance: null,
      chartWidth: 0,
      chartHeight: 0,
      chartFont: 0,
      chartTime: null,
      chart: null,

      // 页面自适应数据
      chartBarBorderRadius: 0,
      chartBarWidth: 0,
      chartTitleText: 0,
      chartLabelText: 0,
      initOptions: {
        renderer: "svg"
      },
      option: {
        title: [
          {
            text: '疾病诊断排行',
            left: "2%",
            top: "3%",
            textStyle: {
              color: "#0dc1ff"
            },
          },
          {
            text: '(万人次)',
            top: "5%",
            left: 'right',
            textStyle: {
              color: "#0dc1ff"
            },
          }
        ], 
        grid: {
          left: "3%",
          right: "3%",
          bottom: "1%",
          top: "13%",
          containLabel: true,
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "none"
          },
          formatter: function(params) {
            return params[0].name + " : " + params[0].value
          }
        },
        xAxis: {
          show: false,
          type: 'value'
        },
        yAxis: [
          {
            type: "category",
            inverse: true,
            axisLabel: {
              show: true,
              textStyle: {
                color: "#fff"
              },
            },
            splitLine: {
              show: false
            },
            axisTick: {
              show: false
            },
            axisLine: {
              show: false
            },
          },
          {
            type: "category",
            inverse: true,
            axisTick: "none",
            axisLine: "none",
            show: true,
            axisLabel: {
              textStyle: {
                color: "#fff"
              }
            },
          }
        ],
        series: [
          {
            name: "值",
            type: "bar",
            zlevel: 1,
            itemStyle: {
              normal: {
                color: this.$echarts.graphic.LinearGradient(0, 0, 1, 0, [
                  {
                    offset: 0,
                    color: "rgb(57, 89, 255, 1)"
                  },
                  {
                    offset: 1,
                    color: "rgb(46, 200, 207, 1)"
                  }
                ])
              }
            },
          },
          {
            name: "背景",
            type: "bar",
            barGap: "-100%",
            itemStyle: {
              normal: {
                color: "rgba(24, 31, 68, 1)",
              }
            }
          }
        ]
      }
    }
  },
  beforeMount(){
    this.chartHeight = Math.round(this.screenHeight * 0.33)
  },
  mounted() {
    // 获取接口数据
    this.getChartData()
    // 页面大小改变时触发
    window.addEventListener('resize',this.getScreenHeight, false);
    // 页面大小改变时触发
    window.addEventListener('resize',this.getScreenWidth, false);
    // 自适应浏览器获取宽高大小定时器
    this.resizeScreen();
    const myChart = this.$echarts.init(this.$refs['right-main'])
    this.chart = myChart
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
    window.removeEventListener('resize',this.getScreenHeight, false);
    // 页面大小改变时触发销毁
    window.removeEventListener('resize',this.getScreenWidth, false);
    // Echarts图表自适应销毁
    window.removeEventListener("resize", this.screenAdapter);
  }, 
  methods: {
    initChart() {
      this.chart.setOption(this.option)
    },
    // 获取接口数据
    getChartData() {
      chartRightTopTwo().then(res => {
        if (res.code === 200) {
          this.disease_name = res.datas.disease_name
          this.disease_count = res.datas.disease_count
          this.disease_max = res.datas.disease_max
          const tempList = []
          this.disease_count.forEach(item => {
            tempList.push(this.disease_count[0])
          })
          this.disease_max = tempList
          this.updateChartData()

        } else {
          this.$message({
            type: "error",
            message: res
          })
        }
      })
    },
    updateChartData() {
      const dataOption = {
        yAxis: [
          {
            data: this.disease_name
          },
          {
            data: this.disease_count
          }
        ],
        series: [
          {
            data: this.disease_count
          },
          {
            data: this.disease_max
          }
        ]
      }
      this.chart.setOption(dataOption)
    },
    screenAdapter() {
      this.chartBarBorderRadius = Math.round(this.screenWidth / 100);
      this.chartBarWidth = Math.round(this.screenWidth / 100);
      this.chartLabelText = Math.round(this.screenWidth / 133);
      this.chartTitleText = Math.round(this.screenWidth / 89);
      const adapterOption = {
        title: [
          {
            textStyle: {
              fontSize: this.chartTitleText
            }
          },
          {
            textStyle: {
              fontSize: this.chartLabelText
            }
          }
        ],
        yAxis: [
          {
            axisLabel: {
              textStyle: {
                fontSize: this.chartLabelText
              }
            }
          },
          {
            axisLabel: {
              textStyle: {
                fontSize: this.chartLabelText
              }
            }
          }
        ],
        series: [
          {
            itemStyle: {
              normal: {
                borderRadius: this.chartBarBorderRadius
              }
            },
            barWidth: this.chartBarWidth
          },
          {
            itemStyle: {
              normal: {
                borderRadius: this.chartBarBorderRadius
              }
            },
            barWidth: this.chartBarWidth
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
    getScreenWidth(){
      this.screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
      this.chartWidth = Math.round(this.screenWidth * 0.18);
      this.chartFont = Math.round(this.screenWidth / 100);
      this.chart.resize()
    },
  }
}
</script>

<style>

</style>