<template>
  <div>
    <div :style="{ height: chartRightOne + 'px'}" class="screen-padding-bottom">
      <dv-border-box-10>
        <chart-top-part-one />
      </dv-border-box-10>
    </div>
    <div :style="{ height: chartRightTwo + 'px'}">
      <dv-border-box-10>
        <chart-top-part-two />
      </dv-border-box-10>
    </div>
  </div>
</template>

<script>
import chartTopPartOne from './chartTopPartOne'
import chartTopPartTwo from './chartTopPartTwo'
export default {
  components: {
    chartTopPartOne,
    chartTopPartTwo
  },
  props: {
    chartRightOne: {
      type: Number,
      default: 0
    },
    chartRightTwo: {
      type: Number,
      default: 0
    },
  }
}
</script>

<style>

</style>