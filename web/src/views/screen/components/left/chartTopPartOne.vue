<template>
  <el-row :gutter="6">
    <el-col :span="12">
      <div :style="{ height: chartHeight + 'px' }">
        <dv-border-box-10>
          <chart-sub-one />
        </dv-border-box-10>
      </div>
    </el-col>
    <el-col :span="12">
      <div :style="{ height: chartHeight + 'px' }">
        <dv-border-box-10>
          <chart-sub-two />
        </dv-border-box-10>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import chartSubOne from './chartSubOne'
import chartSubTwo from './chartSubTwo'

export default {
  components: {
    chartSubOne,
    chartSubTwo
  },
  props: {
    chartHeight: {
      type: Number,
      default: 0
    }
  }

}
</script>

<style>

</style>