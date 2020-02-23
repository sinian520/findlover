<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 头像区域 -->
      <div class="avater_box">
        <img src="../assets/logo.png" alt="">
      </div>
      <!-- 登录表单区域 -->
      <el-form ref="loginRef" :model="loginform" :rules="loginrules" label-width="0px" class="login_form">
        <!-- 用户名   prop绑定验证规则 -->
        <el-form-item prop="username">
          <el-input v-model="loginform.username"  placeholder="邮箱" prefix-icon="iconfont icon-RectangleCopy" ></el-input>
        </el-form-item>
        <!-- 密码 -->
        <el-form-item prop="password">
          <el-input v-model="loginform.password"  placeholder="密码" prefix-icon="iconfont icon-mima" type="password"></el-input>
        </el-form-item>
        <!-- 按钮 -->
        <el-form-item class="btns">
            <span>
            <el-link :underline="false" href="/register"  target="_blank">没有账号？点我注册</el-link>
            </span>
          <el-button type="primary" @click="login" label="right">登录</el-button>
          <el-button type="info" @click="resetloginform"label="right">重置</el-button>
        </el-form-item>
      </el-form>

    </div>
  </div>
</template>

<script>
    export default {
        data() {
            return {
                loginform: {
                    username: '',
                    password: ''
                },
                loginrules: {
                    username: [{
                        required: true,
                        message: '请输入用户名',
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    password: [{
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                    }, {
                        min: 6,
                        max: 6,
                        message: '密码长度为6位',
                        trigger: 'blur'
                    }],
                }
            }
        },

        methods: {
            // 重置
            resetloginform() {
                this.$refs.loginRef.resetFields();
            },
            login() {

                let param = new URLSearchParams()
                param.append('username', this.loginform.username)
                param.append('password', this.loginform.password)
                console.log(this.loginform.username);
                this.$refs.loginRef.validate(async vaild => { //vue前台验证规则
                    if (vaild) {
                        const {
                            data: res
                        } = await this.$http.post('LoginView/', param);
                        console.log(res)
                        if (res.code == "1001" || res.code == "1002") {
                            return this.$message.error(res.msg);
                        } else {
                            this.$message.success("登陆成功！");
                            window.sessionStorage.setItem("token", res.token);
                            this.$router.push('/firstpage');
                        }
                    }

                });


            },
        },
    }
</script>

<style lang="less" scoped>
    .login_container {
        height: 100%;
        background-image: url('../assets/img/2.png');
        background-repeat: no-repeat;
        background-size: 100%, 100%;
        background-position: center;
    }
    
    .login_box {
        width: 450px;
        height: 300px;
        background-color: #fff;
        border-radius: 3px;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }
    
    .avater_box {
        position: absolute;
        width: 130px;
        height: 130px;
        border: 1px splid #eee;
        border-radius: 50%;
        padding: 10px;
        box-shadow: 0 0 10px #ddd;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #fff;
    }
    
    .avater_box img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        background-color: #eee;
    }
    
    .login_form {
        position: absolute;
        bottom: 0;
        width: 100%;
        padding-left: 20px;
        padding-right: 20px;
        /* border-box 告诉浏览器去理解你设置的边框和内边距的值是包含在width内的 */
        box-sizing: border-box;
    }
    
    .btns {
        display: flex;
        /*弹性布局 */
        justify-content: flex-end;
        /*元素在主轴中心开始排列 */
    }
    
    .btns span {
        position: fixed;
        bottom: 10px;
        left: 140px;
        color: grey;
    }
</style>