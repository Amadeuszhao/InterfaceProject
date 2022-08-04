<template>
    <div>
        <el-row>
          <el-col :span="16" :offset="4">
            <el-tag
               v-for="tag in mdfilelist"
               :key="tag"
                effect="plain"
               >
               {{tag}}
            </el-tag>
          </el-col>
      </el-row>
    </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      mdfilelist: [],
      target: this.baseUrl()
    }
  },
  mounted () {
    var that = this
    axios.get(that.target + 'markdown/howmany').then(function (ret) {
      that.mdfilelist = ret.data.filelist
    })
  }
}
</script>
