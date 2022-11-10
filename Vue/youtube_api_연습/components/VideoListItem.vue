<template>
  <div @click="sendPlayItem">
    <img :src="listItemProps.snippet.thumbnails.high.url" alt="썸네일 고화질">
    <h2> 제목 : {{listItemProps.snippet.title}}</h2>
    <h3> 내용 : {{listItemProps.snippet.description}}</h3>
  </div>
</template>

<script>
export default {
  name : 'VideoListItem',
  props : {
    listItemProps : Object,
  },
  methods: {
    sendPlayItem() {
      this.$emit('send-play-item', this.listItemProps.id.videoId)
    }
  }
}
</script>

<style>

</style>