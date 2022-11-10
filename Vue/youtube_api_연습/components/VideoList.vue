<template>
  <div>
    <div v-for="(listItemProps, videoIndex) in listProps" :key="videoIndex">
      <VideoListItem
        :list-item-props="listItemProps"
        @send-play-item="sendPlayItem"
      />
    </div>
  </div>
</template>

<script>
import VideoListItem from './VideoListItem.vue'
export default {
  name : 'VideoList',
  data(){
    return {
      listItemProps : "",
    }
  },
  props : {
    listProps : Array,
  },
  components : {
    VideoListItem
  },
  methods: {
    sendPlayItem(videoId){
      this.$emit('send-play-item', videoId)
    }
  }
}

</script>

<style>

</style>