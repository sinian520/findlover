<template>

  <el-container>
    <el-header class="top_img" style="height: 90px;"><img src="//images.jiayuan.com/w4/wap/i/gift/ximg/20200115/1579079608383.png" alt="顶部图片"></el-header>
    <el-container>
      <el-aside class="side_img"><img src="" alt="侧面图片"></el-aside>
      <el-main class="main">
        <el-card class="box-card">
          <el-form :label-position="right" :model="form" :rules="rules"  ref="form" label-width="100px">
            <!-- 昵称 -->
            <el-form-item label="称呼:" prop="username">
                <el-tooltip class="item" effect="light" content="为自己起个好听的名字吧" placement="bottom-start">
                    <el-input v-model="form.username"  class="form"></el-input>
                </el-tooltip>
            </el-form-item>
            <el-form-item label="电话:" prop="phone">
              <el-input v-model.number="form.phone" class="form"></el-input>
            </el-form-item>
            <!-- <el-form-item label="微信：" prop="phone">
              <el-input v-model="tele"></el-input>
            </el-form-item> -->
            <el-form-item label="密码:" prop="password">
                <el-tooltip class="item" effect="light" content="密码为6位字符" placement="bottom-start">
                    <el-input  class="form" type="password" v-model="form.password" autocomplete="off"></el-input>
                </el-tooltip>
            </el-form-item>
            <el-form-item label="确认密码:" prop="checkPass">
                <el-input  class="form" type="password" v-model="form.checkPass" autocomplete="off"></el-input>
            </el-form-item>

              <!-- 生日 -->
              <el-form-item label="出生日期:" prop="">
                  <el-date-picker
                    v-model="form.value1"
                    type="date"
                    placeholder="选择日期">
                  </el-date-picker>
              </el-form-item>

             <!-- 性别 -->
             <el-form-item label="我是:">
                <el-radio v-model="form.radio" label="男">男</el-radio>
                <el-radio v-model="form.radio" label="女">女</el-radio>
            </el-form-item>

            <!-- 所在地 -->
            <el-form-item label="所在地:">
                <el-cascader
                v-model="form.value"
                :options="options"
                @change="handleChange"
                style="width: 300px;"
                ></el-cascader>
            </el-form-item>
            
            <!-- 婚配情况 -->
            <el-form-item label="婚姻情况:" class="">
                <el-radio v-model="form.radiotype" label="未婚">未婚</el-radio>
                <el-radio v-model="form.radiotype" label="离异">未婚</el-radio>
                <el-radio v-model="form.radiotype" label="丧偶">未婚</el-radio>
            </el-form-item>


            <el-form-item label="邮箱:" prop="email">
                <el-input v-model="form.email" class="form" type="email"></el-input>
                <el-button type="primary" plain   @click="check">发送验证信息</el-button>
            </el-form-item>
            <el-form-item label="验证信息:" prop="info">
                <el-input v-model="form.info"  class="form"></el-input>
            </el-form-item>
            <el-form-item class="btns">
                <el-button type="primary" @click="submit">用户注册</el-button>
                <el-button type="info" @click="goLogin">返回登录</el-button>
            </el-form-item>
          </el-form>
        </el-card>

      </el-main>
    </el-container>
  </el-container>

</template>

<script>
    export default {
        data() {
            var validatephone = (rule, value, callback) => {
                if (!value) {
                    return new Error("请输入电话号码");
                } else {
                    const reg = /^1[3|4|5|7|8][0-9]\d{8}$/;
                    const isPhone = reg.test(value);
                    value = Number(value); //转换为数字
                    if (typeof value === "number" && !isNaN(value)) { //判断是否为数字
                        value = value.toString(); //转换成字符串
                        if (value.length < 0 || value.length > 12 || !isPhone) { //判断是否为11位手机号
                            callback(new Error("手机号码格式如:138xxxx8754"));
                        } else {
                            callback();
                        }
                    } else {
                        callback(new Error("请输入电话号码"));
                    }
                }
            };
            var validateemail = (rule, value, callback) => {
                if (!value) {
                    callback();
                } else {
                    const reg = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;
                    const email = reg.test(value);
                    if (!email) {
                        callback(new Error("邮箱格式如:admin@163.com"));
                    } else {
                        callback();
                    }
                }
            };
            var validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                    if (this.form.checkPass !== '') {
                        // 执行校验绑定字符串checkPass的条目
                        this.$refs.form.validateField('checkPass');
                    }
                    callback();
                }
            };
            var validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.form.password) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return {
                form: {
                    username: '',
                    phone: '',
                    email: '',
                    info: '',
                    password: '',
                    checkPass: '',
                    radio: '男',
                    // 出生日期
                    value1: '',
                    // 所在地
                    value: [],
                    radiotype: '未婚',
                },
                rules: {
                    username: [{
                        required: true,
                        message: '请输入用户名',
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    phone: [{
                        required: true,
                        validator: validatephone,
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    email: [{
                        required: true,
                        validator: validateemail,
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    info: [{
                        required: true,
                        message: '请填入验证信息',
                        trigger: 'blur'
                    }],
                    password: [{
                        required: true,
                        validator: validatePass,
                        trigger: 'blur'
                    }],
                    checkPass: [{
                        required: true,
                        validator: validatePass2,
                        trigger: 'blur'
                    }],
                    // 年月日
                    pickerOptions: {
                        disabledDate(time) {
                            return time.getTime() > Date.now();
                        },
                        shortcuts: [{
                            text: '今天',
                            onClick(picker) {
                                picker.$emit('pick', new Date());
                            }
                        }]
                    },

                },

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
                }]


            }
        },

        methods: {
            //邮箱验证
            async check() {
                if (this.form.email) {
                    var param = new URLSearchParams();
                    param.append('email', this.form.email);
                    const {
                        data: res
                    } = await this.$http.post('RegisterCheck/', param);
                    console.log(res)
                    if (res.code == "1001") {
                        return this.$message.error(res.msg);
                    } else {
                        this.$message.success(res.msg);
                    }

                } else {
                    return this.$message.error("请填写邮箱");
                }
            },
            handleChange(value) {
                this.form.value = value;
            },
            submit() {
                var param = new URLSearchParams();
                param.append('email', this.form.email);
                param.append('username', this.form.username);
                param.append('phone', this.form.phone);
                param.append('sex', this.form.radio);
                param.append('password', this.form.password);
                param.append('info', this.form.info);
                param.append('where', this.form.value);
                var resDate = this.form.value1.getFullYear() + '-' + (this.form.value1.getMonth() + 1) + '-' + this.form.value1.getDate();
                param.append('date', resDate);
                param.append('marrytype', this.form.radiotype);
                this.$refs.form.validate(async vaild => { //vue前台验证规则
                    if (vaild) {
                        const {
                            data: res
                        } = await this.$http.post('Register/', param);
                        console.log(res)
                        if (res.code == "1001" || res.code == "1002") {
                            return this.$message.error(res.msg);
                        } else {
                            this.$message.success("注册成功");
                            this.$router.push('/login');
                        }
                    }

                });
            },
            goLogin() {
                this.$router.push('/login');
            }
        }
    }
</script>

<style lang="less" scoped>
    .top_img {
        padding-left: 123px;
    }
    
    .side_img {
        position: absolute;
        left: 10%;
        width: 200px;
        height: 100%;
        background-color: rgba(35, 192, 113, 0.933);
    }
    
    .main {
        position: absolute;
        left: 34%;
        background-color: #eeee;
        width: 705px;
        height: 100%;
    }
    
    .form {
        width: 300px;
    }
    
    .block {
        float: left;
        width: 150px;
    }
    
    .btns {
        display: flex;
        /*弹性布局 */
        justify-content: center;
        /*元素在主轴中心开始排列 */
    }
    
    .item {
        margin: 4px;
    }
</style>