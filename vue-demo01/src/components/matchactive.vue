<template>
    <div class="container">
        <div style="margin: 10px"> 
            <el-switch
            style="display: inline;margin-left: 30px;"
            v-model="type"
            active-color="#13ce66"
            inactive-color="#ff4949"
            active-text="活动进行中"
            inactive-text="活动已结束"
            @change='changeStatus($event)'>
            </el-switch>
            <el-button type="danger" class="button" @click="join">发布活动</el-button>
        </div>
        <div v-if="myapply.length==0" class="nochoose">您还没有发布过任何活动，点击发布活动信息</div>
        <div class="main">
        <el-card v-for="o in myapplyshow" :key="o.id">
            <div class="spanlist">
                <el-row>
                    <el-col :span="6">
                        <h4>{{o.tele}}</h4></el-col>
                </el-row>
                    <el-row>
                        <el-col :span="4"><div class="grid-content bg-purple">举行日期：</div></el-col>
                        <el-col :span="12"><div class="grid-content bg-purple-light">{{o.time}}</div></el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="4"><div class="grid-content bg-purple">活动地点：</div></el-col>
                        <el-col :span="6"><div class="grid-content bg-purple-light">{{o.place}}</div></el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="4"><div class="grid-content bg-purple">活动资金：</div></el-col>
                        <el-col :span="6"><div class="grid-content bg-purple-light">{{o.money}}元</div></el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="4"><div class="grid-content bg-purple">邀请人数：</div></el-col>
                        <el-col :span="6"><div class="grid-content bg-purple-light">{{o.Count}}人</div></el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="4"><div class="grid-content bg-purple">活动内容：</div></el-col>
                        <el-col :span="12"><div class="grid-content bg-purple-light">{{o.activities}}</div></el-col>
                    </el-row>
            </div>
            <div class="spanright">  
                <div class="grid-content bg-purple-light">举办人：{{o.name}}</div>
                <div class="text" v-if="!o.status">活动已结束</div>
                <div class="text" v-if="o.status">活动进行中</div>
                <el-button type="danger" plain @click="evaluate(o.id)" v-if="type">查看评价</el-button>
                <el-button type="danger" plain @click="usershow(o.id)" v-if="!type">查看参与用户</el-button>
            </div>
            <div v-for="i in evalu" :key="i.id" class="pl" v-if="o.id==i.partyid">
                <el-col :span="18"><div class="grid-content bg-purple">{{i.name}}</div></el-col>
                <el-col :span="4"><div class="">评分:{{i.planA}}</div></el-col>
                <el-col :span="12"><div class="pinglun">评价:{{i.evaluate}}</div></el-col>
            </div>
            <div v-if="user.length!=0&&!type">
                <el-table :data="user"  style="width: 100%" >
                    <el-table-column prop="name"  label="用户" width="80"></el-table-column>
                    <el-table-column prop="sex"  label="性别" width="80"></el-table-column>
                    <el-table-column prop="age"  label="年龄" width="80"></el-table-column>
                    <el-table-column prop="profession"  label="职业" width="100"></el-table-column>
                    <el-table-column prop="tele"  label="联系电话" width="150"></el-table-column>
                    <el-table-column prop="emile"  label="邮箱" width="200"></el-table-column>
                    <el-table-column prop="live"  label="所在地" width="200"></el-table-column>
                    
                </el-table>
            </div>
            </el-card>
        </div>  
    </div>

</template>

<script>
    export default {
        data() {
            return {
                // 显示
                myapplyshow: [],
                myapply: [],
                //发布分类
                type: true,
                evalu: [],
                user: [],
            };
        },
        created() {
            this.getShow();
        },
        methods: {
            async getShow() {
                var user = window.sessionStorage.getItem("user");
                var param = new URLSearchParams();
                param.append('user', user)
                const {
                    data: res
                } = await this.$http.post('Showactive/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    this.myapply = JSON.parse(res.my);
                    var a = this.myapply.filter((obj, index) => {
                        return obj.status == false
                    })
                    this.myapplyshow = a
                }
                //前端显示
                console.log(this.myapply);

            },
            // 开关
            changeStatus($event) {
                console.log($event)
                if ($event == true) {
                    let a = this.myapply.filter((obj, index) => {
                        return obj.status == false
                    })
                    this.myapplyshow = a
                    console.log(this.myapplyshow);
                } else {
                    let a = this.myapply.filter((obj, index) => {
                        return obj.status == true
                    })
                    this.myapplyshow = a
                    console.log(this.myapplyshow);
                }
            },
            // #获取评价
            async evaluate(id) {
                var param = new URLSearchParams();
                param.append('id', id);
                const {
                    data: res
                } = await this.$http.post('GetEvaluate/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else
                    this.evalu = JSON.parse(res.evaluate);
                if (this.evalu.length == 0) {
                    console.log(this.evalu);
                    this.$message.info("该活动暂无评价")
                }

            },
            // 查看参与用户
            async usershow(id) {
                var param = new URLSearchParams();
                param.append('id', id);
                const {
                    data: res
                } = await this.$http.post('GetActiveUser/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else
                    this.user = JSON.parse(res.user);
                if (this.user.length == 0) {
                    console.log(this.user);
                    this.$message.info("暂时没有人报名")
                }
            },
            join() {
                this.$router.push('/activeapply')
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
    
    .choose {
        width: 100%;
        height: 80px;
    }
    
    .nochoose {
        width: 100%;
        height: 100%;
        background-color: #FFF;
        color: #606266;
        text-align: center;
        line-height: 400px;
    }
    
    .main {
        width: 100%;
        margin-left: 30px;
    }
    
    .spanlist {
        margin-left: 50px;
        float: left;
        width: 500px;
        margin-bottom: 20px;
    }
    
    .spanright {
        margin-left: 50px;
        float: left;
        width: 150px;
        margin-bottom: 20px;
        text-align: center;
    }
    
    .text {
        margin-top: 60px;
        padding-bottom: 30px;
    }
    
    .text1 {
        margin-top: 30px;
        padding-bottom: 30px;
    }
    
    .value {
        margin-top: 20px;
    }
    
    .pl {
        width: 100%;
        height: 50px;
        margin-left: 20px;
    }
    
    .pinglun {
        color: #606266;
        font-size: 14px;
        margin-top: 10px;
    }
    
    .button {
        margin-left: 60%;
    }
</style>