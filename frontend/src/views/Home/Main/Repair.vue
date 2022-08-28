<template>
  <div id='RepairSelection'>
  <h2>Choose evaluation metric: </h2>
  <select @click='clear_selection' v-model='metric_selection' style='width: 200px'>
    <option v-for='(key,value) in metric_options' v-bind:key='key' :value='key'>
      {{ value }}
    </option>
  </select>
  <h2>Choose dataset:{{dataset_selection}}</h2>
    <select @click='clear_selection' v-model='dataset_selection' style='width: 200px'>
    <option v-if='metric_selection' disabled value=''>Please choose metric first</option>
    <option v-for='options in metric_selection.dataset' v-bind:key='options' :value='options'>
      {{options}}
    </option>
  </select>
  <br>
   <br>
   <br>
  <div v-if='dataset_selection'>Selected model: {{metric_selection.model}}</div>
  <br>
  <button @click='JSON_generate(dataset_selection)' >Generate Report</button>
  <br>
  <DiagramGeneration v-if='showDiagram' :config='jsonData' />
  <br>
  <table v-if='showDiagram' align='center'>
      <thead>
        <tr>
          <th scope='col'>Metric</th>
          <th scope='col'>Before</th>
          <th scope='col'>After</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for='(key,value) in jsonData.Scores' v-bind:key='key'>
          <td >{{value}}</td>
          <td >{{key[0]}}</td>
          <td >{{key[1]}}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import DiagramGeneration from './Diagram.vue'
import fullJsonData from './assets/fullJsonData.json'
export default {
  name: 'RepairSelection',
  components: {
    DiagramGeneration
  },
  data () {
    return {
      showDiagram: false,
      buttonPressable: false,
      metric_selection: {},
      dataset_selection: '',
      jsonData: '',
      metric_options: { 'Fairness Repair': { dataset: ['Census Income', 'German Credit', 'Bank Marketing'], model: '6-layer Feed Forward Neural Network' }, 'Backdoor Removal': { dataset: ['German Traffic Sign Benchmark', 'MNIST', 'Fashion-MNIST'], model: 'CNN' }, 'Safety Violation Repairing': { dataset: ['ACAS N2,9', 'ACAS N3,3', 'ACAS N1,9'], model: '6-layer Feed Forward Neural Network' } },
      fullJsonData: fullJsonData
    }
  },
  methods: {
    JSON_generate (dataset) {
      if (dataset !== '') {
        this.showDiagram = true
        this.jsonData = this.fullJsonData[dataset]
      }
    },
    clear_selection () {
      this.showDiagram = false
    }
  }
}

</script>
<style>
  td{
    padding-left: 15px;
    border-bottom: 1px solid #ddd;
    text-align: center;
  }
  th{
    padding-left: 15px;
    border-bottom: 1px solid #ddd;
  }
</style>
