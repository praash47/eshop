<template>
  <div>
    <!-- Breadcrumbs -->
    <div class="breadcrumbs">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="bread-inner">
                        <ul class="bread-list">
                            <li><router-link to="/">Home</router-link><i class="ti-arrow-right"></i></li>
                            <li>
                              <router-link :to="'/shop-grid/' + category_name">
                                {{ category_name }}
                              </router-link><i class="ti-arrow-right"></i>
                            </li>
                            <li>
                              <router-link :to="'/shop-grid/' + category_name + '/' + subcategory_name">
                                {{ subcategory_name }}
                              </router-link><i class="ti-arrow-right"></i>
                            </li>
                            <li>{{ product.product_name }}</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- End Breadcrumbs -->
    <!-- main product card -->
    <div class="card">
      <div class="card-body">
        <h1 class="card-title">{{ product.product_name }}</h1>
        <div class="row">
          <!-- product image section -->
          <div class="col-md-6 col-sm-12">
            <img :src="'http://127.0.0.1:8000' + product.img1" :alt="product.product_name">
          </div>

          <!-- product description section -->
          <div class="col-md-6 col-sm-12">
            <span class="price">Rs. {{ product.price }}</span>
            <h2>Description</h2>
            <p>{{ product.description }}</p><br>
            <p>
              <span :class="colorCodeInStock">
                <strong>In stock:</strong> {{ product.stock_num }} | 
              </span>
              <strong>Views:</strong> {{ product.views }}<br>
              <strong >Rating: </strong>
              <star-rating :star-size="25" 
                           :inline=true
                           :show-rating=false
                           v-model:rating="rated_value"
                             />
              <button class="btn btn-sm" v-if="rated_value > 0" @click="rated_value = 0">
                Reset
              </button>
            </p><br>
            <details>
              <summary style="cursor: pointer;">Click to show product ratings</summary>
              <div>
                <p>Please login so that your rating shows up here.</p>
                <span v-for="rating in ratings" :key="rating.id">
                  <label>User id: {{ rating.user }} - </label> 
                  <star-rating :star-size="15" 
                           :inline=true
                           :read-only=true
                           :rating=rating.rating_value
                             /> |
                </span>
              </div>
            </details>
            <span class="order-section">
              <span id="order" v-if="productHasQuantity">
                <button @click="plus()">+</button>
                  <input type="text" :value="quantity" readonly="readonly" style="width: 20px;"> 
                <button @click="minus()">-</button>
              </span>
              <span id="order" v-else-if="product.in_stock">
                <button class="btn" @click="plus()">
                  <i class="ti-shopping-cart"></i> Add to Cart
                </button>
              </span> 
              <button class="btn" v-if="isInWishlist" @click="removeFromWishlist()">
                <i class="fa fa-times" aria-hidden="true"></i> Remove from Wishlist
              </button>
              <button class="btn wishlist" v-else @click="addToWishlist()">
                <i class="fa fa-heart-o" aria-hidden="true"></i> Add to Wishlist
              </button>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import stateMixins from '../mixins/stateMixins'
import fetch from '../mixins/fetch'
import { sendRequest } from './functions'
import StarRating from 'vue-star-rating'

export default {
  name: 'Product',
  mixins: [fetch, stateMixins],
  components: {
    StarRating
  },
  data () {
    return {
      product: "",
      ratings: "",
      rated_value: 0,
      hasUserRated: false,
    }
  },
  watch: {
    rated_value () {
      if (this.$store.state.user) {
        this.fetchRating()
      }
    }
  },
  mounted () {
    this.fetchProduct()
    this.fetchRating()
    this.backUpViews()
  },
  computed: {
    colorCodeInStock () {
      if(this.product.in_stock) {
        return 'text-success'
      }
      return 'text-danger'
    },
    productHasQuantity () {
      return this.$store.getters.productQuantity(this.product) > 0
    },
    quantity () {
      return this.$store.getters.productQuantity(this.product)
    },
    subcategory_name () {
      for (let i = 0; i < this.subcategories.length; i++) {
        if (this.product.sub_category == this.subcategories[i].id) {
          return this.subcategories[i].subcat_name.toLowerCase()
        }  
      }
      return null
    },
    category_name () {
      for (let i = 0; i < this.subcategories.length; i++) {
        if (this.product.sub_category == this.subcategories[i].id) {
          for (let j = 0; j < this.categories.length; j++) {
            if (this.subcategories[i].category == this.categories[j].id) {
              return this.categories[j].cat_name.toLowerCase()
            }
          } 
        }  
      }
      return null
    }
  },
  methods: {
    async fetchProduct () {
      const product_name = this.$route.params.product_name
      let data = {
        "needed": "single_product",
        "product_name": product_name
      }
      let req = await sendRequest('server/products/', data)
      this.product = req.data[0]
      this.$store.commit('updateViews', this.product)
    },
    async fetchRating () {
      // Know about the values
      let data = {
        "user_name": this.$store.state.user,
        "rating_option": "",
        "rating_value": this.rated_value,
        "product_name": this.$route.params.product_name
      }

      if(!this.hasUserRated && this.rated_value > 0) {
        data.rating_option = "add"
      }
      else if(this.hasUserRated && this.rated_value > 0) {
        data.rating_option = "update"
      }
      else if(this.hasUserRated && this.rated_value == 0) {
        data.rating_option = "delete"
      }

      let req = await sendRequest('server/ratings/', data)
      this.ratings = req.data
      this.assignUserRating()
    },
    async assignUserRating () {
      if (this.$store.state.user) {
        // Get to know if user has already rated
        let data = {
          "user": this.$store.state.user,
          "purpose": "get_id_from_name"
        }
        let req = await sendRequest('server/customer/', data)

        let [hasUserRated, rating] = this.checkUserRated(req)
        
        if (hasUserRated) {
          this.rated_value = rating.rating_value
        }
        this.hasUserRated = hasUserRated
      }
    },    
    checkUserRated (req) {
      if (this.ratings) {
        let rating = this.ratings.find(i => i.user === req.data.id)
        if(rating) {
          return [true, rating]
        }
      }
      return [false, null]
    },
    async backUpViews() {
      const timeInSecToBackup = 60
      const now = new Date()
      const prev_time = new Date(localStorage.getItem('lastViewsBackup'))
      localStorage.setItem('lastViewsBackup', now)
      if (prev_time) {
        if ((now - prev_time) >= timeInSecToBackup * 1000) {
          if(this.$store.state.user) {
            let data = {
              username: this.$store.state.user,
              views: localStorage.getItem('views')
            }
            await sendRequest('server/views/', data)
          }
        }
      }  
    }
  }
}
</script>
<style scoped>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}
.price, .order-section {
  display: block;
  margin: 50px 0;
}
.price {font-size: 3rem;}
.order-section input {
  width: 50px;
  margin-right: 20px;
  margin-left: 10px;
}
.order-section .submit {
  width: 100px;
  height: 40px;
  background: #2ECC40;
  color: #fff;
}
.btn.wishlist {
  background: #FF4136;
  margin-left: 5px;
}
</style>
