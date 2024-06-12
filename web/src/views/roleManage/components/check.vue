<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogFormVisible"
    @close="dialogClose"
    width="40%"
  >
    <el-form ref="form" :model="form" label-position="right" label-width="120px">
      <el-form-item label="角色名称: ">
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
      <el-form-item label="权限: ">
        <template v-for="(item, index) in form.powers" >
          <el-tag :key="index">{{ item }}</el-tag>
        </template>
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
  name: "roleCheck",
  data() {
    return {
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
          this.form.powers = (Object.values(res.datas.datas.powers))
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