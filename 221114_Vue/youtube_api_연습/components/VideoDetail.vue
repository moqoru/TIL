<template>
  <div>
    <div v-if="visible">
      <iframe id="ytplayer" type="text/html" width="640" height="360"
      :src="videoURL"
      frameborder="0">
      </iframe>
    </div>
  </div>
</template>

<script>
export default {
  name : 'VideoDetail',
  data(){
    return {
      visible : false,
      videoURL : null,
    }
  },
  props : {
    detailProps : String,
  },
  watch : {
    detailProps() {
      this.visible = true
      this.videoURL = `https://www.youtube.com/embed/${this.detailProps}?autoplay=0&origin=http://example.com`
    }
  }
}
</script>

<style>

</style>