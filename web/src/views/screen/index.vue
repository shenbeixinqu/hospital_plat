<template>
  <div class="screen-index">
    <!-- datav loading加载动画 -->
    <dv-loading v-if="loading">Loading...</dv-loading>
    <!-- 总体布局 -->
    <div v-else class="screen-body">
      <!-- 第一部分 头部 start -->
      <div class="header">
        <dv-decoration-10 class="dv-dec-10-left" />
        <dv-decoration-8 class="dv-dec-8-left" :color="decorationColor"/>
        <!-- 标题 -->
        <span class="title screen-font-bold colorDeepskyblue" :style="{'font-size': Math.round(this.screenWidth/80) + 'px'}">医院当年综合数据</span>
        <dv-decoration-8 class="dv-dec-8-right" :reverse="true" :color="decorationColor" />
        <dv-decoration-10 class="dv-dec-10-right"/>
      </div>
      <!-- 第一部分 头部 end -->
      
      <!-- 第二部分 布局 start -->
      <div class="screen-layout">
        <el-row>
          <el-col :span="5">
            <div :style="{ height: chartOne + 'px'}">
              <dv-border-box-9 style="padding:12px">
                <left-top-chart />
              </dv-border-box-9>
            </div>
          </el-col>
          <el-col :span="14">
            <div :style="{ height: chartTwo + 'px'}">
              <dv-border-box-12 style="padding:12px">
                <center-top-chart />
              </dv-border-box-12>
            </div>
          </el-col>
          <el-col :span="5">
            <div :style="{ height: chartThree + 'px'}">
              <dv-border-box-9 style="padding:12px">
                <right-top-chart />
              </dv-border-box-9>
            </div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <div :style="{ height: chartFour + 'px'}">
              <dv-border-box-9 style="padding:12px">
                <left-bottom-chart />
              </dv-border-box-9>
            </div>
          </el-col>
          <el-col :span="8">
            <div :style="{ height: chartFive + 'px'}">
              <dv-border-box-9 style="padding:12px">
                <center-bottom-chart />
              </dv-border-box-9>
            </div>
          </el-col>
          <el-col :span="8">
            <div :style="{ height: chartSix + 'px'}">
              <dv-border-box-9 style="padding:12px">
                <right-bottom-chart />
              </dv-border-box-9>
            </div>
          </el-col>
        </el-row>
      </div>
      <!-- 第二部分 布局 end -->
    </div>
  </div>
</template>

<script>
import leftTopChart from './components/left/chartTop'
import leftBottomChart from './components/left/chartBottom'
import centerTopChart from './components/center/chartTop'
import centerBottomChart from './components/center/chartBottom'
import rightTopChart from './components/right/chartTop.vue'
import rightBottomChart from './components/right/chartBottom'

export default {
  components: {
    leftTopChart,
    leftBottomChart,
    centerTopChart,
    centerBottomChart,
    rightTopChart,
    rightBottomChart
  },
  created() {
    // window.addEventListener('resize',this.getScreenHeight, false);
    // window.addEventListener('resize',this.getScreenWidth, false);
  },
  mounted() {
    // 页面大小改变时触发
    window.addEventListener('resize',this.getScreenHeight, false);
    window.addEventListener('resize',this.getScreenWidth, false);
    this.cancelLoading();
    this.resizeScreen();
  },
  beforeDestroy() {
    clearInterval(this.screenTime)
    // 页面大小改变时触发
    window.removeEventListener('resize',this.getScreenHeight, false);
    // 页面大小改变时触发
    window.removeEventListener('resize',this.getScreenWidth, false);
  },
  data() {
    return {
      loading: true,
      decorationColor: ['#568aea', '#000000'],
      screenTime: null,
      screenWidth: window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
      // chartOne: 450,
      // chartTwo: 200,
      // chartThree: 450,
      // chartFour: 200,
      // chartFive: 200,
      // chartSix: 200,
      chartOne: 410,
      chartTwo: 380,
      chartThree: 410,
      chartFour: 260,
      chartFive: 260,
      chartSix: 260,
    }
  },
  methods: {
    cancelLoading() {
      setTimeout(() => {
        this.loading = false
      }, 100)
    },
    resizeScreen() {
      this.screenTime = setInterval(() => {
        this.getScreenHeight();
        this.getScreenWidth()
      }, 200)
    },
    // 获取浏览器高度进行自适应
    getScreenHeight() {
      this.screenHeight = window.innerHeight || document.documentElement.innerHeight || document.body.clientHeight;
      this.chartOne = Math.round(this.screenHeight * 0.55)
      this.chartTwo = Math.round(this.screenHeight * 0.55)
      this.chartThree = Math.round(this.screenHeight * 0.55)
      this.chartFour = Math.round(this.screenHeight * 0.35)
      this.chartFive = Math.round(this.screenHeight * 0.35)
      this.chartSix = Math.round(this.screenHeight * 0.35)
    },
    // 字体大小根据宽度自适应
    getScreenWidth(){
      this.screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
    }
  }
}
</script>

<style>

</style>