<template>
  <el-form class="el-form" :model="form" ref="form" :rules="rules" label-width="200px">
    <el-form-item label="患者就诊省份显示数量" prop="consultation_count">
      <el-input
        class="form-length"
        v-model.number="form.consultation_count"
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
      <el-button type="primary" size="small">应用</el-button>
      <el-button size="small">恢复默认设置</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
      },
      rules: {
        consultation_count: [
          { required: true, validator: this.validateIntegerInRangeTen, trigger: 'blur' }
        ],
        disease_count: [
          { required: true, validator: this.validateIntegerInRangeTen, trigger: 'blur' }
        ],
        department_max_count: [
          { required: true, validator: this.validateIntegerInRangeSix, trigger: 'blur' }
        ],
        department_min_count: [
          { required: true, validator: this.validateIntegerInRangeFour, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 自定义验证函数
    validateIntegerInRangeTen(rule, value, callback) {
      const num = Number(value);
      console.log("num", num, typeof(num))
      if (!Number.isInteger(num) || num < 10 || num > 12) {
        callback(new Error('请输入10到12之间的整数'));
      } else {
        callback();
      }
    },
    validateIntegerInRangeSix(rule, value, callback) {
      const num = Number(value);
      console.log("num", num, typeof(num))
      if (!Number.isInteger(num) || num < 6 || num > 8) {
        callback(new Error('请输入6到8之间的整数'));
      } else {
        callback();
      }
    },
    validateIntegerInRangeFour(rule, value, callback) {
      const num = Number(value);
      console.log("num", num, typeof(num))
      if (!Number.isInteger(num) || num < 4 || num > 6) {
        callback(new Error('请输入4到6之间的整数'));
      } else {
        callback();
      }
    },
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