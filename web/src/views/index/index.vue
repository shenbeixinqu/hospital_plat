<template>
  <div class="index-container">
    <el-row :gutter="20">
      <page-header />
    </el-row>
    <el-tabs v-model="activeName" type="card" @tab-click="tabClick">
      <template v-for="(item, index) in tabData">
        <el-tab-pane :label="item.label" :name="item.name" :key="index">
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
        { label: "@我", name: "my" },
        { label: "科室", name: "room" },
        { label: "全院", name: "all" },
      ],
      activeName: "my",
      statisticsData: {},
    };
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
