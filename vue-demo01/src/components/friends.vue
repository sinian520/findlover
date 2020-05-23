<template>
    <div>
        <el-container class="container">
            <el-aside width="300px">
               <div v-for="(item,index) in friendlist" :key="item.id" :class="{listback :item.choose} "class="list" @click="choose(item.emile)">  <!-- @click="choose(user.email)" -->
                    <div class="listlo">
                        <el-avatar :src="item.photo"></el-avatar>
                    </div>
                    <div class="listlo">
                        <span class="dete">
                            <el-button circle icon="el-icon-delete" @click.stop="open(item.emile) "></el-button>
                        </span>
                        <div class="listname">{{item.name}}</div>
                        <div class="listdiv">
                            <span>{{item.age}}岁</span>
                            <span>{{item.live}}</span>
                            <span>{{item.height}}</span>
                        </div>
                    </div>
                    
                </div>
            </el-aside>
            <el-main>
                <div class="nochoose" :style="{display: show1}">
                    查看好友信息，了解他/她
                    <span class="el-icon-s-custom"></span>/<span class="el-icon-s-check"></span>
                </div>
                <div class="choosef" :style="{display: show2}">
                    <el-row>
                        <el-col :span="10">
                            <img :src="friendinfo.photo" alt="朋友照片">
                        </el-col>
                        
                        <el-col :span="14">
                            <div class="grid-content ">
                                <h1>{{friendinfo.name}}</h1>
                                <span>{{friendinfo.age}}</span>
                                <div class="spanlist">
                                    <table>
                                        <tr>
                                            <td>婚姻：<span>{{friendinfo.marriage}}</span></td>
                                            <td>家乡：<span>{{friendinfo.live}}</span></td>
                                        </tr>
                                        <tr>
                                            <td>职业：<span>{{friendinfo.profession}}</span></td>
                                            <td>月薪：<span>{{friendinfo.money}}</span></td>
                                        </tr>
                                        <tr>
                                            <td>学历：<span>{{friendinfo.education}}</span></td>
                                            <td>生日：<span>{{friendinfo.birthday}}</span></td>
                                        </tr>
                                    </table>
                                </div>
                                
                            </div>
                        </el-col>
                    </el-row>
                    
                    
                    <div class="heng">自我介绍
                        <div class="bg-purple-dark">{{friendinfo.charater}}
                        </div>
                    </div>
                    <div class="heng">联系方式</div>
                    <div class="spanlist">
                        <el-col :span="10">电话：<span>{{friendinfo.tele}}</span></el-col>
                    <el-col :span="12">微信：<span>{{friendinfo.WXchart}}</span></el-col>
                    </div>
                </div>
            </el-main>
          </el-container>
    </div>

</template>

<script>
    export default {
        data() {
            return {
                //右侧显示
                show1: 'block',
                show2: 'none',
                friendlist: [],
                // 朋友信息
                friendinfo: {
                    name: '',
                    age: '',
                    profession: '',
                    money: '',
                    photo: '',
                    birthday: '',
                    education: '',
                    marriage: '',
                    live: '',
                    tele: '',
                    WXchart: '',
                    charater: ''

                }
            };
        },
        created() {
            this.getFriends();
        },
        methods: {
            async getFriends() {
                //获取用户朋友
                var user = window.sessionStorage.getItem("user");
                let param = new URLSearchParams()
                param.append('user', user)
                const {
                    data: res
                } = await this.$http.post('GetFriends/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else
                    this.friendlist = JSON.parse(res.list); //字符串转json的函数



            },
            // 选择改变颜色显示好友信息
            choose(id) {
                console.log(id)

                this.show1 = "none",
                    this.show2 = "block"
                var count = 0;
                this.friendlist.forEach((obj, index) => {

                    if (obj.emile == id) {
                        this.friendinfo.education = obj.education
                        this.friendinfo.name = obj.type + "/" + obj.name
                        this.friendinfo.age = obj.age + "岁/" + obj.height + "/" + obj.weight
                        this.friendinfo.profession = obj.profession
                        this.friendinfo.money = obj.money
                        this.friendinfo.birthday = obj.birthday
                        this.friendinfo.photo = obj.photo
                        this.friendinfo.marriage = obj.marriage
                        this.friendinfo.tele = obj.tele
                        this.friendinfo.WXchart = obj.WXchart
                        this.friendinfo.charater = obj.charater
                    }
                    obj.choose = false;
                })
                console.log(this.friendinfo.photo)
                for (let key in this.friendinfo) {
                    if (!this.friendinfo[key])
                        this.friendinfo[key] = "以后告诉你"
                    if (this.friendinfo[key] == "http://127.0.0.1:8000/static/") {
                        this.friendinfo[key] = this.friendinfo[key] + "img/headimg.jpg"
                        console.log(this.friendinfo[key])
                    }

                }
                let change = this.friendlist.map(function(obj, index) {
                    if (obj.emile == id) {
                        obj.choose = true;
                    }
                    return obj

                })

            },
            async del(id) {
                // 删除对象数组中的index的一项
                // this.productlist.splice(index, 1)
                // this.showlist = this.productlist

                // 用id删除
                //获取用户朋友
                let param = new URLSearchParams()
                param.append('user', id)
                    // const {
                    //     data: res
                    // } = await this.$http.post('GetFriends/', param)
                    // if (res.code == 1002 || res.code == 1001)
                    //     return this.$maessage.error(res.msg)
                    // else
                    //     this.friendlist = JSON.parse(res.list)


                console.log(id)
                let dellist = this.friendlist.filter(function(obj, index) {

                    return obj.emile != id;
                })
                console.log(dellist)
                this.friendlist = [...dellist]

            },

            // 删除好友确认
            open(id) {
                this.$confirm('是否确定删除此好友?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    //删除朋友


                    this.del(id);
                    this.$message({
                        type: 'success',
                        message: '删除成功!'
                    });



                }).catch(() => {
                    this.$message({
                        type: 'info',
                        message: '已取消删除'
                    });
                });
            },

        }
    }
</script>

<style lang="less" scoped>
    body {
        margin: 0;
    }
    
    .container {
        width: 850px;
        margin-left: 200px;
        height: 500px;
    }
    
    .el-aside {
        background-color: #E9EEF3;
        color: #333;
        padding: 0;
        border-right: 1px solid #D3DCE6;
    }
    
    .el-main {
        border-right: 1px solid #D3DCE6;
        color: #333;
    }
    
    .list {
        width: 100%;
        height: 100px;
        border-bottom: 1px solid #D3DCE6;
        margin: 0px;
    }
    
    .listlo {
        float: left;
        height: 100%;
    }
    
    .listdiv span {
        margin-left: 5px;
        font-size: 14px;
    }
    
    .listback {
        background-color: #e4e7ed;
    }
    
    .el-avatar {
        width: 75px;
        height: 75px;
        margin-top: 15px;
        margin-left: 5px;
    }
    
    .listname {
        width: 170px;
        height: 30px;
        margin-top: -10px;
        margin-left: 20px;
        font-weight: 500;
    }
    
    .dete {
        width: 20px;
        height: 20px;
        margin-left: 170px;
    }
    
    .nochoose {
        width: 100%;
        height: 100%;
        background-color: #FFF;
        color: #606266;
        text-align: center;
        line-height: 400px;
    }
    
    .choosef {
        width: 100%;
        height: 100%;
    }
    
    .choosef img {
        width: 200px;
        height: 230px;
    }
    
    .spanlist {
        margin-top: 20px;
        color: #909399;
        text-align: left;
    }
    
    .spanlist span {
        color: #303133;
    }
    
    td {
        width: 40%;
        height: 40px;
        margin-left: 20px;
    }
    
    .heng {
        color: #f45c5c;
        font-size: 16px;
        font-weight: 600;
    }
    
    .el-row {
        margin-bottom: 20px;
        &:last-child {
            margin-bottom: 0;
        }
    }
    
    .bg-purple-dark {
        background-color: #e5e6e741;
        color: #303133;
        font-weight: 100;
    }
    
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
        text-align: center;
    }
    
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>