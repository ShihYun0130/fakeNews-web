<template>
  <v-app>
    <div id="chart">
        <v-container fill-height fluid>
          <v-col align-start column>
              <div class="mysubtitle white--text mt-10 xs-12 mb-12">統計資訊</div>
              <v-row justify="center" class="pt-3">
                <VueApexCharts width="550px" type="bar" :options="options" :series="series"></VueApexCharts>
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
                  id: 'vuechart-example'
              },
              xaxis: {
                  categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998]
              }
          },
          series: [{
              name: 'series-1',
              data: [30, 40, 45, 50, 49, 60, 70, 91]
          }],
          chartOptions: {
              responsive: [{
                  breakpoint: 480,
                  options: {
                      chart: {
                          width: 200
                      },
                      legend: {
                          position: 'bottom'
                      }
                  }
              }]
          },
          myColors: ['#FF9100', '#E65100'],
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
