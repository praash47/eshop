<template>
<div id="app">
  <Header :message="message" @modalclosed="resetMessage" />
  <router-view @successAuthMessage="emitBack" />
  <Recommendation />
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
import Recommendation from './components/Recommendation.vue'

export default {
  data() {
    return {
      message: "",
      trending_products: '',
    }
  },
  components: {
    Header,
    Footer,
    Recommendation
  },
  mounted () {
    const views = JSON.parse(localStorage.getItem('views'))
    if (views) this.$store.state.views = views

    const wishlist = JSON.parse(localStorage.getItem('wishlist'))
    if (wishlist) this.$store.state.wishlist = wishlist
  },
  methods: {
    emitBack (message) {
      // emitting the message received from child for displaying in message box.
      this.message = message
    },
    resetMessage () {
      this.message = ""
    }
  }
}
</script>