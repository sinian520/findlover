<template>
    <div class="container">
        <div>
            <div class="block" @click="updatepage">
                <el-carousel height="311px">
                  <el-carousel-item v-for="item in img" :key="item.id">
                    <img :src="item.idView" class="banner_img"/>
                  </el-carousel-item>
                </el-carousel>
            </div>
            <div class="blockright">
                <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
                    <el-menu-item index="1"></el-menu-item>
                    <el-menu-item index="1"></el-menu-item>
                    <el-menu-item index="1">人气</el-menu-item>
                    <el-menu-item index="1"></el-menu-item>
                    <el-menu-item index="2"></el-menu-item>
                    <el-menu-item index="2">最新</el-menu-item>
                    <el-menu-item index="2"></el-menu-item>
                    <el-menu-item index="2"></el-menu-item>
                </el-menu>

                <el-table :data="tableData" style="width: 100%" :show-header="false" >
                    <el-table-column width="80">
                        <template slot-scope="scope">
                           <span style="margin-left: 10px; color: #f84747ee; font-style: italic; font-weight: 700;font-size:15px;"> Top{{ scope.row.pxid }}</span>
                        </template>
</el-table-column>
<el-table-column width="200">
    <template slot-scope="scope">
                            <div class="subject">{{ scope.row.table }}</div>
                        </template>
</el-table-column>
<el-table-column width="80">
    <template slot-scope="scope">
        <span style=" text-align: right; color: #859af5ee; font-style: italic; font-weight: 100;font-size:10px;">人气{{ scope.row.count }}</span>
    </template>
</el-table-column>
</el-table>


</div>
</div>

<div style="color:#fff; font-size:x-small">哈哈哈</div>

<el-row class="heng">
    <span class="span1">幸福时刻</span>
    <el-divider direction="vertical"></el-divider>
    <span class="small">与大家分享人生的幸福时刻</span>
</el-row>

<el-row>
    <!-- :key="o.id"会有重复 -->
    <el-col :span="8" v-for="(o, index) in threeshow" key="index" :offset="index > 0 ? 2 : 0">
        <el-card :body-style="{ padding: '0px'}">
            <div></div>
            <img :src="o.img" class="image">
            <div class="text">
                <span>{{o.table}}</span>
                <el-button type="text" class="button" icon="el-icon-collection-tag">{{o.count}}</el-button>
                <p>{{o.subject}}</p>
                <div class="bottom clearfix">
                    <el-button type="danger" round @click="send(o.id)">送祝福</el-button>
                    <span class="button">{{o.day}}</span>
                </div>
            </div>
        </el-card>
    </el-col>
</el-row>





</div>

</template>

<script>
    export default {
        data() {
            return {
                //轮播图
                img: [{
                        id: 0,
                        idView: require('../assets/img/1.jpg')
                    }, {
                        id: 1,
                        idView: require('../assets/img/2.png')
                    },


                ],
                //导航栏
                activeIndex: '1',

                //排名
                tableData: [],
                list: [],
                otherlist: [],
                //显示
                allshow: [],
                threeshow: [],

            };
        },
        created() {
            this.getShow()

        },
        methods: {
            async getShow() {
                const {
                    data: res
                } = await this.$http.post('Showlove/')
                if (res.code == 1002 || res.code == 1001)
                    return this.$maessage.error(res.msg)
                else {
                    this.list = JSON.parse(res.hot); //字符串转json的函数
                    this.otherlist = JSON.parse(res.new);
                    this.allshow = JSON.parse(res.allshow);
                }
                //前端显示
                this.tableData = this.list
                    //下方显示
                this.threeshow = [];
                for (var i = 0; i < 3; i++) {
                    this.threeshow.push(this.allshow[i]);
                    this.allshow.splice(0, 1);
                    this.allshow.push(this.threeshow[i])
                    console.log("id    " + this.threeshow[i])
                }
                // 时间控制函数
                window.setInterval(() => {
                    this.threeshow = [];
                    if (this.allshow) {
                        for (var i = 0; i < 3; i++) //遍历
                        {
                            this.threeshow.push(this.allshow[i]);
                            this.allshow.splice(0, 1);
                            this.allshow.push(this.threeshow[i])

                        }

                    }
                }, 10000);

            },
            //送祝福
            async send(id) {
                var param = new URLSearchParams();
                param.append('id', id);
                console.log("*************" + id)
                const {
                    data: res
                } = await this.$http.post('AddCount/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    //前端
                    this.$alert('感谢你的祝福,祝你也找到另一半哦！', {
                        confirmButtonText: '确定',
                    });
                    this.getShow()

                }



            },
            //上传恋爱展
            updatepage() {
                this.$router.push('/showupdate')
            },
            //导航栏
            handleSelect(key, keyPath) {
                console.log(key, keyPath);
                if (key == 1) {
                    this.tableData = this.list
                } else {
                    this.tableData = this.otherlist
                }
            }
        }
    }
</script>

<style lang="less" scoped>
    .container {
        width: 950px;
        margin-left: 150px;
    }
    
    .block {
        width: 58%;
        float: left;
        height: 311px;
        margin-top: 20px;
    }
    
    .banner_img {
        width: 100%;
        height: 100%;
    }
    
    .blockright {
        margin-top: 20px;
        width: 40%;
        float: left;
        height: 310px;
        margin-left: 10px;
        border: 1px solid #DCDFE6;
    }
    
    .subject {
        width: 200px;
        height: 25px;
        overflow: hidden;
        text-overflow: ellipsis;
        /*显示省略号 */
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
    /* 展示恩爱 */
    
    .el-col {
        width: 300px;
        margin-left: 10px;
        margin-top: 20px;
    }
    
    .bottom {
        margin-top: 13px;
        line-height: 12px;
    }
    
    .button {
        padding: 0;
        float: right;
        color: #f56c6c
    }
    
    .image {
        width: 100%;
        height: 200px;
        display: block;
    }
    
    .text {
        padding: 14px;
    }
    
    p {
        width: 240px;
        height: 200px;
        overflow: hidden;
        text-overflow: ellipsis;
        margin-left: 20px;
        /*显示省略号 */
    }
    
    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }
    
    .clearfix:after {
        clear: both
    }
</style>