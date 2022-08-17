<template>
     <div>
       <el-row>
             <el-col :span="12" :offset="6">
                 <h1 style="font-size:30px"><i class="el-icon-s-home" style="margin-right:20px"></i>Model Attack</h1>
             </el-col>
        </el-row>
        <el-row>
            <el-button tagName="adversarial" :type="type1" v-on:click="changeOnClick(1)" round>Adversarial Attack</el-button>
            <el-button tagNme="backdoor" :type="type2" v-on:click="changeOnClick(2)" round>Backdoor Attack</el-button>
            <el-button tagName="text" :type="type3" v-on:click="changeOnClick(3)" round>Text Attack</el-button>
        </el-row>
        <div style="margin-top:10px">
        <adversarial v-if="attackSelected === 1"></adversarial>
        <backdoor v-if="attackSelected === 2"></backdoor>
        <textattack v-if="attackSelected === 3"></textattack>
        </div>
    </div>
</template>
<script>
import Adversarial from './Adversarial.vue'
import Backdoor from './Backdoor.vue'
import Textattack from './Textattack.vue'
export default {
  name: 'Attack',
  components: {
    adversarial: Adversarial,
    backdoor: Backdoor,
    textattack: Textattack
  },
  data () {
    return {
      attackSelected: 1,
      type1: 'primary',
      type2: '',
      type3: ''
    }
  },
  methods: {
    changeOnClick (id) {
      if (id === 1) {
        this.type1 = 'primary'
        this.type2 = ''
        this.type3 = ''
        this.attackSelected = 1
      } else if (id === 2) {
        this.type1 = ''
        this.type2 = 'primary'
        this.type3 = ''
        this.attackSelected = 2
      } else {
        this.type1 = ''
        this.type2 = ''
        this.type3 = 'primary'
        this.attackSelected = 3
      }
    }
  }
}
</script>
