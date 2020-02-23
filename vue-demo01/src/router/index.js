import Vue from 'vue'
import Router from 'vue-router'
import login from '../components/login.vue'
import firstpage from '../components/firstpage.vue'
import register from '../components/register.vue'
import personal from '../components/personal.vue'

Vue.use(Router)

const router = new Router({
    mode: 'history', //去掉url的#
    routes: [{ //直接访问login
            path: '/',
            redirect: '/login'
        },
        {
            path: '/login',
            component: login
        },
        {
            path: '/firstpage',
            component: firstpage
        },
        {
            path: '/register',
            component: register
        },
        {
            path: '/personal',
            component: personal
        }
    ]
})


//挂载路有导航守卫
router.beforeEach((to, from, next) => {
    // to 将要访问路径
    // from 代表从哪个路径跳转来
    // next() 放行  next('/login') 强制跳转
    if (to.path === '/login') return next();
    if (to.path === '/register') return next();
    const tokenStr = window.sessionStorage.getItem('token');

    if (!tokenStr) {
        if (from.path === '/Register') {
            next();
            console.log("以允许");
        } else
            return next('/login');
    }
    next();
})

export default router