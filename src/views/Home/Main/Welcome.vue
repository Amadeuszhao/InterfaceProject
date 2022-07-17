<template>
<div>
   <Guide></Guide>
   <Footer style="padding:0px"></Footer>
</div>
</template>
<script>
import Guide from '@/components/Guide'
import Footer from '@/components/Footer'
export default {
  name: 'Welcome',
  data () {
    return {

    }
  },
  components: {
    Guide, Footer
  }
}
</script>
