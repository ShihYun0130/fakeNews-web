<template>
  <v-app>
    <div id="newsInput">

        <v-container full-height fluid>
            <v-row justify="center" class="pa-10">
                <h1 class="mytitle white--text">查詢該新聞是否為假新聞</h1>
            </v-row>
            <v-row justify="center" >
                <v-col md="6" class="myform pa-10" justify="center">
                    <v-row class="mb-4"><h2 class="mytext white--text">新聞標題</h2>
                    <span id="must_fill" style="color:white;font-size:14px;">&nbsp(必填)</span>
                    </v-row>
                    <v-row><input class="myinput" v-model="title" /></v-row>
                    <v-row class="mt-10 mb-4"><h2 class="mytext white--text">新聞來源</h2></v-row>
                    <v-row><input class="myinput" v-model="source" /></v-row>
                    <v-row class="mt-10 mb-4"><h2 class="mytext white--text">新聞內文</h2></v-row>
                    <v-row><textarea class="mytextarea" v-model="content" /></v-row>
                    <v-row justify="end" class="mt-10 mytext"><button class="newsInput-go" @click="submit" >送出</button></v-row>
                </v-col>
            </v-row>

        </v-container>
    </div>
  </v-app>
</template>

<script>
import { validationMixin } from 'vuelidate'
import { required, maxLength, email } from 'vuelidate/lib/validators'
import axios from 'axios'
import Router from 'vue-router'
import env from '../env';

export default {
    name: "NewsInput",
    props: {
        loading: Boolean,
    },
    data: function(){ 
        return {
            title: '',
            source: '',
            content: '',
            result: []
        } 
    },
    methods: {
        submit() {
            if(this.title != ""){
                localStorage.setItem('title', JSON.stringify(this.title));
                localStorage.setItem('content', JSON.stringify(this.content));
                this.$router.push({ name: 'ShowResult', params: { title: this.title, content: this.content } });
            }
            else{
                document.getElementById("must_fill").setAttribute("style","color:red;font-size:14px;");
            }
        }    
    }

}
</script>

<style>
.myform {
    background: rgb(28,28,28,0.9);
}
.myinput {
    border: white solid 1px;
    outline: none;
    color: white;
    width: 100%;
    height: 30px;
    padding: 10px
}
.mytextarea {
    border: white solid 1px;
    outline: none;
    color: white;
    width: 100%;
    resize: none;
    height: 100px;
    padding: 10px

}
.newsInput-go {
    border: solid white 1px;
    border-radius: 0;
    padding: 5px 40px;
    outline: none;
    box-shadow: 3px 3px 6px rgb(123, 123, 123);
    background:  transparent;
    color: white;
    transition: 0.8s;
}
.newsInput-go:hover{
    border: solid white 1px;
    border-radius: 0;
    padding: 5px 40px;
    outline: none;
    box-shadow: 3px 3px 6px rgb(123, 123, 123);
    background:  white;
    color: black;
    transition: 0.8s;
}
.newsInput-clear {
    border: solid #26C6DA 1px;
    color: #26C6DA;
}
.newsInput-clear:hover {
    border: solid #26C6DA 1px;
    background:  #26C6DA;
}
</style>
