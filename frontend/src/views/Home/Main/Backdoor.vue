<template>
     <div>
       <el-row>
             <el-col :span="12" :offset="6">
                 <h1 style="font-size:25px"><i class="el-icon-s-home" style="margin-right:20px"></i>Backdoor attack</h1>
                 <p align="justify" style="margin:50px 0px">Backdoor attack
                 </p>
             </el-col>
        </el-row>
        <el-row>
      <el-col :span="16" :offset="4">
        <!-- Top Controls -->
        <div id="top-controls">
          <div class="container">
            <div class="timeline-controls">
              <button class="mdl-button mdl-js-button mdl-button--icon ui-resetButton" id="reset-button"
                title="Reset the process">
                <i class="material-icons">replay</i>
              </button>
              <button class="mdl-button mdl-js-button mdl-button--fab mdl-button--colored ui-playButton"
                id="play-pause-button" title="Run/Pause"  v-on:click="getAttackData">
                <i class="material-icons">play_arrow</i>
                <i class="material-icons">pause</i>
              </button>
            </div>
            <div class="control ui-activation">
              <label for="activations">Select Model</label>
              <div class="select">
                <select id="activations">
                  <option value="RELU">MNIST-RELU</option>
                  <option value="SIGMOID">MNIST-SIGMOID</option>
                  <option value="TANH">MNIST-TANH</option>
                </select>
              </div>
            </div>
            <div class="control ui-activation">
              <label for="target">Trigger Target</label>
              <div class="select">
                <select id="activations">
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option value="5">5</option>
                  <option value="6">6</option>
                  <option value="7">7</option>
                  <option value="8">8</option>
                  <option value="9">9</option>
                  <option value="0">0</option>
                </select>
              </div>
            </div>
          </div>
        </div>

        <!-- Main Part -->
        <div id="main-part" class="l--page">

          <!--  Data Column-->
          <div class="column data">
            <h4>
              <span>Select</span>
            </h4>
            <div class="ui-dataset">
              <p>Which data do you want to use?</p>
            </div>
            <div class="dataset-list">
              <div class="dataset" title="demo">
                <el-image class="data-thumbnail" :src="asset"></el-image>
              </div>
              <div class="dataset" title="demo">
                <el-image class="data-thumbnail" :src="asset"></el-image>
              </div>
              <div class="dataset" title="demo">
                <el-image class="data-thumbnail" :src="asset"></el-image>
              </div>
              <div class="dataset" title="demo">
                <el-image class="data-thumbnail" :src="asset"></el-image>
              </div>
              <div class="dataset" title="demo">
                <el-image class="data-thumbnail" :src="asset"></el-image>
              </div>
              <div class="dataset" title="demo">
                <el-image class="data-thumbnail" :src="asset"></el-image>
              </div>
            </div>
          </div>
          <div class="column data">
            <h4>
              <span>Original</span>
            </h4>
            <div class="ui-dataset">
              <p>Demonstration of original image</p>
            </div>
            <div v-if="show_image==true" style="margin-top: 20px">
            <div>
              <img v-bind:src="image" width="100%"/>
            </div>
            <div style="margin-top: 20px">
              <p>image class: {{image_class}}</p>
            </div>
            </div>
          </div>
          <div class="column data">
            <h4>
              <span>Attack</span>
            </h4>
            <div class="ui-dataset">
              <p>Demonstration of attacked image</p>
            </div>
            <div v-if="show_image==true" style="margin-top: 20px">
            <div>
              <img v-bind:src="attack_image" width="100%"/>
            </div>
            <div style="margin-top: 20px">
              <p>attack class: {{attack_class}}</p>
            </div>
            </div>
          </div>
        </div>
      </el-col>
    </el-row>
    </div>
</template>
<script>
const asset = require('./assets/2.png')
export default {
  name: 'Backdoor',
  components: {
  },
  data () {
    return {
      asset: asset,
      image: '',
      perturbation: '',
      attack_image: '',
      image_class: '',
      attack_class: '',
      show_image: false
    }
  },
  mounted () {
    this.image = ''
    this.perturbation = ''
    this.attack_image = ''
    this.image_class = ''
    this.attack_class = ''
    this.show_image = false
  },
  methods: {
    getAttackData () {
      const self = this
      this.$axios.get('http://localhost:8000/api/backdoor_attack/1', {})
        .then(function (res) {
          self.image = res.data.image
          self.perturbation = res.data.perturbation
          self.attack_image = res.data.attack_image
          self.image_class = res.data.image_class
          // self.perturbation_class = res.data.perturbation_class
          self.perturbation_class = 'data:image/jpeg;base64,'
          self.attack_class = res.data.attack_class
        })
        .then(() => {
          self.show_image = true
        }).catch(function (err) {
          console.log(err)
        })
    }
  }
}
</script>
