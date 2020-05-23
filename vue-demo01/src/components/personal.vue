<template>
    <div class="container">
        <el-container>
            <el-aside width="300px"></el-aside>
            <el-main>
                <el-row>
                    <el-col :span="12"><div class="grid-content bg-purple">
                        我的资料
                    </div></el-col>
                    <el-col :span="12">
                        <div class="grid-content bg-purple-light">
                            <span>资料完整度</span>
                            <div class="progress">
                            <el-progress :percentage="percentage" :color='customColor':stroke-width="10"></el-progress>
                            </div>
                        </div>
                    </el-col>
                </el-row>
<!-- 填写信息提示 -->
            <div class="info">完整的基本资料不仅能让异性初步的了解你，更能让异性搜索到你的重要保证</div>
            
            <el-tabs v-model="activeName" type="card" @tab-click="handleClick" >
                <el-tab-pane label="基本信息" name="first">
                    <el-form ref="form" :model="form" label-width="80px">
                            <!-- <div class='left'> -->
                                <el-form-item label="昵称:">
                                    <el-input v-model="form.name"></el-input>
                                </el-form-item>
                                <el-form-item label="性别:" >
                                    <el-input :disabled="true" v-model="form.sex""></el-input>
                                </el-form-item>
                                <el-form-item label="年龄:" prop="age">
                                    <el-input  v-model="form.age"></el-input>
                                </el-form-item>
                                <el-form-item label="婚姻状况:">
                                    <el-input  v-model="form.marry"></el-input>
                                </el-form-item>
                                <el-form-item label="生日:">
                                    <el-input v-model="form.date" :disabled="true"></el-input>
                                </el-form-item>
                                <el-form-item label="所在地:">
                                    <el-input v-model="form.located""></el-input>
                                </el-form-item>
                                <el-form-item label="身高(cm):">
                                    <el-input v-model="form.height""></el-input>
                                </el-form-item>
                                <el-form-item label="体重(kg):">
                                    <el-input v-model="form.weight"></el-input>
                                </el-form-item>
                                
                               
                            <!-- </div> -->
                            <!-- <div class='left'> -->
                                <el-form-item label="邮箱:">
                                    <el-input v-model="form.email" :disabled="true"></el-input>
                                </el-form-item>
                                <el-form-item label="电话:">
                                    <el-input  v-model="form.phone"></el-input>
                                </el-form-item>
                                <el-form-item label="学历:">
                                    <el-input v-model="form.education""></el-input>
                                </el-form-item>
                                
                                <el-form-item label="职业:">
                                    <el-input v-model="form.work""></el-input>
                                </el-form-item>
                                <el-form-item label="月薪(元):">
                                  <el-input  v-model="form.money"></el-input>
                                </el-form-item>
                               
                                <el-form-item label="微信:">
                                    <el-input v-model="form.wchat"></el-input>
                                </el-form-item>
                                <el-form-item >
                                    <i>* 深色输入框信息不可更改，若有需要请联系17545866339</i>
                                </el-form-item>
                                
                            <!-- </div> -->
                            
                            <el-form-item class="save">
                                <el-button type="danger" @click="submit1">保存信息</el-button>
                            </el-form-item>
                        </el-form>
                </el-tab-pane>
                <el-tab-pane label="上传照片" name="second">
                    <div class="photo">
                        <!-- action表示照片要上传的后台api地址 list-type上传的ui效果  :data额外提交的参数-->
                        <el-upload :on-preview="handlePreview" :on-remove="handleRemove" :on-success="handleSuccess"
                        :on-error="handleError"class="upload-demo" :headers="headertoken" :file-list="photo"
                        drag action="http://127.0.0.1:8000/UploadPersonal/" :before-upload="BeforeUpload"
                        list-type="picture" multiple auto-upload name="photo" :data={data:this.form.email}>
                            <i class="el-icon-upload"></i>
                            <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                            <div class="el-upload__tip" slot="tip">只能上传jpg/png文件，且不超过500kb,最后一次上传图片为头像</div>
                        </el-upload>
                        <div class="photoright">
                            <img src="../assets/img/头像示范.png" alt="示范图片">
                        </div>
                    </div>
                </el-tab-pane>
                <el-tab-pane label="自我介绍" name="third">
                    <div >
                        <span class="i"> 给自己选择几个有代表的标签吧</span>
                       
                        <el-tag v-for="tag in tags" :key="tag.name"  :type="tag.type" @click="handlemove(tag)">
                         {{tag.name}}
                        </el-tag>
                        <el-card class="box-card">
                            <div v-if="tagchecks!=null" class="carddiv">
                                <el-tag v-for="tag in tagchecks" :key="tag.name" closable :type="tag.type" :disable-transitions="false"
                                     @close="handleClose(tag)">
                                {{tag.name}}
                                </el-tag>       
                            </div>
                            <el-form ref="form" label-width="80px">
                                <el-form-item label="个人介绍:">
                                    <el-input type="textarea" :autosize="{ minRows: 4, maxRows: 6}" v-model="personal" placeholder="听说你上得了厅堂，下得了厨房，杀得了木马，翻得了围墙，但是为什么没有人知道呢？快写下你的优秀，让TA看到吧!"></el-input>
                                    <i>*最多可输入500字</i>
                                </el-form-item>

                                <el-form-item class="save">
                                    <el-button type="danger" @click="submit2">保存信息</el-button>
                                </el-form-item>
                            </el-form>
                        </el-card> 
                    </div>
                </el-tab-pane>
            </el-tabs>
        
            

                
            </el-main>
        </el-container>
    </div>
  </template>

<script>
    export default {
        data() {

            //年龄验证规则
            var checkAge = (rule, value, callback) => {
                setTimeout(() => {
                    if (!Number.isInteger(value)) {
                        callback(new Error('请输入数字值'));
                    } else {
                        if (value < 18) {
                            callback(new Error('必须年满18岁'));
                        } else {
                            callback();
                        }
                    }
                }, 1000);
            };
            return {
                form: {
                    name: '',
                    sex: '',
                    education: '',
                    located: '',
                    date: '',
                    money: '',
                    age: '',
                    work: '',
                    marry: '',
                    email: '',
                    phone: '',
                    wchat: '',
                    height: '',
                    weight: '',
                },
                // 个人信息
                personal: '',
                //头像
                photo: [{
                    name: '',
                    url: ''
                }],
                rules: {
                    age: [{
                        validator: checkAge,
                        trigger: 'blur'
                    }]
                },
                // 标签页
                activeName: 'first',
                // 进度条
                percentage: 0,

                customColor: '#f56c6c',
                tags: [{
                    name: '阳光',
                    type: ''
                }, {
                    name: '幽默',
                    type: 'success'
                }, {
                    name: '宅',
                    type: 'info'
                }, {
                    name: '善良',
                    type: 'warning'
                }, {
                    name: '温柔',
                    type: 'danger'
                }, {
                    name: '孝顺',
                    type: 'warning'
                }, {
                    name: '开朗',
                    type: ''
                }, {
                    name: '性感',
                    type: 'success'
                }, {
                    name: '可爱',
                    type: 'info'
                }, {
                    name: '顾家',
                    type: 'warning'
                }, {
                    name: '浪漫',
                    type: 'warning'
                }, {
                    name: '酷',
                    type: 'warning'
                }, {
                    name: '帅气',
                    type: 'info'
                }, {
                    name: '热情',
                    type: 'warning'
                }, {
                    name: '包容',
                    type: 'warning'
                }, {
                    name: '靠谱',
                    type: 'warning'
                }, ],
                tagchecks: [],
                //上传图片添加token
                headertoken: {
                    // Authorization: window.sessionStorage.getItem("tokens")
                },

            }
        },

        created() {
            this.getPersonal();
            this.handleClick();
        },

        methods: {
            // 获取个人信息
            async getPersonal() {
                var user = window.sessionStorage.getItem("user");
                let param = new URLSearchParams()
                param.append('user', user)
                console.log(user);
                const {
                    data: res
                } = await this.$http.post('Personal/', param)
                if (res.code == 1002)
                    return this.$maessage.error(res.msg)

                console.log(res);
                this.form.name = res.name;
                this.form.sex = res.sex;
                this.form.located = res.live;
                this.form.date = res.birthday;
                this.form.marry = res.marriage;
                this.form.email = res.emile;
                this.form.phone = res.tele;
                this.form.education = res.education;
                this.form.money = res.money;
                this.form.age = res.age;
                this.form.work = res.work;
                this.form.wchat = res.wchat;
                this.personal = res.personal;
                this.form.height = res.height;
                this.form.weight = res.weight;
                this.photo[0].url = res.photo;
                this.photo[0].name = "用户头像";
                //进度条显示
                for (let obj in this.form) {
                    if (this.form[obj]) {
                        this.percentage += 5;
                        console.log(obj);
                    }
                    console.log(obj, "--", this.form[obj]);
                }
                if (this.photo[0].url) this.percentage += 15;
                if (this.personal) {
                    this.percentage += 15;
                }


            },
            async submit1() {
                console.log(this.form.email);
                var param = new URLSearchParams();
                param.append('personal', this.personal);
                param.append('email', this.form.email);
                param.append('name', this.form.name);
                param.append('live', this.form.located);
                param.append('tele', this.form.phone);
                param.append('marriage', this.form.marry);
                param.append('education', this.form.email);
                param.append('money', this.form.money);
                param.append('age', this.form.age);
                param.append('work', this.form.work);
                param.append('wchat', this.form.wchat);
                param.append('height', this.form.height);
                param.append('weight', this.form.weight);



                const {
                    data: res
                } = await this.$http.post('ChangePersonal/', param);
                console.log(res)
                if (res.code == "1001" || res.code == "1002") {
                    return this.$message.error(res.msg);
                } else {
                    this.$message.success("个人信息修改成功");
                }
            },
            async submit2() {
                console.log(this.form.email);
                //个人标签
                var tag = "/";
                for (var i = 0; i < this.tagchecks.length; i++) {
                    tag = tag + this.tagchecks[i].name + "/";
                }
                this.personal = this.personal + "/" + tag;
                var param = new URLSearchParams();
                param.append('personal', this.personal);
                param.append('email', this.form.email);
                param.append('photo', this.photo);
                const {
                    data: res
                } = await this.$http.post('Change2Personal/', param);
                console.log(res)
                if (res.code == "1001" || res.code == "1002") {
                    return this.$message.error(res.msg);
                } else {
                    this.$message.success("保存成功");
                }
            },
            // 进度条
            format(percentage) {
                return percentage === 100 ? '满' : `${percentage}%`;
            },
            // 上传照片
            handleSuccess(response, file, fileList) {
                console.log(response);
                console.log(file);
                console.log(fileList);
                this.$message.success("上传成功");
            },
            handleError() {
                this.$message.error("上传失败,请重新上传图片!");
            },
            handleRemove(file, fileList) {
                console.log(file, fileList);
            },
            // 处理图片预览效果
            handlePreview(file) {
                console.log(file);
            },
            BeforeUpload(file) {
                console.log(file);
            },
            beforeRemove(file, fileList) {
                return this.$confirm(`确定移除 ${ file.name }？`);
            },

            // 标签页
            handleClick(tab, event) {
                console.log(tab, event);
            },

            //tag性格标签
            handlemove(tag) {
                console.log(tag);
                this.tagchecks.push(tag);
                this.tags.splice(this.tags.indexOf(tag), 1);
            },
            handleClose(tag) {
                this.tags.push(tag);
                this.tagchecks.splice(this.tagchecks.indexOf(tag), 1);
            },

        }
    }
</script>

<style lang="less" scoped>
    .container {
        width: 1220px;
    }
    
    .el-aside {
        background-color: #D3DCE6;
        padding-left: 150px;
    }
    
    .el-main {
        padding-right: 150px;
    }
    /* main布局我的资料和进度条 */
    
    .bg-purple {
        font-size: 20px;
        font-weight: 500;
        margin-left: 50px;
    }
    
    .bg-purple-light span {
        color: #bbbbbb;
        font-size: 14px;
        margin-top: 5px;
        margin-left: 40px;
    }
    
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
    
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
    
    .progress {
        float: right;
        width: 250px;
        color: #eef115;
        margin-top: 3px;
    }
    
    .info {
        width: 650px;
        height: 30px;
        background-color: #f84747ee;
        color: #fff;
        margin-top: 20px;
        font-size: 16px;
        padding-left: 100px;
        padding-top: 13px;
    }
    
    .el-tabs {
        margin-top: 30px;
    }
    
    .left {
        float: left;
        width: 50%;
        height: 500px;
    }
    
    .upload-demo {
        width: 490px;
        float: left;
    }
    
    .photoright {
        float: left;
    }
    
    .save {
        margin-left: 300px;
    }
    
    .el-form-item {
        margin-top: 20px;
    }
    
    .photo {
        width: 750px;
        height: 350px;
    }
    
    .i {
        color: hotpink;
        font-size: small;
    }
    
    .carddiv {
        width: 100%;
        height: 70px;
        background-color: #f7f7f7;
        padding-top: 5px;
    }
    
    .el-tag {
        margin-left: 10px;
    }
</style>