<template>
  <div>
    <div :style="{ height: chartLeftOne + 'px'}">
      <chart-top-part-one :chartHeight="chartLeftOne" />
    </div>
    <div :style="{ height: chartLeftTwo + 'px'}" style="padding-top: 6px">
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
    chartLeftOne: {
      type: Number,
      default: 0
    },
    chartLeftTwo: {
      type: Number,
      default: 0
    }
  }
}
</script>

<style>

</style>