<template>
    <div id="footer">
      <v-container class="con" fill-height fluid>
        <v-footer color="transparent" class="navBar-toolbar pa-0 ma-0" fluid>
        </v-footer>
        <v-layout align-center justify-space-between>
          <v-flex class="white--text">2019 National Taiwan University Information Management CCC Lab Project</v-flex>
          <v-flex class="white--text text-right" >Photo by Max Muselmann on Unsplash,<br>
                    charlotte Ljones on StackSnap,<br>
                    Toa Heftiba on StackSnap</v-flex>
        </v-layout>
      </v-container>
    </div>
</template>

<script>
export default {
    name: "footer"
}
</script>

<style>
#footer {
    font-size: 10px;
    font-family: 'Noto Sans TC', sans-serif;
    background-color: rgb(28,28,28,0.9);
}
.con {
  padding: 0 7.3% !important;
}
.navBar-toolbar {
    height: 60px!important;
    box-shadow: none!important;
}

</style>
