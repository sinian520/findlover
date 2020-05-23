<template>
    <div class="container">
        <el-page-header @back="goBack" content="我要发布活动信息">
        </el-page-header>
        <!-- 活动申请单 -->
        <el-card class="box-card">
            <el-form :rules="rules"  ref="form" :model="form" label-width="100px"  label-position="right">
                <el-form-item label="活动名称" prop="name">
                  <el-input v-model="form.name"></el-input>
                </el-form-item>
                <el-form-item label="活动地点" prop="region">
                    <el-input v-model="form.region"></el-input>
                </el-form-item>
                <el-form-item label="活动时间" prop="date1">
                  <el-col :span="11">
                    <el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
                  </el-col>
                  <el-col class="line" :span="1">———</el-col>
                  <el-col :span="12">
                    <el-time-picker placeholder="选择开始时间" v-model="form.date2" style="width: 100%;" value-format="HH:mm" ></el-time-picker>
                  </el-col>
                </el-form-item>
                <el-form-item label="资金/每人" prop="money">
                    <el-input v-model="form.money" placeholder="人/元"></el-input>
                </el-form-item>
                <el-form-item label="活动人数" prop="count">
                    <el-input v-model="form.count" placeholder="活动人数应大于四人"></el-input>
                </el-form-item>
                <el-form-item label="活动内容" prop="desc">
                  <el-input type="textarea" v-model="form.desc" placeholder="介绍一下您准备的活动内容" :autosize="{ minRows: 4, maxRows: 6}"></el-input>
                </el-form-item>
                <el-form-item>
                  <el-button type="primary" @click="onSubmit">立即创建</el-button>
                  <el-button @click="resetForm('form')">取消</el-button>
                </el-form-item>
              </el-form>
        </el-card>
          
    </div>

</template>

<script>
    export default {
        data() {
            var validatecount = (rule, value, callback) => {
                if (value === '' || !value) {
                    callback(new Error("请输入活动人数"));

                } else {
                    console.log(value)
                    value = Number(value); //转换为数字
                    if (typeof value === "number" && !isNaN(value)) { //判断是否为数字
                        if (value < 4)
                            callback(new Error("请输入大于4的人数"));
                        else
                            callback();
                    } else {
                        callback(new Error("请输入数字"));
                    }
                }
            };
            var validatemoney = (rule, value, callback) => {
                if (value === '' || !value) {
                    callback(new Error("请输入活动金额"));
                } else {
                    value = Number(value); //转换为数字
                    if (typeof value === "number" && !isNaN(value)) { //判断是否为数字
                        callback();
                    } else {
                        callback(new Error("请输入数字"));
                    }
                }
            };

            var validatedate1 = (rule, value, callback) => {
                if (value === '' || !value) {
                    callback(new Error("请选择活动日期"));
                } else {
                    var myDate = new Date()
                    console.log(value)
                    var chose = new Date(value)
                    console.log(myDate.getDate())
                    myDate.setDate(myDate.getDate() + 3)
                    console.log(myDate.getDate())
                    if (chose < myDate) {
                        callback(new Error("请输入当前日期三天后的日期"));
                    } else {
                        callback();
                    }

                }
            };
            return {
                form: {
                    name: '',
                    region: '',
                    date1: '',
                    date2: '',
                    money: '',
                    count: '',
                    desc: ''
                },
                rules: {
                    name: [{
                        required: true,
                        message: '请输入活动名称',
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    region: [{
                        required: true,
                        message: '请输入活动场所',
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    date1: [{
                        required: true,
                        validator: validatedate1,
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    money: [{
                        required: true,
                        validator: validatemoney,
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    count: [{
                        required: true,
                        validator: validatecount,
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    desc: [{
                        required: true,
                        message: '请输入活动名称',
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                },
            };
        },
        created() {},
        methods: {
            onSubmit() {
                var user = window.sessionStorage.getItem("user");
                var param = new URLSearchParams();
                param.append('user', user)
                param.append('name', this.form.name);
                param.append('money', this.form.money);
                param.append('count', this.form.count);
                param.append('region', this.form.region);
                param.append('desc', this.form.desc);
                var resDate = this.form.date1.getFullYear() + '-' + (this.form.date1.getMonth() + 1) + '-' + this.form.date1.getDate() + " " + this.form.date2;
                console.log(resDate)
                param.append('date', resDate);
                this.$refs.form.validate(async vaild => { //vue前台验证规则
                    if (vaild) {
                        const {
                            data: res
                        } = await this.$http.post('Activeapply/', param);
                        console.log(res)
                        if (res.code == "1001" || res.code == "1002") {
                            return this.$message.error(res.msg);
                        } else {
                            this.$message.success(res.msg);
                        }
                    }

                });
            },
            // 返回
            goBack() {
                this.$router.push('/matchactive')
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<style lang="less" scoped>
    .container {
        width: 950px;
        margin-left: 150px;
    }
    
    .text {
        font-size: 14px;
    }
    
    .item {
        padding: 18px 0;
    }
    
    .box-card {
        width: 100%;
        margin-top: 20px;
    }
</style>