import Vue from 'vue';
import Vuetify from 'vuetify/lib';

import colors from 'vuetify/lib/util/colors'

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#1C1C1C",
        secondary: "#FF9100",
        accent: colors.yellow.lighten1, // #3F51B5
        error: colors.red,
      },
    },
  },
  // icons: {
  //   iconfont: 'mdi',
  // },
});
