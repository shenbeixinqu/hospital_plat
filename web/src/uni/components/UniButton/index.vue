<template>
  <el-button size="small" :type="type" :disabled="isDisabled" @click="onClick">
    {{ buttonText }}
  </el-button>
</template>

<script>
export default {
  props: {
    buttonText: {
      type: String,
      default: '确定'
    },
    disabledDelay: {
      type: Number,
      default: 3000 // 按钮禁用的时间，单位为毫秒
    },
    type: {
      type: String,
      default: "primary"
    }
  },
  data() {
    return {
      isDisabled: false
    };
  },
  methods: {
    onClick() {
      if (this.isDisabled) return;
      this.isDisabled = true; // 禁用按钮
      // 执行点击操作
      this.$emit('click');
      // 延迟解除禁用状态
      setTimeout(() => {
        this.isDisabled = false;
      }, this.disabledDelay);
    }
  }
};
</script>