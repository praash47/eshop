<template>
<div id="app">
  <Header />
  <router-view :productslist="products"/>
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
import {sendRequest} from './views/request'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  data() {
    return {
      products: []
    }
  },
  components: {
    Header,
    Footer
  },
  mounted () {
    this.fetchProducts()
  },
  methods: {
    fetchProducts: function() {
      var vm = this;
      let data = {
        'type': 'fetch',
        'to': 'all_products'
      };
      let r = sendRequest('post', 'http://127.0.0.1:8000/server/products/', data);
      r.then(function(response) {
        vm.products = response['data']
      })
      .finally(function() {
        setTimeout(vm.fetchProducts, 1000)
      });
    }
  }
}
</script>