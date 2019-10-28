<template>
  <v-app>
    <div id="about">
        <v-container fill-height fluid>
          <v-layout row justify-start align-center>
          <div class="about-container">
              <img class="groupPC" :src="groupPC" alt="group picture" />
              <div class="about-text">Defaker 是一套能自動辨別新聞真偽、並給予其可信度分數的系統。
                在這個假新聞充斥的社會，每天在網路世界中被分享轉傳的錯誤資訊可說是不計其數，
                而其所製造出的動盪與對立，無庸置疑地帶來了可觀的威脅。<br/>因此，以新聞本身與社群的迴響作為訓練資料，
                我們透過機器的分析與學習能力，建構出一套能有效辨別新聞真偽的模型，並以此建立一個簡易的資訊系統，
                來提供閱讀新聞的大眾一個參考與查詢的依據，輔助人們判斷訊息的真偽，甚至主動抓出可疑的新聞或訊息來源。
                <div class="mytext">
                </div>
              </div>
            <!-- <v-flex white--text mt-10 class="mytitle">大標題24px</v-flex>
            <v-flex white--text mt-10 class="mysubtitle">中標題20px</v-flex>
            <v-flex orange--text text--accent-3 mt-10 class="mytext">Primary color #FF9100</v-card></v-flex>
            <v-flex orange--text text--darken-4 mt-5 class="mytext">Secondary color #E5100</v-card></v-flex> -->
          </div>
          </v-layout>
        </v-container>
    </div>
  </v-app>
</template>

<script>
import groupPC from '../assets/groupPC.png'

export default {
  data: () => ({
    groupPC,
  }),
}
</script>

<style>
.groupPC {
  width: 50%;
  margin-right: 40px;
}
.about-container {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: center;
  color: white;
}
.about-text {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
}
</style>
