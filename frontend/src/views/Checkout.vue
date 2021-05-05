<template>
    <div class="checkout-container">
        <!-- Breadcrumbs -->
		<div class="breadcrumbs">
			<div class="container">
				<div class="row">
					<div class="col-12">
						<div class="bread-inner">
							<ul class="bread-list">
								<li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
								<li><router-link to="/cart">Cart<i class="ti-arrow-right"></i></router-link></li>
								<li class="active"><router-link to="/checkout">Checkout</router-link></li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- End Breadcrumbs -->
				
		<!-- Start Checkout -->
		<section class="shop checkout section">
			<div class="container">
				<div class="row"> 
					<div class="col-lg-8 col-12">
						<div class="checkout-form">
							<h2>Make Your Checkout Here</h2>
							<p>Please register in order to checkout more quickly</p>
							<!-- Form -->
                            <UserDetailsAddEdit />
							<!--/ End Form -->
						</div>
					</div>
					<div class="col-lg-4 col-12">
						<div class="order-details">
							<!-- Order Widget -->
							<div class="single-widget">
								<h2>CART TOTALS</h2>
								<div class="content">
									<ul>
										<li>Sub Total<span>Rs. 330.00</span></li>
										<li>Shipping<span>Free</span></li>
										<li class="last">Total<span>Rs. 340.00</span></li>
									</ul>
								</div>
							</div>
							<!--/ End Order Widget -->
							<!-- Order Widget -->
							<div class="single-widget">
								<h2>Payments</h2>
								<div class="content">
                                    <input name="payment" id="1" type="radio"> <label for="1">eSewa</label><br>
                                    <input name="payment" id="2" type="radio"> <label for="2">Cash On Delivery</label><br>
                                    <input name="payment" id="3" type="radio"> <label for="3">PayPal</label>
								</div>
							</div>
							<!--/ End Order Widget -->
							<!-- Payment Method Widget -->
							<div class="single-widget payement">
								<div class="content">
									<img src="images/payment-method.png" alt="#">
								</div>
							</div>
							<!--/ End Payment Method Widget -->
							<!-- Button Widget -->
							<div class="single-widget get-button">
								<div class="content">
									<div class="button">
										<router-link to="orders" class="btn">Proceed to payment</router-link>
									</div>
								</div>
							</div>
							<!--/ End Button Widget -->
						</div>
					</div>
				</div>
			</div>
		</section>
		<!--/ End Checkout -->
    </div>
</template>
<script>
import UserDetailsAddEdit from '../components/user/UserDetailsAddEdit.vue'
export default {
    name: 'Checkout',
    components: {
        UserDetailsAddEdit,
    }
}
</script>