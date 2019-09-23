<template>
    <div>
        <v-container fill-height fluid>
          <v-layout align-start column >
            <v-flex white--text mt-10 class="mysubtitle">熱門搜索</v-flex>
            <v-col cols="12">
              <v-row
                v-for="n in 2"
                :key="n"
              >
                <v-col
                  v-for="k in 4 "
                  :key="k"
                  >
                  <Card />
                </v-col>
              </v-row>
            </v-col>
        </v-layout>
        </v-container>
    </div>
</template>

<script>
import Card from './Card'

export default {
  data: () => ({
    total: 10,
  }),
  components: {
    Card
  },
  computed: {

 },
}
</script>

<style>

</style>
