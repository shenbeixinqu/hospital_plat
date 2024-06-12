<template>
  <div class="depart-container">
    <uni-query-form>
      <uni-query-form-left-panel>
        <el-row :gutter="14" class="row-style">
          <el-col :span="6">
            <div class="text-content">组织名称:</div>
          </el-col>
          <el-col :span="10">
            <el-input
              size="small"
              placeholder="请输入组织名称"
              clearable
              v-model="queryForm.name"
            />
          </el-col>
          <el-col :span="6">
            <div class="text-content">请选择上级组织:</div>
          </el-col>
          <el-col :span="12">
            <el-select v-model="queryForm.pid" clearable filterable placeholder="请选择" size="small">
              <el-option
                v-for="item in departSelectData"
                :key="item.id"
                :label="item.name"
                :value="item.id">
              </el-option>
            </el-select>
          </el-col>
          <el-col :span="3">
            <el-button size="small" type="primary" @click="fetchData"
              >搜索</el-button
            >
          </el-col>
        </el-row>
      </uni-query-form-left-panel>
      <uni-query-form-left-panel>
        <el-button
          icon="el-icon-plus"
          size="small"
          type="primary"
          @click="handleEdit()"
          >添加组织</el-button
        >
      </uni-query-form-left-panel>
    </uni-query-form>
    <el-table
      :loading="listLoading"
      :data="dataList"
      :header-cell-style="hederCellStyle"
    >
      <el-table-column label="组织ID" align="center" prop="id" />
      <el-table-column label="组织名称" align="center" prop="name" />
      <el-table-column label="上级组织" align="center" prop="parentName" />
      <el-table-column label="组织编制人数(启用/锁定)" align="center">
        <template slot-scope="scope">
            {{ scope.row.userTotal }} ({{ scope.row.userOpen}}/{{ scope.row.UserLock }})
        </template>
      </el-table-column>
      <el-table-column label="创建时间" align="center" prop="addtime" />
      <el-table-column label="操作" align="center">
        <template #default="{ row }">
          <el-button type="text" @click="handleCheck(row)">查看</el-button>
          <el-button type="text" @click="handleEdit(row)">编辑</el-button>
          <el-button type="text" @click="handleDel(row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    
    <!-- 组件 -->
    <check ref="check" />
    <edit ref="edit" @fetch-data="fetchData" />
    
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
import { departList, departSelect, departDel } from "@/api/depart";
import Edit from './componets/edit.vue'
import Check from './componets/check.vue'

export default {
  name: "departManage",
  components: {
    Edit,
    Check
  },
  created() {
    this.fetchData();
    this.fetchSelectData()
  },
  data() {
    return {
      dataList: [],
      departSelectData: [],
      listLoading: true,
      total: 0,
      layout: "total, sizes, prev, pager, next, jumper",
      hederCellStyle: {
        backgroundColor: "#f5f7fa",
        color: "#303133",
      },
      queryForm: {
        pn: 1,
        limit: 10,
        name: "",
        pid: "",
      },
    };
  },
  methods: {
    async fetchData() {
      this.listLoading = true;
      const {
        datas: { datas, total },
      } = await departList(this.queryForm);
      this.total = total;
      this.dataList = datas;
      this.listLoading = false;
      this.fetchSelectData()
    },
    async fetchSelectData() {
      const { datas: { datas }} = await departSelect()
      this.departSelectData = datas
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
      this.$refs.check.showCheck(row);
    },
    handleEdit(row) {
      if (row) {
        row.pid = row.parentId.toString()
        this.$refs.edit.showEdit(this.departSelectData, row);
      } else {
        this.$refs.edit.showEdit(this.departSelectData);
      }
    },
    handleDel(row) {
      this.$confirm("确定要删除当前项吗?", "温馨提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          departDel(row.id).then((res) => {
            if (res.datas.status === 200) {
              this.$message({
                type: "success",
                message: "删除成功",
              });
              this.fetchData();
            }
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
};
</script>

<style lang="scss" scoped>
  .row-style {
    display: flex;
  }
  .text-content {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
</style>