<template>
  <v-app>
    <div id="chart">
        <v-container fill-height fluid>
          <v-col column>
              <v-row class="mytitle white--text mt-10">統計資訊</v-row>
              <v-row>
                  <div class="mytext white--text mt-5 mb-6">各媒體於本系統累積疑似假新聞之數量</div>
                  <div class="mysubtext white--text mt-6">(假新聞機率高於50%)</div>
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

export default {
  components: {
      VueApexCharts,
  },
  beforeDestroy () {
    clearInterval(this.interval)
  },
  data: function() {
      return {
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
                  categories: ['TVBS', 'ETtoday', '蘋果日報', '中國時報', '自由時報', '聯合報', '中央社', '新頭殼'],
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
          series: [{
              name: '疑似假新聞數量',
              data: [50, 60, 92, 73, 63, 53, 70, 42]
          }],

      }
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

</style>
