<template>
  <div>
    <svg :width="width" :height="height" viewbox="0 0 width height">
       <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
          <polygon points="0 0, 10 3.5, 0 7" opacity=".6"  />
        </marker>
      </defs>
      <text class="layerHead" v-for="info in nodeGraph.layerConfig" v-bind:key="info.layer_name" :x="info.x" :y="info.y" text-anchor="middle">{{info.layer_name}}</text>
      <text class="layerHead" v-for="info in nodeGraph.layerConfig" v-bind:key="info.layer_name" :x="info.x" :y="info.y+15" text-anchor="middle">{{info.layer_size}}</text>
      <circle class="circle" v-for="node in nodeGraph.nodes" v-bind:key="node" :cx="node.x" :cy="node.y" :r="nodeSize" :fill="node.color"/>
      <circle class="dot" v-for="dot in nodeGraph.dots" v-bind:key="dot" :cx="dot.x" :cy="dot.y" :r="nodeSize/4" />
      <text class="nodeText" v-for="node in nodeGraph.nodes" v-bind:key="node" :x="node.x-8" :y="node.y+3" fill="white" font-size=".6em">{{node.label}}</text>
      <line class="link" v-for="line in nodeGraph.links" v-bind:key="line" :x1="line.x1" :x2="line.x2" :y1="line.y1" :y2="line.y2" marker-end="url(#arrowhead)" />
  </svg>
  </div>
</template>
<script>
export default {
  name: 'DiagramGeneration',
  data () {
    return {
      layer_count: null,
      maxLayerSize: null,
      minLayerSize: 32790,
      width: window.innerWidth,
      height: 500,
      yoffset: 40,
      xdist: 80,
      nodeSize: null,
      nodeUnit: null,
      nodeGraph: []
    }
  },
  props: ['config'],
  mounted () {
    this.initiate()
  },
  methods: {
    initiate () {
      this.layer_count = this.config.layer_names.length
      if (this.layer_count > 10) {
        this.height = 600
      }
      this.minMaxSize()
      this.nodeGraph = this.buildNodeGraph()
    },
    minMaxSize () {
      for (const value of Object.values(this.config.layers)) {
        if (value.layer_size > this.maxLayerSize) {
          this.maxLayerSize = value.layer_size
        }
        if (value.layer_size < this.minLayerSize) {
          this.minLayerSize = value.layer_size
        }
      };
      var ratio = Math.log(this.maxLayerSize) / Math.log(this.minLayerSize)
      // if (this.minLayerSize > 6){ratio = Math.sqrt(ratio)};
      this.nodeUnit = (this.height - this.yoffset) / ratio
      if (this.minLayerSize < 7) {
        this.nodeSize = (this.nodeUnit / this.minLayerSize / 2 - 6).toFixed(0)
      } else {
        this.nodeSize = (this.nodeUnit / 16 - 1).toFixed(0)
      }
      this.xdist = this.width / (this.layer_count + 1)
    },
    colorShade (num) {
      // Return a CSS HSL string
      var percent = 50 + (1 - num) * 45
      percent = percent.toFixed(0)
      return 'hsl(0, 100%, ' + percent + '%)'
    },
    buildNodeGraph () {
      var newGraph = {
        nodes: [],
        links: [],
        dots: []
      }
      var layerConfig = []
      var hiddenLayers = []
      for (var layer = 0; layer < this.layer_count; layer++) {
        var layerName = this.config.layer_names[layer]
        var newHiddenLayer = []
        var layerSize = this.config.layers[layerName].layer_size
        var guilty = this.config.layers[layerName].guilty
        var drawLayerSize = layerSize
        if (layerSize > 6) {
          drawLayerSize = 8
        }
        var ydist = this.nodeUnit * Math.log(layerSize) / Math.log(this.minLayerSize) / drawLayerSize
        // nodes
        if (this.minLayerSize < 7) { ydist = ydist * Math.sqrt(Math.log(layerSize) / Math.log(this.minLayerSize)) }
        for (var i = 0; i < 6; i++) {
          if (i >= layerSize) { break }
          var newTempLayer = { layer: layer, label: '', color: 'hsl(210, 100%, 85%)', layer_size: layerSize, x: (layer + 0.5) * this.xdist, y: (this.height + this.yoffset) / 2 - ((drawLayerSize - 1) / 2 - i) * ydist }
          if (guilty) {
            newTempLayer.label = this.config.layers[layerName].data[i]
            newTempLayer.color = this.colorShade(newTempLayer.label)
          }
          if (layerSize > 6 && i === 5) {
            newGraph.dots.push({ x: newTempLayer.x, y: newTempLayer.y })
            newGraph.dots.push({ x: newTempLayer.x, y: newTempLayer.y + ydist })
            newTempLayer.y = newTempLayer.y + ydist * 2
          }
          newHiddenLayer.push(newTempLayer)
        }
        hiddenLayers.push(newHiddenLayer)
        layerConfig.push({ layer_name: layerName, layer_size: layerSize, layer: layer, x: (layer + 0.5) * this.xdist, y: this.yoffset / 2 })
        if (layer < this.layer_count - 1) {
          newGraph.links.push({ x1: (layer + 0.5) * this.xdist + 14, x2: (layer + 1.5) * this.xdist - this.nodeSize - 10, y1: (this.height + this.yoffset) / 2, y2: (this.height + this.yoffset) / 2 })
        }
      }
      newGraph.nodes = newGraph.nodes.concat.apply([], hiddenLayers)
      newGraph.layerConfig = layerConfig
      return newGraph
    }
  }
}
</script>
<style scoped>
  .circle {
    stroke: #999;
    stroke-width: 0px;
  }
  .dot {
    stroke: #999;
    stroke-width: 0px;
    fill: #000000;
  }
  .nodeText{
    font-family: Rubik, sans-sarif
  }
  .layerHead{
    font-size: 0.9rem;
    font-family: Rubik, sans-sarif;
  }
  .link {
    stroke: #999;
    stroke-opacity: .6;

  }
</style>
