<template>
  <v-app>
  <div id="app">
    <div v-show="$route.path==='/About' || $route.path==='/NewsInput' ||  $route.path==='/NewsList' ||  $route.path==='/ShowResult' ||  $route.path==='/UserList' ||  $route.path==='/Statistics' || $route.path==='/ShowUserResult' ||  $route.path==='/ShowResult2' || $route.path==='/ErrorPage' ">
      <NavBar />
    </div>
    <router-view ></router-view>
    <div v-show="$route.path==='/About' || $route.path==='/NewsInput' ||  $route.path==='/NewsList' ||  $route.path==='/ShowResult' ||  $route.path==='/UserList' ||  $route.path==='/Statistics' || $route.path==='/ShowUserResult' ||  $route.path==='/ShowResult2' ||  $route.path==='/ShowResult' ||  $route.path==='/UserList' ||  $route.path==='/Chart' || $route.path==='/ShowUserResult' ||  $route.path==='/ShowResult2' || $route.path==='/ErrorPage'">
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
  }),
  methods: {
  }
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

/* font size*/
.mybigtitle{
  font-size: 47px
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
.mysubtext{
  font-size: 10px
}

/*link*/
.mylinkText{
  color: white;
  text-decoration: underline;
}
.mylinkText:hover {
  color: #FF9100;
  transition: 0.3s;
  outline: none;
}
.mylinkText:active{
  color: #FD5D00
}
.mylinkClean{
  color: white;
  text-decoration: none;
  outline: none;
}
.mylinkClean:hover{
  color: #FF9100;
  transition: 0.3s;
  outline: none;
}
.mylinkClean:active{
  color: #FD5D00
}

/*card*/
.rounded-card{
    border-radius: 0;
}
</style>
