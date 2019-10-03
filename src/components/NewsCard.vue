<template>
  <v-card
    class="rounded-card"
    height="350px"
    width="250px"
    color=rgb(28,28,28,0.88)
  >

    <v-container pa-4 fill-height fluid>
      <v-layout class="card-layout"  column> <!--all-->

        <v-layout class="card-layout" column> <!--top-->
          <v-flex xs-12>
            <div class='white--text mysubtext text-right'>假新聞機率</div>
            <div  class='orange--text text--accent-3 mybigtitle text-right'>{{ percent }}</div >
            <div  class='white--text mytitle text-right space'>{{ title }}</div >
          </v-flex>
        </v-layout>

        <v-col class="pb-0" column align='end'> <!--bottom-->
          <v-col class="pa-0" column>
            <v-row class='white--text mysubtext text-left'>新聞來源: {{ resource }}</v-row>
            <v-row class='white--text mysubtext text-left'>Ptt轉貼ID: {{ pttID }}</v-row>
            <v-row class='white--text mysubtext text-left'>新聞發佈時間: {{ newsTime }}</v-row>
            <v-row class='white--text mysubtext text-left'>Ptt轉貼時間: {{ pttTime }}</v-row>
          </v-col>
          <v-col class="pa-0 mt-3" >
            <v-row justify='space-between' align='end' >
              <div class='white--text mytext'>搜尋次數: {{ searchTimes }}</div>
              <router-link to="/ShowResult2" class="text-dec white--text">
              <v-btn
              color="white"
              class="mysubtext rounded-card"
              x-small
              tile
              >
                閱讀更多
              </v-btn>
              </router-link>
            </v-row>
          </v-col>
        </v-col>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>
export default {
  props: ['percent', 'title', 'resource', 'pttID', 'newsTime', 'pttTime', 'searchTimes' ],
  data: () => ({
  }),
}
</script>

<style>
.space {
  letter-spacing: 1.5px;
  line-height: 25px
}
.card-layout{
  min-height: 15%;
  width: 100%;
}

</style>
