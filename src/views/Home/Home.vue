<template>
    <div>
        <el-container>
           <el-header><HomeNav></HomeNav></el-header>
           <el-main style="padding:0px"><router-view></router-view></el-main>
        </el-container>
        <!-- <router-view></router-view> -->
    </div>
</template>
<script>
import HomeNav from '@/components/HomeNav'
export default {
  name: 'Home',
  components: {
    HomeNav
  }
}
</script>
<style scoped>
</style>
