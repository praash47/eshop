<template>
    <div>
      <div class="wishlist-container" v-if="user_logged_in">
        <!-- Breadcrumbs -->
        <div class="breadcrumbs">
          <div class="container">
            <div class="row">
              <div class="col-12">
                <div class="bread-inner">
                  <ul class="bread-list">
                    <li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
                    <li class="active"><router-link to="/wishlist">Wishlist</router-link></li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div><br>
        <!-- End Breadcrumbs -->
        <h1>Wishlist</h1>
        
        
        <div class="product-grid">
            <SingleProduct class="product-item" v-for="product in wishlist" :key="product.id"
            :product="product" @click="updateWishlist()"/>
        </div>
      </div>
      <LoginToView type="page" v-else/>
    </div>
</template>
<script>
import stateMixins from '../../mixins/stateMixins'
import LoginToView from '../../components/LoginToView.vue'
import SingleProduct from '../../components/SingleProduct.vue'

export default {
  name: 'Wishlist',
  mixins: [stateMixins],
  components: {
    LoginToView,
		SingleProduct
  },
  data () {
    return {
      wishlist: ''
    }
  },
  mounted () {
    this.wishlist = this.$store.state.wishlist
  },
  methods: {
    updateWishlist() {
      this.wishlist = this.$store.state.wishlist
    }
  }
}
</script>
<style scoped>
.product-grid {
    width: 100%;
    margin: 20px auto;
    columns: 5;
    column-gap: 40px;
}
.product-grid .product-item {
    width: 100%;
    margin: 0 0 20px;
    padding: 10px;
    overflow: hidden;
    break-inside: avoid; 
}
@media (max-width: 1200px) {
    .product-grid {
        columns: 4;
    }
}
@media (max-width: 1000px) {
    .product-grid {
        columns: 3;
    }
}
@media (max-width: 750px) {
    .product-grid {
        columns: 2;
    }
}
@media (max-width: 500px) {
    .product-grid {
        columns: 1;
    }
}
</style>