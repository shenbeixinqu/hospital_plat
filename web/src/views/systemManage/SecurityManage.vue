<template>
  <div class="index-container">
    <el-tabs v-model="activeName" type="card">
      <el-tab-pane label="停用锁定配置" name="stopLock">
        <stop-lock />
      </el-tab-pane>
      <el-tab-pane label="自动登出策略" name="autoLogout">
        <auto-logout />
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import StopLock from './components/stopLock.vue'
import AutoLogout from './components/autoLogout.vue'
export default {
  components: {
    StopLock,
    AutoLogout
  },
  data() {
    return {
      activeName: "stopLock"
    }
  }
}
</script>

<style>

</style>