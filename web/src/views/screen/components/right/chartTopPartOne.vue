<template>
  <div id="part-one">
    <div class="container">
      <div class="column-left">
        <div class="column">
          <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          <div class="desc">
            <div class="title">接诊后无诊断</div>
            <div class="info">
              <span class="count">
                {{ datas.data_one }}
              </span>人次
            </div>
          </div>
        </div>
        <div class="column">
          <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          <div class="desc">
            <div class="title">医生拒诊</div>
            <div class="info">
              <span class="count">
                {{ datas.data_two }}
              </span>人次
            </div>
          </div>
        </div>
        <div class="column">
          <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          <div class="desc">
            <div class="title">投诉(无方案)</div>
            <div class="info">
              <span class="count">
                {{ datas.data_three }}
              </span>人次
            </div>
          </div>
        </div>
      </div>
      <div class="column-right">
        <div class="column">
          <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          <div class="desc">
            <div class="title">无电子病历</div>
            <div class="info">
              <span class="count">
                {{ datas.data_four }}
              </span>人次
            </div>
          </div>
        </div>
        <div class="column">
          <div>
            <img src="@/assets/bg_image/icon.png" alt="描述文字" class="image" />
          </div>
          <div class="desc">
            <div class="title">超时拒诊</div>
            <div class="info">
              <span class="count">
                {{ datas.data_five }}
              </span>人次
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { chartRightTopOne } from "@/api/screen/home";

export default {
  data() {
    return {
      datas: {},
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      chartRightTopOne().then((res) => {
        if (res.code === 200) {
          this.datas = res.datas;
          console.log("Res123456", res);
          console.log("datas", this.datas);
        } else {
          this.$message({
            type: "error",
            message: res,
          });
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
#part-one {
  .container {
    display: flex;
    justify-content: space-between;
    color: white;
    padding: 16px;
  }
  .column-left,
  .column-right {
    width: 50%;
  }
  .column {
    display: flex;
    padding-bottom: 8px
  }
  .title {
    font-size: 12px;
  }
  .desc {
    display: flex;
    flex-direction: column;
    padding-left: 4px;
  }
  .info {
    color: #0dc1ff;
  }
  .count {
    font-weight: 700;
    font-size: 18px
  }
  .image {
    width: 34px;
    height: 34px;
  }
}
</style>