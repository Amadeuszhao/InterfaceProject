<template>
    <div>
      <!-- 945 304 -->
        <el-row>
           <el-col :span="24"><MainNav></MainNav></el-col>
        </el-row>
        <router-view></router-view>
    </div>
</template>
<script>
import MainNav from '@/components/MainNav'
export default {
  name: 'Main',
  components: {
    MainNav
  }
}
</script>
<style scoped>
</style>
