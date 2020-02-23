<template>
    <div class="home_container">
        <div class="top">
            <span>欢迎来到"一缘"</span>
        </div>
        <div class='head'>
            <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect"
      background-color="#960404" text-color="#fff"  active-text-color="#ffd04b">
                <el-menu-item index="1">首页</el-menu-item>
                <el-menu-item index="2">好友管理</el-menu-item>
                <el-menu-item index="3">会员中心</el-menu-item>
                <el-menu-item index="4">恋爱展</el-menu-item>
                <el-menu-item index="5">心里测试</el-menu-item>
                <el-menu-item index="6">线下活动</el-menu-item>
                <el-menu-item index="7">情感求助</el-menu-item>
                <el-menu-item index="8">红娘服务</el-menu-item>
                <!-- 头像区域 -->



                <el-popover placement="top-start" trigger="hover" content="点击修改个人信息" class="avater_box">
                        <el-button slot="reference" type="text" @click="information">
                            <el-avatar src="logo.png"></el-avatar>
                        </el-button>
                </el-popover>


                <el-button @click="userexit" type="text" class="exit">退出</el-button>
            </el-menu>
        </div>
        <div class="container">
            <el-container>
                <el-main>
                    Main
                </el-main>
                <el-header>
                    <div class="heng">
                        <span>找女/男朋友</span>
                    </div>
                </el-header>
                <el-main></el-main>
                <el-header>Header</el-header>
                <el-main>Main</el-main>
                <el-header>Header</el-header>
                <el-main>Main</el-main>
                <el-header>Header</el-header>
                <el-main>Main</el-main>
            </el-container>
        </div>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                activeIndex: '1',
                activeIndex2: '1',
                tabPosition: 'left'
            };
        },
        methods: {
            userexit() {
                window.sessionStorage.clear();
                this.$router.push("/login");
            },
            information() {
                this.$router.push("/personal");
            },
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            }
        }
    }
</script>

<style lang="less" scoped>
    .home_container {
        height: 100%;
        width: 100%;
    }
    
    .top {
        width: 100%;
        height: 35px;
        background-color: black;
        color: #fff;
        position: fixed;
        top: 0;
        left: 0;
    }
    
    .top span {
        position: absolute;
        margin-left: 20px;
        margin-top: 5px;
        font-style: 宋体;
        letter-spacing: 5px;
    }
    
    .head {
        width: 100%;
        position: fixed;
        top: 35px;
        left: 0;
    }
    
    .avater_box {
        height: 60px;
        position: absolute;
        left: 90%;
        background-color: #960404;
    }
    
    .exit {
        position: absolute;
        margin-top: 10px;
        left: 95%;
    }
    
    .container {
        margin-top: 98px;
        widows: 100%;
    }
    
    .el-main {
        width: 100%;
        height: 500px;
        border: 1px solid;
    }
    
    .el-header {
        width: 100%;
        height: 80px;
        border: 1px solid;
    }
    
    .heng {
        width: 95%;
        height: 40px;
        border: 1px solid;
        margin-top: 10px;
        margin-left: 20px;
        background-color: #b40000;
    }
    
    .heng span {
        color: #fff;
        font-size: 25px;
        font-weight: 700;
        margin-left: 5px;
    }
</style>