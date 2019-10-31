<template>
  <v-app>
    <loading loader="bars"
        :active.sync="isLoading"
        :can-cancel="true"
        :is-full-page="false"
        color="#EE8802"
        background-color="transparent">
    </loading>
    <div id="chart">
        <v-container fill-height fluid>
          <v-col column>
              <v-row class="mytitle white--text mt-10">統計資訊</v-row>
              <v-row>
                    <div class="mytext white--text mt-5 mb-6">本系統資料庫標籤為假新聞，各家媒體累積比例</div>
              </v-row>
              <v-row justify="center" class="sta_space">
                  <VueApexCharts width="600px" type="bar" :options="options_fake" :series="series_fake"></VueApexCharts>
              </v-row>
              <v-row>

                  <div class="mytext white--text mt-5 mb-6">使用本系統查詢之新聞，各家媒體累積數量</div>
              </v-row>
              <v-row justify="center">
                  <VueApexCharts width="600px" type="bar" :options="options" :series="series"></VueApexCharts>
              </v-row>
          </v-col>
        </v-container>
    </div>
  </v-app>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import axios from 'axios'
import env from '../env';

import VueLoading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/vue-loading.css'

export default {
  components: {
      VueApexCharts,
  },
  beforeDestroy () {
    clearInterval(this.interval)
  },
  data: function() {
      return {
          isLoading: true,
          interval: {},
          value: 0,
          options: {
              chart: {
                  id: 'media-fakenews',
                  toolbar: {
                    show: false,
                  },
              },
              xaxis: {
                  categories: ['222', '333', 'dfs',],
                  labels: {
                    style: {
                      fontSize: '14px',
                      fontFamily: 'Noto Sans TC, sans-serif',
                      colors: 'white',
                    }
                  }
              },
              yaxis: {
                  labels: {
                    style: {
                      fontSize: '14px',
                      fontFamily: 'Noto Sans TC, sans-serif',
                      color: 'white',
                    }
                  }
              },
              colors: ['#FF9100' ],
          },
          series: [],
          options_fake: {
            chart: {
                id: 'media-fakenews2',
                toolbar: {
                  show: false,
                },
            },
            xaxis: {
                categories: ['蘋果', '自由', '聯合','風傳媒','東森','奇摩','壹週刊','中時','TVBS','上報','其他'],
                labels: {
                  style: {
                    fontSize: '14px',
                    fontFamily: 'Noto Sans TC, sans-serif',
                    colors: 'white',
                  }
                }
            },
            yaxis: {
                labels: {
                  style: {
                    fontSize: '14px',
                    fontFamily: 'Noto Sans TC, sans-serif',
                    color: 'white',
                  }
                }
            },
            colors: ['#FF9100' ],
          },
          series_fake:  [{
              name: '本系統內的假新聞',
              data: [6/40, 6/40, 9/40, 1/40, 3/40, 3/40, 1/40, 5/40, 2/40, 2/40, 2/40]
          }],
          news: []

      }
  },
  mounted() {

    axios
    .get(env+'/api/stat')
    .then(response => {
      let series = [];
      let news = [];
      console.log("response stat", response.data);
      for (var i = 0, len = response.data.length; i < len; i++) {
        series = series.concat([response.data[i].fakeNewsNB]);
        news = news.concat([response.data[i].name]);
      }
      this.series.push({
          name: '使用本系統查詢之新聞數量',
          data: series
      });
      console.log("news", news);
      console.log(this.options);

      this.news = news;
      console.log(this.options);

      this.options = {
        ...this.chartOptions, ...{
          xaxis: {
            categories: news
          }
        }
      };
    })
    .catch(error => {
        console.log(error)
        this.errored = true
    })
    .finally(() => {
        this.interval2 = setTimeout(() => {
            this.isLoading = false
        },1000);

    })

  },
  methods: {
      wordClickHandler(name, value, vm) {
      console.log('wordClickHandler', name, value, vm);
      },
      progress(event,progress,stepValue){
          console.log(stepValue);
      },
      progress_end(event){
          console.log("Circle progress end");
      }
  },

}
</script>

<style>
.sta_space{
  margin-bottom: 60px
}

</style>
