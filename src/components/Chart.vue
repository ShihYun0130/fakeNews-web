<template>
  <v-app>
    <div id="about">
      <NavBar />
        <v-container class="mycon" fill-height fluid>
          <v-layout align-start column>
            <v-flex white--text mt-10 class="mytitle">大標題24px</v-flex>
            <v-flex white--text mt-10 class="mysubtitle">中標題20px</v-flex>
            <v-flex white--text mt-10 class="mytext">內文14px壬戌之秋，七月既望，蘇子與客泛舟遊於赤壁之下。清風徐來，水波不興。舉酒屬客，誦明月之詩，歌窈窕之章。少焉，月出於東山之上，徘徊於斗牛之間。白露橫江，水光接天。縱一葦之所如，凌萬頃之茫然。浩浩乎如馮虛御風，而不知其所止；飄飄乎如遺世獨立,羽化而登仙。
            於是飲酒樂甚，扣舷而歌之。歌曰：“桂棹兮蘭槳，擊空明兮溯流光。渺渺兮予懷，望美人兮天一方。”客有吹洞簫者，倚歌而和之。其聲嗚嗚然，如怨如慕，如泣如訴；餘音嫋嫋，不絕如縷。舞幽壑之潛蛟，泣孤舟之嫠婦。
            蘇子愀然，正襟危坐，而問客曰：“何爲其然也？”客曰：“‘月明星稀，烏鵲南飛。’此非曹孟德之詩乎？西望夏口，東望武昌，山川相繆，鬱乎蒼蒼，此非孟德之困於周郎者乎？方其破荊州，下江陵，順流而東也，舳艫千里，旌旗蔽空，釃酒臨江，橫槊賦詩，固一世之雄也，而今安在哉？況吾與子漁樵於江渚之上，侶魚蝦而友麋鹿，駕一葉之扁舟，舉匏樽以相屬。寄蜉蝣於天地，渺滄海之一粟。哀吾生之須臾，羨長 江之無窮。挾飛仙以遨遊，抱明月而長終。知不可乎驟得，託遺響於悲風。”
            蘇子曰：“客亦知夫水與月乎？</v-flex>
            <v-flex orange--text text--accent-3 mt-10 class="mysubtitle">Primary color #FF9100</v-card></v-flex>
            <v-flex orange--text text--darken-4 mt-5 class="mysubtitle">Secondary color #E5100</v-card></v-flex>
            <v-flex grey--text grey--lighten-1 mt-5 mb-12 class="mysubtitle">Grey color #BDBDBD</v-card></v-flex>



        </v-layout>
        </v-container>
        <Footer />
    </div>
  </v-app>
</template>

<script>
import NavBar from './NavBar';
import Footer from './Footer';
export default {

  components: {
    NavBar,
    Footer
  },


  data: () => ({
  }),

}
</script>

<style>
#about {
    font-family: 'Noto Sans TC', sans-serif;
    background-image: url('../assets/bg.png');
    background-repeat: no-repeat;
    background-size:cover;

}
.mycon {
  padding: 0 7.3% !important;
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
