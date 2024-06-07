<template>
  <el-form class="el-form" :model="form" :rules="rules" ref="form" label-width="150px">
    <el-form-item label="账户锁定策略">
      <el-switch
        v-model="form.if_switch"
        active-color="#1890ff"
        @change="switchChange"
      />
      <div class="desc">开启后用户在登录连续失败时将被限制登录</div>
    </el-form-item>
    <template v-if="form.if_switch">
      <el-form-item label="认证错误锁定" prop="group">
        <div>同一用户登录连续错误
          <el-input size="small" class="form-length" v-model="form.error_one" clearable />次,
          账户将被临时锁定<el-input size="small" class="form-length" v-model="form.lock_minute" clearable />分钟
          </div>
        <div class="desc">
          临时锁定在锁定时间到期后可再次尝试登录。为0时表示不启用本条策略
        </div>
        <div>
          同一用户登录连续错误
          <el-input size="small" class="form-length" v-model="form.error_two" clearable />次, 账户将被锁定。
        </div>
        <div class="desc">
          锁定后需要管理员解锁后才能使用。为0时表示不启用本条策略
        </div>
      </el-form-item>
      <el-form-item label="休眠用户锁定" prop="not_login_day">
        <div>
          用户
          <el-input size="small" class="form-length" v-model="form.not_login_day" clearable />
          天未登录, 账号将自动锁定
        </div>
        <div class="desc">
          锁定后需要管理员解锁后才能使用。为0时表示不启用本条策略
        </div>
      </el-form-item>
      <el-form-item class="form-button">
        <el-button type="primary" size="small" @click="formApply">应用</el-button>
      </el-form-item>
    </template>
  </el-form>
</template>

<script>
import { stopLockData, stopLockApply } from '@/api/system/security'
export default {
  created() {
    this.getStopLockData()
  },
  data() {
    return {
      form: {
      },
      rules: {
        group: [
          {
            validator: (rule, value, callback) => {
              if (!Number.isInteger(Number(this.form.error_one)) || this.form.error_one < 0 || this.form.error_one > 10) {
                callback(new Error('请输入0到10之间的整数'))
              } else if (!Number.isInteger(Number(this.form.lock_minute)) || this.form.lock_minute < 0 || this.form.lock_minute > 200) {
                callback(new Error('请输入0到200之间的整数'))
              } else if (!Number.isInteger(Number(this.form.error_two)) || this.form.error_two < 0 || this.form.error_two > 20) {
                callback(new Error('请输入0到20之间的整数'))
              } else {
                callback()
              }
            },
            trigger: "blur"
          }
        ],
        not_login_day: [
          { required: true, validator: this.validateIntegerInRangeThirty, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    // 自定义验证函数
    validateIntegerInRangeThirty(rule, value, callback) {
      const num = Number(value);
      if (!Number.isInteger(num) || num < 0 || num > 30) {
        callback(new Error('请输入0到30之间的整数'));
      } else {
        callback();
      }
    },
    // 获取初始数据
    getStopLockData() {
      stopLockData().then(res => {
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
    // 开关切换
    switchChange(val) {
      if (val === false) {
        this.form = {
          if_switch: false,
          error_one: 0,
          lock_minute: 0,
          error_two: 0,
          not_login_day: 0
        }
        this.formApply('switch')
      }
    },
    getApplyMessage() {
      stopLockApply(this.form).then(res => {
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
    },
    formApply(params) {
      if (params === 'switch') {
        this.getApplyMessage()
      } else {
        this.$refs.form.validate(valid => {
          if (valid) {
            this.getApplyMessage()
          }
        })
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