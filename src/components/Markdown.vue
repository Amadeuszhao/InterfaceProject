<template>
    <div>
        <mavon-editor
      class="md"
     :value="context"
     :subfield = "prop.subfield"
     :defaultOpen = "prop.defaultOpen"
     :toolbarsFlag = "prop.toolbarsFlag"
     :editable="prop.editable"
     :scrollStyle="prop.scrollStyle"
  ></mavon-editor>
    </div>
</template>
<script>
import axios from 'axios'
export default {
  data () {
    return {
      context: 'not find markdown',
      target: this.baseUrl() + 'markdown/what?name='
    }
  },
  props: {
    filename: String
  },
  components: {
  },
  mounted () {
    var that = this
    axios.get(that.target + that.filename).then(function (ret) {
      that.context = ret.data.md
    })
  },
  computed: {
    prop () {
      const data = {
        subfield: false, // 单双栏模式
        defaultOpen: 'preview', // edit： 默认展示编辑区域 ， preview： 默认展示预览区域
        editable: false,
        toolbarsFlag: false,
        scrollStyle: true
      }
      return data
    }
  }
}
</script>
