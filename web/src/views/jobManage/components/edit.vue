<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogFormVisible"
    @close="dialogClose"
    width="40%"
  >
    <el-form ref="form" :model="form" :rules="rules" label-width="120px">
      <el-form-item label="工种名称" prop="name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="工种备注">
        <el-input type="textarea" v-model="form.remark" />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button size="small" @click="dialogClose">取消</el-button>
      <my-button @click="handleSubmit" />
    </template>
  </el-dialog>
</template>

<script>
import { jobAdd, jobEdit } from '@/api/job'

export default {
  name: "jobEdit",
  data() {
    return {
      title: "",
      handle_type: "",
      dialogFormVisible: false,
      form: {},
      rules: {
        name: [
          {
            required: true,
            message: "工种名称不能为空",
            trigger: "blur"
          }
        ]
      }
    }
  },
  methods: {
    showEdit(row) {
      if (!row) {
        this.title = "添加工种"
        this.handle_type = '1'
      } else {
        this.title = "编辑工种"
        this.handle_type = '2'
        this.form = Object.assign({}, row)
      }
      this.dialogFormVisible = true;
    },
    // 关闭
    dialogClose() {
      this.$refs.form.resetFields();
      this.form = this.$options.data().form;
      this.dialogFormVisible = false;
    },
    handleSubmit() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          if (this.handle_type === '1') {
            jobAdd(this.form).then(res => {
              if (res.datas.status === 200) {
                this.$message({
                  type: "success",
                  message: `${this.title}成功`,
                });
                this.$emit("fetch-data");
                this.dialogClose()
              } else {
                this.$message({
                  type: "error",
                  message: res.msg,
                });
              }
            })
          } else {
            jobEdit(this.form, this.form.id).then(res => {
              if (res.datas.status === 200) {
                this.$message({
                  type: "success",
                  message: `${this.title}成功`,
                });
                this.$emit("fetch-data");
                this.dialogClose()
              } else {
                this.$message({
                  type: "error",
                  message: res.msg,
                });
              }
            })
          }
        }
      })
    }
  }
}
</script>

<style>

</style>