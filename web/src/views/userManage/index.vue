<template>
  <div class="user-container">
    <uni-query-form>
      <uni-query-form-left-panel>
        <el-row :gutter="10" class="row-style">
          <el-col :span="6">
            <div class="text-content">医生姓名:</div>
          </el-col>
          <el-col :span="8">
            <el-input
              size="small"
              placeholder="请输入姓名"
              clearable
              v-model="queryForm.name"
            />
          </el-col>
          <el-col :span="6">
            <div class="text-content">科室或人员:</div>
          </el-col>
          <el-col :span="8">
            <el-select
              v-model="queryForm.depid"
              size="small"
              clearable
              filterable
              placeholder="请选择"
              @change="changeDepartId"
            >
              <el-option
                v-for="item in departSelectData"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              />
            </el-select>
          </el-col>
          <el-col :span="8">
            <el-select
              v-model="queryForm.usid"
              size="small"
              clearable
              filterable
              placeholder="请选择"
            >
              <el-option
                v-for="item in userSelectData"
                :key="item.id"
                :label="item.realname"
                :value="item.id"
              />
            </el-select>
          </el-col>
          <el-col :span="5">
            <el-button size="small" type="primary" @click="fetchData"
              >搜索</el-button
            >
          </el-col>
        </el-row>
        <el-row :gutter="10" class="row-style">
          <el-col :span="6">
            <div class="text-content">入职时间:</div>
          </el-col>
          <el-col :span="12">
            <el-date-picker v-model="sedt" size="small" type="daterange" format="yyyy-MM-dd" value-format="yyyy-MM-dd" range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期" />
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
      <el-table-column label="用户ID" align="center" prop="id" />
      <el-table-column label="医生姓名" align="center" prop="realName" />
      <el-table-column label="科室" align="center" prop="depart" />
      <el-table-column label="入职时间" align="center" prop="joinDate">
        <template slot-scope="scope">
          {{ formatDateString(scope.row.joinDate) }}
        </template>
      </el-table-column>
      <el-table-column label="角色" align="center" prop="role" />
      <el-table-column label="工种" align="center" prop="job" />
      <el-table-column label="年龄" align="center" prop="age" />
      <el-table-column label="添加时间" align="center" prop="addtime">
        <template slot-scope="scope">
          {{ formatDateString(scope.row.addtime) }}
        </template>
      </el-table-column>
      <el-table-column label="账号状态" align="center" prop="locked">
        <template slot-scope="scope">
          <el-switch
            v-model="scope.row.locked"
            active-color="#13ce66"
            inactive-color="#555">
          </el-switch>
        </template>
      </el-table-column>
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
import { userList } from "@/api/users";
import { departSelect } from "@/api/depart";
import { userAllList } from "@/api/common"
import { formatDate } from "@/utils"
import Edit from "./components/Edit.vue"

export default {
  name: "usersManage",
  created() {
    this.fetchData();
    this.fetchDepartSelectData()
  },
  components: {
    Edit
  },
  data() {
    return {
      dataList: [],
      departSelectData: [], // 科室
      userSelectData: [],

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
        depid: "",
        usid: "",
        sdt: "",
        edt: "",
      },
      sedt: '', // 搜索参数-开始结束时间
    };
  },
  methods: {
    formatDateString(params) {
      return formatDate(params)
    },
    async fetchData() {
      this.listLoading = true;
      this.queryForm.sdt = this.sedt ? this.sedt[0] : ''; // 提醒开始日期
      this.queryForm.edt = this.sedt ? this.sedt[1] : ''; // 提醒结束日期
      const {
        datas: { datas, total },
      } = await userList(this.queryForm);
      this.total = total;
      this.dataList = datas;
      this.listLoading = false;
    },
    async fetchDepartSelectData() {
      const { datas: { datas }} = await departSelect()
      this.departSelectData = datas
    },
    async fetchUserSelectData(params) {
      const { datas: { datas }} = await userAllList(params)
      this.userSelectData = datas
    },
    // 更改科室人员
    changeDepartId(val) {
      this.fetchUserSelectData({did: val})
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
        this.$refs.edit.showEdit(row);
      } else {
        this.$refs.edit.showEdit();
      }
    },
  },
};
</script>

<style lang="scss" scoped>
  .row-style {
    display: flex;
    margin-bottom: 6px;
    text-align: left;
  }
  .text-content {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
</style>