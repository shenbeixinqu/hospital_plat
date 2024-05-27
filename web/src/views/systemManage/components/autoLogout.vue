<template>
  <el-form class="el-form" :model="form" ref="form" :rules="rules" label-width="150px">
    <el-form-item label="自动登出策略">
      <el-switch 
        v-model="form.if_switch"
        active-color="#1890ff"
      />
      <div class="desc">开启后用户长时间不操作平台,会自动登出账号</div>
    </el-form-item>
    <template v-if="form.if_switch">
      <el-form-item label="自动退出登录" prop="not_operate_minute">
        <div>
          平台登录后,若连续
          <el-input size="small" class="form-length" v-model="form.not_operate_minute" clearable/>
          分钟操作,账号会自动登出
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
import { autoLogoutData, autoLogoutApply} from '@/api/system/security'
export default {
  created() {
    this.getAutoLogoutData()
  },
  components: {
    autoLogoutData,
    autoLogoutApply
  },
  data() {
    return {
      form: {},
      rules: {
        not_operate_minute: [
          { required: true, validator: this.validateIntegerInRangeTen, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 自定义验证函数
    validateIntegerInRangeTen(rule, value, callback) {
      const num = Number(value);
      if (!Number.isInteger(num) || num < 10 || num > 100) {
        callback(new Error('请输入10到100之间的整数'));
      } else {
        callback();
      }
    },
    // 获取初始数据
    getAutoLogoutData() {
      autoLogoutData().then(res => {
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
          autoLogoutApply(this.form).then(res => {
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