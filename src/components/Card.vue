<template>
  <v-card
    class="rounded-card"
    height="350px"
    color=rgb(28,28,28,0.88)
  >

    <v-container pa-4 fill-height fluid>
      <v-layout class="card-layout"  column> <!--all-->
        <v-layout class="card-layout" column> <!--top-->
          <v-flex xs-12>
            <div class='white--text mysubtext text-right'>假新聞機率</div>
            <div  class='orange--text text--accent-3 mysuptitle text-right'>{{ percent }}</div >
            <div  class='white--text mytitle text-right mb-8 space'>{{ title }}</div >
          </v-flex>
        </v-layout>

        <v-layout class="card-layout" column align-end justify-start> <!--bottom-->
          <v-layout class="card-layout">
            <v-flex xs-12>
              <div class='white--text mysubtext text-left'>新聞來源: {{ resource }}</div>
              <div class='white--text mysubtext'>Ptt轉貼ID: {{ pttID }}</div>
              <div class='white--text mysubtext'>新聞發佈時間: {{ newsTime }}</div>
              <div class='white--text mysubtext'>Ptt轉貼時間: {{ pttTime }}</div>
            </v-flex>
          </v-layout>
          <v-layout class="card-layout" align-end>
            <v-flex class='white--text mytext'>搜尋次數: {{ searchTime }}</v-flex>
            <v-btn
              color="white"
              class="mysubtext rounded-card"
              x-small
              tile
              >
                閱讀更多
            </v-btn>
          </v-layout>
        </v-layout>
      </v-layout>
  </v-container>


  </v-card>
</template>

<script>
export default {
  data: () => ({
    percent: "90%",
    resource: "自由時報",
    pttID: "ak904",
    newsTime: "2019-09-14 16:07",
    pttTime: "2019-09-14 20:32 ",
    title: "民進黨一早爆料：韓國瑜將請3個月無薪假",
    searchTime: 34,
  }),
}
</script>

<style>
.rounded-card{
    border-radius: 1px;
}
.mysubtext {
  font-size: 10px
}
.mysuptitle{
  font-size: 50px
}
.space {
  letter-spacing: 1.5px;
  line-height: 25px
}
.card-layout{
  min-height: 15%;
  width: 100%;
  }
.card-con{
  padding: 0 !important;
}


</style>
