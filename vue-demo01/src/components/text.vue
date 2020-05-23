<template>
    <div class="container">
        <el-page-header @back="goBack" content="测试题">
        </el-page-header>
        <div>
            <iframe :src="http" id="mobsf" scrolling="no" frameborder="0" width="100%" height="1000px"></iframe>
        </div>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                http: this.$route.params.http,

            };
        },
        created() {},
        // mounted() {
        //     /**
        //      * iframe-宽高自适应显示   
        //      */
        //     function changeMobsfIframe() {
        //         const mobsf = document.getElementById('mobsf');
        //         const deviceWidth = document.body.clientWidth;
        //         const deviceHeight = document.body.clientHeight;
        //         // mobsf.style.width = (Number(deviceWidth) - 120) + 'px'; //数字是页面布局宽度差值
        //         // mobsf.style.height = (Number(deviceHeight) - 80) + 'px'; //数字是页面布局高度差
        //         mobsf.style.width = 100 + '%'; //数字是页面布局宽度差值
        //     }

        //     changeMobsfIframe()

        //     window.onresize = function() {
        //         changeMobsfIframe()
        //     }
        // },
        methods: {
            goBack() {
                this.$router.push('/psychological')
            },
        }
    }
</script>

<style lang="less" scoped>
    .container {
        width: 950px;
        margin-left: 150px;
    }
</style>