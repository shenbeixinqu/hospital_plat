<template>
  <el-form class="el-form" :model="form" ref="form" :rules="rules" label-width="200px">
    <el-form-item label="患者就诊省份显示数量" prop="consultation_count">
      <el-input
        class="form-length"
        v-model="form.consultation_count"
        placeholder="请输入10-12的整数"
        clearable
      />
    </el-form-item>
    <el-form-item label="患者确诊疾病显示数量" prop="disease_count">
      <el-input
        class="form-length"
        v-model="form.disease_count"
        placeholder="请输入10-12的整数"
        clearable
      />
    </el-form-item>
    <el-form-item label="就诊患者最多科室显示数量" prop="department_max_count">
      <el-input
        class="form-length"
        v-model="form.department_max_count"
        placeholder="请输入6-8的整数"
        clearable
      />
    </el-form-item>
    <el-form-item label="就诊患者最少科室显示数量" prop="department_min_count">
      <el-input
        class="form-length"
        v-model="form.department_min_count"
        placeholder="请输入4-6的整数"
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
import { distributedData, distributedApply} from '@/api/system/screen'
export default {
  created() {
    this.getDistributedData()
  },
  data() {
    return {
      form: {
      },
      resetData: [10, 10, 6, 6],
      rules: {
        consultation_count: [
          { required: true, validator: this.validateIntegerInRangeTen, trigger: 'change' }
        ],
        disease_count: [
          { required: true, validator: this.validateIntegerInRangeTen, trigger: 'change' }
        ],
        department_max_count: [
          { required: true, validator: this.validateIntegerInRangeSix, trigger: 'change' }
        ],
        department_min_count: [
          { required: true, validator: this.validateIntegerInRangeFour, trigger: 'change' }
        ]
      }
    }
  },
  methods: {
    // 自定义验证函数
    validateIntegerInRangeTen(rule, value, callback) {
      const num = Number(value);
      if (!Number.isInteger(num) || num < 10 || num > 12) {
        callback(new Error('请输入10到12之间的整数'));
      } else {
        callback();
      }
    },
    validateIntegerInRangeSix(rule, value, callback) {
      const num = Number(value);
      if (!Number.isInteger(num) || num < 6 || num > 8) {
        callback(new Error('请输入6到8之间的整数'));
      } else {
        callback();
      }
    },
    validateIntegerInRangeFour(rule, value, callback) {
      const num = Number(value);
      if (!Number.isInteger(num) || num < 4 || num > 6) {
        callback(new Error('请输入4到6之间的整数'));
      } else {
        callback();
      }
    },
    // 获取初始数据
    getDistributedData() {
      distributedData().then(res => {
        if (res.code === 200) {
          this.form = res.datas
        } else {
          this.$message({
            type: "error",
            message: res,
          });
        }
      })
    },
    // 应用
    formApply() {
      this.$refs.form.validate(valid => {
        if (valid) {
          distributedApply(this.form).then(res => {
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
        consultation_count: this.resetData[0],
        disease_count: this.resetData[1],
        department_max_count: this.resetData[2],
        department_min_count: this.resetData[3]
      }
    }
  }
}
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