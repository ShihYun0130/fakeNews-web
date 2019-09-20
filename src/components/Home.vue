<template>
    <div id="home">
        <v-container fill-height fluid>
            <v-layout align-end> <!--置底-->
              <v-flex xs12>
                  <div class="mysubtitle white--text mb-n7">看看誰在說謊?</div><!--Margin Bootom Negative 7 level-->
                  <div class="hometitle white--text">DeFaker</div>
                  <router-link to="/NewsInput"><button class="home-start mb-12">新聞查詢</button></router-link>
              </v-flex>
          </v-layout>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'home',
}
</script>

<style>
#home {
    background-image: url('../assets/home.png');
    background-repeat: no-repeat;
    background-position: center;
    background-size:cover;
    height: 100vh
}
.container {
  padding: 0 7.3% !important;
}

.hometitle {
  font-size: 90px
}

.home-start {
    color: white;
    font-size: 18px;
    border: solid white 1px;
    padding: 5px 40px;
    outline: none;
    box-shadow: 3px 3px 6px rgb(123, 123, 123);
    transition: 0.5s;
}
.home-start:hover {
    color: black;
    border: solid white 1px;
    padding: 5px 40px;
    margin: 0.5vh 0;
    outline: none;
    box-shadow: 0 1px 5px rgb(123, 123, 123);
    background:  white;
    transition: 0.5s;
}
.home-start:active {
    background: #BDBDBD;
}
</style>
