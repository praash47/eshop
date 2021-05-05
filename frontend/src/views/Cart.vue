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
                  <th class="text-center"><i class="ti-trash remove-icon"></i></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="image" data-title="No"><img src="https://via.placeholder.com/100x100" alt="#"></td>
                  <td class="product-des" data-title="Description">
                    <p class="product-name"><a href="#">Women Dress</a></p>
                    <p class="product-des">Maboriosam in a tonto nesciung eget  distingy magndapibus.</p>
                  </td>
                  <td class="price" data-title="Price"><span>Rs. 110.00 </span></td>
                  <td class="qty" data-title="Qty"><!-- Input Order -->
                    <input type="number" style="max-width:100px;">
                    <!--/ End Input Order -->
                  </td>
                  <td class="total-amount" data-title="Total"><span>Rs. 220.88</span></td>
                  <td class="action" data-title="Remove"><a href="#"><i class="ti-trash remove-icon"></i></a></td>
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
                      <li>Cart Subtotal<span>Rs. 330.00</span></li>
                      <li>Shipping<span>Free</span></li>
                      <li class="last">You Pay<span>Rs. 310.00</span></li>
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
export default {
  name: 'Cart',
  data () {
      return {
      }
  }
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
