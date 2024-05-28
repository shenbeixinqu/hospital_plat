<template>
  <el-form class="el-form" :model="form" :rules="rules" ref="form" label-width="150px">
    <el-form-item label="自动生成报告策略">
      <el-switch
        v-model="form.if_switch"
        active-color="#1890ff"
        @change="switchChange"
      />
      <div class="desc">开启后会按规则自动生成业务报告</div>
    </el-form-item>
    <template v-if="form.if_switch">
        <el-form-item label="个人年度报告" prop="person">
          <div>
            下一年
            <el-input v-model="form.person_report_month" size="small" class="form-length" clearable />
            月
            <el-input v-model="form.person_report_day" size="small" class="form-length" clearable />
            号
          </div>
          <div class="desc">为0时表示不启用本条策略</div>
        </el-form-item>
        <el-form-item label="科室年度报告" prop="department">
          <div>
            下一年
            <el-input v-model="form.department_report_month" size="small" class="form-length" clearable />
            月
            <el-input v-model="form.department_report_day" size="small" class="form-length" clearable />
            号
          </div>
          <div class="desc">为0时表示不启用本条策略</div>
        </el-form-item>
        <el-form-item label="全年年度报告" prop="all">
          <div>
            下一年
            <el-input v-model="form.all_report_month" size="small" class="form-length" clearable />
            月
            <el-input v-model="form.all_report_day" size="small" class="form-length" clearable />
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
import { yearReportData, yearReportApply} from '@/api/system/report'
export default {
  created() {
    this.getYearReportData()
  },
  data() {
    return {
      form: {},
      rules: {
        person: [
          {
            validator: (rule, value, callback) => {
              if (!Number.isInteger(Number(this.form.person_report_month)) || this.form.person_report_month < 0 || this.form.person_report_month > 12) {
                callback(new Error('请输入0到12之间的整数'))
              } else if (!Number.isInteger(Number(this.form.person_report_day)) || this.form.person_report_day < 0 || this.form.person_report_day > 31) {
                callback(new Error('请输入0到31之间的整数'))
              }  else {
                callback()
              }
            },
            trigger: "blur"
          }
        ],
        department: [
          {
            validator: (rule, value, callback) => {
              if (!Number.isInteger(Number(this.form.department_report_month)) || this.form.department_report_month < 0 || this.form.department_report_month > 12) {
                callback(new Error('请输入0到12之间的整数'))
              } else if (!Number.isInteger(Number(this.form.department_report_day)) || this.form.department_report_day < 0 || this.form.department_report_day > 31) {
                callback(new Error('请输入0到31之间的整数'))
              }  else {
                callback()
              }
            },
            trigger: "blur"
          }
        ],
        all: [
          {
            validator: (rule, value, callback) => {
              if (!Number.isInteger(Number(this.form.all_report_month)) || this.form.all_report_month < 0 || this.form.all_report_month > 12) {
                callback(new Error('请输入0到12之间的整数'))
              } else if (!Number.isInteger(Number(this.form.all_report_day)) || this.form.all_report_day < 0 || this.form.all_report_day > 31) {
                callback(new Error('请输入0到31之间的整数'))
              }  else {
                callback()
              }
            },
            trigger: "blur"
          }
        ]
      }
    }
  },
  methods: {
    getYearReportData() {
      yearReportData().then(res => {
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
          person_report_month: 0,
          person_report_day: 0,
          department_report_month: 0,
          department_report_day: 0,
          all_report_month: 0,
          all_report_day: 0
        }
        this.formApply()
      }
    },
    formApply() {
      this.$refs.form.validate(valid => {
        if (valid) {
          yearReportApply(this.form).then(res => {
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
  }
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