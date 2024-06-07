<template>
  <div class="index-container">
    <el-row :gutter="20">
      <page-header />
    </el-row>
    <el-tabs v-model="activeName" type="card" @tab-click="tabClick">
      <template v-for="(item, index) in tabData">
        <el-tab-pane :label="item.label" :name="item.name" :key="index" v-if="checkPermission(item.permission)">
          <rank :statisticsData="statisticsData" v-if="activeName === item.name" />
        </el-tab-pane>
      </template>
    </el-tabs>
  </div>
</template>

<script>
import PageHeader from "./components/PageHeader.vue";
import Rank from "./components/rank.vue";
import { statistics_data } from "@/api/index";
import { mapGetters } from 'vuex';

export default {
  name: "Index",
  created() {
    this.get_statistics_data();
  },
  components: {
    PageHeader,
    Rank,
  },
  data() {
    return {
      tabData: [
        { label: "@我", name: "my", "permission":  0 },
        { label: "科室", name: "room", "permission": 9 },
        { label: "全院", name: "all", "permission": 10 },
      ],
      activeName: "my",
      statisticsData: {
        month_repeat_count: 0,
        month_repeat_count_same: 0,
        month_repeat_count_ring: 0,
        year_repeat_count: 0,
        year_repeat_count_same: 0,

        month_accept_count: 0,
        month_accept_count_same: 0,
        month_accept_count_ring: 0,
        year_accept_count: 0,
        year_accept_count_same: 0,

        month_drug_income: 0 ,
        month_drug_income_same: 0,
        month_drug_income_ring: 0,
        year_drug_income: 0,
        year_drug_income_same: 0,
      },
    };
  },
  computed: {
    ...mapGetters({
      role: "acl/role"
    })
  },
  methods: {
    get_statistics_data() {
      statistics_data({ type: this.activeName }).then((res) => {
        if (res.datas.status === 200) {
          this.statisticsData = res.datas;
        } else {
          console.log(res.msg)
        }
      });
    },
    // tab切换，请求后台接口
    tabClick() {
      this.get_statistics_data();
    },
    // 验证是否有对应的权限
    checkPermission(permission) {
      if (permission === 0) {
        return true
      } else {
        return this.role.includes(permission)
      }
    }
  },
};
</script>

<style lang="scss" scoped>
.index-container {
  padding: 0 !important;
  background: $base-color-background !important;

  ::v-deep {
    .access,
    .authorization,
    .version-information {
      min-height: 268px;
    }

    .el-card {
      .el-card__header {
        position: relative;

        .card-header-tag {
          position: absolute;
          top: 15px;
          right: $base-margin;
        }

        > div > span {
          display: flex;
          align-items: center;

          i {
            margin-right: 3px;
          }
        }
      }

      .el-card__body {
        position: relative;

        .echarts {
          width: 100%;
          height: 127px;
        }

        .card-footer-tag {
          position: absolute;
          right: $base-margin;
          bottom: 15px;
        }
      }
    }

    .bottom {
      padding-top: 20px;
      margin-top: 5px;
      color: #595959;
      text-align: left;
      border-top: 1px solid $base-border-color;
    }
  }
}
</style>
