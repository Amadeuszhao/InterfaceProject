<template>
<div>
 <el-carousel :interval="4000" type="card" height="540px">
        <el-carousel-item>
          <img style="width: 960px; height: 540px" src="@/assets/pics/p1.jpg">
        </el-carousel-item>
        <el-carousel-item>
          <img style="width: 960px; height: 540px" src="@/assets/pics/p2.jpg">
        </el-carousel-item>
        <el-carousel-item>
          <img style="width: 960px; height: 540px" src="@/assets/pics/p3.jpg">
        </el-carousel-item>
        <el-carousel-item>
          <img style="width: 960px; height: 540px" src="@/assets/pics/p4.jpg">
        </el-carousel-item>
        <el-carousel-item>
          <img style="width: 960px; height: 540px" src="@/assets/pics/p5.jpg">
        </el-carousel-item>
        <el-carousel-item>
          <img style="width: 960px; height: 540px" src="@/assets/pics/p6.jpg">
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
