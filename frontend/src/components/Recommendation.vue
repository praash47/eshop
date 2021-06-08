<template>
    <div class="recommendation">      
    <div id="mySidenav" class="sidenav" :style="'width: ' + width">
        <a class="closebtn" @click="closeNav">&times;</a>
        <products-showcase title="Recommendations" :products="recommended_products"/>
    </div>

    <span class="recommendation-button" @click="openNav"><i class="fa fa-commenting"></i><br>Recommendations</span>
    </div>
</template>
<script>
import ProductsShowcase from './home/ProductsShowcase.vue'
import { sendRequest } from '@/views/functions.js'

export default {
    name: 'Recommendation',
    components: { ProductsShowcase },
    data () {
        return {
            width: '0',
            recommended_products: ''
        }
    },
    watch: {
      trendingProducts () {
        this.getRecommendations()
      }
    },
    mounted() {
      const to_update_in = 5000
      setInterval(this.getRecommendations, to_update_in)
    },
    methods: {
        openNav () {
          this.width = '100%'
        },
        closeNav () {
          this.width = '0'
        },
        getRecommendations () {
          if(this.$store.state.user) {
            this.fetchRecommendations()
          } else {
            this.fetchProductsByType("trending_products")
          }
        },  
        async fetchRecommendations () {
          let data = {
            "username": this.$store.state.user,
            "wishlist": this.$store.state.wishlist
          }
          let req = await sendRequest('server/recommendations/', data)
          this.recommended_products = req.data
          if (Object.keys(req.data).length === 0) {
            // if object is empty, simply populate with trending_products.
            this.fetchProductsByType("trending_products")
          }
        },
        async fetchProductsByType (products_type) {
          let data = {
            "needed": products_type
          }
          let req = await sendRequest('server/products/', data)
          this.recommended_products = req.data
        }
    }
}

</script>
<style>
body {
  max-width: 100%;
  box-sizing: border-box;
  overflow-x: hidden;
}
.recommendation-button {
  position: fixed;
  z-index: 10;
  top: 15%;
  right: 0;
  width: 80px;
  height: 300px;
  padding: 10px;
  background: rgb(255, 145, 0);
  box-shadow: 2px 2px 15px rgba(#000, .1);
  writing-mode: vertical-rl;
  cursor: pointer;
  color: white;
  font-size: 30px;
}
.sidenav {
  height: 100%;
  width: 0;
  position: fixed;
  z-index: 999;
  top: 0;
  left: 0;
  background-color: #fff;
  border-right: 1px solid gray;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
  text-align:center;
}

.sidenav a {
  padding: 8px 8px 8px 32px;
  text-decoration: none;
  font-size: 25px;
  color: #818181;
  display: block;
  transition: 0.3s;

}

.sidenav a:hover{
  color: #f1f1f1;
}

.sidenav .closebtn {
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 50px;
  cursor: pointer;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
  body {
    width: 100%;
  }
}
</style>