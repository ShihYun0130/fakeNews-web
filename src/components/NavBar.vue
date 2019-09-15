<template>
    <div id="navBar">
        <v-toolbar light color="primary" class="no-shadow navBar-toolbar">
            <router-link class="home-title" to="/Home"><v-toolbar-title class="lime--text text--darken-4">Title</v-toolbar-title></router-link>

            <div class="flex-grow-1"></div>

            <v-toolbar-items>
                <v-btn text class="lime--text text--darken-4">
                    <router-link class="link-newsInput white--text" to="/NewsInput">新聞查詢</router-link>
                </v-btn>
                <v-btn text class="white--text" to="/History">真假新聞</v-btn>
                <v-btn text class="white--text">可疑人物</v-btn>
            </v-toolbar-items>
        </v-toolbar>
    </div>
</template>

<script>
export default {
    name: "navBar"
}
</script>

<style>
#navBar {
    font-size: 1.5vw;
}
.home-title {
    text-decoration: none;
}
.navBar-toolbar {
    height: 60px!important;
}
.no-shadow {
    box-shadow: none!important;
}
.link-newsInput {
    text-decoration: none;
    background: inherit;
}
</style>