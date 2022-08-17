<template>
  <div>
    <el-row>
      <el-col :span="12" :offset="6">
        <h1 style="font-size:25px"><i class="el-icon-user-solid" style="margin-right:20px"></i>Adversarial Attack</h1>
        <h3></h3>
        <p align="justify" style="margin:50px 0px">
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
            <div class="control ui-attack_method">
              <label for="attack_method">Attack Method</label>
              <div class="select">
                <select id="attack_method">
                  <option value="pgd">pgd</option>
                  <option value="fgsm">fgsm</option>
                </select>
              </div>
            </div>
            <div class="control ui-activation">
              <label for="activations">Source Model</label>
              <div class="select">
                <select id="activations">
                  <option value="relu">MNIST</option>
                  <option value="tanh">CIFAR10</option>
                </select>
              </div>
            </div>
            <div class="control ui-regularization">
              <label for="regularizations">Attack Model</label>
              <div class="select">
                <select id="regularizations">
                  <option value="L1">MNIST</option>
                  <option value="L2">CIFAR10</option>
                </select>
              </div>
            </div>
            <div class="control ui-regularizationRate">
              <label for="regularRate">Eps</label>
              <div class="select">
                <select id="regularRate">
                  <option value="0">0</option>
                  <option value="0.1">0.1</option>
                  <option value="0.3">0.3</option>
                </select>
              </div>
            </div>
            <div class="control ui-problem">
              <label for="problem">Iteration</label>
              <div class="select">
                <select id="problem">
                  <option value="classification">10</option>
                  <option value="regression">20</option>
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
            <div>
            <div v-if="show_image==true">
              <img v-bind:src="original_image"/>
            </div>
            <div>
              <p>image class: {{image_class}}</p>
            </div>
            </div>
          </div>
          <div class="column data">
            <h4>
              <span>Pertubation</span>
            </h4>
            <div class="ui-dataset">
              <p>Demonstration of perturbation</p>
            </div>
            <div v-if="show_image==true">
            <div>
              <img v-bind:src="perturbation"/>
            </div>
            <div>
              <p>perturbation class: {{perturbation_class}}</p>
            </div>
            </div>
          </div>
          <div class="column data">
            <h4>
              <span>Attack</span>
            </h4>
            <div class="ui-dataset">
              <p>Demonstration of attack</p>
            </div>
            <div v-if="show_image==true">
            <div>
              <img v-bind:src="attack_image"/>
            </div>
            <div>
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
  name: 'Adversarial',
  data () {
    return {
      asset: asset,
      original_image: '',
      perturbation: '',
      attack_image: '',
      image_class: '',
      perturbation_class: '',
      attack_class: '',
      show_image: false
    }
  },
  components: {
  },
  mounted () {
    this.original_image = ''
    this.perturbation = ''
    this.attack_image = ''
    this.image_class = ''
    this.perturbation_class = ''
    this.attack_class = ''
    this.show_image = false
  },
  methods: {
    getAttackData () {
      /* 'https://fa12-219-74-123-206.ap.ngrok.io/api/adversarial_attack/2' */
      const self = this
      this.$axios.get('http://127.0.0.1:8000/api/adversarial_attack/2', {})
        .then(function (res) {
          console.log(res.data.attack_image)
          self.original_image = res.data.image
          self.perturbation = res.data.perturbation
          self.attack_image = res.data.attack_image
          self.image_class = res.data.image_class
          self.perturbation_class = res.data.perturbation_class
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
<style scoped>
  @import 'assets/bundle.css'
</style>
