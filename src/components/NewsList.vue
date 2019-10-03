<template>
    <div>
        <v-container fill-height fluid>
          <v-layout column>
            <v-row class="mytitle white--text mt-10">熱門搜索</v-row>
            <v-row class="mytext white--text mt-5 mb-6">兩周內於本系統搜尋次數排名</v-row>
            <v-row>
                <v-col
                  v-for="(news, index) in newss"
                  :key="index"
                  >
                  <NewsCard
                    :percent="news.percent"
                    :title="news.title"
                    :resource="news.resource"
                    :pttID="news.pttID"
                    :newsTime="news.newsTime"
                    :pttTime="news.pttTime"
                    :searchTimes="news.searchTimes"
                    />
                </v-col>
              </v-row>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import NewsCard from './NewsCard'

export default {
  data: () => ({
    total: 10,

    newss :[
      {
        percent: "92%",
        title: "帶韓粉爸看《返校》後「想起來了」 網友：國家會感謝你的",
        resource: "自由時報",
        pttID: "CLV518",
        newsTime: "2019-09-24 11:27",
        pttTime: "2019-09-24 16:00 ",
        searchTimes: 159
      },
      {
        percent: "47%",
        title: "二度主動抖內柯營遭拒 郭董回應超霸氣",
        resource: "鏡週刊",
        pttID: "permoon",
        newsTime: "2019-09-24 06:58",
        pttTime: "2019-09-24 09:21 ",
        searchTimes: 127
      },
      {
        percent: "87%",
        title: "全民卡韓？高雄狂舉債借錢！韓國瑜竟稱：市民要求越來越高",
        resource: "三立",
        pttID: "creativegod",
        newsTime: "2019-09-23 12:47",
        pttTime: "2019-09-23 15:55",
        searchTimes: 94
      },
      {
        percent: "93%",
        title: "《返校》那些年的奇葩禁書 金庸 & 英文文法",
        resource: "GQ",
        pttID: "filmwalker",
        newsTime: "2019-09-18 18:09",
        pttTime: "2019-09-19 15:36",
        searchTimes: 92
      },
      {
        percent: "51%",
        title: "信徒看到韓 大喊「感恩市長、讚嘆市長」",
        resource: "中時電子報",
        pttID: "filmwalker",
        newsTime: "2019-09-21 13:21",
        pttTime: "2019-09-21 14:12",
        searchTimes: 85
      },
      {
        percent: "75%",
        title: "房價不再飆漲 蔡英文：房屋不是炒作的商品",
        resource: "中時電子報",
        pttID: "cores",
        newsTime: "2019-09-19 20:55",
        pttTime: "2019-09-20 12:35",
        searchTimes: 78
      },
      {
        percent: "63%",
        title: "郭辦「拜託韓市長不用來」沒用 韓競選：絕不會沒有聯絡",
        resource: "新頭殼",
        pttID: "mited",
        newsTime: "2019-09-20 10:37",
        pttTime: "2019-09-20 11:07",
        searchTimes: 69
      },
      {
        percent: "90%",
        title: "柯文哲臉書按讚潮全是阿拉伯人？小編：非團隊所為",
        resource: "聯合報",
        pttID: "Salcea",
        newsTime: "2019-09-20 09:00",
        pttTime: "2019-09-20 00:15",
        searchTimes: 62
      },




    ]

  }),

  components: {
    NewsCard
  },

  computed: {
  },
}
</script>

<style>

</style>
