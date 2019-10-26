<template>
    <v-app>
        <div id="showResult">
            <v-container fluid class="pa-0">
                <div class="result-news-container">
                    <h1 class="mytitle result-news">{{title}}</h1>
                    <div class="mytext result-news">{{content}}</div>
                    <div class="myprogresscircle">
                        <v-progress-circular
                            :rotate="300"
                            :size="180"
                            :width="10"
                            :value="value"
                            color="white"
                            >
                            <v-col>
                              <v-row>
                                  <v-col class="percent pa-0 font-weight-bold">{{value}}%</v-col>
                              </v-row>
                              <v-row>
                                  <v-col class="mysubtext pa-0 text-center mt-n1">為假新聞</v-col>
                              </v-row>
                            </v-col>
                        </v-progress-circular>
                    </div>
                    <div class="myprogresscircle-small"></div>
                </div>
                <v-row justify="start" class="mt-10">
                    <v-col md="5" class="pt-10 pb-10 result-analysis result-analysis-left">
                        <h2 class="mysubtitle mb-2">Ptt 轉發 ID：<router-link to="/ShowUserResult"><span class="mylinkText">{{PttId}}</span></router-link></h2>
                        <div class="mytext ptt-title">
                            <div>登入次數：724</div>
                            <div class="myspace">有效文章數：{{postNB}}</div>
                        </div>
                        <div class="mytext">相關ID：cloud7515、ReeJan</div>
                    </v-col>
                    <v-col md="4" class="pt-10 pb-10 result-analysis result-analysis-right">
                        <h2 class="mysubtitle mb-2">Ptt 轉發時間：{{time}}</h2>
                        <div class="mytext">Ptt 轉發 IP：{{ip}}</div>
                        <div class="mytext">第一次轉貼至本系統時間：{{currentDate}}</div>
                    </v-col>
                </v-row>
                <v-row justify="start">
                    <v-col md="5" class="result-analysis result-analysis-left">
                        <h2 class="mysubtitle mb-2">Ptt 留言數量：{{PttReplyNum}}</h2>
                        <VueApexCharts type=donut width=380 :options="chartOptions" :series="pieseries" />
                    </v-col>
                    <v-col md="4" class="result-analysis result-analysis-right">
                        <h2 class="mysubtitle mb-2">Ptt 留言情緒分析</h2>
                        <VueApexCharts width="400" type="bar" :options="options" :series="series"></VueApexCharts>
                    </v-col>
                </v-row>
                <v-row justify="start" class="mb-10">
                    <v-col md="9" class="result-analysis result-analysis-left result-analysis-right">
                        <h2 class="mysubtitle mb-2">Ptt 留言文字雲</h2>
                        <img class="wordcloud" v-bind:src="imageBytes" />
                    </v-col>
                </v-row>

                <v-row justify="end" class="mb-10">
                    <v-col md="9" class="pb-10 result-analysis result-analysis-left">
                        <router-link to="/NewsList"><h2 class="mysubtitle mt-10 mb-10 mylinkClean">熱門搜索</h2></router-link>
                        <v-simple-table dark class="hot-table" color="transparent">

                            <template v-slot:default>
                            <thead>
                                <tr>
                                <th class="text-left">新聞標題</th>
                                <th class="text-left">搜尋次數</th>
                                <th class="text-left">假新聞機率</th>
                                </tr>
                            </thead>
                            <tbody>

                                <tr v-for="(news, index) in hotnews" :key="index">
                                <td>{{ news.title }}</td>
                                <td>{{ news.searchCount }}</td>
                                <td>{{ news.prediction }}%</td>
                                </tr>


                            </tbody>
                            </template>

                        </v-simple-table>
                    </v-col>
                </v-row>
            </v-container>
        </div>
    </v-app>
</template>

<script>
import VueApexCharts from 'vue-apexcharts';
import wordcloud from 'vue-wordcloud';
import wordCloud_result from '../assets/wordCloud-result.png'
import axios from 'axios';
import env from '../env';

export default {
    name: "ShowResult",
    components: {
        VueApexCharts,
        wordcloud,
    },
    beforeDestroy () {
      clearInterval(this.interval)
    },
    data: function() {
        return {
            result: {},
            title: '',
            source: '',
            time: '',
            content: '',
            PttId: '',
            ip: '',
            postNB: '',
            imageBytes: '',
            PttReplyNum: 0,
            wordCloud_result,
            currentDate: '',
            interval: {},
            value: 0,
            options: {
                chart: {
                    id: 'vuechart-example',
                    toolbar: {
                      show: false,
                    },
                },
                xaxis: {
                    categories: ['負面', '正面'],
                    labels: {
                      style: {
                        fontSize: '14px',
                        fontFamily: 'Noto Sans TC, sans-serif',
                        colors: 'white',
                      },
                    }
                },
                tooltip: {
                  enabled: true,
                },
                colors: ['#FF9100' ],
            },
            series: [],
            pieseries: [20, 20, 0],
            chartOptions: {
                responsive: [{
                    breakpoint: 480,
                    options: {
                        chart: {
                            width: 200
                        },
                        legend: {
                            position: 'bottom'
                        },

                    }
                }],
                labels: ['推文', '噓文', '箭頭'],
                colors: ['#6AB82D', '#CC3333','#FF9100' ],
                legend: {
                    fontSize: '14px',
                    fontFamily: 'Noto Sans TC, sans-serif',
                    labels: {
                        colors: 'white',
                    },
                }
            },
            myColors: ['#FF9100', '#E65100', '#E78403', '#EE8802', '#FD2F00'],
            myFont: 'Noto Sans TC, sans-serif',
            hotnews: [{}],
        }
    },
    created() {
        
    },
    mounted() {
        let title = JSON.parse(localStorage.getItem('title'));
        axios
            .post(env+'/api/query', { title: title } )
            .then(response => {
                console.log("response", response);
                let result = response.data.resource;

                // error page
                if (!result.title) {
                    console.log("error");
                    this.$router.replace({name: 'ErrorPage'});
                }

                this.result = response.resource;
                this.title = result.title;
                // predict value
                this.value = new Number(result.pred);
                this.interval = setTimeout(() => {
                    if (this.value === 100) {
                        return (this.value = 0)
                    }
                }, 1000)
                // this.title = result.title;
                this.source = result.source;
                this.time = result.time;
                this.content = result.content;
                this.PttId = result.uid;
                this.ip = result.ip;
                this.postNB = result.postNB;
                this.PttReplyNum = result.msg_a;
                this.pieseries = [
                    new Number(result.msg_p), 
                    new Number(result.msg_b), 
                    new Number(result.msg_n)
                ];
                this.series.push({
                    name: '留言個數',
                    data: [
                        new Number(result.sep[0]) + new Number(result.sep[1]), 
                        new Number(result.sep[2]) + new Number(result.sep[3]),
                    ]
                });
                
                let wc = result.wc;
                wc = wc.slice(2);
                wc = wc.slice(0, -1);
                console.log(wc);
                this.imageBytes = "data:image/png;base64,"+wc;
            })
            .catch(error => {
                console.log(error)
                this.errored = true
            })
            .finally(() => this.loading = false)
        
        

        axios
        .get(env+'/api/search')
        .then(response => {
            console.log("hot", response);
            this.hotnews = response.data;
            
        })
        .catch(error => {
            console.log(error)
            this.errored = true
        })


        // record current time
        function formatDate(date) {
            let day = date.getDate();
            let monthIndex = date.getMonth();
            let year = date.getFullYear();
            let h = date.getHours();
            let m = date.getMinutes();
            let s = date.getSeconds();
            return year.toString()+'年'+(monthIndex+1).toString()+'月'+day.toString()+'日'+" "+h.toString()+':'+m.toString()+':'+s.toString();
        }

        console.log(formatDate(new Date())); 
        this.currentDate = formatDate(new Date());

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
#showResult {
    color: white;
    margin-top: 50px;
}
.result-news-container {
    padding-right: 18vw;
}
.result-news {
    margin: 30px 0;
    padding: 0 7.3%!important;
}
.v-progress-circular {
  margin: 1rem;
}
.myprogresscircle {
    position: fixed;
    top: 100px;
    right: 80px;
}
.myprogresscircle-small {
    position: fixed;
    top: 136px;
    right: 116px;
    width: 140px;
    height: 140px;
    border:#FF9100 dotted 3px;
    border-radius: 100%;
}
.result-analysis {
    background: rgb(28,28,28,0.9);
}
.result-analysis-left {
    padding-left: 7.3%!important;
}
.ptt-title {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
}
.wordcloud {
    width: 95%;
}
.myspace {
    margin-left: 30px;
}
.hot-table {
    width: 600px;
}
.percent{
  font-size: 35px;
}
.apexcharts-tooltip {
    background: #f3f3f3;
    color: black;
    font-Size: '10px';
    font-family: 'Noto Sans TC', sans-serif;
}
</style>
