<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogFormVisible"
    @close="dialogClose"
  >
    <el-form ref="form" :model="form">
      <el-form-item label="数据权限:">
        <el-radio-group v-model="form.data">
          <el-radio :label="0">仅本人</el-radio>
          <el-radio :label="1">本部门</el-radio>
          <el-radio :label="2">本部门及下级</el-radio>
          <el-radio :label="3">全部</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item label="功能权限:">
        <el-tree
          ref="tree"
          style="margin-left: 100px; margin-top: 20px"
          :data="powerList"
          show-checkbox
          node-key="id"
          default-expand-all
          highlight-current
          :default-checked-keys="rolePowerList"
          :props="defaultProps">
        </el-tree>
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
import { roleObtain, roleAssign } from '@/api/role'
import { powerList } from '@/api/power'

export default {
  data() {
    return {
      title: "分配权限",
      form: {
        role_id: "",
        data: "",
        powers: ""
      },
      powerList: [], // 所有权限列表
      rolePowerList: [], // 角色权限列表
      defaultProps: {
        children: 'children',
        label: 'name'
      },
      dialogFormVisible: false,
    }
  },
  methods: {
    showAssign(row) {
      this.form.data = 1
      this.form.role_id = row.id
      this.getPowerList()
      this.getRolePowerList(row.id)
      this.dialogFormVisible = true
    },
    // 获取权限信息
    getPowerList() {
      powerList({ rt: 1 }).then(res => {
        if (res.datas.status === 200) {
          this.powerList = res.datas.datas
        } else {
          this.$message({
            type: "error",
            message: res.msg,
          });
        }
      })
    },
    // 获取角色权限列表
    getRolePowerList(id) {
      roleObtain(id).then(res => {
        if (res.datas.status === 200) {
          this.rolePowerList = res.datas.datas.power
          // this.rolePowerList = [ 2, 3, 4, 9]
        } else {
          this.$message({
            type: "error",
            message: res.msg,
          });
        }
      })
    },
    // 关闭dialog
    dialogClose() {
      this.dialogFormVisible = false;
    },
    // 提交
    handleSubmit() {
      // 获取选中的节点
      let nodeData = this.$refs.tree.getCheckedNodes()
      let ids = this.extractIds(nodeData)
      this.form.powers = ids
      roleAssign(this.form, this.form.role_id).then(res => {
        if (res.datas.status === 200) {
          this.$message({
            type: "success",
            message: "操作成功",
          });
          this.dialogClose()
        } else {
          this.$message({
            type: "error",
            message: res.msg,
          });
        }
      })
    },    
    // 提炼id
    extractIds(data) {
      let ids = [];
      data.forEach(item => {
        // if (item.children && item.children.length > 0) {
        //     ids = ids.concat(extractIds(item.children));
        // }
        ids.push(item.id);
      });
      return ids.join(",");
    }
  }
}
</script>

<style>

</style>