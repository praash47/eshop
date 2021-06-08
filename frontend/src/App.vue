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
import { sendRequest } from './views/functions'

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

    this.fetchOffers()
  },
  methods: {
    emitBack (message) {
      // emitting the message received from child for displaying in message box.
      this.message = message
    },
    resetMessage () {
      this.message = ""
    },
    async fetchOffers() {
      let req = await sendRequest('server/offers/')
      let offer_info = req.data.offer_info
      let offer_products = req.data.offer_products
      for (let i in offer_info) {
        let id = offer_products[i].id
        let offer = offer_info.find(i => i.product == id)
        let offer_price = offer.offer_price
        this.$store.state.offers.push({...offer_products[i], offer_price: offer_price})
      }
    }
  }
}
</script>