<template>
    <div class="container">
        <el-page-header @back="goBack" content="我要秀恩爱">
        </el-page-header>
        <div class="main">
            <el-form ref="form" :model="form" label-width="80px" :rules="rules" >
                <el-form-item label="文章标题" prop="name">
                  <el-input v-model="form.name" placeholder="我的恋爱"></el-input>
                </el-form-item>
                <el-form-item label="主要内容" prop="desc">
                    <el-input type="textarea" placeholder="相处中有哪些有趣有爱的小事呢，秀一下吧！" :autosize="{ minRows: 7, maxRows: 7}" v-model="form.desc"></el-input>
                </el-form-item>
                <el-form-item label="照片墙" prop="photo">
                <el-upload action="/as"
                ref="upload"
               :http-request="handleUpload"
                multiple :auto-upload="false"
                list-type="picture-card"
                :with-credentials='true'
                :on-preview="handlePictureCardPreview"
                :on-remove="handleRemove"
                :on-success="handleAvatarSuccess"
                :before-upload="BeforeUpload"
                :limit="1"
                :on-exceed="handleExceed"
                name="file">
                
                <i class="el-icon-plus"></i>
                </el-upload>
                <el-dialog :visible.sync="dialogVisible">
                    <img width="100%" :src="dialogImageUrl" alt="">
                </el-dialog>
                </el-form-item>
                <el-form-item>
                    <el-button type="danger" @click="postshow(form)" style="margin-left: 40%;" :disabled="onclick">立即发布</el-button>
                </el-form-item>
            </el-form>
        </div>
        
    </div>

</template>

<script>
    export default {
        data() {
            return {
                form: {
                    name: '',
                    desc: '',
                    photo: [],
                },
                rules: {
                    name: [{
                        required: true,
                        message: '请输入发布标题',
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    desc: [{
                        required: true,
                        message: '请输入发布内容',
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                    photo: [{
                        required: true,
                        message: '请上传照片',
                        trigger: 'blur' //鼠标失去焦点时更新
                    }],
                },
                // 照片
                dialogImageUrl: '',
                dialogVisible: false,

                //控制按钮只执行一次
                onclick: false,

            };
        },
        created() {},
        methods: {
            // 返回
            goBack() {
                this.$router.push('/showtime')
            },
            // 照片
            handleRemove(file, fileList) {
                console.log(file, fileList);
                this.form.photo.remo
            },
            handlePictureCardPreview(file) {
                this.dialogImageUrl = file.url;
                this.dialogVisible = true;
                console.log(this.dialogImageUrl);
            },
            handleAvatarSuccess(response, file, fileList) { //图片上传成功
                // this.form.photo.push(file)
                console.log(response);
            },
            handleExceed(files, fileList) {
                this.$message.warning('当前限制选择 1 个文件');
            },
            BeforeUpload(file, fileList) {
                console.log(file);
                const isJPG = ['image/jpeg', 'image/png', 'image/gif', 'image/pdf'].includes(file.type);

                if (!isJPG) {
                    this.$message.error('上传只能是图片');
                }
            },
            handleUpload(file) {
                this.form.photo.push(file.file);
            },
            async postshow() {
                //获取用户朋友
                var user = window.sessionStorage.getItem("user");
                let param = new FormData(); //上传图片

                this.$refs.upload.submit() // 这里是执行文件上传的函数，其实也就是获取我们要上传的文件
                param.append('user', user)
                param.append('table', this.form.name)
                param.append('subject', this.form.desc)
                this.form.photo.forEach(function(file) {
                    console.log("xxxxxxx" + file.toString());
                    param.append('file', file); // 因为要上传多个文件，所以需要遍历一下才行
                    //不要直接使用我们的文件数组进行上传，你会发现传给后台的是两个Object
                })
                console.log(this.form.photo)
                console.log(param)
                console.log("hhhhhhhhhhh")

                this.$refs.form.validate(async vaild => { //vue前台验证规则
                    if (vaild) {
                        const {
                            data: res
                        } = await this.$http.post('UploadShowlove/', param)
                        if (res.code == 1002 || res.code == 1001)
                            return this.$message.error(res.msg)
                        else {
                            this.$message.success(res.msg)
                            this.onclick = true;
                        }
                    }

                });



            },
        }
    }
</script>

<style lang="less" scoped>
    .container {
        width: 950px;
        margin-left: 150px;
    }
    
    .main {
        width: 100%;
        margin-top: 30px;
    }
</style>