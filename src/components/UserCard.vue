<template>
      <v-expansion-panels
      popout="popout"
      inset="inset"
      multiple="multiple"
      dark="dark"
    >
      <v-expansion-panel>
        <v-expansion-panel-header>
          <v-row style="text-align:center;">
            <v-col cols="1" class="userDetail">abomb</v-col>
            <v-col cols="1" class="userDetail">1892</v-col>
            <v-col cols="1" class="userDetail">275</v-col>
            <v-col cols="2" class="userDetail">2</v-col>
            <v-col cols="4" class="userDetail">
              <span class="fakePercent">92%&nbsp&nbsp</span>
              <span>網曝大選殘酷真相 絕望嘆：DPP為大選不擇手段</span>
            </v-col>
            <v-col cols="3" class="userDetail">snsdakb48、dtlove17、yillusionwei、Dinenger、j32072、team1245、AFIE</v-col>
          </v-row>
        </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-row style="margin-left:-25px;">
              <v-col cols="1" class="userDetail"></v-col>
              <v-col cols="1" class="userDetail"></v-col>
              <v-col cols="1" class="userDetail"></v-col>
              <v-col cols="2" class="userDetail"></v-col>
              <v-col cols="4" class="userDetail">
                <span class="fakePercent">76%&nbsp&nbsp</span>
                <span>批小英兩岸政策「跟人家大小聲」柯文哲：我們都是Chinese</span>
              </v-col>
              <v-col col="2"></v-col>
            </v-row>

          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
</template>

<script>
  export default {
    data: () => ({
    }),
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
