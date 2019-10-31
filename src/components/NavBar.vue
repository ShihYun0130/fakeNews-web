<template>
    <div id="navBar">
      <v-container fill-height fluid>
        <v-toolbar color="transparent" class="navBar-toolbar pa-0">
            <router-link class="text-dec white--text" to="/Home"><button class="mylink"><img src="../assets/logo.png" class="nav-img"></button></router-link>
            <div class="flex-grow-1"></div>
            <router-link class="text-dec white--text pl-8" to="/NewsInput"><button class="mylink">新聞查詢</button></router-link>
            <router-link class="text-dec white--text pl-8" to="/NewsList"><button class="mylink">熱門搜索</button></router-link>
            <router-link class="text-dec white--text pl-8" to="/UserList"><button class="mylink">可疑人物</button></router-link>
            <router-link class="text-dec white--text pl-8" to="/Statistics"><button class="mylink">統計資訊</button></router-link>
            <router-link class="text-dec white--text pl-8" to="/About"><button class="mylink">關於我們</button></router-link>


        </v-toolbar>
      </v-container>
    </div>
</template>

<script>
export default {
    name: "navBar"
}
</script>

<style>
#navBar {
    font-size: 13px;
    font-family: 'Noto Sans TC', sans-serif;
    background-color: rgb(28,28,28,0.9)
}
.navBar-toolbar {
    height: 60px!important;
    box-shadow: none!important;
}
.v-toolbar__content {
     padding: 0!important;
}
.text-dec {
    text-decoration: none;
    box-shadow: none!important;
}
.mylink:hover {
  color: #FF9100;
  transition: 0.3s;
  outline: none;
}

.mylink:active{
  color: #FD5D00;
  outline: none;
}

.nav-img{
  width: 90px
}



</style>
