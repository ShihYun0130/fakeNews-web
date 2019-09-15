<template>
    <v-container fluid row justify-center class="grey lighten-5" id="showResult">
    <!-- Stack the columns on mobile by making one full-width and the other half-width -->
    <div class="showResult-title">
        <div class="title-bg">查</div>
        <div class="title-bg">詢</div>
        <div class="title-bg">結</div>
        <div class="title-bg">果</div>
    </div>
    <v-layout column class="flex xs3">
        <v-flex xs5 class="rectangle item1">
            <h3>新聞公開發佈時間：</h3>
            <span style="color: black">2019年9月14日</span>
            <br/>
            <h3>偵測結果：</h3>
            <div class="show-possibility">90%為假新聞</div>
        </v-flex>
        <v-flex xs5 class="rectangle item2">
            <div style="color: #26C6DA"><h3 style="display: inline; color: black">Ptt 發文ID：</h3>Bignana</div>
            <br/>
            <h3>與它關係密切的 ID 們：</h3>
            <div class="show-IDs">snsdakb48、dtlove17、yillusionwei、Dinenger、j32072、team1245、AFIE</div>
        </v-flex>
        <v-flex xs2 class="rectangle item3">看看大家都查了什麼</v-flex>
    </v-layout>
    <v-layout column class="flex xs7">
        <v-flex xs5 class="rectangle item4">
            <h2 class="show-title lime--text text--darken-3">批小英兩岸政策「跟人家大小聲」柯文哲：我們都是Chinese</h2>
            <div>新聞來源：<a href="https://news.ltn.com.tw/news/politics/breakingnews/2915650">https://news.ltn.com.tw/news/politics/breakingnews/2915650</a></div>
            <div class="item4-content">
                <img class="wordCloud_1" :src=wordCloud_1 />
                <div class="show-newsContent">〔即時新聞／綜合報導〕台北市長柯文哲創立台灣民眾黨，意圖在明年2020立委選戰中爭取不分區立委席次。近日柯文哲接受香港媒體鳳凰衛視節目專訪，主持人提問對明年大選和台灣政治看法，柯文哲表示，「我們華人、我們Chinese，是很愛面子的國家」，認為總統蔡英文的兩岸政策過於僵硬，並酸國民黨總統候選人韓國瑜「根本沒準備好」。
                    柯文哲日前接受鳳凰衛視「石評大財經」專訪，談論有關上任台北市長後的經驗，以及對於明年大選的看法。柯文哲認為，現在蔡英文的兩岸政策過於僵硬，「我們華人、我們Chinese，都是很愛面子的國家」，批評蔡英文只會跟對岸「大小聲」，並指出這是蔡英文應該解決的問題。
                    柯文哲表示，要維持台灣國家主權與民主自由，不用向對岸大小聲。他舉2017年世大運為例，認為當時所作所為「哪裡沒有顧到台灣主權、台灣安全？」他表示，要顧及台灣的主權，不一定要像現在蔡英文的做法。
                    至於另一名總統參選人韓國瑜，柯文哲則大笑，「他根本來沒準備好，這根本太可怕！」
                    針對可能宣布參選的郭台銘，柯文哲則認為，郭必須要學會「捨得」，「有捨才有得啊！其實大家都知道答案，只是看他能不能做到而已。」
                </div>
            </div>
            
        </v-flex>
        <v-flex xs7 class="rectangle item5">
            <div class="item5-left">
                <div class="reply-analysis-title">Ptt 留言情緒分析</div>
                <img class="mood_analysis" :src=mood_analysis />
                <div class="item5-left-bottom">
                    <span class="item5-num"><span class="item5-left-bottom-total">留言數量</span>：200</span>
                    <span class="item5-num"><span class="item5-left-bottom-total">推噓文比例</span>：50%</span>
                </div>
            </div>
            <div class="item5-right">
                <img class="wordCloud_2" :src=wordCloud_2 />
                <div class="reply-cloud-title">Ptt 留言文字雲</div>
            </div>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import wordCloud_1 from '../assets/wordcloud.png';
import mood_analysis from '../assets/mood_analysis.png';
import wordCloud_2 from '../assets/wordcloud2.png';

export default {
    data: () => ({
      expand: true,
      expand2: false,
      wordCloud_1,
      wordCloud_2,
      mood_analysis
    }),
  }
</script>

<style>
#showResult {
    min-width: 400px;
}
.showResult-title {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    color: #9E9D24;
    font-size: 30px;
}
.title-bg {
    border: #C0CA33 solid 2px;
    border-radius: 10px;
    background: #C0CA33;
    padding: 20px;
    margin: 10px;
    color: white;
    /* box-shadow: rgb(116, 116, 116) 2px 2px 5px; */
}
.rectangle {
    background: white;
    margin: 8px;
    color: white;
    text-align: left;
    padding: 3.5vw;
    border-radius: 3px;
    box-shadow: rgb(174, 174, 174) 2px 2px 6px;

    display: flex;
    flex-direction: column;
    justify-content: center;

    white-space: nowrap;

    transition: 2s;
}
.show-title {
    white-space: pre-wrap;
}
h3 {
    color: black;
}
.item1 {
    padding-left: 35px;
}
.item2 {
}
.item3 {
    background: #C0CA33;
    color: white;
    font-size: 2vw;
    align-items: center;
    transition: 1s;
}
.item3:hover {
    background: #9E9D24;
    color: white;
    font-size: 2vw;
    align-items: center;
    transition: 1s;
    cursor: pointer;
}
.item4 {
    color: rgb(55, 55, 55);
    height: 30vw;
    padding: 2.5vw;
}
.show-possibility {
    color: #F48FB1;
    font-size: 3.1vw;
}
.show-IDs {
    color: #26C6DA;
    font-size: 1.3vw;
    white-space: pre-wrap;
}
.wordCloud_1 {
    width: 35%;
    height: 95%;
}
.wordCloud_2 {
    width: 90%;
}
.item4-content {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 90%;
    height: 60%;
    margin: 1vw 0;
}
.show-newsContent {
    width: 50%;
    height: 100%;
    overflow: scroll;
    white-space: normal;
    padding: 10px;
    border-top: solid #26C6DA 2px;
    border-bottom: solid #26C6DA 2px;
}
.mood_analysis {
    width: 100%;
}
.item5 {
    padding: 1.5vw 3.5vw;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}
.item5-left {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    color: black;
    width: 50%;
    height: 80%;
}
.item5-left-bottom {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding-top: 0;
    padding-bottom: 0; 
}
.item5-right {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    color: black;
    width: 50%;
    height: 80%;
}
.reply-analysis-title {
    text-align: center;
    border: #26C6DA solid 1.4px;
    border-radius: 50px;
    color: white;
    background: #26C6DA;
    width: 100%;
}
.reply-cloud-title {
    text-align: center;
    border: #26C6DA solid 1.4px;
    border-radius: 50px;
    color: white;
    background: #26C6DA;
    width: 80%;
}
.item5-num {
    margin: 0 0.5vw;
}
.item5-left-bottom-total {
    text-align: center;
    border: #26C6DA solid 1.4px;
    border-radius: 50px;
    color: white;
    background: #26C6DA;
    padding: 0 1.5vw;
}
</style>