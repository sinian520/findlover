import Vue from 'vue'
import App from './App'
import router from './router'
// 导入全局样式表
import './assets/css/global.css'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import { Form, FormItem, Input, Button, Message, Container } from 'element-ui'

import axios from 'axios'
//导入字体图标
import './assets/font/iconfont.css'


// 配置请求的根路径
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
Vue.prototype.$http = axios
    //弹框组件提示挂载
Vue.prototype.$message = Message
Vue.use(Button)
Vue.use(Form)
Vue.use(FormItem)
Vue.use(Input)
Vue.use(Container)
Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(router);
/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    render: h => h(App)
})