<template>
    <div>
      <el-row>
        <el-col :span="16">
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" router>
            <el-menu-item index="/logo"><img style="width: 60px; height: 40px" src="@/assets/pics/logo.png"></el-menu-item>
            <el-menu-item index="/main">AI Security Box</el-menu-item>
            <el-menu-item index="/project">Basic Introduction</el-menu-item>
        </el-menu>
        </el-col>
      </el-row>
    </div>
</template>
<script>

</script>
<style scoped>
.el-menu.el-menu--horizontal{
    border-bottom:0px
}
</style>
