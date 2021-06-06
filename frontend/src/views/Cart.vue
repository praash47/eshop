<template>
  <div class="cart-container">
    <!-- Breadcrumbs -->
    <div class="breadcrumbs">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="bread-inner">
              <ul class="bread-list">
                <li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
                <li class="active"><router-link to="/cart">Cart</router-link></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- End Breadcrumbs -->
        
    <!-- Shopping Cart -->
    <div class="shopping-cart section">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <!-- Shopping Summery -->
            <table class="table shopping-summery">
              <thead>
                <tr class="main-hading">
                  <th>PRODUCT</th>
                  <th>NAME</th>
                  <th class="text-center">UNIT PRICE</th>
                  <th class="text-center">QUANTITY</th>
                  <th class="text-center">TOTAL</th> 
                </tr>
              </thead>
              <tbody>
                <tr v-for="item in cart" :key="item.id">
                  <td class="image" data-title="No">
                  <router-link :to="'/product/' + item.product_name">
                    <img :src="'http://192.168.5.113:8000' + item.img1" :alt="item.product_name">
                  </router-link>
                  </td>
                  <td class="product-des" data-title="Description">
                  <router-link :to="'/product/' + item.product_name">
                    <p class="product-name">{{ item.product_name }}</p>
                  </router-link>
                  </td>
                  <td class="price" data-title="Price"><span>Rs. {{ item.price }} </span></td>
                  <td class="qty" data-title="Qty"><!-- Input Order -->
                    <button @click="plus(item)">+</button>
                      <input type="text" :value="item.quantity" readonly="readonly" style="width: 20px;"> 
                    <button @click="minus(item)">-</button>
                    <!--/ End Input Order -->
                  </td>
                  <td class="total-amount" data-title="Total"><span>Rs. {{ item_total(item) }}</span></td>
                </tr>
              </tbody>
            </table>
            <!--/ End Shopping Summery -->  
          </div>
        </div>
        <div class="row">
          <div class="col-12">
            <!-- Total Amount -->
            <div class="total-amount">
              <div class="row">
                <div class="col">
                  <div class="right">
                    <ul>
                      <li>Cart Subtotal<span>Rs. {{ cart_total }}</span></li>
                      <li>Shipping<span>Free</span></li>
                      <li class="last">You Pay <span>Rs. {{ cart_total }}</span></li>
                    </ul>
                    <div class="button5">
                      <router-link to="checkout" class="btn">Checkout</router-link>
                      <router-link to="shop-grid" class="btn">Continue shopping</router-link>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!--/ End Total Amount -->
          </div>
        </div>
      </div>
    </div>
	<!--/ End Shopping Cart -->
  </div>
</template>
<script>
import stateMixins from '../mixins/stateMixins'

export default {
  name: 'Cart',
  mixins: [stateMixins]
}
</script>
<style scoped>
.cart {
  margin: 20px;
}
.cart h1 {
  margin: 20px;
}
</style>
