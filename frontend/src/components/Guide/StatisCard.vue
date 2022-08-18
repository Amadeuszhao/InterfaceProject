<template>
    <div>
    <el-card :body-style="{ padding: '0px' }" shadow="hover">
      <img :src=picsrc class="image">
      <div style="padding: 14px;">
        <h1><i :class=whattype[type].icon></i>{{whattype[type].title}}</h1>
        <div class="bottom clearfix">
          <!-- <time class="time">{{ currentDate }}</time> -->
          <p>{{whattype[type].describe}}</p>
          <router-link :to=whattype[type].route><el-button type="primary" icon="el-icon-share" class="button">Have a Look</el-button></router-link>
        </div>
      </div>
    </el-card>
    </div>
</template>
<script>
export default {
  data () {
    return {
      whattype: [
        { pic_src: '@/assets/pics/adversarial.png', title: 'adversarial attack', describe: 'adversarial attack for image models', route: '/attack', icon: 'el-icon-user-solid' },
        { pic_src: '@/assets/pics/backdoor.png', title: 'backdoor attack', describe: 'backdoor attack for image models', route: '/attack', icon: 'el-icon-s-home' }
      ],
      picsrc: null
    }
  },
  mounted () {
    if (this.type === 0) {
      this.picsrc = require('@/assets/pics/adversarial.png')
    } else if (this.type === 1) {
      this.picsrc = require('@/assets/pics/backdoor.png')
    }
  },
  props: {
    type: Number
  },
  methods: {
    getWhatType () {
      var ans = [
        { pic_src: '@/assets/pics/adversarial.png', title: 'adversarial attack', describe: 'adversarial attack for image models' },
        { pic_src: '@/assets/pics/backdoor.png', title: 'backdoor attack', describe: 'backdoor attack for image models' }
      ]
      return ans
    },
    jump () {
      this.$router.push({ name: 'login' })
    }
  }
}
</script>
<style scoped>
  .time {
    font-size: 13px;
    color: #999;
  }

  .button {
    float: right;
  }

  .image {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
  p{
      line-height: 150%;
  }
  h1 i{
      margin-right: 20px;
  }
</style>
