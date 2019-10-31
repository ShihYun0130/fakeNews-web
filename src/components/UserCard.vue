<template>
      <v-expansion-panels
      popout="popout"
      inset="inset"
      multiple="multiple"
      dark="dark"
    >
      <v-expansion-panel>
        <v-expansion-panel-header disabled="isDisabled">
          <v-row style="text-align:center;">
            <v-col cols="3" class="userDetail">{{pttId.uid}}</v-col>
            <v-col cols="3" class="userDetail">{{pttId.postNB}}</v-col>
            <v-col cols="4" class="userDetail" v-for="(news, index) in pttId.news" :key="index">
              <span class="fakePercent">{{news.pred}}%&nbsp&nbsp</span>
              <span><button @click="clickNews(news.title)">{{news.title}}</button></span>
            </v-col>
          </v-row>
        </v-expansion-panel-header >
          <v-expansion-panel-content>
            <v-row style="margin-left:-25px;">
              <v-col cols="1" class="userDetail"></v-col>
              <v-col cols="1" class="userDetail"></v-col>
              <v-col cols="1" class="userDetail"></v-col>
              <v-col cols="2" class="userDetail"></v-col>
              <v-col cols="4" class="userDetail" v-for="(news, index) in pttId.news" :key="index">
                <span class="fakePercent">{{news.pred}}%&nbsp&nbsp</span>
                <span><button @click="clickNews(news.title)">{{news.title}}</button></span>
              </v-col>
              <v-col col="2"></v-col>
            </v-row>

          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
</template>

<script>
  export default {
    props: {
      pttId: Object,
      FakeNewsNB: Number,
      news: Array,
      postNB: Number,
      uid: String,
    },
    data: function() {
      return {
        newsNum: 0,
        isDisabled: true
      }
    },
    mounted() {
      this.newsNum = this.pttId.news.length;
      if(this.pttId.news.length == 1) {
        this.isDisabled = true;
      }
    },
    methods: {
      clickNews(title) {
        this.$router.push({name: 'ShowResult2', params: { title: title }});
      }
    }
  }
</script>

<style>
  .userDetail{
    color: #ffffff;
    font-size: 15px;
  }
  .fakePercent{
    color: #FF9100;
  }
  .v-expansion-panels{
      border-radius: 0px !important;
  }
  .v-expansion-panels:not(.v-expansion-panels--accordion) > .v-expansion-panel--active {
    border-radius:  0px !important;
}
</style>
