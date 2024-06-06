<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogFormVisible"
    @close="dialogClose"
    width="40%"
  >
    <el-form ref="form" :model="form" :rules="rules" label-width="80px">
      <el-form-item label="角色名称" prop="name">
        <el-input v-model="form.name" />
      </el-form-item>
      <el-form-item label="角色备注">
        <el-input type="textarea" v-model="form.remark" />
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button size="small" @click="dialogClose">取消</el-button>
      <el-button size="small" type="primary" @click="handleSubmit"
        >确定</el-button
      >
    </template>
  </el-dialog>
</template>

<script>
import { roleAdd, roleEdit } from '@/api/role'

export default {
  data() {
    return {
      name: "roleEdit",
      title: "",
      handle_type: "",
      dialogFormVisible: false,
      form: {},
      rules: {
        name: [
          {
            required: true,
            message: "角色名称不能为空",
            trigger: "blur"
          }
        ]
      },
    }    
  },
  methods: {
    showEdit(row) {
      if (!row) {
        this.title = "添加角色"
        this.handle_type = '1'
      } else {
        this.title = "编辑角色"
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
    // 提交
    handleSubmit() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          if (this.handle_type === '1') {
            roleAdd(this.form).then(res => {
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
            roleEdit(this.form, this.form.id).then(res => {
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

