<template>
  <div class="app">
    <div class="row">      
      <Categories />
      <Slider/>
    </div>
    <FeaturedCats />
    <ProductsShowcase title="Featured Products" :products="featured_products" />
    <ProductsShowcase title="Trending Items" :products="trending_products"/>
    <ProductsShowcase title="New Arrivals" :products="latest_products" />
    <ProductsShowcase title="Offers" :products="offer_products" />
  </div>
</template>

<script>
import Categories from '../components/home/Categories.vue'
import Slider from '../components/home/Slider.vue'
import FeaturedCats from '../components/home/FeaturedCats.vue'
import ProductsShowcase from '../components/home/ProductsShowcase.vue'
import { sendRequest } from './functions'

export default {
  name: 'EshopHome',
  components: {
    Categories,
    Slider,
    FeaturedCats,
    ProductsShowcase
  },
  mounted () {
    this.fetchAllProducts()
  },
  data () {
    return {
      categories: {},
      latest_products: "",
      trending_products: "",
      featured_products: ""
    }
  },
  computed: {
    offer_products() {
      return this.$store.state.offers
    }
  },
  methods: {
    fetchAllProducts () {
      this.fetchProductsByType("latest_products")
      this.fetchProductsByType("trending_products")
      this.fetchFeaturedProducts()
    },
    async fetchProductsByType (products_type) {
      let data = {
        "needed": products_type
      }
      let req = await sendRequest('server/products/', data)
      this[products_type] = req.data
    },
    async fetchFeaturedProducts () {
      let req = await sendRequest('server/featured_products/')
      this.featured_products = req.data
    }
  }
}

</script>

<style>
</style>
