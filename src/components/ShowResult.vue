<template>
    <v-app>
        <div id="showResult">
            <v-container fluid class="pa-0">
                <h1 class="mytitle result-news">批小英兩岸政策「跟人家大小聲」柯文哲：Chinese都愛面子</h1>
                <div class="mytext result-news">新聞來源：自由時報<br/>新聞發布時間：2019-09-14 16:07</div>
                <div class="mytext result-news">〔即時新聞／綜合報導〕台北市長柯文哲創立台灣民眾黨，意圖在明年2020立委選戰中爭取不分區立委席次。
                近日柯文哲接受香港媒體鳳凰衛視節目專訪，主持人提問對明年大選和台灣政治看法，柯文哲表示，「我跟你講，華人、Chinese中國人，是很愛面子的國家」，
                認為總統蔡英文的兩岸政策過於僵硬，並酸國民黨總統候選人韓國瑜「根本沒準備好」。
                柯文哲日前接受鳳凰衛視「石評大財經」專訪，談論有關上任台北市長後的經驗，以及對於明年大選的看法。柯文哲認為，
                現在蔡英文的兩岸政策過於僵硬，「華人、Chinese，是很愛面子的國家」，批評蔡英文只會跟對岸「大小聲」，並指出這是蔡英文應該解決的問題。
                柯文哲表示，要維持台灣國家主權與民主自由，不用向對岸大小聲。他舉2017年世大運為例，認為當時所作所為「哪裡沒有顧到台灣主權、台灣安全？」
                他表示，要顧及台灣的主權，不一定要像現在蔡英文的做法。
                至於另一名總統參選人韓國瑜，柯文哲則大笑，「他根本來沒準備好，這根本太可怕！」
                針對可能宣布參選的郭台銘，柯文哲則認為，郭必須要學會「捨得」，「有捨才有得啊！其實大家都知道答案，只是看他能不能做到而已。」</div>
                

                <v-row justify="start" class="mt-10">
                    <v-col md="5" class="pt-10 pb-10 result-analysis result-analysis-left">
                        <h2 class="mysubtitle mb-2">Ptt 轉發 ID：Bignana</h2>
                        <div class="mytext ptt-title">
                            <div>登入次數：982</div>
                            <div class="myspace">有效文章數：120</div>
                        </div>
                        <div class="mytext">相關ID：sdf384r、dsjf84535、j943243、asd9877、iuy743、abc123、ptt</div>
                    </v-col>
                    <v-col md="4" class="pt-10 pb-10 result-analysis result-analysis-right">
                        <h2 class="mysubtitle mb-2">Ptt 轉發時間：2019-09-14 16:07</h2>
                        <div class="mytext">Ptt 轉發 IP：115.82.19.34(台灣)</div>
                        <div class="mytext">第一次轉貼至本系統時間：2019-09-15 08:01</div>
                    </v-col>
                </v-row>
                <v-row justify="start">
                    <v-col md="5" class="result-analysis result-analysis-left">
                        <h2 class="mysubtitle mb-2">Ptt 留言數量：200</h2>
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
                        <wordcloud
                        :data="defaultWords"
                        nameKey="name"
                        valueKey="value"
                        :color="myColors"
                        :showTooltip="true"
                        :wordClick="wordClickHandler"
                        class="wordCloud"
                        >
                        </wordcloud>
                    </v-col>
                </v-row>

                <v-row justify="end" class="mb-10">
                    <v-col md="9" class="pb-10 result-analysis result-analysis-left">
                        <h2 class="mysubtitle mt-10 mb-10">熱門搜索</h2>
                        <v-simple-table dark class="hot-table">
                            <template v-slot:default>
                            <thead>
                                <tr>
                                <th class="text-left">新聞標題</th>
                                <th class="text-left">搜尋次數</th>
                                <th class="text-left">假新聞機率</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="item in desserts" :key="item.name">
                                <td>{{ item.name }}</td>
                                <td>{{ item.calories }}</td>
                                <td>{{ item.calories }}%</td>
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
export default {
    data: function() {
        return {
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
            pieseries: [44, 55, 41, 17, 15],
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
            defaultWords: [{
                "name": "Cat",
                "value": 26
                },
                {
                "name": "fish",
                "value": 19
                },
                {
                "name": "things",
                "value": 18
                },
                {
                "name": "look",
                "value": 16
                },
                {
                "name": "two",
                "value": 15
                },
                {
                "name": "fun",
                "value": 9
                },
                {
                "name": "know",
                "value": 9
                },
                {
                "name": "good",
                "value": 9
                },
                {
                "name": "run",
                "value": 6
                },
                {
                "name": "go",
                "value": 6
                },
                {
                "name": "eat",
                "value": 6
                },
                {
                "name": "pray",
                "value": 5
                },
                
            ],
            desserts: [
            {
                name: '中國奪我友邦 國軍智庫：對岸「經援外交」可能跳票',
                calories: 159,
            },
            {
                name: '中國奪我友邦 國軍智庫：對岸「經援外交」可能跳票',
                calories: 237,
            },
            {
                name: '中國奪我友邦 國軍智庫：對岸「經援外交」可能跳票',
                calories: 262,
            },
            {
                name: '中國奪我友邦 國軍智庫：對岸「經援外交」可能跳票',
                calories: 305,
            },
            {
                name: '中國奪我友邦 國軍智庫：對岸「經援外交」可能跳票',
                calories: 356,
            },
            {
                name: '中國奪我友邦 國軍智庫：對岸「經援外交」可能跳票',
                calories: 375,
            },
            {
                name: '中國奪我友邦 國軍智庫：對岸「經援外交」可能跳票',
                calories: 392,
            },
            {
                name: '中國奪我友邦 國軍智庫：對岸「經援外交」可能跳票',
                calories: 408,
            }
            ],
        }
    },
    methods: {
        wordClickHandler(name, value, vm) {
        console.log('wordClickHandler', name, value, vm);
        }
    },
    components: {
        VueApexCharts,
        wordcloud
    }
}
</script>

<style>
#showResult {
    color: white;
    margin-top: 50px;
}
.result-news {
    margin: 30px 0;
    padding: 0 7.3%!important;
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
</style>