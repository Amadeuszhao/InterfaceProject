import Vue from 'vue'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'
import echarts from 'echarts'
import Video from 'video.js'
import 'video.js/dist/video-js.css'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import less from 'less'

// use
Vue.use(less)
Vue.use(mavonEditor)
Vue.prototype.$video = Video

Vue.prototype.$echarts = echarts
Vue.prototype.$axios = axios
Vue.use(ElementUI)
Vue.prototype.$http = axios
Vue.config.productionTip = false
Vue.prototype.baseUrl = function () {
  return 'http://caballer.top:8001/'
}
Vue.prototype.baseVPN = function () {
  return 'http://n735zs2xov.52http.tech/spo_extract'
}
Vue.prototype.loginVPN = function () {
  return 'http://172.28.184.218:8001/'
}
new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
