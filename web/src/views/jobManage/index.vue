<template>
  <div class="job-container">
    <uni-query-form>
      <uni-query-form-left-panel>
        <el-row :gutter="20">
          <el-col :span="18">
            <el-input
              size="small"
              placeholder="请输入工种名称"
              clearable
              v-model="queryForm.name"
            />
          </el-col>
          <el-col :span="6">
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
          >添加</el-button
        >
      </uni-query-form-left-panel>
    </uni-query-form>
    <el-table
      :loading="listLoading"
      :data="dataList"
      :header-cell-style="hederCellStyle"
    >
      <el-table-column label="工种ID" align="center" prop="id" />
      <el-table-column label="工种名称" align="center" prop="name" />
      <el-table-column label="创建时间" align="center" prop="addtime" />
      <el-table-column label="更新时间" align="center" prop="uptime" />
      <el-table-column label="备注" align="center" prop="remark" />
      <el-table-column label="操作" align="center">
        <template #default="{ row }">
          <el-button type="text" @click="handleCheck(row)">查看</el-button>
          <el-button type="text" @click="handleEdit(row)">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 组件 -->
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
import { jobList } from "@/api/job";
import Edit from "./components/edit.vue"

export default {
  name: "jobManage",
  components: {
    Edit,
  },
  created() {
    this.fetchData();
  },
  data() {
    return {
      dataList: [],
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
      },
    };
  },
  methods: {
    async fetchData() {
      this.listLoading = true;
      const {
        datas: { datas, total },
      } = await jobList(this.queryForm);
      this.total = total;
      this.dataList = datas;
      this.listLoading = false;
    },
    handleSizeChange(val) {
      this.queryForm.limit = val;
      this.fetchData();
    },
    handleCurrentChange(val) {
      this.queryForm.pn = val;
      this.fetchData();
    },
    handleCheck(row) {},
    handleEdit(row) {
      if (row) {
        this.$refs.edit.showEdit(row)
      } else {
        this.$refs.edit.showEdit()
      }
    },
  },
};
</script>

<style>
</style>