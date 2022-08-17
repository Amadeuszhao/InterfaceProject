<template>
    <div class='nav'>
        <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" router>
            <el-menu-item index="/welcome">Welcome</el-menu-item>
            <el-menu-item index="/attack">Model Evaluation</el-menu-item>
            <el-menu-item index="/verify">Model Verification</el-menu-item>
            <!-- <el-submenu index="/image">
                <template slot="title">Model Attack</template>
                <el-menu-item index="/adversarial">adversarial attack</el-menu-item>
                <el-menu-item index="/backdoor">backdoor attack</el-menu-item>
                <el-menu-item index="/text">text attack</el-menu-item>
            </el-submenu> -->
            <el-submenu index="/repair">
                <template slot="title">Model Mitigation</template>
                <el-menu-item index="/demo">Demo</el-menu-item>
            </el-submenu>
            <el-menu-item index="/project">About Us</el-menu-item>
        </el-menu>
    </div>
</template>
<script>
export default {
  name: 'MainNav',
  data () {
    return {
      activeIndex: this.$route.path
    }
  }
}
</script>
<style scoped>
.nav{
    margin-top: 25px;
    display:inline-block
}
</style>
