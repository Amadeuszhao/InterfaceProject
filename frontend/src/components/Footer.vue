<template>
    <div>
        <div class="one">
            <el-row>
                <el-col :span="24">
                    <h1>Friendly Links</h1>
                    <a href="https://scholar.google.com/"><el-button type="primary"  circle><i class="el-icon-picture" ></i></el-button></a>
                </el-col>
            </el-row>
        </div>
        <div class="two">
            <el-row>
                <el-col :span="24">
                    <p style="margin-top:40px">© 2022 RISE Lab, Inc. All Rights Reserved.</p>
                </el-col>
            </el-row>
        </div>
    </div>
</template>
<style scoped>
.el-row{
    text-align: center;
}
.one{
    background-color: #4f4f4f;
    color: azure;
    padding:20px;
}
.two{
    background-color: #404040;
    color: azure;
    padding:30px;
}
a{
    text-decoration: none;
    color: azure;
}
h1{
    font-size: 25px;
}
p{
   font-size: 15px;
}
i{
    font-size: 25px;
}
.el-button{
    margin:20px;
}

</style>
