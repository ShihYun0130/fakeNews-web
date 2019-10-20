<template>
  <v-app>
    <div id="userList">
        <v-container fill-height fluid>
          <v-layout class="card-layout" column>
            <v-flex xs-12 white--text mt-10 class="mytitle">可疑人物</v-flex>
            <v-flex xs-6 mt-8 ml-3 mb-8>
                <v-row><input class="myinput user-search" placeholder="請輸入Ptt ID"/></v-row>
              <!--<v-row>
                <v-text-field
                  style="width:500px;"
                  label="請輸入 Ptt ID"
                  solo
                ></v-text-field>
              </v-row>-->
            </v-flex>
            <v-flex xs-12> <div class='white--text mysubtext text-right'>*於本系統檢測超過50%機率之新聞</div></v-flex>
            <v-flex white--text mt-5 class="mytext">
              <v-col cols="12" style="width:1600px;">
                <v-row style="text-align:center;" ma-2>
                  <v-col cols="1">Ptt ID</v-col>
                  <v-col cols="1">登入次數</v-col>
                  <v-col cols="1">有效文章數</v-col>
                  <v-col cols="2">轉發假新聞次數*</v-col>
                  <v-col cols="4">轉發之假新聞</v-col>
                  <v-col cols="3">相關 ID</v-col>
                </v-row>

                <v-row class="UserCard"><UserCard/></v-row>
                <v-row class="UserCard"><UserCard/></v-row>
                <v-row class="UserCard"><UserCard/></v-row>
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
export default {
  data: function() {
        return {
        }
    },
  components: {
        UserCard,
        UserCardEX
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
