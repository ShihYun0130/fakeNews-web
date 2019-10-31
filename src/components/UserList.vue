<template>
  <v-app>
    <loading loader="bars"
        :active.sync="isLoading"
        :can-cancel="true"
        :is-full-page="false"
        color="#EE8802"
        background-color="transparent">
    </loading>
    <div id="userList">
        <v-container fill-height fluid>
          <v-layout class="card-layout" column>
            <v-flex xs-12 white--text mt-10 class="mytitle">可疑人物</v-flex>
            <!--<v-flex xs-6 mt-8 ml-3 mb-8>
                <v-row><input class="myinput user-search" placeholder="請輸入Ptt ID"/></v-row>
            </v-flex>-->
            <v-flex xs-12> <div class='mytext white--text mt-5 mb-6'>本系統資料庫標籤為假新聞，其轉發的Ptt ID</div></v-flex>
            <v-flex white--text mt-5 class="mytext">
              <v-col cols="12" style="width:1600px;">
                <v-row style="text-align:center;" ma-2>
                  <v-col cols="3">Ptt ID</v-col>
                  <v-col cols="3">有效文章數</v-col>
                  <v-col cols="4">轉發之新聞</v-col>
                </v-row>

                <v-row class="UserCard" v-for="(pttId, index) in pttIds" :key="index">
                  <UserCard :pttId="pttId" />
                </v-row>
              </v-col>
            </v-flex>
          </v-layout>
        </v-container>
    </div>
  </v-app>
</template>

<script>
import UserCard from './UserCard'
import UserCardEX from './UserCardEX'
import axios from 'axios';
import env from '../env';

import VueLoading from 'vue-loading-overlay'
import 'vue-loading-overlay/dist/vue-loading.css'

export default {
  data: function() {
    return {
      pttIds: [],
      isLoading: true
    }
  },
  mounted() {
    axios
    .get(env+'/api/suspect_user')
    .then(response => {
      for (var i = 0, len = response.data.length; i < len; i++) {
        this.pttIds.push(response.data[i]);
      }
    }).catch(error => {
        console.log(error)
        this.errored = true
    })
    .finally(() => {
        this.interval2 = setTimeout(() => {
            this.isLoading = false
        },1000);
    })
    console.log("pttids", this.pttIds);
  },
  components: {
        UserCard,
        UserCardEX,
        loading: VueLoading
  }
}

</script>


<style>
  .UserCard{
      padding: 10px 0 10px 0
  }
  ::-webkit-input-placeholder {
    font-size: 14px;
  }
</style>
