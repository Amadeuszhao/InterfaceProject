<template>
    <div>
        <el-row>
             <el-col :span="12" :offset="6">
                 <h1 style="font-size:30px"><i class="el-icon-s-help" style="margin-right:20px"></i>Ai Verification</h1>
                 <p align="justify" style="margin:50px 0px">Ai Verification</p>
             </el-col>
        </el-row>
        <el-row>
             <el-col :span="16" :offset="4">
             </el-col>
        </el-row>
    </div>
</template>
<script>
export default {
  name: 'StatisEntity',
  data () {
    return {
      myname: 'house',
      mylimit: '50'
    }
  },
  components: {
  }
}
</script>
<style scoped>
body{
  padding: 0;
  margin: 0;
}
</style>
