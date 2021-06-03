<template>
    <div class="checkout-container">
		<div v-if="user_logged_in">
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
								<p>Please shop more even after checkout!</p>
								<!-- Form -->
								<UserDetailsAddEdit type="Update" />
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
											<li>Sub Total<span>Rs. {{ cart_total }}</span></li>
											<li>Shipping<span>Free</span></li>
											<li class="last">Total<span>Rs. {{ cart_total }}</span></li>
										</ul>
									</div>
								</div>
								<!--/ End Order Widget -->
								<!-- Order Widget -->
								<form v-on:submit.prevent="order">
								<div class="single-widget">
									<h2>Payments</h2>
									<div class="content">
										<input name="payment" id="1" type="radio" required="required"> <label for="1">eSewa</label><br>
										<input name="payment" id="2" type="radio" required="required"> <label for="2">Cash On Delivery</label><br>
										<input name="payment" id="3" type="radio" required="required"> <label for="3">PayPal</label>
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
											<button type="submit" class="btn" v-if="cart_total > 0">
												Proceed to payment
											</button>
										</div>
									</div>
								</div>
								<!--/ End Button Widget -->
								</form>
							</div>
						</div>
					</div>
				</div>
			</section>
			<!--/ End Checkout -->
		</div>
		<LoginToView type="page" v-else/>
    </div>
</template>
<script>
import UserDetailsAddEdit from '../../components/user/UserDetailsAddEdit.vue'
import LoginToView from '../../components/LoginToView.vue'
import stateMixins from '../../mixins/stateMixins'
import { sendRequest } from '../../views/functions'

export default {
    name: 'Checkout',
    mixins: [stateMixins],
	emits: ['successAuthMessage'],
    components: {
        UserDetailsAddEdit,
		LoginToView
    },
	methods: {
		async order () {
			let orderInfo = {
				"username": this.$store.state.user,
				"cancelId": "",
				"data": {
					"orderDetails": JSON.stringify(this.$store.state.cart),
					"total": this.cart_total
				}
			}
			let req = await sendRequest('server/orders/', orderInfo)

			if(req.data.success == "true") {
				this.$router.push('/orders')
				localStorage.setItem('cart', JSON.stringify([]))
				this.$store.state.cart = []
				this.$emit('successAuthMessage', 'Order Placement Sucessful!')
			}
		}
	}
}
</script>