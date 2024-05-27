<template>
  <div class="index-container">
    <el-tabs v-model="activeName" type="card">
      <el-tab-pane label="患者分布大屏" name="distributed">
        <distributed /> 
      </el-tab-pane>
      <el-tab-pane label="当日预警大屏" name="warning">
        <warning />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import Distributed from './components/distributed.vue'
import Warning from './components/warning.vue'
export default {
  components: {
    Distributed,
    Warning
  },
  data() {
    return {
      activeName: "distributed",
    }
  },
}
</script>

<style>

</style>