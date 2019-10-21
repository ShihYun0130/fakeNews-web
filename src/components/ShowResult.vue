<template>
    <v-app>
        <div id="showResult">
            <v-container fluid class="pa-0">
                <div class="result-news-container">
                    <h1 class="mytitle result-news">{{title}}</h1>
                    <div class="mytext result-news">新聞來源：{{source}}<br/>新聞發布時間：{{time}}</div>
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
                            <div class="myspace">有效文章數：105</div>
                        </div>
                        <div class="mytext">相關ID：cloud7515、ReeJan</div>
                    </v-col>
                    <v-col md="4" class="pt-10 pb-10 result-analysis result-analysis-right">
                        <h2 class="mysubtitle mb-2">Ptt 轉發時間：2019-09-02 18:51</h2>
                        <div class="mytext">Ptt 轉發 IP：61.228.39.106 (臺灣)</div>
                        <div class="mytext">第一次轉貼至本系統時間：2019-09-30 18:01</div>
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
                        <img :src=wordCloud_result alt="word cloud" class="wordcloud" />
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
            title: this.$route.params.result.title,
            source: '',
            time: '',
            content: '',
            PttId: '',
            PttReplyNum: 0,

            wordCloud_result,
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
                    categories: ['開心', '驚奇', '有趣', '無感', '害怕', '悲傷', '憤怒'],
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
            series: [{
                name: '留言個數',
                data: [30, 40, 45, 50, 49, 60, 70]
            }],
            pieseries: [0,0,0],
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
            defaultWords: [{
                "name": "台灣",
                "value": 55
                },
                {
                "name": "笑死",
                "value": 34
                },
                {
                "name": "郭文貴",
                "value": 10
                },
                {
                "name": "來啊",
                "value": 32
                },
                {
                "name": "快打",
                "value": 17
                },
                {
                "name": "美國",
                "value": 12
                },
                {
                "name": "香港",
                "value": 11
                },
                {
                "name": "笑你不敢",
                "value": 10
                },
                {
                "name": "來阿",
                "value": 9
                },
                {
                "name": "哈哈哈",
                "value": 6
                },
                {
                "name": "要打快打",
                "value": 8
                },
                {
                "name": "拜託快打",
                "value": 8
                },
                {
                "name": "日本",
                "value": 5
                },
                {
                "name": "打台灣",
                "value": 5
                },
                {
                "name": "呵呵",
                "value": 5
                },
                {
                "name": "不可能",
                "value": 5
                },
                {
                "name": "班農",
                "value": 5
                },
                {
                "name": "北七",
                "value": 5
                },
                {
                "name": "給你錢",
                "value": 5
                },

            ],
            hotnews: [
            {
                
            },
            ],
        }
    },
    beforeMount () {
        let result = JSON.parse(window.localStorage.getItem('result')||'[]');
        // predict value
        let pred = new Number(result.pred * 100);
        this.value = pred.toFixed(3);
        this.interval = setTimeout(() => {
            if (this.value === 100) {
                return (this.value = 0)
            }
        }, 1000)
        this.title = result.title;
        this.source = result.source;
        this.time = result.time;
        this.content = result.content;
        this.PttId = result.uid;
        this.PttReplyNum = result.msg_a;
        this.pieseries = [
            result.msg_p, 
            result.msg_b, 
            result.msg_n
        ];


        let hot = JSON.parse(window.localStorage.getItem('hot')||'[]');
        if(!hot){
            axios
            .get('http://localhost:5000/api/search')
            .then(response => {
                console.log("hot", response);
                window.localStorage.setItem('hot', JSON.stringify(response.data));
                hot = response.data;
                
            })
            .catch(error => {
                console.log(error)
                this.errored = true
            })
        }
        this.hotnews = hot;
        
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
  font-size: 45px;
}
.apexcharts-tooltip {
    background: #f3f3f3;
    color: black;
    font-Size: '10px';
    font-family: 'Noto Sans TC', sans-serif;
}
</style>
