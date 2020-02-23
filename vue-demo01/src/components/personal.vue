<template>
    <div class="container">
        <el-container>
            <el-header class="top_img"></el-header>
            <el-main>
                <el-row>
                    <el-col :span="12"><div class="grid-content bg-purple">
                        
                    </div></el-col>
                    <el-col :span="12"><div class="grid-content bg-purple-light"></div></el-col>
                </el-row>
            </el-main>
          </el-container>
    </div>
  </template>

<script>
    export default {
        data() {
            return {}

        },

        methods: {
            // 重置

        },
    }
</script>

<style lang="less" scoped>
    .container {
        height: 100%;
    }
    
    .top_img {
        width: 100%;
        height: 15%;
        background-color: brown;
    }
    
    .el-row {
        margin-bottom: 20px;
    }
    
    .el-col {
        border-radius: 4px;
    }
    
    .bg-purple-dark {
        background: #99a9bf;
    }
    
    .bg-purple {
        background: #d3dce6;
    }
    
    .bg-purple-light {
        background: #e5e9f2;
    }
    
    .grid-content {
        border-radius: 4px;
        height: 500px;
    }
    
    .row-bg {
        padding: 10px 0;
        background-color: #f9fafc;
    }
</style>