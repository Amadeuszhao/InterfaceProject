<template>
    <div>
        <el-row>
             <el-col :span="12" :offset="6">
                 <h1 style="font-size:30px"><i class="el-icon-view" style="margin-right:20px"></i>model repair</h1>
                 <p align="justify" style="margin:50px 0px">model repair
                 </p>
             </el-col>
        </el-row>
        <el-card class="box-card" shadow="never">
          <div slot="header" class="clearfix">
            <span><i class="el-icon-caret-bottom"></i></span>
            <el-button style="float: right; padding: 3px 0" type="text" @click="flushvisual"><i class="el-icon-refresh"></i></el-button>
            <el-button style="float: right; margin-left:15px;margin-right:20px;padding:0px" type="text"><el-input-number v-model="limit" :step="100" size='mini'></el-input-number></el-button>
            <el-button style="float: right; padding: 5px 0px" type="text">
              <el-switch
                  v-model="iffocus"
                  active-color="#13ce66"
                  inactive-color="#ff4949">
              </el-switch>
            </el-button>
          </div>
          <div>
          </div>
       </el-card>
    </div>
</template>
<script>
export default {
  name: 'Global',
  data () {
    return {
      limit: '200',
      iffocus: true
    }
  },
  updated () {
    this.$refs.child.getdatas()
  },
  mounted () {
    this.$refs.child.getdatas()
  },
  components: {
  },
  methods: {
    flushvisual () {
      this.$refs.child.getdatas()
    }
  }
}
</script>
