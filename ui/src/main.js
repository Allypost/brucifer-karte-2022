import { createApp, Vue } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js';
import JsonCSV from 'vue-json-csv';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueJwtDecode from 'vue-jwt-decode'
import Vuex from 'vuex';
import VueNavigationBar from 'vue-navigation-bar';
import 'vue-navigation-bar/dist/vue-navigation-bar.css';
import "./../node_modules/bulma/css/bulma.css";


const app= createApp(App).use(store).use(router)


app.component('downloadCsv', JsonCSV).component('VueJwtDecode', VueJwtDecode)

app.use(Vuex)

app.component('VueNavigationBar', VueNavigationBar);

import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faTrashCan, faCheck, faXmark } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faTrashCan)
library.add(faCheck)
library.add(faXmark)

app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')


