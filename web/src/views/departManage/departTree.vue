<template>
  <div class="chart-container">
    <div ref="chart-main" class="chart" />
  </div>
</template>

<script>
export default {
  mounted() {
    this.initChart();
  },
  data() {
    return {
      chartData: [],
      option: {},
      selectedNode: null, // 用于存储当前选中的节点
    };
  },
  methods: {
    initChart() {
      const myChart = this.$echarts.init(this.$refs["chart-main"]);
      this.chart = myChart;
      this.getChartData();
      const option = this.getOption();
      this.chart.setOption(option);
      // this.chart.on("click", this.nodeClick);
    },
    getChartData() {
      this.chartData = [
        {
          name: "院长",
          children: [
            {
              name: "分管副院长",
              children: [{ name: "内分泌科" }, { name: "神经内科" }],
            },
            {
              name: "分管副院长",
              children: [{ name: "儿科" }],
            },
          ],
        },
      ];
    },
    getOption() {
      const option = {
        tooltip: {
          trigger: "item",
          triggerOn: "mousemove",
        },
        series: [
          {
            type: "tree",
            data: this.chartData,
            top: "5%",

            avoidLabelOverlap: true, //防止标签重叠
            layout: "orthogonal",
            orient: "TB", //树形方向  TB为上下结构  LR为左右结构

            symbol: "emptyCircle", //图形形状  rect方形  roundRect圆角 emptyCircle圆形 circle实心圆
            symbolSize: 14,
            edgeShape: "polyline", //线条类型  curve曲线
            initialTreeDepth: -1, //初始展开的层级
            expandAndCollapse: false, //子树折叠和展开的交互，默认打开
            lineStyle: {
              //结构线条样式
              width: 0.7,
              color: "#1E9FFF",
              type: "broken",
            },
            label: {
              backgroundColor: "#81c5f7",
              position: "left",
              verticalAlign: "middle", //文字垂直对齐方式
              align: "center",
              borderColor: "#1E9FFF",
              color: "#333",
              borderWidth: 1,
              borderRadius: 5,
              padding: 5,
              height: 30,
              width: 70,
              offset: [12, 0], //节点文字与圆圈之间的距离
              fontSize: 14,
              // 节点文本阴影
              shadowBlur: 10,
              shadowColor: "rgba(0,0,0,0.25)",
              shadowOffsetX: 0,
              shadowOffsetY: 2,
            },
            leaves: {
              label: {
                position: "right",
                verticalAlign: "middle",
                align: "left",
                overflow: "break", //break为文字折行，  truncate为文字超出部分省略号显示
                lineOverflow: "truncate", //文字超出高度后 直接截取
              },
            },
            expandAndCollapse: true,
            initialExpand: false,
            animationDuration: 550,
            animationDurationUpdate: 750,
          },
        ],
        expandAndCollapse: false,
        animationEasing: "cubicOut",
        animationEasingUpdate: "cubicOut",
      };
      return option;
    },
    nodeClick(param) {
      // 取消之前节点的选中状态
      if (this.selectedNode) {
        this.setSelected(this.selectedNode, false);
      }
      // 设置当前点击节点为选中状态
      this.selectedNode = param.data;
      this.setSelected(this.selectedNode, true);
      // 可选：执行其他操作，如打开编辑弹窗等
    },
    setSelected(node, selected) {
      const option = this.chart.getOption();
      console.log("option1", option)
      const series = option.series;
      console.log("series1", series)
      const tree = series[0].data[0];
      console.log("tree1", tree)
      tree.children.forEach((child) => {
        if (child === node) {
          child.itemStyle = selected
            ? { ...child.itemStyle, backgroundColor: "#f00" }
            : { ...child.itemStyle, backgroundColor: "#0f0" };
        } else {
          child.itemStyle = {
            ...child.itemStyle,
            backgroundColor: "#f00",
          };
        }
      });
      console.log("tree2", tree)
      this.chart.setOption(option);
      this.chart.resize();
    },
  },
};
</script>

<style lang="scss" scoped>
.chart-container {
  .chart {
    height: 30rem;
  }
}
</style>