<template>
    <div>
        <el-row>
             <el-col :span="12" :offset="6">
                 <h1 style="font-size:30px"><i class="el-icon-chat-line-round" style="margin-right:20px"></i>Text Attack</h1>
                 <p align="justify" style="margin:50px 0px">enter sentence for attack！
                 </p>
             </el-col>
        </el-row>
        <el-row  style="margin-bottom:20px">
            <el-col :span="12" :offset="6"><el-button type="primary" style="float:left" @click=getdata>generate</el-button></el-col>
        </el-row>
        <el-row >
            <el-col :span="12" :offset="6">
                <el-input
                    type="textarea"
                    :rows="14"
                    placeholder="input text message"
                    v-model="textarea">
                </el-input>
            </el-col>
        </el-row>
</div>
</template>
<script>
import axios from 'axios'
import echarts from 'echarts'
export default {
  data () {
    return {
      textarea: 'This sentence is a simple place holder.',
      tableData: [],
      target: this.baseVPN(),
      graphData: {},
      myGraphChart: null
    }
  },
  mounted () {
    this.myGraphChart = echarts.init(document.getElementById('showtablemain'))
  },
  methods: {
    getdata () {
      var that = this
      that.tableData = []
      const postdata = new FormData()
      postdata.append('text', that.textarea)
      axios.post(that.target, postdata).then(function (ret) {
        var datalist = ret.data
        that.getGraph(datalist)
        for (var i = 0; i < datalist.length; i++) {
          var item = { subject: '', predicate: '', object: '' }
          item.subject = datalist[i][0]
          item.predicate = datalist[i][1]
          item.object = datalist[i][2]
          that.tableData.push(item)
        }
      })
    },
    getGraph (datalist) {
      var that = this
      var nodelist = []
      var linklist = []
      for (var i = 0; i < datalist.length; i++) {
        var subj = datalist[i][0]
        var pred = datalist[i][1]
        var obj = datalist[i][2]
        var nodex = that.getNode(subj)
        var nodez = that.getNode(obj)
        var idx = that.ifHavenode(nodelist, nodex)
        var idz = that.ifHavenode(nodelist, nodez)
        var linknode = that.getlinkNode(idx, idz, pred)
        linklist.push(linknode)
      }
      that.graphData = { type: 'force', categories: [{ name: '实体', keyword: {}, base: '实体节点' }], nodes: nodelist, links: linklist }
      that.getgraphshow()
    },
    getlinkNode (s, t, r) {
      var node = { source: s, target: t, label: { show: true, formatter: 'rel' } }
      node.label.formatter = r
      return node
    },
    getNode (n) {
      var node = { name: n, value: 3, category: 0, symbolSize: 10 }
      return node
    },
    ifHavenode (nodelist, node) {
      for (var i = 0; i < nodelist.length; i++) {
        if (nodelist[i].name === node.name) {
          return i
        }
      }
      nodelist.push(node)
      return nodelist.length - 1
    },
    getgraphshow () {
      var that = this
      var myChart = that.myGraphChart
      myChart.showLoading()
      var option = {
        legend: {
          data: ['实体节点']
        },
        series: [{
          type: 'graph',
          layout: 'force',
          animation: false,
          label: {
            position: 'right',
            formatter: '{b}'
          },
          roam: true,
          draggable: true,
          data: that.graphData.nodes.map(function (node, idx) {
            var newNode = { id: 0, name: '', value: 0, category: '', symbolSize: 0 }
            newNode.id = idx
            newNode.name = node.name
            newNode.value = node.value
            newNode.category = node.category
            newNode.symbolSize = node.symbolSize

            return newNode
          }),
          focusNodeAdjacency: true,
          categories: that.graphData.categories,
          force: {
            edgeLength: 15,
            repulsion: 20,
            gravity: 0
          },
          edgeSymbol: ['circle', 'arrow'],
          edges: that.graphData.links.map(function (node, idx) {
            var newLink = { source: 0, target: 0, label: {} }
            newLink.source = node.source
            newLink.target = node.target
            newLink.label = node.label
            return newLink
          })
        }]
      }

      myChart.setOption(option)
      myChart.hideLoading()
    }
  }
}
</script>
