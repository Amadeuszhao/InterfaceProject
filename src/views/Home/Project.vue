<template>
    <div>
      <h1>Project Introduction</h1>
      <el-row>
          <el-col :span="16" :offset="4"><Markdown :filename=whatmd></Markdown></el-col>
      </el-row>
    </div>
</template>
<script>
import Markdown from '@/components/Markdown'
export default {
  data () {
    return {
      whatmd: 'project.md'
    }
  },
  components: {
    Markdown
  }
}
</script>
