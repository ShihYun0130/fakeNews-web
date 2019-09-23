<template>
  <v-app>
    <div id="userList">
        <v-container fluid>
          <v-layout align-start column justify-start>
            <v-flex xs12 white--text mt-10 class="mytitle">可疑人物</v-flex>
            <v-flex xs12 mt-10 ml-3>
              <v-row>
                <v-text-field
                  style="width:500px;"
                  label="請輸入 Ptt ID"
                  solo
                ></v-text-field>      
              </v-row>
            </v-flex>
            <v-flex white--text mt-5 class="mysubtitle">
              <v-col cols="12" style="width:1600px;">
                <v-row style="text-align:center;">
                  <v-col cols="1">Ptt ID</v-col>
                  <v-col cols="1">登入次數</v-col>
                  <v-col cols="1">有效文章數</v-col>
                  <v-col cols="2">轉發假新聞次數*</v-col>
                  <v-col cols="4">轉發新聞</v-col>
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
export default {
  data: function() {
        return {
        }
    },
  components: {
        UserCard
  }
}

</script>

<style>
  .UserCard{
    padding:10px;
    padding-left:0px;
  }
</style>