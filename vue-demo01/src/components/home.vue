<template>
    <div class="home_container">
        <!-- 轮播图 -->
        <div class="block">
            <el-carousel :height="imgHeight+'px'">
              <el-carousel-item v-for="item in img" :key="item.id">
                <img ref="imgHeight" :src="item.idView" class="banner_img"/>      
              </el-carousel-item>
            </el-carousel>
        </div>



        <!-- 优质推荐  -->
        <div class="people">
            <div class="title">
                <span class="span1">优质会员</span>
                <el-divider direction="vertical"></el-divider>
                <span class="small">优先推荐可靠度更高更值得信赖</span>
                <el-button style="float: right; padding: 7px 15px;color:#fff" type="text" @click="vipchange">换一批>></el-button>
            </div>
            <div id="box">
                    <ul>
                        <li v-for="v in vipusershow"  :key="v.id">
                            <img :src="v.photo" alt="">
                            <span>{{v.age}}</span>
                            <span>{{v.marriage}}</span>
                            <el-button type="danger" size="mini" style="margin-left: 10px;" @click="friend(v.id)">加朋友</el-button>
                        </li>
                    </ul>
            </div>
            <div class="title">
                <span class="span1">找呀找呀找朋友</span>
                <el-divider direction="vertical"></el-divider>
                <span class="small">诚挚帮助寻找符合心意的他/她</span>
                <el-button style="float: right; padding: 7px 15px;color:#fff" type="text">更多>></el-button>
            </div>
            <div id="box1">
                <div class="find">
                    <span style="color: #333;">我要找：</span>
                    
                    <el-select v-model="age" placeholder="年龄范围--不限--">
                        <el-option
                          v-for="item in ageoptions"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value">
                        </el-option>
                    </el-select>
                    <el-cascader
                    v-model="located"
                    :options="options"
                    @change="handleChange"
                    style="width: 300px;"
                    placeholder="地域--不限--"
                    ></el-cascader>
                    <el-select v-model="character" placeholder="性格--不限--">
                        <el-option
                          v-for="item in coptions"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value">
                        </el-option>
                    </el-select>
                    <el-button type="danger" icon="el-icon-search" plain  @click="userfilter">搜索</el-button>
                </div>
                <el-divider></el-divider>                  
                <ul>
                    <li v-for="v in allusershow"  :key="v.id">
                        <img :src="v.photo" alt="用户照片">
                        <div class="subject">{{v.age}}岁,{{v.live}},{{v.marriage}},{{v.profession}}<br>{{v.education}},
                            {{v.charater}}
                        </div>   
                        <el-button type="danger" style="margin-left: 10px;" size="mini" @click="friend(v.id)">加朋友</el-button>
                        <el-button type="danger" size="mini"  @click="send(v.id)">送玫瑰</el-button>
                    </li>
                </ul>
            </div>
           
        </div>
       
    </div>

</template>

<script>
    export default {
        data() {
            return {
                //轮播图
                img: [{
                        id: 0,
                        idView: require('../assets/img/banner-vip-list.jpg')

                    }, {
                        id: 1,
                        idView: require('../assets/img/long1.jpg')
                    }, {
                        id: 2,
                        idView: require('../assets/img/long4.jpg')
                    }, {
                        id: 3,
                        idView: require('../assets/img/true.jpg')
                    }

                ],
                imgHeight: "350",
                //选择框
                age: "",
                ageoptions: [{
                    value: '18~25',
                    label: '18~25岁'
                }, {
                    value: '25~30',
                    label: '25~30岁'
                }, {
                    value: '30~35',
                    label: '30~35岁'
                }, {
                    value: '35~40',
                    label: '35~40岁'
                }, {
                    value: '40~45',
                    label: '40~45岁'
                }, {
                    value: '45~50',
                    label: '45~50岁'
                }, {
                    value: '50~200',
                    label: '50岁以上'
                }],
                located: "",
                // 所在地
                options: [{
                    value: '黑龙江',
                    label: '黑龙江',
                    children: [{
                        value: '哈尔滨',
                        label: '哈尔滨',
                    }, {
                        value: '齐齐哈尔',
                        label: '齐齐哈尔'
                    }, {
                        value: '鸡西',
                        label: '鸡西'
                    }, {
                        value: '鹤岗',
                        label: '鹤岗'
                    }, {
                        value: '双鸭山',
                        label: '双鸭山'
                    }, {
                        value: '大庆',
                        label: '大庆'
                    }, {
                        value: '伊春',
                        label: '伊春'
                    }, {
                        value: '佳木斯',
                        label: '佳木斯'
                    }, {
                        value: '七台河',
                        label: '七台河'
                    }, {
                        value: '牡丹江',
                        label: '牡丹江'
                    }]
                }, {
                    value: '河南',
                    label: '河南',
                }, {
                    value: '吉林',
                    label: '吉林',
                }, {
                    value: '辽宁',
                    label: '辽宁',
                }, {
                    value: '江苏',
                    label: '江苏',
                }, {
                    value: '江西',
                    label: '江西',
                }],
                character: "",
                coptions: [{
                    value: '帅气',
                    label: '帅气'
                }, {
                    value: '酷',
                    label: '酷'
                }, {
                    value: '阳光',
                    label: '阳光'
                }, {
                    value: '温柔',
                    label: '温柔'
                }, {
                    value: '有才气',
                    label: '有才气'
                }, {
                    value: '自由',
                    label: '自由'
                }, {
                    value: '性感',
                    label: '性感'
                }, {
                    value: '浪漫',
                    label: '浪漫'
                }, {
                    value: '靠谱',
                    label: '靠谱'
                }],
                //后台用户
                alluser: [],
                vipuser: [],
                // 显示用户
                allusershow: [],
                vipusershow: [],
                //登录用户
                myuser: '',
            };
        },
        created() {
            this.getPersonal()
        },
        methods: {
            // 所在地
            handleChange(value) {
                this.located = value;
            },
            //vip换一批
            vipchange() {
                var arr = this.vipuser;

                var result = [];

                var ranNum = 10;

                for (var i = 0; i < ranNum; i++) {

                    var ran = Math.floor(Math.random() * (arr.length - i));

                    result.push(arr[ran]);

                    arr[ran] = arr[arr.length - i - 1];

                };
                this.vipusershow = result;
                console.log(this.vipusershow);
            },
            async getPersonal() {
                var user = window.sessionStorage.getItem("user");
                let param = new URLSearchParams()
                this.myuser = user
                param.append('user', user)
                console.log(user);
                const {
                    data: res
                } = await this.$http.post('HomeUser/', param)
                if (res.code == 1002)
                    return this.$message.error(res.msg)

                this.vipuser = JSON.parse(res.vip);
                this.alluser = JSON.parse(res.ordinary);
                if (this.vipuser.length == 0) {
                    this.$message.info("暂无会员用户")
                }
                if (this.alluser.length == 0) {
                    this.$message.info("暂无用户")
                }
                console.log(this.vipuser);
                console.log(this.alluser);
                // 显示会员
                if (this.vipuser.length > 10)
                    this.vipusershow = this.vipuser.slice(0, 10)
                else
                    this.vipusershow = this.vipuser
                    // 显用户
                if (this.alluser.length > 10)
                    this.allusershow = this.alluser.slice(0, 10)
                else
                    this.allusershow = this.alluser
            },
            // 添加朋友
            async friend(id) {
                var param = new URLSearchParams();
                param.append('userid', this.myuser);
                param.append('friendid', id);
                const {
                    data: res
                } = await this.$http.post('AddFriend/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    this.$message.success(res.msg)
                }
            },
            // 送玫瑰
            async send(id) {
                var param = new URLSearchParams();
                param.append('id', id);
                const {
                    data: res
                } = await this.$http.post('AddUserCount/', param)
                if (res.code == 1002 || res.code == 1001)
                    return this.$message.error(res.msg)
                else {
                    //前端
                    this.$alert('已帮你送去玫瑰表达你的喜爱之情！', {
                        confirmButtonText: '确定',
                    });

                }

            },
            //查询
            userfilter() {
                console.log(this.alluser)
                console.log(this.located)
                console.log(this.character)
                console.log(this.age)
                var low = this.age.split("~")[0]
                var height = this.age.split("~")[1]


                let a = this.alluser.filter((obj, index) => {
                    //查找包含关键字的
                    if (this.age && this.character && this.located) {
                        return obj.age >= low && obj.age <= height && obj.character.includes(this.character) && obj.live.includes(this.located)
                    } else if (this.age && this.character) {
                        return obj.age >= low && obj.age <= height && obj.character.includes(this.character)
                    } else if (this.character && this.located) {
                        return obj.character.includes(this.character) && obj.live.includes(this.located)
                    } else if (this.age && this.located) {
                        return obj.age >= low && obj.age <= height && obj.live.includes(this.located)
                    } else if (this.age) {
                        return obj.age >= low && obj.age <= height
                    } else if (this.character) {
                        return obj.character.includes(this.character)
                    } else if (this.located) {
                        return obj.live.includes(this.located)
                    } else
                        return;
                })

                this.allusershow = a;
                if (this.allusershow.length == 0) {
                    this.allusershow = this.newactive
                    this.$message.info("没有找到符合条件的活动")
                }
            },
        }
    }
</script>

<style lang="less" scoped>
    .home_container {
        width: 1220px;
    }
    
    .banner_img {
        width: 100%;
        height: 350px;
    }
    
    .people {
        width: 1120px;
        margin-left: 50px;
    }
    
    .clearfix {
        border: #960404 solid 1px;
    }
    
    .title {
        width: 100%;
        height: 50px;
        color: #fff;
        background-color: #960404;
        margin-top: 20px;
        padding-top: 10px;
        box-sizing: border-box;
    }
    
    .span1 {
        font-weight: 500;
        font-size: 20px;
        margin-left: 30px;
    }
    
    .small {
        font-weight: 100;
        font-size: 10px;
        margin-left: 0px;
    }
    /* 显示图片 */
    
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
        height: 230px;
    }
    
    #box img {
        width: 180px;
        height: 190px;
    }
    
    #box span {
        margin-left: 10px;
    }
    
    #box1 ul {
        display: flex;
        flex-wrap: wrap;
        margin-left: 0px;
    }
    
    #box1 li {
        list-style: none;
        border: 1px solid #eee;
        margin-left: 20px;
        margin-top: 15px;
        width: 180px;
        height: 300px;
    }
    
    #box1 img {
        width: 180px;
        height: 200px;
    }
    
    .find {
        display: block;
        margin-left: 80px;
        margin-top: 20px;
    }
    
    .subject {
        font-size: 14px;
        padding: 10px;
        width: 170px;
        height: 30px;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        /*强制不换行*/
        /*显示省略号 */
    }
</style>