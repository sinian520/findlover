<template>
    <div class="container">
        <el-tabs tab-position="left" >
            <el-tab-pane label="最新活动">
                <div class="choose">
                    <el-form :inline="true" :model="formInline" class="demo-form-inline">
                        <el-form-item >
                            <el-input v-model="formInline.region" placeholder="活动地点"></el-input>
                        </el-form-item>
                        <el-form-item >
                            <el-date-picker type="date" placeholder="活动时间" v-model="formInline.date" style="width: 100%;"></el-date-picker>
                        </el-form-item>
                        <el-form-item>
                            <el-input v-model="formInline.user" placeholder="举办人昵称"></el-input>
                        </el-form-item>
                        <el-form-item>
                          <el-button type="danger" @click="newactivefilter">过滤</el-button>
                        </el-form-item>
                    </el-form>
                </div>
                <div v-if="newactive.length==0" class="nochoose">还没有正在进行的活动</div>
                <div class="main">
                    <el-card v-for="o in show" :key="o.id">
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
                            <div class="text">活动进行中</div>
                            <el-button type="danger" @click="attend(o.id)">我要报名</el-button>
                        </div>
                    </el-card>
                </div>
                
            </el-tab-pane>
            <div>
            </div>
            <el-tab-pane label="精彩回顾">
                <div v-if="oldactive.length==0" class="nochoose">还没有精彩活动</div>
                <div class="main">
                <el-card v-for="o in oldactive" :key="o.id">
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
                        <div class="text1">活动已结束</div>
                        <el-button type="danger" @click="evaluate(o.id)">查看评价</el-button>
                    </div>
                    <div v-for="i in evalu" :key="i.id" class="pl">
                        <el-col :span="18"><div class="grid-content bg-purple">{{i.name}}</div></el-col>
                        <el-col :span="4"><div class="">评分:{{i.planA}}</div></el-col>
                        <el-col :span="12"><div class="pinglun">评价{{i.evaluate}}</div></el-col>
                    </div>
                </el-card>
                
            </div>
            </el-tab-pane>

            <el-tab-pane label="我的参加">
                <div v-if="myattend.length==0" class="nochoose">您还没有参加过任何线下活动</div>
                <div class="main">
                    <el-card v-for="o in myattend" :key="o.id">
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
                            <div class="text" v-if="o.evaluate">{{o.evaluate}}</div>
                            <el-popover placement="right" width="400" trigger="click" v-if="o.evaluate=='未评论'">
                               <el-rate v-model="myrate" :colors="colors "  style="display: inline;"></el-rate>
                                <el-input type="textarea" placeholder="期待您的评价" :autosize="{ minRows: 4, maxRows: 4}" v-model="myevalu"></el-input>
                                <div style="text-align: right; margin: 10px">
                                    <el-button type="danger" plain size="mini"  @click="submitevalue(o.id)">确定</el-button>
                                </div>
                                <el-button slot="reference" type="danger" v-if="o.evaluate=='未评论'">评价</el-button>
                            </el-popover>
                        </div>
                    </el-card>
                </div>
            </el-tab-pane>
        </el-tabs>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                //查询条件
                formInline: {
                    user: '',
                    region: '',
                    date: '',
                },
                //前端显示
                show: [], //活动信息查询界面
                newactive: [],
                oldactive: [],
                evalu: [],
                myattend: [],
                //评分
                myrate: null,
                colors: ['#99A9BF', '#F7BA2A', '#FF9900'], // 等同于 { 2: '#99A9BF', 4: { value: '#F7BA2A', excluded: true }, 5: '#FF9900' }
                //我的评价
                myevalu: '',
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
                    this.oldactive = JSON.parse(res.old); //字符串转json的函数
                    this.newactive = JSON.parse(res.new);
                    this.myattend = JSON.parse(res.attend);
                    this.show = this.newactive;
                }
                //前端显示
                console.log(this.oldactive);
                console.log(this.newactive);
                console.log(this.myattend);

            },
            //查询
            newactivefilter() {
                let a = this.newactive.filter((obj, index) => {
                    //查找包含关键字的
                    if (this.formInline.region && this.formInline.user && this.formInline.date) {
                        return obj.place.includes(this.formInline.region) && obj.time.includes(this.formInline.date) && obj.name.includes(his.formInline.user)
                    } else if (this.formInline.region && this.formInline.user) {
                        return obj.place.includes(this.formInline.region) && obj.name.includes(his.formInline.user)
                    } else if (this.formInline.user && this.formInline.date) {
                        return obj.time.includes(this.formInline.date) && obj.name.includes(his.formInline.user)
                    } else if (this.formInline.date && this.formInline.region) {
                        return obj.place.includes(this.formInline.region) && obj.time.includes(this.formInline.date)
                    } else if (this.formInline.user) {
                        return obj.name.includes(this.formInline.user)
                    } else if (this.formInline.region) {
                        return obj.place.includes(this.formInline.region)
                    } else if (this.formInline.date) {
                        return obj.time.includes(this.formInline.date)
                    } else
                        return;
                })

                this.show = a;
                if (this.show.length == 0) {
                    this.show = this.newactive
                    this.$message.info("没有找到符合条件的活动")
                }
            },
            // 报名参加
            async attend(id) {
                var user = window.sessionStorage.getItem("user");
                var param = new URLSearchParams();
                param.append('user', user)
                param.append('partyid', id);
                const {
                    data: res
                } = await this.$http.post('AttendActive/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else
                    this.$message.success(res.msg)
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
                console.log(this.evalu);
                if (this.evalu.length == 0) {
                    console.log(this.evalu);
                    this.$message.info("该活动暂无评价")
                }
            },
            //进行评价
            async submitevalue(id) {

                var user = window.sessionStorage.getItem("user");
                var param = new URLSearchParams();
                param.append('user', user)
                param.append('partyid', id);
                param.append('rate', this.myrate)
                param.append('evaluate', this.myevalu);
                const {
                    data: res
                } = await this.$http.post('PostEvaluate/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    this.$message.success(res.msg)
                    console.log("hhhhhhhhhhhh" + id);
                    for (var a = 0; a < this.myattend.length; a++) {
                        if (this.myattend[a].id == id) {
                            console.log("1111111111111" + this.myattend[a].id);
                            this.$set(this.myattend[a], 'evaluate', "已评论")
                            console.log("1111111111111" + this.myattend[a]);
                        }
                        console.log(this.myattend[a]);

                    }


                }


            },

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
    
    .demo-form-inline {
        padding-left: 30px;
        padding-top: 20px;
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
    
    .nochoose {
        width: 100%;
        height: 100%;
        background-color: #FFF;
        color: #606266;
        text-align: center;
        line-height: 400px;
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
</style>