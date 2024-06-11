<template>
  <el-col :span="24">
    <el-card class="page-header" shadow="never">
      <el-avatar class="page-header-avatar" :src="avatar" />
      <div class="page-header-tip">
        <p class="page-header-tip-title">
          {{ handleTips() }}
        </p>
        <p class="page-header-tip-description">
          <span>科室: {{ dep_name| depNameFilter }}</span>
          <span class="page-header-split-span">|</span>
          <span>角色: {{ role_name }}</span>
          <span class="page-header-split-span">|</span>
        </p>
      </div>
      <div class="page-header-data">
        <div class="page-header-data-part">
          <div class="page-header-data-yesterday">昨日复诊挂号人次</div>
          <div class="page-header-data-number">{{ registered_count }}</div>
        </div>
        <div class="split-line"></div>
        <div class="page-header-data-part">
          <div class="page-header-data-yesterday">昨日患者退号人次</div>
          <div class="page-header-data-number">{{ return_count }}</div>
        </div>
        <div class="split-line"></div>
        <div class="page-header-data-part">
          <div class="page-header-data-yesterday">昨日接诊人次</div>
          <div class="page-header-data-number">{{ admission_count }}</div>
        </div>
      </div>
    </el-card>
  </el-col>
</template>

<script>
import { mapGetters } from "vuex";
import { header_data } from '@/api/index'

export default {
  data() {
    return {
      registered_count: "",
      return_count: "",
      admission_count: ""
    };
  },
  created() {
    this.get_header_data()
  },
  filters: {
    depNameFilter(val) {
      if (val === '') {
        return "暂无"
      } else {
        return val
      }
    }
  }, 
  computed: {
    ...mapGetters({
      avatar: "user/avatar",
      username: "user/username",
      userid: "user/userid",
      dep_name: "user/dep_name",
      role_name: "user/role_name"
    }),
  },
  methods: {
    get_header_data() {
      header_data({ user_id: this.userid }).then(res => {
        this.registered_count = res.datas.registered_count
        this.return_count = res.datas.return_count
        this.admission_count = res.datas.admission_count
      })
    },
    handleTips() {
      const hour = new Date().getHours();
      return hour < 8
        ? `早上好 ${this.username}, 又是元气满满的一天。`
        : hour <= 11
        ? `上午好 ${this.username}, 看到你我好开心。`
        : hour <= 13
        ? `中午好 ${this.username}，忙碌了一上午，记得吃午饭哦。`
        : hour < 18
        ? `下午好 ${this.username}，你一定有些累了，喝杯咖啡提提神。`
        : `晚上好 ${this.username}，愿你天黑有灯，下雨有伞。`;
    },
  },
};
</script>

<style lang="scss" scoped>
.page-header {
  min-height: 105px;
  transition: $base-transition;

  ::v-deep {
    * {
      transition: $base-transition;
    }

    .el-card__body {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
    }
  }

  &-avatar {
    width: 60px;
    height: 60px;
    margin-right: 20px;
    border-radius: 50%;
  }

  &-tip {
    flex: auto;
    // width: calc(100% - 500px);
    min-width: 200px;

    &-title {
      margin-bottom: 12px;
      font-size: 20px;
      font-weight: bold;
      color: #3c4a54;
    }

    &-description {
      font-size: $base-font-size-default;
      color: #808695;
    }
  }

  &-data {
    display: flex;
    &-part {
      padding: 0 8px;
    }
    &-yesterday {
      color: #929292;
    }
    &-number {
      font-size: 30px;
      font-weight: 700;
      text-align: right;
    }
  }

  &-avatar-list {
    flex: 1;
    min-width: 100px;
    margin-left: 20px;
    text-align: right;

    p {
      margin-right: 9px;
      line-height: 0;

      span {
        padding: 0 13px;
      }
    }
  }
  &-split-span {
    padding-right: 8px;
    padding-left: 8px;
  }
  .split-line {
    width: 2px;
    height: 48px;
    background-color: #ccc;
  }
}
</style>
