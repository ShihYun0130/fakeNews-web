<template>
    <div id="home">
        <v-container fluid>
            <v-layout column align-center>
            <v-flex xs4 justify-center>
                <img class="apple-logo" :src=apple_logo />
            </v-flex>
            <v-flex xs3>
                <div class="home-intro light-blue--text text--darken-3">Find out who is lying!</div>
            </v-flex>
            <v-flex xs3>
                <router-link to="/NewsInput"><button class="light-blue--text text--darken-3 home-start">Start</button></router-link>
            </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
import apple_logo from '../assets/apple_logo.png';
export default {
    name: 'home',
    data: function() {
        return {
            apple_logo
        }
    }
}
</script>

<style>
#home {
    font-family: 'Geo', sans-serif;
    font-size: 2vw;
}
.apple-logo {
    width: 35vw;
    margin: 3vw;
    min-width: 250px;
}
.home-intro {
    font-size: 30px;
}
.home-start {
    font-size: 18px;
    border-radius: 50px;
    border: solid #BBDEFB 1px;
    padding: 5px 40px;
    margin: 2.5vh 0;
    outline: none;
    box-shadow: 3px 3px 6px rgb(123, 123, 123);
    transition: 0.5s;
}
.home-start:hover{
    border-radius: 50px;
    border: solid #BBDEFB 1px;
    padding: 5px 40px;
    margin: 2.5vh 0;
    outline: none;
    box-shadow: 0 1px 5px rgb(123, 123, 123);
    background:  #BBDEFB;
    transition: 0.5s;
}
</style>