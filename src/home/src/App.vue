<template>
  <div>
     <Home/>
  </div>
</template>

<script lang="js" setup>
/**
 * @description: App.vue
 * @author: sinvon
 * @create 2024年11月26日02:04:34
 */
import Home from './views/Home.vue'
import { ref } from 'vue'
const props = defineProps({

})
</script>

<style lang="less">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
