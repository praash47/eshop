<template>
  <div class="app">
    <div class="row">      
      <Categories />
      <Slider />
    </div>
    <FeaturedCats />
    <ProductsShowcase title="Featured Products" :products="test_products" />
    <ProductsShowcase title="Trending Items" :products="test_products"/>
    <ProductsShowcase title="New Arrivals" :products="latest_products" />
    <ProductsShowcase title="Offers" :products="test_products" />
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
      test_products: [
        {'id': 0, 'product_name': 'Book', 'price': 6000},
        {'id': 1, 'product_name': 'Wool', 'price': 6000},
        {'id': 2, 'product_name': 'Khadkulo', 'price': 10000},
        {'id': 3, 'product_name': 'Water Bottle', 'price': 145000},
        {'id': 4, 'product_name': 'Wooden Bed', 'price': 2000},
        {'id': 5, 'product_name': 'Sofa', 'price': 1500},
        {'id': 6, 'product_name': 'Cupboard', 'price': 400},
        {'id': 7, 'product_name': 'Fan', 'price': 600},
        {'id': 8, 'product_name': 'Clock', 'price': 300},
      ],
      categories: {},
      latest_products: ""
    }
  },
  methods: {
    fetchAllProducts () {
      this.fetchLatestProducts()
    },
    async fetchLatestProducts () {
      let data = {
        "needed": "latest_products"
      }
      let req = await sendRequest('server/products/', data)
      this.latest_products = req.data
    }
  }
}

</script>

<style>
</style>
