<template>
    <div class="container">
        <div class="show">
            <el-card shadow="never" v-for="(item,index) in totaldata" :key="index" body-style="padding:0px; background-color: #eeeeee;">
                <el-col :span="6" class="author">
                    <img :src="item.photo" alt="用户照片">
                    <div class="author_show">
                        <p>{{item.name}}</p> 
                        <p>{{item.type}}</p>  
                    </div>
                </el-col>
                <el-col :span="18" class="text">
                    <div >
                        <p class="">{{item.title}}</p> 
                        <pre>{{item.text}}</pre>  
                        <!-- <img src="//images.baihe.com/images/baihe_new/images/default_pictures/100_100/nopic_female.gif" alt=""> -->
                        <div class="time">
                            <span>{{item.time}}</span>
                            
                            <el-popover placement="right" width="400" trigger="click">
        
                                 <el-input type="textarea" placeholder="回复" :autosize="{ minRows: 4, maxRows: 4}" v-model="reponse"></el-input>
                                 <div style="text-align: right; margin: 10px">
                                     <el-button type="danger" plain size="mini"  @click="postreponse(item.id)">确定</el-button>
                                 </div>
                                 <el-button  slot="reference" style="color:blue" type="text">回复</el-button>
                             </el-popover>
                            
                        </div>
                        <el-collapse accordion>
                            <el-collapse-item>
                              <template slot="title">
                                <el-button type="text"  @click=getreponse(item.id)>查看用户回复</el-button >
                                
                              </template>
<div v-for="o in reponseshow" :key="o.id" class="textdiv">
    <el-row>
        <el-col :span="2">
            <img :src="o.photo" alt="" class="img">
        </el-col>
        <el-col :span="22">
            <span>{{o.name}}:</span>{{o.Text}}
            <div class="time">
                <span>{{o.time}}</span>
            </div>
        </el-col>
    </el-row>

</div>

</el-collapse-item>
</el-collapse>
</div>


</el-col>
</el-card>


</div>

<!-- 分页显示 -->
<div class="pagination">
    <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage" :page-sizes="[5, 10, 20, 40]" :page-size="pagesize" layout="total, sizes, prev, pager, next, jumper" :total="userList.length">
    </el-pagination>
</div>
<!-- 发补贴子 -->
<div class="back">
    <el-card class="box-card">
        <p>发表帖子</p>
        <el-input v-model="title" placeholder="标题"></el-input>
        <el-input type="textarea" placeholder="让表达与分享带走你的悲伤" :autosize="{ minRows: 10, maxRows: 10}" v-model="desc"></el-input>
        <el-button type="danger" @click="subject" style=" margin-top: 10px;">立即发布</el-button>
        <!-- <el-col :span="12"></el-col> -->
    </el-card>
</div>
</div>

</template>

<script>
    export default {
        data() {
            return {
                //发布帖子
                title: '',
                desc: '',
                //回复
                reponse: '',
                reponseshow: '',
                //分页
                currentPage: 1, //初始页
                pagesize: 5, //    每页的数据
                userList: [], //复制20条一样的item数据
            };
        },
        created() {
            this.getShow();
        },
        computed: {
            totaldata: function() {
                console.log(this.pagesize)
                return this.userList.slice((this.currentPage - 1) * this.pagesize, this.currentPage * this.pagesize);
            }
        },

        methods: {
            //分页
            handleSizeChange(val) {
                this.pagesize = val
                console.log(`每页 ${val} 条`);
            },
            handleCurrentChange(val) {
                this.currentPage = val;
                console.log(`当前页${val} `);
            },
            //显示帖子
            async getShow() {
                const {
                    data: res
                } = await this.$http.post('AskHelp/')
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    this.userList = JSON.parse(res.askList); //字符串转json的函数
                }
                if (this.userList.photo == "") {
                    this.userList.photo == "//images.baihe.com/images/baihe_new/images/default_pictures/100_100/nopic_female.gif"
                }

                //前端显示
                console.log(this.userList);

            },
            //显示回复
            async getreponse(id) {
                let param = new FormData();
                console.log(id);
                param.append('id', id)
                const {
                    data: res
                } = await this.$http.post('Reponseshow/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    this.reponseshow = JSON.parse(res.comment); //字符串转json的函数
                }
                console.log(this.reponseshow);
                if (this.reponseshow) {
                    for (var i in this.reponseshow) {
                        if (i.photo == "") {
                            i.photo == "//images.baihe.com/images/baihe_new/images/default_pictures/100_100/nopic_female.gif"
                        }
                    }
                } else {
                    this.$message.info("还没有回复")
                }
                this.getShow()

            },
            //发布贴子
            async subject() {
                var user = window.sessionStorage.getItem("user");
                let param = new FormData(); //上传图片
                // this.$refs.upload.submit() // 这里是执行文件上传的函数，其实也就是获取我们要上传的文件
                param.append('user', user)
                param.append('title', this.title)
                param.append('desc', this.desc)
                const {
                    data: res
                } = await this.$http.post('PostHelp/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    this.$message.success(res.msg)
                }

            },
            //回复
            async postreponse(id) {
                var user = window.sessionStorage.getItem("user");
                let param = new FormData(); //上传图片
                // this.$refs.upload.submit() // 这里是执行文件上传的函数，其实也就是获取我们要上传的文件
                param.append('user', user)
                param.append('dyID', id)
                param.append('reponse', this.reponse)
                const {
                    data: res
                } = await this.$http.post('PostReponse/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    this.$message.info(res.msg)
                }
                this.getreponse(id);
                this.reponse = ""

            },

        },

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
    
    .back {
        background-color: #E4E7ED;
        text-align: center;
        width: 100%;
        height: 450px;
        padding: 40px;
        box-sizing: border-box;
    }
    
    .box-card {
        width: 90%;
        margin-left: 40px;
    }
    
    .show {
        position: static;
        border-left: 1px solid #E5E5E5;
        border-bottom: 1px solid #E1E4E6;
        width: 100%;
    }
    
    .author {
        text-align: center;
        line-height: 20px;
        background-color: #eeeeee;
        height: 100%;
    }
    
    .author img {
        margin-top: 20px;
        width: 110px;
        height: 120px;
        border: 2px solid #fff;
    }
    
    .author_show {
        text-align: center;
        line-height: 15px;
    }
    
    .text {
        box-sizing: border-box;
        padding: 20px;
        background-color: #fff;
    }
    
    .pagination {
        text-align: center;
    }
    
    .box-card {
        width: 100%;
    }
    
    .time {
        text-align: right;
        color: #606266;
        font-size: 14px;
    }
    /* 保持输入框格式不变 */
    
    pre {
        white-space: pre-wrap;
        /*css-3*/
        white-space: -moz-pre-wrap;
        /*Mozilla,since1999*/
        white-space: -pre-wrap;
        /*Opera4-6*/
        white-space: -o-pre-wrap;
        /*Opera7*/
        word-wrap: break-word;
        /*InternetExplorer5.5+*/
        line-height: 20px;
    }
    
    .textddiv {
        width: 100%;
        text-align: left;
    }
    
    .img {
        width: 50px;
        height: 50px;
        display: inline;
    }
</style>