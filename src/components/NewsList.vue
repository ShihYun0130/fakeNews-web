<template>
    <div>
        <v-container fill-height fluid>
          <v-layout column>
            <v-row class="mytitle white--text mt-10">熱門搜索</v-row>
            <v-row class="mytext white--text mt-5 mb-6">兩周內於本系統搜尋次數排名</v-row>
            <v-row>
                <v-col 
                  v-for="(news, index) in newss"
                  cols="3"
                  :key="index"

                  >
                  <NewsCard
                    :percent="news.prediction"
                    :title="news.title"
                    :resource="news.source"
                    :pttID="news.uid"
                    :newsTime="news.PostTime"
                    :pttTime="news.QueryTime"
                    :searchTimes="news.searchCount"
                    />
                </v-col>
              </v-row>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import NewsCard from './NewsCard';
import axios from 'axios';
import env from '../env';

export default {
  data: () => ({
    total: 8,
    newss :[]

  }),
  mounted() {
    axios.get(env+'/api/search')
    .then(response => {
        console.log("hot", response);
        this.newss = response.data;
        
    })
    .catch(error => {
        console.log(error)
        this.errored = true
    })

  },
  components: {
    NewsCard
  },

  computed: {
  },
}
</script>

<style>

</style>
