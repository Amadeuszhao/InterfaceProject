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
                  id="play-pause-button" title="Run/Pause" v-on:click="resultHidden = !resultHidden">
                  <i class="material-icons">play_arrow</i>
                  <i class="material-icons">pause</i>
                </button>
              </div>
              <div class="control ui-model">
                <label for="model">Select Model</label>
                <div class="select">
                  <select id="model">
                    <option value="LeNet-5">LeNet-5</option>
                    <option value="ResNet-50">ResNet-50</option>
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
        <el-row v-if="resultHidden">
             <el-col :span="16" :offset="6">
              <div>
                <el-table
                  id="table"
                  v-loading="loading"
                  :data="tableData"
                  :cell-class-name="tableClassChecker"
                  style="width: 100%">
                  <!-- <slot name="columns"> -->
                    <el-table-column
                      label="parameter"
                      prop="param"/>
                    <el-table-column
                      label="fairness"
                      prop="fairness"
                      />
                    <el-table-column
                      label="robustness"
                      prop="robustness"
                      />
                      <!-- <el-table-column label="File">
                        {{d.file}}
                      </el-table-column> -->
                      <!-- <template slot-scope="{row}">
                        <slot :name="column.prop || column.type || column.label" :row="row">
                          {{row[column.prop]}}
                        </slot>
                      </template> -->
                    <!-- </el-table-column>
                    <el-table-column label="Path">
                      {{d.path}} -->
                    <el-table-column
                      label="verification"
                      prop='verify'
                    />
                  <!-- </slot> -->
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
export default {
  name: 'StatisEntity',
  data () {
    return {
      myname: 'house',
      mylimit: '50',
      resultHidden: false,
      loading: false,
      selectedProperty: 'Fairness',
      properties: [
        { id: 1, name: 'Fairness' },
        { id: 2, name: 'Robustness' },
        { id: 3, name: 'Local Robustness' }
      ],
      tableData: [{
        param: '0.1',
        fairness: '0.8',
        robustness: '0.3',
        verify: 'Not verified'
      },
      {
        param: '0.3',
        fairness: '0.5',
        robustness: '0.7',
        verify: 'Verified'
      }],
      page: 1,
      total: 10,
      sortParams: []
    }
  },
  components: {
  },
  methods: {
    tableClassChecker ({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 3) {
        if (row.verify === 'Verified') {
          return 'greenClass'
        } else {
          return 'redClass'
        }
      }
    }
  }
}
</script>
<style scoped>
body{
  padding: 0;
  margin: 0;
}
</style>
