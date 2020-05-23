<template>
    <div class="container">
        <el-row class="heng">
            <span class="span1">爱情测试</span>
            <el-divider direction="vertical"></el-divider>
            <span class="small">了解属于你的爱情真谛</span>
        </el-row>
        <div id="box">
            <ul>
                <li v-for="v in textshow"  :key="v.id" @click="text(v.http)">
                        <img :src="v.img" alt="">
                        <span>{{v.subject}}</span>
                        <div class="time">
                        <span>有{{v.count}}人测试过</span>
                        </div>
                </li>
            </ul>
        </div>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                textshow: [],

            };
        },
        created() {
            this.getShow()
        },
        //  mounted() {
        //     /**
        //      * iframe-宽高自适应显示   
        //      */
        //     function changeMobsfIframe() {
        //         const mobsf = document.getElementById('mobsf');
        //         const deviceWidth = document.body.clientWidth;
        //         const deviceHeight = document.body.clientHeight;
        //         mobsf.style.width = (Number(deviceWidth) - 120) + 'px'; //数字是页面布局宽度差值
        //         mobsf.style.height = (Number(deviceHeight) - 80) + 'px'; //数字是页面布局高度差
        //     }

        //     changeMobsfIframe()

        //     window.onresize = function() {
        //         changeMobsfIframe()
        //     }
        // },
        methods: {
            //显示心理测试
            async getShow() {
                const {
                    data: res
                } = await this.$http.post('GetText/')
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    this.textshow = JSON.parse(res.List); //字符串转json的函数
                }

                //前端显示
                console.log(this.textshow);

            },
            text(http) {
                this.$router.push({
                    name: 'textpage',
                    params: {
                        http: http
                    }
                })
            }
        }

    }
</script>

<style lang="less" scoped>
    .container {
        width: 950px;
        margin-left: 150px;
        min-height: 600px;
        height: auto!important;
        height: 600px;
    }
    
    #box {
        width: 100%;
    }
    
    #box ul {
        display: flex;
        flex-wrap: wrap;
        margin-left: 0px;
    }
    
    #box li {
        list-style: none;
        border: 1px solid #eee;
        margin-left: 20px;
        margin-top: 15px;
        width: 180px;
        height: 240px;
    }
    
    #box img {
        width: 180px;
        height: 190px;
    }
    
    .time {
        text-align: right;
        color: #606266;
        font-size: 14px;
    }
    
    .heng {
        color: #f56c6c;
        padding-top: 10px;
        box-sizing: border-box;
    }
    
    .span1 {
        font-weight: 500;
        font-size: 25px;
        margin-left: 30px;
    }
    
    .small {
        font-weight: 100;
        font-size: 15px;
        margin-left: 0px;
    }
</style>