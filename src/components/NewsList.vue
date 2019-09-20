<template>
    <div>
        <v-container fluid row justify-center>
            <v-col class="cards" cols="12">
                <v-row>
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                </v-row>
                <v-row>
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                </v-row>
                <v-row>
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                </v-row>
                <v-row>
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                    <Card class="ma-3" />
                </v-row>
            </v-col>
        </v-container>
    </div>
</template>

<script>
import Card from './Card'

export default {
    components: {
        Card
    }
}
</script>

<style>
.cards {
    padding: 1vw;
}
</style>