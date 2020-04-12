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
                <el-button style="float: right; padding: 7px 15px;color:#fff" type="text">换一批>></el-button>
            </div>
            <div id="box">
                    <ul>
                        <li v-for="v in 10">
                            <img src="" alt="">
                            <h4></h4>
                            <el-button type="danger" size="mini">危险按钮</el-button>
                            <el-button type="danger" size="mini">危险按钮</el-button>
                        </li>
                    </ul>
            </div>
            <div class="title">
                <span class="span1">找呀找呀找朋友</span>
                <el-divider direction="vertical"></el-divider>
                <span class="small">诚挚帮助寻找符合心意的他/她</span>
                <el-button style="float: right; padding: 7px 15px;color:#fff" type="text">更多>></el-button>
            </div>
            <div id="box">
                <div class="find">
                    <span style="color: #333;">我要找：</span>
                    
                    <el-select v-model="age" placeholder="年龄范围">
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
                    placeholder="地域"
                    ></el-cascader>
                    <el-select v-model="character" placeholder="性格">
                        <el-option
                          v-for="item in coptions"
                          :key="item.value"
                          :label="item.label"
                          :value="item.value">
                        </el-option>
                    </el-select>
                    <el-button type="danger" icon="el-icon-search" plain>搜索</el-button>
                </div>
                <el-divider></el-divider>                  
                <ul>
                    <li v-for="v in 10">
                        <img src="" alt="">
                        <h4></h4>
                        <el-button type="danger" size="mini">加朋友</el-button>
                        <el-button type="danger" size="mini">送玫瑰</el-button>
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
                        idView: require('../assets/img/1.jpg')
                    }, {
                        id: 1,
                        idView: require('../assets/img/2.png')
                    }, {
                        id: 2,
                        idView: require('../assets/img/banner-vip-list.jpg')
                    }, {
                        id: 3,
                        idView: require('../assets/img/home1.jpg')
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
                    value: '40-45',
                    label: '40-45岁'
                }, {
                    value: '45-50',
                    label: '45~50岁'
                }, {
                    value: '50-200',
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
            };
        },
        created() {},
        methods: {
            handleChange(value) {
                this.located = value;
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
        border: #960404 solid 1px;
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
        padding: 15px;
        list-style: none;
        border: 1px solid #eee;
        margin-left: 20px;
        margin-top: 15px;
        width: 150px;
        height: 200px;
    }
    
    #box img {
        width: 150px;
        height: 170px;
    }
    
    .find {
        display: block;
        margin-left: 80px;
        margin-top: 20px;
    }
</style>