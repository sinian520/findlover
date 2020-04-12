<!-- 主页框架 -->

<template>
    <div class="home_container">
        <el-container>
            <el-header style="height: 100px;">
                <div class="top">
                    <p>欢迎来到"一缘"</p>
                </div>
                <div class='head'>
                    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
              background-color="#960404" text-color="#fff"  active-text-color="#ffd04b"  router    default-active="this.$router.path">
                        <el-menu-item index="home">首页</el-menu-item>
                        <el-menu-item index="friends">好友管理</el-menu-item>
                        <el-menu-item index="vippage">会员中心</el-menu-item>
                        <el-menu-item index="4">恋爱展</el-menu-item>
                        <el-menu-item index="5">心里测试</el-menu-item>
                        <el-menu-item index="6">线下活动</el-menu-item>
                        <el-menu-item index="7">情感求助</el-menu-item>
                        <el-menu-item index="">红娘服务</el-menu-item>
                        <!-- 头像区域 -->
        
        
                        <el-popover placement="top-start" trigger="hover" content="点击完善个人信息呦" class="avater_box">
                                <el-button slot="reference" type="text" @click="information">
                                    <el-avatar :src="this.user.img"></el-avatar>
                                </el-button>
                        </el-popover>
        
        
                        <el-button @click="userexit" type="text" class="exit">退出</el-button>
                    </el-menu>
                </div>
            </el-header>
            <el-main>
                <!-- 路由占位符 -->
                <router-view></router-view>
                
            </el-main>
            <div class="footer">
                <p>关于一缘 |
                    商务合作 |
                    版权所有 |     
                    联系我们 |
                    诚聘人才 |
                    寻求帮助
                    <br>
                    版权所有解释权归本人所有
                    123005895060 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
                    
                    违反和不良信息举报电话 18846562389
                </p>

            </div>
        </el-container>
        
    </div>

</template>

<script>
    export default {
        data() {
            return {
                //导航栏
                activeIndex: '1',
                tabPosition: 'left',
                user: {
                    name: "",
                    img: "",
                },
            };
        },
        created() {
            this.getPersonal();
        },
        methods: {
            //退出
            userexit() {
                window.sessionStorage.clear();
                this.$router.push("/login");
            },
            //个人信息
            information() {
                this.$router.push("/personal");
            },
            //导航栏
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
            },
            async getPersonal() {
                var user = window.sessionStorage.getItem("user");
                let param = new URLSearchParams()
                param.append('user', user)
                console.log(user);
                const {
                    data: res
                } = await this.$http.post('Personal/', param)
                if (res.code == 1002)
                    return this.$message.error(res.msg)

                console.log(res);
                this.user.name = res.name;
                this.user.img = res.photo;
                if (this.user.img == "") {
                    this.user.img == "//images.baihe.com/images/baihe_new/images/default_pictures/100_100/nopic_female.gif"
                }
                console.log(this.user.img);

            }
        }
    }
</script>

<style lang="less" scoped>
    .home_container {
        height: 100%;
        width: 1230px;
        display: block;
    }
    
    .el-main {
        border: 1px solid;
        padding: 0;
        width: 100%;
    }
    
    .el-menu-demo {
        height: 63px;
    }
    
    .top {
        width: 1230px;
        height: 35px;
        background-color: black;
        color: #fff;
        position: absolute;
        top: 0;
        left: 0;
    }
    
    .top p {
        position: absolute;
        margin-left: 20px;
        margin-top: 5px;
        font-style: 宋体;
        letter-spacing: 5px;
    }
    
    .head {
        width: 1230px;
        position: absolute;
        top: 35px;
        left: 0;
    }
    
    .avater_box {
        height: 60px;
        position: absolute;
        right: 90px;
        background-color: #960404;
    }
    
    .el-avatar {
        height: 60px;
        width: 60px;
        margin-top: -10px;
    }
    
    .exit {
        position: absolute;
        margin-top: 15px;
        left: 95%;
        color: #fff;
    }
    
    .footer {
        width: 100%;
        height: 150px;
        background-color: #555;
    }
    
    .footer p {
        padding-top: 25px;
        font-size: 14px;
        line-height: 30px;
        color: #aaa;
        text-align: center;
    }
</style>