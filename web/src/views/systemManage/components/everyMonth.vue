<template>
  <el-form class="el-form" :model="form" ref="form" :rules="rules" label-width="150px">
    <el-form-item label="自动生成报告策略">
      <el-switch 
        v-model="form.if_switch"
        active-color="#1890ff"
        @change="switchChange"
      />
      <div class="desc">开启后会按规则自动生成业务报告。</div>
    </el-form-item>
    <template v-if="form.if_switch">
       <el-form-item label="个人每月报告" prop="person_report_date">
        <div>
          个人每月报告
          <el-input size="small" class="form-length" v-model="form.person_report_date" clearable/>
          号
        </div>
        <div class="desc">为0时表示不启用本条策略</div>
       </el-form-item>
       <el-form-item label="科室每月报告" prop="department_report_date">
        <div>
          科室每月报告
          <el-input size="small" class="form-length" v-model="form.department_report_date" clearable/>
          号
        </div>
        <div class="desc">为0时表示不启用本条策略</div>
       </el-form-item>
       <el-form-item label="全院每月报告" prop="all_report_date">
        <div>
          全院每月报告
          <el-input size="small" class="form-length" v-model="form.all_report_date" clearable/>
          号
        </div>
        <div class="desc">为0时表示不启用本条策略</div>
       </el-form-item>
       <el-form-item class="form-button">
        <el-button type="primary" size="small" @click="formApply">应用</el-button>
      </el-form-item>
    </template>
  </el-form>
</template>

<script>
import { monthReportData, monthReportApply } from '@/api/system/report'

export default {
  created() {
    this.getMonthReportData()
  },
  data() {
    return {
      form: {},
      rules: {
        person_report_date: [
          { required: true, validator: this.validateIntegerInRangeOne, trigger: 'blur' }
        ],
        department_report_date: [
          { required: true, validator: this.validateIntegerInRangeOne, trigger: 'blur' }
        ],
        all_report_date: [
          { required: true, validator: this.validateIntegerInRangeOne, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 自定义验证函数
    validateIntegerInRangeOne(rule, value, callback) {
      const num = Number(value);
      const res = !Number.isInteger(num) || num < 0 || num > 28
      if (!Number.isInteger(num) || num < 0 || num > 28) {
        callback(new Error('请输入0到28之间的整数'));
      } else {
        callback();
      }
    },
    getMonthReportData() {
      monthReportData().then(res => {
        if (res.code === 200) {
          this.form = res.datas
        } else {
          this.$message({
            type: "error",
            message: res
          })
        }
      })
    },
    switchChange(val) {
      if (val === false) {
        this.form = {
          if_switch: false,
          person_report_date: 0,
          department_report_date: 0,
          all_report_date: 0
        }
        this.formApply()
      }
    },
    formApply() {
      this.$refs.form.validate(valid => {
        if (valid) {
          monthReportApply(this.form).then(res => {
            if (res.code === 200) {
              this.$message({
                type: "success",
                message: res.msg
              })
            } else {
              this.$message({
                type: "error",
                message: res
              })
            }
          })
        }
      })
    }
  },
}
</script>

<style lang="scss" scoped>
.el-form {
  margin-top: 60px;
}
.form-length {
  width: 7%;
  margin: 0 4px;
}
.form-button {
  margin-top: 40px;
}
.desc {
  color: #aaa;
  font-size: 12px;
}
</style>