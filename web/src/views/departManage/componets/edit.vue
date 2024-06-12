<template>
  <el-dialog
    :title="title"
    :visible.sync="dialogFormVisible"
    @close="dialogClose"
    width="40%"
  >
    <el-form ref="form" :model="form" :rules="rules" label-width="120px">
      <el-form-item label="组织名称:" prop="name">
        <el-input clearable v-model="form.name" />
      </el-form-item>
      <el-form-item label="上级组织:">
        <el-select v-model="form.pid" filterable clearable placeholder="请选择">
          <el-option
            v-for="item in departSelectData"
            :key="item.id"
            :label="item.name"
            :value="item.id"
            :disabled="item.disabled"
          >
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="组织描述:">
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
import { departAdd, departEdit } from "@/api/depart";

export default {
  name: "departEdit",
  data() {
    return {
      departSelectData: [],
      title: "",
      handle_type: "",
      dialogFormVisible: false,
      form: {},
      rules: {
        name: [
          {
            required: true,
            message: "组织名称不能为空",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    showEdit(departSelectData, row) {
      this.departSelectData = JSON.parse(JSON.stringify(departSelectData));
      if (!row) {
        this.title = "添加组织";
        this.handle_type = "1";
      } else {
        this.title = "编辑组织";
        this.handle_type = "2";
        this.form = Object.assign({}, row);
        this.departSelectData = this.addRequired(this.departSelectData, row.id);
      }
      this.dialogFormVisible = true;
    },
    // 关闭
    dialogClose() {
      this.$refs.form.resetFields();
      this.form = this.$options.data().form;
      this.dialogFormVisible = false;
    },
    // 递归处理组织下拉
    addRequired(data, targetId) {
      data.forEach((item) => {
        if (item.id.toString() === targetId.toString()) {
          item.disabled = true
        }
        if (item.parentId.toString() === targetId.toString()) {
          item.disabled = true;
          this.addRequired(data, item.id);
        } else {
          return;
        }
      });
      return data;
    },
    handleSubmit() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          if (this.handle_type === "1") {
            departAdd(this.form).then((res) => {
              if (res.datas.status === 200) {
                this.$message({
                  type: "success",
                  message: `${this.title}成功`,
                });
                this.$emit("fetch-data");
                this.dialogClose();
              } else {
                this.$message({
                  type: "error",
                  message: res.msg,
                });
              }
            });
          } else {
            departEdit(this.form, this.form.id).then((res) => {
              if (res.datas.status === 200) {
                this.$message({
                  type: "success",
                  message: `${this.title}成功`,
                });
                this.$emit("fetch-data");
                this.dialogClose();
              } else {
                this.$message({
                  type: "error",
                  message: res.msg,
                });
              }
            });
          }
        }
      });
    },
  },
};
</script>

<style>
</style>