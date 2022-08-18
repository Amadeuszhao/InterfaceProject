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
        { title: 'AI verification', describe: 'AI verification', route: '/verify', icon: 'el-icon-chat-line-round' },
        { title: 'Text attack', describe: 'text related attack', route: '/attack', icon: 'el-icon-search' }
      ],
      picsrc: null
    }
  },
  mounted () {
    if (this.type === 0) {
      this.picsrc = require('@/assets/pics/verification.png')
    } else {
      this.picsrc = require('@/assets/pics/text_attack.jpg')
    }
  },
  props: {
    type: Number
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
