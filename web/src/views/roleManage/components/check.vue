<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogFormVisible"
    @close="dialogClose"
  >
    <el-form ref="form" :model="form">
      <el-form-item label="角色名称：">
        <span>{{ form.name }}</span>
      </el-form-item>
      <el-form-item label="创建时间：">
        <span>{{ form.addtime }}</span>
      </el-form-item>
      <el-form-item label="更新时间：">
        <span>{{ form.uptime }}</span>
      </el-form-item>
      <el-form-item label="备注：">
        <span>{{ form.remark }}</span>
      </el-form-item>
      <el-form-item label="权限:">
        <span>{{ form.powers }}</span>
      </el-form-item>
    </el-form>
    <template #footer>
      <el-button size="small" @click="dialogClose">关闭</el-button>
    </template>
  </el-dialog>
</template>

<script>
import { roleObtain } from "@/api/role";

export default {
  data() {
    return {
      name: "roleCheck",
      title: "角色查看",
      form: {},
      dialogFormVisible: false,
    };
  },
  methods: {
    showCheck(row) {
      this.form = Object.assign({}, row);
      this.getRolePowerList(row.id);
      this.dialogFormVisible = true;
    },
    
    // 获取角色权限列表
    getRolePowerList(id) {
      roleObtain(id).then((res) => {
        if (res.datas.status === 200) {
          this.form.powers = (Object.values(res.datas.datas.powers)).join(',')
        } else {
          this.$message({
            type: "error",
            message: res.msg,
          });
        }
      });
    },
  
    dialogClose() {
      this.form = this.$options.data().form;
      this.dialogFormVisible = false;
    },
  },
};
</script>

<style>
</style>