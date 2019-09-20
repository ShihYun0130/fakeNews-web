<template>
  <v-app>
  <div id="app">
    <div v-show="$route.path==='/About' || $route.path==='/NewsInput' ||  $route.path==='/NewsList' ||  $route.path==='/ShowResult' ||  $route.path==='/UserList' ||  $route.path==='/Chart' ">
      <NavBar />
    </div>
    <router-view />
    <div v-show="$route.path==='/About' || $route.path==='/NewsInput' ||  $route.path==='/NewsList' ||  $route.path==='/ShowResult' ||  $route.path==='/UserList' ||  $route.path==='/Chart' ">
      <Footer />
    </div>
  </div>
  </v-app>
</template>

<script>
import NavBar from './components/NavBar';
import Footer from './components/Footer';

export default {
  name: 'App',
  components: {
    NavBar,
    Footer
  },
  data: () => ({
    //
  }),
};
</script>

<style>
#app {
  font-family: 'Noto Sans TC', sans-serif;
  background-image: url('./assets/bg.png');
  background-repeat: no-repeat;
  background-size:cover;
}
.container {
  padding: 0 7.3% !important;
}
.layout{
  min-height: 100vh
}
.mytitle{
  font-size: 24px
}
.mysubtitle{
  font-size: 20px
}
.mytext{
  font-size: 14px
}
</style>
