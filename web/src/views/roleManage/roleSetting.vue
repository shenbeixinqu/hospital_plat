<template>
  <div class="role-container">
    <uni-query-form>
      <uni-query-form-left-panel>
        <el-button
          icon="el-icon-plus"
          size="small"
          type="primary"
          @click="handleEdit()"
          >添加</el-button
        >
      </uni-query-form-left-panel>
    </uni-query-form>
    <el-table
      :loading="listLoading"
      :data="dataList"
    >
      <el-table-column label="角色ID" align="center" prop="id" />
      <el-table-column label="角色名称" align="center" prop="name" />
      <el-table-column label="创建时间" align="center" prop="addtime" />
      <el-table-column label="更新时间" align="center" prop="uptime" />
      <el-table-column label="备注" align="center" prop="remark" />
      <el-table-column label="操作" align="center">
        <template #default="{ row }">
          <el-button type="text" @click="handleCheck(row)">查看</el-button>
          <el-button type="text" @click="handleEdit(row)">编辑</el-button>
          <el-button type="text" @click="handleDel(row)">删除</el-button>
          <el-button type="text" @click="handleAssign(row)">分配权限</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 组件 -->
    <check ref="check" />
    <edit ref="edit" @fetch-data="fetchData" />
    <assign ref="assign" />
    
    <!-- 分页 -->
    <el-pagination
      background
      :current-page="queryForm.pn"
      :page-size="queryForm.limit"
      :total="total"
      :layout="layout"
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
    />
  </div>
</template>

<script>
import { roleList, roleDel } from '@/api/role'
import Check from './components/check.vue'
import Edit from './components/edit.vue'
import Assign from './components/assign.vue'

export default {
  name: "roleSetting",
  components: {
    Check,
    Edit,
    Assign
  },
  created() {
    this.fetchData()
  },
  data() {
    return {
      dataList: [],
      listLoading: true,
      total: 0,
      selectRows: "",
      layout: "total, sizes, prev, pager, next, jumper",
      queryForm: {
        pn: 1,
        limit: 10,
        name: ""
      },
    }
  },
  methods: {
    async fetchData() {
      this.listLoading = true
      const {
        datas: { datas, total },
      } = await roleList(this.queryForm)
      this.total = total
      this.dataList = datas
      this.listLoading = false
    },
    handleSizeChange(val) {
      this.queryForm.limit = val;
      this.fetchData();
    },
    handleCurrentChange(val) {
      this.queryForm.pn = val;
      this.fetchData();
    },
    handleCheck(row) {
      this.$refs.check.showCheck(row)
    },
    handleEdit(row) {
      if (row) {
        this.$refs.edit.showEdit(row)
      } else {
        this.$refs.edit.showEdit()
      }
    },
    handleDel(row) {
      this.$confirm("确定要删除当前项吗?", "温馨提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          roleDel(row.id).then(res => {
            if (res.datas.status === 200) {
                this.$message({
                  type: "success",
                  message: "删除成功",
                });
                this.fetchData();
              }
          })
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        })
    },
    handleAssign(row) {
      this.$refs.assign.showAssign(row)
    }
  }
}
</script>

<style>

</style>