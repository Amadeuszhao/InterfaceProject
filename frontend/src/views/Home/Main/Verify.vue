<template>
    <div>
        <el-row>
             <el-col :span="12" :offset="6">
                 <h1 style="font-size:30px"><i class="el-icon-s-help" style="margin-right:20px"></i>Ai Verification</h1>
                 <p align="justify" style="margin:50px 0px">Please select model to verify!</p>
             </el-col>
        </el-row>
        <el-row>
          <el-col :span="12" :offset="6">
          <div id="top-controls">
            <div class="container">
              <div class="timeline-controls">
                <button class="mdl-button mdl-js-button mdl-button--icon ui-resetButton" id="reset-button"
                  title="Reset the process">
                  <i class="material-icons">replay</i>
                </button>
                <button class="mdl-button mdl-js-button mdl-button--fab mdl-button--colored ui-playButton"
                  id="play-pause-button" title="Run/Pause" @click="loadTable">
                  <i class="material-icons">play_arrow</i>
                  <i class="material-icons">pause</i>
                </button>
              </div>
              <div class="control ui-model">
                <label for="model">Select Model</label>
                <div class="select">
                  <select id="model">
                    <option value="LeNet-5">LeNet</option>
                    <!-- <option value="ResNet-50">ResNet-50</option> -->
                  </select>
                </div>
              </div>
              <div class="control ui-verify">
                <label for="verify">Select Property</label>
                <div class="select">
                  <select v-model="selectedProperty">
                    <option v-for="property in properties" v-bind:key="{ id: property.id, text: property.name }">
                      {{property.name}}
                    </option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          </el-col>
        </el-row>
        <el-row style="padding-top: 30px">
          <el-col :span="16" :offset="8">
          <div id="main" style="width: 600px;height:400px;"></div>
          </el-col>
        </el-row>
        <el-row v-if="resultShow" style="padding-top: 30px">
             <el-col :span="16" :offset="4">
              <div>
                <el-table
                  id="table"
                  v-loading="loading"
                  :data="tableData"
                  style="width: 100%">
                  <!-- <slot name="columns"> -->
                    <el-table-column
                      label="result"
                      prop="result"/>
                    <el-table-column
                    label="total input bounds"
                    prop="total"
                      />
                    <el-table-column
                      label="verified"
                      prop="verify"
                      />
                    <el-table-column
                      label="falsified"
                      prop="falsify"
                      />
                    <el-table-column
                      label="timeout"
                      prop="timeout"
                    />
                    <el-table-column
                      label="time"
                      prop="time"
                    />
                  </el-table>
                <!-- <slot name="pagination" :page="page" :total="total">
                  <el-pagination
                    v-model="page"
                    :total="total"
                    @current-change="getTableData"
                    layout="prev, pager, next"
                    >
                  </el-pagination>
                </slot> -->
              </div>
             </el-col>
        </el-row>
    </div>
</template>
<script>
import verifyData from './assets/verifyData.json'
import * as echarts from 'echarts'

export default {
  name: 'StatisEntity',
  data () {
    return {
      myname: 'house',
      mylimit: '50',
      resultShow: false,
      loading: false,
      selectedProperty: 'Robustness',
      properties: [
        // { id: 1, name: 'Fairness' },
        { id: 1, name: 'Robustness' }
        // { id: 3, name: 'Local Robustness' }
      ],
      tableData: [{
        result: 'result1',
        total: '45',
        verify: verifyData[0].Verified,
        falsify: verifyData[0].Falsified,
        timeout: verifyData[0].Timeout,
        time: verifyData[0].Time
      },
      {
        result: 'result2',
        total: '36',
        verify: verifyData[1].Verified,
        falsify: verifyData[1].Falsified,
        timeout: verifyData[1].Timeout,
        time: verifyData[1].Time
      },
      {
        result: 'result3',
        total: '4',
        verify: verifyData[2].Verified,
        falsify: verifyData[2].Falsified,
        timeout: verifyData[2].Timeout,
        time: verifyData[2].Time
      },
      {
        result: 'result4',
        total: '42',
        verify: verifyData[3].Verified,
        falsify: verifyData[3].Falsified,
        timeout: verifyData[3].Timeout,
        time: verifyData[3].Time
      },
      {
        result: 'result5',
        total: '40',
        verify: verifyData[4].Verified,
        falsify: verifyData[4].Falsified,
        timeout: verifyData[4].Timeout,
        time: verifyData[4].Time
      }
      ],
      page: 1,
      total: 10,
      sortParams: []
    }
  },
  methods: {
    async loadTable () {
      await this.loadChart()
      this.resultShow = true
    },
    async loadChart () {
      var chartDom = document.getElementById('main')
      var myChart = echarts.init(chartDom)
      var option

      option = {
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        legend: {},
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: ['Result1', 'Result2', 'Result3', 'Result4', 'Result5']
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: 'Verified',
            type: 'bar',
            stack: 'count',
            emphasis: {
              focus: 'series'
            },
            data: [0, 0, 0, 8, 0]
          },
          {
            name: 'Falsified',
            type: 'bar',
            stack: 'count',
            emphasis: {
              focus: 'series'
            },
            data: [0, 8, 0, 0, 32]
          },
          {
            name: 'Timeout',
            type: 'bar',
            stack: 'count',
            emphasis: {
              focus: 'series'
            },
            data: [45, 28, 4, 34, 8]
          }
        ]
      }
      myChart.setOption(option)
    }
  },
  mounted () {
  }
}
</script>
<style scoped>
@import 'assets/bundle.css';
body{
  padding: 0;
  margin: 0;
}
</style>
