<template>
  <div class="app">
    <div class="row">      
      <Categories />
      <Slider />
    </div>
    <FeaturedCats />
    <ProductsShowcase title="Featured Products" :data="products" />
    <ProductsShowcase title="Trending Items" :data="trendings"/>
    <ProductsShowcase title="New Arrivals" :data="trendings" />
    <ProductsShowcase title="Offers" :data="trendings" />
  </div>
</template>

<script>
import Categories from '../components/home/Categories.vue'
import Slider from '../components/home/Slider.vue'
import FeaturedCats from '../components/home/FeaturedCats.vue'
import ProductsShowcase from '../components/home/ProductsShowcase.vue'

export default {
  name: 'Eshop',
  components: {
    Categories,
    Slider,
    FeaturedCats,
    ProductsShowcase
  },
  data () {
    return {
      trendings: [
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
      products: '',
    }
  }
}
</script>

<style>
</style>
