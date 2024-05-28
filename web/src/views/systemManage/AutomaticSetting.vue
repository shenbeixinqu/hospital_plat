<template>
  <div class="index-container">
    <el-tabs v-model="activeName" type="card">
      <el-tab-pane label="每月报告策略" name="month">
        <every-month />
      </el-tab-pane>
      <el-tab-pane label="每年报告策略" name="year">
        <every-year />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import EveryMonth from './components/everyMonth.vue'
import EveryYear from './components/everyYear.vue'
export default {
  components: {
    EveryMonth,
    EveryYear
  },
  data() {
    return {
      activeName: "month"
    }
  }
}
</script>

<style>

</style>