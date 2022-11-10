<template>
  <div id="app">
    <h1> My First Youtube Project </h1>
    <TheSearchBar
      @search-input="getSearchData"
    />
    <VideoDetail
      :detail-props="detailProps"
    />
    <VideoList
      :list-props="listProps"
      @send-play-item="sendPlayItem"
    />
  </div>
</template>

<script>
import axios from 'axios'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'
import TheSearchBar from './components/TheSearchBar.vue'
export default {
  name: 'App',
  data(){
    return {
      listProps : null,
      detailProps : null,
      APIKey : "", 
    }
  },
  components: {
    VideoDetail,
    VideoList,
    TheSearchBar,
  },
  methods: {
    getSearchData(searchInputData){
      const youtubeAPIURL = `https://www.googleapis.com/youtube/v3/search/?key=${this.APIKey}&part=snippet&type=video&q=${searchInputData}`
      
      axios({
        method: 'get',
        url: youtubeAPIURL
      })
      .then((response) => {
        const lists = response.data.items
        this.listProps = lists
      })
      .catch((error) => {
        console.log(error)
      })
    },
    sendPlayItem(videoId){
      this.detailProps = videoId
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
