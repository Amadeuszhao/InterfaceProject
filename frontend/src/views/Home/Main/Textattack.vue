<template>
    <div>
        <el-row>
             <el-col :span="12" :offset="6">
                 <h1 style="font-size:25px"><i class="el-icon-chat-line-round" style="margin-right:20px"></i>Text Attack</h1>
                 <p align="justify" style="margin:50px 0px">Enter sentence for attack！
                 </p>
             </el-col>
        </el-row>
        <el-row>
          <el-col :span="12" :offset="6">
          <div id="top-controls">
            <div class="container">
              <div class="control ui-model">
                <label for="model">Select Model</label>
                <div class="select">
                  <select id="model">
                    <option value="lstm">LSTM</option>
                    <option value="rnn">RNN</option>
                  </select>
                </div>
              </div>
              <div class="control ui-attack_method">
                <label for="attack_method">Attack Method</label>
                <div class="select">
                  <select id="attack_method">
                    <option value="PGD">PGD</option>
                    <option value="FGSM">FGSM</option>
                  </select>
                </div>
              </div>
              <div class="control ui-sentence">
                <label for="sentence">Select Text</label>
                <div class="select">
                  <select id="sentence" @change="onChange($event)" v-model="sentenceSelected">
                    <option v-for="t in textData" v-bind:key="t.id" :value="t.name">{{t.subname}}</option>
                  </select>
                </div>
              </div>
              <div class="control ui-data">
                <label for="dataset">Dataset</label>
                <div class="select">
                  <select id="dataset">
                    <option value="imdb">IMDB</option>
                    <option value="yelp">YELP</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          </el-col>
        </el-row>
        <el-row  style="margin-top: 20px">
            <el-col :span="12" :offset="6"><el-button type="primary" style="float:left" @click="onClickGenerate()">generate</el-button></el-col>
        </el-row>
        <el-row style="margin-top: 20px">
            <el-col :span="12" :offset="6">
                <el-input
                    type="textarea"
                    :rows="14"
                    placeholder="Input text message more than 10 characters"
                    v-model="textarea">
                </el-input>
            </el-col>
        </el-row>
        <el-row  style="margin-top: 20px">
            <el-col :span="12" :offset="6">
              <!--  Data Column-->
                <div class="column sentence" v-if="isGenerated">
                <h4>
                  <span>Original</span>
                </h4>
                <div class="ui-sentence">
                  <p align="justify">Demonstration of original sentence and target result</p>
                </div>
                <div class="ui-sentence">
                  <p align="justify" class="plaintext">{{originalText}}
                 </p>
                </div>
                <div class="ui-sentence" style="margin-top: 20px">
                  <p align="justify" class="plaintext">Target: {{originalClass}}
                 </p>
                </div>
                </div>
            </el-col>
        </el-row>
        <el-row  style="margin-top: 20px">
            <el-col :span="12" :offset="6">
              <!--  Data Column-->
                <div class="column sentence" v-if="isGenerated">
                <h4>
                  <span>Attacked</span>
                </h4>
                <div class="ui-sentence">
                  <p align="justify">Demonstration of the sentence after attack and target result</p>
                </div>
                <div class="ui-sentence">
                  <p align="justify" class="plaintext">{{attackedText}}
                 </p>
                </div>
                <div class="ui-sentence" style="margin-top: 20px">
                  <p align="justify" class="plaintext">Target: {{attackedClass}}
                 </p>
                </div>
                </div>
            </el-col>
        </el-row>
</div>
</template>
<script>
import axios from 'axios'
import echarts from 'echarts'
export default {
  name: 'Textattack',
  data () {
    return {
      textarea: '',
      attackedText: '',
      originalText: '',
      originalClass: '',
      attackedClass: '',
      sentenceSelected: '',
      textData: [
        {
          id: 1,
          name: "I went and saw this movie [[last]] [[night]] after being coaxed to by a few friends of mine. I'll admit that I was reluctant to see it because from what I knew of Ashton Kutcher he was only able to do comedy. I was wrong. Kutcher played the character of Jake Fischer very well, and Kevin Costner played Ben Randall with such professionalism. The sign of a good movie is that it can toy with our emotions. This one did exactly that. The entire theater (which was sold out) was overcome by laughter during the first half of the movie, and were moved to tears during the second half. While exiting the theater I not only saw many women in tears, but many full grown men as well, trying desperately not to let anyone see them crying. This movie was great, and I suggest that you go see it before you judge.",
          subname: 'I went and saw...'
        },
        {
          id: 2,
          name: "Last summer I had an appointment to get new tires and had to wait a super long time. I also went in this week for them to fix a minor problem with a tire they put on. They[fixed] it for free, and the very next morning I had the same issue. I called to complain, and the[manager] didn't even apologize!!! So frustrated. [[Never]] going back.  They seem overpriced, too.",
          subname: 'Last summer I ...'
        }
      ],
      tableData: [],
      target: this.baseVPN(),
      graphData: {},
      myGraphChart: null,
      isGenerated: false
    }
  },
  mounted () {
    this.myGraphChart = echarts.init(document.getElementById('showtablemain'))
  },
  methods: {
    onChange (event) {
      this.textarea = event.target.value
    },
    onClickGenerate () {
      const self = this
      if (this.textarea.length < 10) {
        return
      }
      this.$axios.get('http://127.0.0.1:8000/api/text_attack/1', {})
        .then(function (res) {
          self.originalText = res.data.text
          self.attackedText = res.data.attack_text
          self.originalClass = res.data.text_class
          self.attackedClass = res.data.attack_class
        })
        .then(function () {
          self.isGenerated = true
        }).catch(function (err) {
          console.log(err)
        })
    },
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
