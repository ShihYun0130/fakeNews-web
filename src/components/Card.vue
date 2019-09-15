<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-img
      class="white--text"
      height="200px"
      :src=taiwan
    >
      <v-card-title class="align-end fill-height">中國自由行政策鬆綁？ 金門縣府：相關內容底定後儘速報告</v-card-title>
    </v-img>

    <v-card-text>
      <span>2019.09.15</span><br>
      <span class="text--primary">
        <span>〔記者吳正庭／金門報導〕</span><br>
        <span>中國暫停47個城市的中國居民赴台自由行後，金門小三通9月以來的中國旅客入出境數只有去年同期的26％......</span>
      </span>
    </v-card-text>

    <v-card-actions>
      <v-btn
        text
        color="orange"
      >
        Share
      </v-btn>
      <v-btn
        text
        color="orange"
      >
        See More
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import taiwan from '../assets/taiwan.png';
export default {
    data: function() {
        return {
            taiwan
        }
    }
}
</script>

<style>

</style>