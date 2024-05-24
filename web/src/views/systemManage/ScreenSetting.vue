<template>
  <div class="index-container">
    <el-tabs v-model="activeName" type="card" @tab-click="tabClick">
      <el-tab-pane label="患者分布大屏" name="distributed">
        <distributed /> 
      </el-tab-pane>
      <el-tab-pane label="当日预警大屏" name="warning">配置管理</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import Distributed from './components/distributed.vue'
export default {
  components: {
    Distributed
  },
  data() {
    return {
      activeName: "distributed",

    }
  },
  methods: {
    tabClick() {

    }
  }
}
</script>

<style>

</style>