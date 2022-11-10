<template>
  <div>
    <input
      type="text"
      v-model="searchInputData"
      @keyup.enter="searchInput"
    >
  </div>
</template>

<script>
export default {
  name : 'TheSearchBar',
  data() {
    return {
      searchInputData: null,
    }
  },
  methods: {
    searchInput() {
      this.$emit('search-input', this.searchInputData)
      this.searchInputData = ""
    }
  }
}
</script>

<style>

</style>