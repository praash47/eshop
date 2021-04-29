<template>
    <div class="wishlist-container">
      <!-- Breadcrumbs -->
      <div class="breadcrumbs">
        <div class="container">
          <div class="row">
            <div class="col-12">
              <div class="bread-inner">
                <ul class="bread-list">
                  <li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
                  <li class="active"><router-link to="wishlist">Wishlist</router-link></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- End Breadcrumbs -->
    <ProductsShowcase title="Wishlist" :data="trendings" />
    </div>
</template>
<script>
import ProductsShowcase from '../../components/home/ProductsShowcase.vue'

export default {
  name: 'Wishlist',
  components: {
    ProductsShowcase,
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
      ]
    }
  }
}
</script>