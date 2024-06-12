<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogFormVisible"
    @close="dialogClose"
    width="40%"
  >
  <el-form ref="form" :model="form" label-position="right" label-width="120px">
      <el-form-item label="工种名称: ">
        {{ form.name }}
      </el-form-item>
      <el-form-item label="创建时间: ">
        {{ form.addtime }}
      </el-form-item>
      <el-form-item label="更新时间: ">
        {{ form.uptime }}
      </el-form-item>
      <el-form-item label="备注: ">
        {{ form.remark }}
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button size="small" @click="dialogClose">关闭</el-button>
    </template>
  </el-dialog>
</template>

<script>
export default {
  name: "jobCheck",
  data() {
    return {
      title: "工种查看",
      form: {},
      dialogFormVisible: false,
    }
  },
  methods: {
    showCheck(row) {
      this.form = Object.assign({}, row);
      this.dialogFormVisible = true;
    },
    dialogClose() {
      this.form = this.$options.data().form;
      this.dialogFormVisible = false;
    },
  }
}
</script>

<style>

</style>