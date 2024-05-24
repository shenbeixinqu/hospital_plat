<template>
  <div class="container">
    <div class="left">
      <div class="item left-item">
        <div class="item-title">当月复诊号人次</div>
        <div class="item-count">{{ statisticsData?.month_repeat_count|formatNumber }}</div>
        <div class="item-radio">
          <div class="arrow-contain">
            <span>月同比</span>
            <div :class="{ 'arrow-up': statisticsData?.month_repeat_count_same >= 0, 'arrow-down': statisticsData?.month_repeat_count_same < 0}"></div>
            <div>{{ Math.abs(statisticsData?.month_repeat_count_same) }}%</div>
          </div>
          <div class="arrow-contain">
            <span>月环比</span>            
            <div :class="{ 'arrow-up': statisticsData?.month_repeat_count_ring >= 0, 'arrow-down': statisticsData?.month_repeat_count_ring < 0}"></div>
            <div>{{  Math.abs(statisticsData?.month_repeat_count_ring) }}%</div>
          </div>
        </div>
      </div>
      <div class="item left-item">
        <div class="item-title"><span class="item-title-red">全年</span>复诊号人次</div>
        <div class="item-count">{{ statisticsData?.year_repeat_count|formatNumber }}</div>
        <div class="item-radio">
          <div class="arrow-contain">
            <span>同比</span>
            <div :class="{ 'arrow-up': statisticsData?.year_repeat_count_same >= 0, 'arrow-down': statisticsData?.year_repeat_count_same < 0}"></div>
            <div>{{  Math.abs(statisticsData?.year_repeat_count_same) }}%</div>
          </div>
        </div>
      </div>
      <div class="item left-item">
        <div class="item-title">当月接诊人次</div>
        <div class="item-count">{{ statisticsData?.month_accept_count|formatNumber }}</div>
        <div class="item-radio">
          <div class="arrow-contain">
            <span>月同比</span>
            <div :class="{ 'arrow-up': statisticsData?.month_accept_count_same >= 0, 'arrow-down': statisticsData?.month_accept_count_same < 0}"></div>
            <div>{{ Math.abs(statisticsData?.month_accept_count_same) }}%</div>
          </div>
          <div class="arrow-contain">
            <span>月环比</span>            
            <div :class="{ 'arrow-up': statisticsData?.month_accept_count_ring >= 0, 'arrow-down': statisticsData?.month_accept_count_ring < 0}"></div>
            <div>{{  Math.abs(statisticsData?.month_accept_count_ring) }}%</div>
          </div>
        </div>
      </div>
      <div class="item left-item">
        <div class="item-title"><span class="item-title-red">全年</span>接诊人次</div>
        <div class="item-count">{{ statisticsData?.year_accept_count|formatNumber }}</div>
        <div class="item-radio">
          <div class="arrow-contain">
            <span>同比</span>
            <div :class="{ 'arrow-up': statisticsData?.year_accept_count_same >= 0, 'arrow-down': statisticsData?.year_accept_count_same < 0}"></div>
            <div>{{  Math.abs(statisticsData?.year_accept_count_same) }}%</div>
          </div>
        </div>
      </div>
      <div class="item left-item">
        <div class="item-title">当月药品收入</div>
        <div class="item-count">{{ statisticsData?.month_drug_income|formatNumber }}</div>
        <div class="item-radio">
          <div class="arrow-contain">
            <span>月同比</span>
            <div :class="{ 'arrow-up': statisticsData?.month_drug_income_same >= 0, 'arrow-down': statisticsData?.month_drug_income_same < 0}"></div>
            <div>{{ Math.abs(statisticsData?.month_drug_income_same) }}%</div>
          </div>
          <div class="arrow-contain">
            <span>月环比</span>            
            <div :class="{ 'arrow-up': statisticsData?.month_drug_income_ring >= 0, 'arrow-down': statisticsData?.month_drug_income_ring < 0}"></div>
            <div>{{  Math.abs(statisticsData?.month_drug_income_ring) }}%</div>
          </div>
        </div>
      </div>
      <div class="item left-item">
        <div class="item-title"><span class="item-title-red">全年</span>药品收入</div>
        <div class="item-count">{{ statisticsData?.year_drug_income|formatNumber }}</div>
        <div class="item-radio">
          <div class="arrow-contain">
            <span>同比</span>
            <div :class="{ 'arrow-up': statisticsData?.year_drug_income_same >= 0, 'arrow-down': statisticsData?.year_drug_income_same < 0}"></div>
            <div>{{  Math.abs(statisticsData?.year_drug_income_same) }}%</div>
          </div>
        </div>
      </div>
    </div>
    <div class="right">
      <div class="item right-item">
        <div class="rank-title">当年全院医生好评排行</div>
        <div>
          <ul v-for="(item, index) in rankData" :key="index">
            <li class="rank-area">
              <div class="rank-name">
                <span class="iconfont rank-icon" :class="rankIconClass(index)"></span>
                <span>{{ item.name}}</span>
              </div>
              <div class="rank-count">
                {{ item.count }}
              </div>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { rank_data } from '@/api/index'
export default {
  created() {
    this.get_rank_data()
  },
  filters: {
    formatNumber(value) {
      return new Intl.NumberFormat().format(value);
    }
  },
  props: {
    statisticsData: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      rankData: []
    }
  },
  methods: {
    // 排名图标
    rankIconClass(val) {
      if (val === 0) {
        return 'icon-jinpai'
      } else if (val === 1) {
        return 'icon-yinpai'
      } else if (val === 2) {
        return 'icon-tongpai'
      } else if (val === 3) {
        return 'icon-weibiaoti-1'
      } else if (val === 4) {
        return 'icon-5'
      } else if (val === 5) {
        return 'icon-6'
      } else if (val === 6) {
        return 'icon-7'
      }
    },
    // 获取排名数据
    get_rank_data() {
      rank_data().then(res => {
        this.rankData = res.datas
      })
    }
  }
};
</script>

<style lang="scss" scoped>
.container {
  display: flex;
}
.item {
  margin: 10px;
  padding: 20px 50px;
  border: 1px solid #e9e9e9;
  border-radius: 10px;
  box-sizing: border-box; /* 确保内边距和边框不会增加宽度 */

  &-title {
    text-align: center;
    font-size: 16px;
    margin: 8px;
    color: #aaa;

    &-red {
      color: #ff3333;
    }
  }
  &-count {
    text-align: center;
    font-size: 30px;
    font-weight: 700;
  }
  &-radio {
    display: flex;
    justify-content: space-between;
    margin: 20px 0 20px 0;
    span {
      margin-right: 10px;
      color: #aaa;
    }
  }
}
.arrow-contain {
  display: flex;
  align-items: center;

}
.left {
  width: 66%;
  display: flex;
  flex-wrap: wrap;

  &-item {
    width: calc(50% - 20px);
    height: 150px;
  }
}
.right {
  width: 33%;

  &-item {
    height: 320px;
  }
}

/** 医院排行 */
.rank-icon {
  font-size: 20px;
  margin-right: 10px;
}
.rank-name {
  font-size: 18px;
}
.rank-title {
  font-size: 20px;
  font-weight: 700;
  color: #000;
  margin: 5px 0 30px ;
}
.rank-area {
  display: flex;
  justify-content: space-between;
  font-size: 16px;
  margin: 10px;
}
/** 箭头样式 */
.arrow-up,
.arrow-down {
  align-items: center;
  width: 0;
  height: 0;
  border-style: solid;
  margin-left: 5px;
}

.arrow-up {
  border-width: 0 5px 5px 5px;
  border-color: transparent transparent green transparent;
}

.arrow-down {
  border-width: 5px 5px 0 5px;
  border-color: red transparent transparent transparent;
}
</style>