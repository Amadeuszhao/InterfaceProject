<template>
<div>
 <el-carousel :interval="4000" type="card" height="400px">
        <el-carousel-item>
        <router-link :to="{ path: '/attack' }">
          <img style="width: 640px; height: 400px" src="@/assets/pics/p1.png">
        </router-link>
        </el-carousel-item>
        <el-carousel-item>
        <router-link :to="{ path: '/verify' }">
          <img style="width: 640px; height: 400px" src="@/assets/pics/p2.png">
        </router-link>
        </el-carousel-item>
        <el-carousel-item>
        <router-link :to="{ path: '/repair' }">
          <img style="width: 640px; height: 400px" src="@/assets/pics/text_attack.jpg">
        </router-link>
        </el-carousel-item>
        <el-carousel-item>
        <router-link :to="{ path: '/project' }">
          <img style="width: 640px; height: 400px" src="@/assets/pics/verification.png">
        </router-link>
        </el-carousel-item>
   </el-carousel>
   <Guide></Guide>
   <Footer style="padding:0px"></Footer>
</div>
</template>
<script>
import Guide from '@/components/Guide'
import Footer from '@/components/Footer'
export default {
  name: 'Welcome',
  data () {
    return {

    }
  },
  components: {
    Guide, Footer
  }
}
</script>
