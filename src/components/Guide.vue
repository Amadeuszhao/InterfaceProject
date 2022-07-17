<template>
    <div>
        <!-- Guide page -->
       <el-row>
           <el-col :span="24">
               <h1 class="guide">QUICK GUIDE </h1>
               <p>Here you can try out our latest  results</p>
           </el-col>
       </el-row>
        <!-- Image attack -->
        <el-row>
           <el-col :span="24">
               <h1 class="guide"><i class="el-icon-data-line guide"></i>Image attack</h1>
           </el-col>
        </el-row>
        <el-row>
           <el-col :span="6" :offset="3"><StatisCard :type=type_0></StatisCard></el-col>
           <el-col :span="6" :offset="6"><StatisCard :type=type_1></StatisCard></el-col>
        </el-row>
        <!-- Model Repair -->
        <el-row>
           <el-col :span="24"><h1 class="guide"><i class="el-icon-view"></i>Model Repair</h1></el-col>
        </el-row>
        <el-row>
           <el-col :span="8" :offset="8"><VisualCard :type=type_0></VisualCard></el-col>
        </el-row>
        <!-- AI Verification -->
        <el-row>
           <el-col :span="24"><h1 class="guide"><i class="el-icon-chat-dot-round"></i>AI Verification</h1></el-col>
        </el-row>
        <el-row>
           <el-col :span="8" :offset="8"><FaqQueryCard :type=type_0></FaqQueryCard></el-col>
        </el-row>
        <!-- Text Attack -->
        <el-row>
           <el-col :span="24"><h1 class="guide"><i class="el-icon-search"></i>Text Attack</h1></el-col>
        </el-row>
        <el-row>
           <el-col :span="8" :offset="8"><FaqQueryCard :type=type_1></FaqQueryCard></el-col>
        </el-row>
    </div>
</template>
<script>
import StatisCard from '@/components/Guide/StatisCard'
import VisualCard from '@/components/Guide/VisualCard'
import FaqQueryCard from '@/components/Guide/FaqQueryCard'
export default {
  data () {
    return {
      type_0: 0,
      type_1: 1,
      type_2: 2,
      type_3: 3

    }
  },
  components: {
    StatisCard, VisualCard, FaqQueryCard
  }
}
</script>
<style scoped>
.guide{
    font-size: 40px;
}
i{
    margin-right: 20px;
}
</style>
