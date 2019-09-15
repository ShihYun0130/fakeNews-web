<template>
  <v-app>
  <NavBar />
  <router-view />
  </v-app>
</template>

<script>
import NavBar from './components/NavBar';

export default {
  name: 'App',
  components: {
    NavBar
  },
  data: () => ({
    //
  }),
};
</script>

<style>
body {
  background: white;
  width: 100vw;
}
</style>
