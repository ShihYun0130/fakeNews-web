<template>
    <v-app>
        <div id="showResult">
            <v-container fluid class="pa-0">
                <div class="result-news-container">
                    <h1 class="mytitle result-news">郭文貴、班農直播 驚爆中共在福建部署50萬大軍準備攻台</h1>
                    <div class="mytext result-news">新聞來源：自由時報<br/>新聞發布時間：2019-09-02 10:38</div>
                    <div class="mytext result-news">〔財經頻道／綜合報導〕流亡美國的中國富豪郭文貴今日與上個月剛被美國總統川普讚譽為「我最好的門生之一」的前白宮首席策士班農（Steve Bannon）直播時爆出猛料，聲稱中共制定名為「雙菱行動」的攻台作戰計劃，在福建已部署50萬大軍和導彈部隊，一旦香港失去全面控制，共軍將突然對台動武，企圖收復台灣。

郭文貴今日與班農直播時聲稱，中共中央國家安全委員會已經定好對台作戰計劃，「在福建，50萬大軍、導彈部隊已經準備好，當香港失去全面控制，美國全面進行制裁、全面進行封鎖，像天安門六四事件一樣，西方和美國對中國進行制裁的時候，共產黨就會發起突然間的對台灣定點斬首行動、軍事打擊，徹底收復台灣，這叫『雙菱行動』」。

郭文貴警示，中共將宣稱香港反送中抗爭是美國和台灣的台獨份子在幕後策劃，且很多香港反送中領袖都藏在台灣，中共要去抓捕這些人，以此為由對台進行軍事行動，以收復臺灣，這是共產黨的核心目的之一。

郭文貴警告，中共對台動武可能隨時發生，此次中共的「雙菱行動」不惜一切代價，不論死多少人、流多少血，要百分之百拿下台灣。郭文貴呼籲，香港現在是台灣最大的保護屏障，「台灣只有站在香港的一邊，保護香港人民，你才能安全。只有大膽地行動，和全世界站在一起，台灣才可能有安全，否則很快將變成炮灰、彈灰」。

班農呼籲，如今香港局勢發展至此，在台灣的愛國者們應引以為鑑，香港有將近200年的法治，是人類史上最偉大的城市之一，台灣必須力挺香港人民，否則台灣就會變成下一個香港。

郭文貴則對班農的說法表示贊同，「台灣的同胞們，如果你現在不和香港同胞絕對、決絕的站在一起、完全無私的站在一起，你就沒任何機會了，你比香港還糟糕，因為導彈打到台灣的時候，能和台灣人站在一起的，不會像香港背後的支持那麼多，因為香港的價值和利益是全世界的核心」。

郭文貴說：「我呼籲所有台灣同胞和支持爆料革命的人，你們嚴肅認真的對待，應該要求台灣政府給予香港所有人一切可能的支持，並且發動全台灣緊急的作戰命令，與香港人民站在一起，把習近平、王岐山收復台灣、收復香港的野心和征服世界、要發動第三次世界大戰的行動阻止在香港大門之內，而不延燒到台灣，為此，台灣應該做好一切的準備和犧牲，只有這樣，才能讓共產黨徹底被消滅，給世界機會，給世界真相，讓世界和香港、台灣站在一起，共同滅掉共產黨」。

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
                        <h2 class="mysubtitle mb-2">Ptt 轉發 ID：<router-link to="/ShowUserResult"><span class="mylinkText">soul5566</span></router-link></h2>
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
                        <h2 class="mysubtitle mb-2">Ptt 留言數量：252</h2>
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
                        :font="myFont"
                        >
                        </wordcloud>
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

                                <tr v-for="news in hotnews">
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
        this.value += 90
      }, 1000)
    },
    data: function() {
        return {
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
            pieseries: [87,31,134],
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
    display: inline-block;
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
