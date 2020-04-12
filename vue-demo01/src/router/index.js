import Vue from 'vue'
import Router from 'vue-router'
import login from '../components/login.vue'
import firstpage from '../components/firstpage.vue'
import register from '../components/register.vue'
import personal from '../components/personal.vue'
import home from '../components/home.vue'
import vippage from '../components/vippage.vue'
import friends from '../components/friends.vue'
import active from '../components/active.vue'
import helppage from '../components/helppage.vue'
import showtime from '../components/showtime.vue'

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
            path: '/register',
            component: register
        },
        {
            path: '/firstpage',
            component: firstpage,
            redirect: '/home',
            children: [{
                    path: '/home',
                    component: home
                },
                {
                    path: '/personal',
                    component: personal
                },
                {
                    path: '/vippage',
                    component: vippage
                },
                {
                    path: '/friends',
                    component: friends
                }, {
                    path: '/active',
                    component: active
                }, {
                    path: '/helppage',
                    component: helppage
                },
                {
                    path: '/showtime',
                    component: showtime
                }
            ]
        },
        // {
        //     path: '/home',
        //     component: home
        // },
        // {
        //     path: '/personal',
        //     component: personal
        // },

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

    if (!tokenStr && to.name.indexOf('login') < 0) { //字符串不含有login字符<0
        if (from.path === '/Register') {
            next();
            console.log("以允许");
        } else
            return next('/login');
    }
    next();
})

export default router