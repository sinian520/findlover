<template>
    <div class="container">
        <!-- 步骤条 -->
        <div class="step">
            <div class="step_top">
                <el-steps :active="active" finish-status="success">
                    <el-step title="选择服务"></el-step>
                    <el-step title="选择支付方式"></el-step>
                    <el-step title="开通服务成功"></el-step>
                </el-steps>
            </div>
            
    
            <div class="step_main">

                <div class="choosevip">
                    <div class="value">
                        <span>{{value}}</span>
                        <span>元</span>


                        <el-popover placement="bottom" width="250"  v-model="visible">
                            <p>扫一扫 微信支付（
                                <span>{{value}}元</span>）
                            </p>
                            <div style="height:230px">
                                <img class="pay"src="../assets/img/联图二维码.png" alt="" >
                            </div>
                            
                            <div style="text-align: right; margin-top:0">
                                <el-button type="danger" plain size="mini"  @click="visible = false">取消</el-button>
                                <el-button type="danger" size="mini" @click="dopay">确定</el-button>
                            </div>
                            <el-button  slot="reference" type="danger" round @click="next" class="btnvip">开通会员>></el-button>
                        </el-popover>
                        
                    </div>
                    
                </div>
                <div class="show">
                    <el-divider content-position="left" > 
                        <h2>会员特权</h2>
                    </el-divider>
                    <ul class="step_buttom">
                    <li>
                        昵称红色显示
                        <br>
                        <span>
                            更显目的昵称，展现瞩目
                        </span>
                    </li>
                    <li>
                        寻求情感帮助
                        <br>
                        <span>
                            优先为您解决恋爱烦恼，为约会保驾护航
                        </span>
                        
    
                    </li>
                    <li>
                        参加线下聚会
                        <br>
                        <span>更多缘分，更多接触让你找到意中人</span>
                    </li>
                    </ul>
                    <el-divider content-position="left"> <h2>补充说明</h2></el-divider>
                    <p class="server">服务将于支付成功后立即开通<br>
                    对服务有任何疑问或存在任何问题请拨打客服服务专线 0418-5462805 (服务时间9:00~15:00)
                    <br>
                    服务一经开通后，不能退款，敬请谅解
                    </p>
                </div>
                
            </div>
            
        </div>

    </div>

</template>

<script>
    export default {
        data() {
            return {
                //步骤条
                active: 1,
                value: "",
                //支付显示
                visible: false,
            };
        },
        created() {
            this.getPrice();
        },
        methods: {
            async getPrice() {
                //获取会员价格
                const {
                    data: res
                } = await this.$http.post('Vip/')
                if (res.code == 1002)
                    return this.$maessage.error(res.msg)
                else
                    this.value = res.msg

                //判断是否是会员

            },


            //开通会员
            next() {
                this.active++;
            },
            //确认
            async dopay() {
                this.visible = false;
                this.active++;
                //成为会员
                var user = window.sessionStorage.getItem("user");
                let param = new URLSearchParams()
                param.append('user', user)
                console.log(user);
                const {
                    data: res
                } = await this.$http.post('Bevip/', param)
                if (res.code == 1002)
                    return this.$message.error(res.msg)
                this.$message.success(res.msg);

            }
        }
    }
</script>

<style lang="less" scoped>
    .container {
        width: 1200px;
        padding: 0px;
    }
    
    .step {
        width: 900px;
        margin-left: 150px;
        margin-top: 20px;
    }
    
    .step_top {
        width: 960px;
    }
    
    .step_main {
        width: 900px;
        margin-top: 30px;
    }
    
    .choosevip {
        height: 350px;
        width: 100%;
        background-image: url("//images10.baihe.com/crystalPrice/bj_gjA.jpg");
    }
    
    .value {
        position: relative;
        width: 100%;
        height: 150px;
        top: 250px;
        padding-left: 200px;
    }
    
    .value span {
        font-weight: 500;
        font-size: 60px;
        color: #fff;
        font-style: italic;
    }
    
    .pay {
        height: 200px;
        width: 250px;
        position: absolute;
        top: auto;
    }
    
    .el-popover {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        bottom: 0;
        margin: auto;
        text-align: center;
    }
    
    .btnvip {
        height: 60px;
        width: 170px;
        font-size: 25px;
        margin-left: 150px;
    }
    
    .show {
        margin-top: 70px;
    }
    
    h2 {
        color: #f84747ee;
        font-weight: 500;
    }
    
    .step_buttom {
        margin-top: 60px;
        height: 100px;
    }
    
    .step_buttom li {
        float: left;
        width: 200px;
        margin-right: 80px;
        color: #f84747ee;
        font-weight: lighter;
    }
    
    .step_buttom li span {
        color: #999;
        font-size: 13px;
    }
    
    .server {
        margin-top: 50px;
        color: #999;
        font-size: 13px;
        line-height: 25px;
        height: 100px;
        margin-left: 40px;
    }
</style>