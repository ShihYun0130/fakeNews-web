<template>
    <div id="footer">
      <v-container fill-height fluid>
        <v-footer color="transparent" class="navBar-toolbar pa-0 ma-0" fluid>
        </v-footer>
        <v-layout align-center justify-space-between id="footer-layout">
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
    background-color: rgb(28,28,28,0.9);
}
.navBar-toolbar {
    height: 60px!important;
    box-shadow: none!important;
}
#footer-layout{
  min-height: 60px
}

</style>
