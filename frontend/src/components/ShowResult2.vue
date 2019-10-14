<template>
    <v-app>
        <div id="showResult">
            <v-container fluid class="pa-0">
                <div class="result-news-container">
                    <h1 class="mytitle result-news">帶韓粉爸看《返校》後「想起來了」 網友：國家會感謝你的</h1>
                    <div class="mytext result-news">新聞來源：自由時報<br/>新聞發布時間：2019-09-24 11:27</div>
                    <div class="mytext result-news">
                      有網友在臉書上表示「誠摯建議帶長輩去看《返校》」，並說起上週末家庭日，拐騙爸媽去看《返校》的故事。該名網友說，父母原先都不知道要看什麼電影，直到抵達電影院時才知道要看《返校》，網友還裝傻向爸媽說是「青春校園片」。

直到電影播畢、出影廳後，父母難得沉默，沒有討論電影劇情，該名網友則和弟弟討論劇情時，弟弟說出「電影怎麼演都是假的！」激怒兩老，他們才願意加入討論。

該名網友還說，也許是因為時代的不同，所以父母對電影劇情有不同的感受，雖然他們沒有哭，但是看見他們閃爍的眼神，「於是他們想起來了」。網友還說，身為韓粉的父親竟沒有任何批評，甚至在隔天，媽媽還瘋狂查詢白色恐怖相關資料，讓他表示「真的很感動」。

此文一出，也引起網友熱烈討論，有網友留言說「太可怕了，爸爸是韓粉」、「慶幸我家長輩沒有韓粉」，也有網友留言說這是「今日最溫馨」；還有網友表示，也要帶自己的韓粉爸媽去看《返校》，更有網友引述電影對白，大讚該名網友「國家會感謝你的」。


                    </div>
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
                        <h2 class="mysubtitle mb-2">Ptt 轉發 ID：<router-link to="/ShowUserResult"><span class="mylinkText">rpg1510</span></router-link></h2>
                        <div class="mytext ptt-title">
                            <div>登入次數：3856</div>
                            <div class="myspace">有效文章數：2464</div>
                        </div>
                        <div class="mytext">相關ID：cloud7515、ReeJa</div>
                    </v-col>
                    <v-col md="4" class="pt-10 pb-10 result-analysis result-analysis-right">
                        <h2 class="mysubtitle mb-2">Ptt 轉發時間：2019-09-24 16:00</h2>
                        <div class="mytext">Ptt 轉發 IP：195.176.3.19 (瑞士)</div>
                        <div class="mytext">第一次轉貼至本系統時間：2019-09-30 19:51</div>
                    </v-col>
                </v-row>
                <v-row justify="start">
                    <v-col md="5" class="result-analysis result-analysis-left">
                        <h2 class="mysubtitle mb-2">Ptt 留言數量：111</h2>
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
                        <img :src=wordCloud_result2 alt="word cloud" class="wordcloud" />
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

                                <tr v-for="(news, index) in hotnews" :key=index>
                                <td>{{ news.title }}</td>
                                <td>{{ news.times }}</td>
                                <td>{{ news.percent }}%</td>
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
import VueApexCharts from 'vue-apexcharts'
import wordcloud from 'vue-wordcloud'
import wordCloud_result2 from '../assets/wordCloud-result2.png'

export default {
    components: {
        VueApexCharts,
        wordcloud,
    },
    beforeDestroy () {
      clearInterval(this.interval)
    },
    mounted () {
      this.interval = setTimeout(() => {
        if (this.value === 100) {
          return (this.value = 0)
        }
        this.value += 92
      }, 1000)
    },
    data: function() {
        return {
            wordCloud_result2,
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
                data: [45, 20, 45, 70, 49, 52, 30]
            }],
            pieseries: [149,38,107],
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
                "name": "返校",
                "value": 55
                },
                {
                "name": "低能卡",
                "value": 34
                },
                {
                "name": "幻想文",
                "value": 10
                },
                {
                "name": "假含粉",
                "value": 32
                },
                {
                "name": "含粉",
                "value": 17
                },
                {
                "name": "自由",
                "value": 12
                },
                {
                "name": "香港",
                "value": 11
                },
                {
                "name": "唬爛",
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
                title: '帶韓粉爸看《返校》後「想起來了」 網友：國家會感謝你的',
                times: 159,
                percent: 92
            },
            {
                title: '二度主動抖內柯營遭拒 郭董回應超霸氣',
                times: 127,
                percent: 47
            },
            {
                title: '全民卡韓？高雄狂舉債借錢！韓國瑜竟稱：市民要求越來越高',
                times: 94,
                percent: 87
            },
            {
                title: '《返校》那些年的奇葩禁書 金庸 & 英文文法',
                times: 92,
                percent: 93
            },
            {
                title: '信徒看到韓 大喊「感恩市長、讚嘆市長」',
                times: 85,
                percent: 51
            },
            {
                title: '房價不再飆漲 蔡英文：房屋不是炒作的商品',
                times: 78,
                percent: 75
            },
            {
                title: '郭辦「拜託韓市長不用來」沒用 韓競選：絕不會沒有聯絡',
                times: 69,
                percent: 63
            },
            {
                title: '柯文哲臉書按讚潮全是阿拉伯人？小編：非團隊所為',
                times: 62,
                percent: 90
            }
            ],
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
.wordCloud {
    display: inline;
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
