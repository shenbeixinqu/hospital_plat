<template>
  <el-form
    class="el-form"
    :model="form"
    ref="form"
    :rules="rules"
    label-width="200px"
  >
    <el-form-item label="昨日接诊量警戒值" prop="admission_count">
      <el-input
        class="form-length"
        v-model="form.admission_count"
        placeholder="请输入100到120之间的整数"
        clearable
      >
        <template slot="append">人次</template>
      </el-input>
    </el-form-item>
    <el-form-item label="昨日退号量警戒值" prop="retreat_count">
      <el-input
        class="form-length"
        v-model="form.retreat_count"
        placeholder="请输入100到120之间的整数"
        clearable
      >
        <template slot="append">人次</template>
      </el-input>
    </el-form-item>
    <el-form-item label="问题发生最多科室显示数量" prop="department_max_count">
      <el-input
        class="form-length"
        v-model="form.department_max_count"
        placeholder="请输入6到8之间的整数"
        clearable
      />
    </el-form-item>
    <el-form-item class="form-button">
      <el-button type="primary" size="small" @click="formApply">应用</el-button>
      <el-button size="small" @click="formReset">恢复默认设置</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { warningData, warningApply} from '@/api/system/screen'
export default {
  created() {
    this.getWarningData()
  },
  data() {
    return {
      form: {},
      resetData: [100, 100, 6],
      rules: {
        admission_count: [
          { required: true, validator: this.validateIntegerInRangeOne, trigger: 'change' }
        ],
        retreat_count: [
          { required: true, validator: this.validateIntegerInRangeOne, trigger: 'change' }
        ],
        department_max_count: [
          { required: true, validator: this.validateIntegerInRangeFour, trigger: 'change' }
        ]
      },
    };
  },
  methods: {
    // 自定义验证函数
    validateIntegerInRangeOne(rule, value, callback) {
      const num = Number(value);
      if (!Number.isInteger(num) || num < 100 || num > 120) {
        callback(new Error("请输入100到120之间的整数"));
      } else {
        callback();
      }
    },
    validateIntegerInRangeSix(rule, value, callback) {
      const num = Number(value);
      if (!Number.isInteger(num) || num < 6 || num > 8) {
        callback(new Error("请输入6到8之间的整数"));
      } else {
        callback();
      }
    },
    // 获取初始数据
    getWarningData() {
      warningData().then(res => {
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
    formApply() {
      this.$refs.form.validate(valid => {
        if (valid) {
          warningApply(this.form).then(res => {
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
    },
    // 恢复默认设置
    formReset() {
      this.form = {
        admission_count: this.resetData[0],
        retreat_count: this.resetData[1],
        department_max_count: this.resetData[2],
      }
    }
  },
};
</script>

<style lang="scss" scoped>
.el-form {
  margin-top: 60px;
}
.form-length {
  width: 50%;
}
.form-button {
  margin-top: 40px;
}
</style>