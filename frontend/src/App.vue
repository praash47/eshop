<template>
<div id="app">
  <Header :message="message" @modalclosed="resetMessage" />
  <router-view @successAuthMessage="emitBack"  />
  <Footer />
</div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  data() {
    return {
      message: ""
    }
  },
  components: {
    Header,
    Footer
  },
  methods: {
    emitBack (message) {
      this.message = message
    },
    resetMessage () {
      this.message = ""
    }
  }
}
</script>