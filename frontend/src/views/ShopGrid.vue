<template>
    <div class="shop-grid-container">
        <!-- Breadcrumbs -->
		<div class="breadcrumbs">
			<div class="container">
				<div class="row">
					<div class="col-12">
						<div class="bread-inner">
							<ul class="bread-list">
								<li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
								<li class="active"><router-link to="shop-grid">Shop Grid</router-link></li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- End Breadcrumbs -->
		
		<!-- Product Style -->
		<section class="product-area shop-sidebar shop section">
			<div class="container">
				<div class="row">
					<div class="col-lg-3 col-md-4 col-12">
						<div class="shop-sidebar">
                            <!-- Shop By Price -->
                            <div class="single-widget range">
                                <h3 class="title">Shop by Price</h3>
                                <div class="price-filter">
                                    <div class="price-filter-inner">
                                        <div id="slider-range"></div>
                                            <div class="price_slider_amount">
                                            <div class="label-input">
                                                <span>Range:</span><input type="text" id="amount" name="price" placeholder="Add Your Price"/>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <ul class="check-box-list">
                                    <li>
                                        <label class="checkbox-inline" for="1"><input name="news" id="1" type="checkbox">$20 - $50<span class="count">(3)</span></label>
                                    </li>
                                    <li>
                                        <label class="checkbox-inline" for="2"><input name="news" id="2" type="checkbox">$50 - $100<span class="count">(5)</span></label>
                                    </li>
                                    <li>
                                        <label class="checkbox-inline" for="3"><input name="news" id="3" type="checkbox">$100 - $250<span class="count">(8)</span></label>
                                    </li>
                                </ul>
                            </div>
                            <!--/ End Shop By Price -->
                            <!-- Single Widget -->
                            <div class="single-widget category">
                                <h3 class="title">Categories</h3>
                                <ul class="categor-list">
                                    <li><a href="#">T-shirts</a></li>
                                    <li><a href="#">jacket</a></li>
                                    <li><a href="#">jeans</a></li>
                                    <li><a href="#">sweatshirts</a></li>
                                    <li><a href="#">trousers</a></li>
                                    <li><a href="#">kitwears</a></li>
                                    <li><a href="#">accessories</a></li>
                                </ul>
                            </div>
                            <!--/ End Single Widget -->
                            <!-- Single Widget -->
                            <div class="single-widget category">
                                <h3 class="title">Sub Categories</h3>
                                <ul class="categor-list">
                                    <li><a href="#">Forever</a></li>
                                    <li><a href="#">giordano</a></li>
                                    <li><a href="#">abercrombie</a></li>
                                    <li><a href="#">ecko united</a></li>
                                    <li><a href="#">zara</a></li>
                                </ul>
                            </div>
                            <!--/ End Single Widget -->
                            <!-- Single Widget -->
                            <div class="single-widget recent-post">
                                <h3 class="title">Recommendations</h3>
                                <!-- Single Post -->
                                <div class="single-post first">
                                    <div class="image">
                                        <img src="https://via.placeholder.com/75x75" alt="#">
                                    </div>
                                    <div class="content">
                                        <h5><a href="#">Girls Dress</a></h5>
                                        <p class="price">$99.50</p>
                                        <ul class="reviews">
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li><i class="ti-star"></i></li>
                                            <li><i class="ti-star"></i></li>
                                        </ul>
                                    </div>
                                </div>
                                <!-- End Single Post -->
                                <!-- Single Post -->
                                <div class="single-post first">
                                    <div class="image">
                                        <img src="https://via.placeholder.com/75x75" alt="#">
                                    </div>
                                    <div class="content">
                                        <h5><a href="#">Women Clothings</a></h5>
                                        <p class="price">$99.50</p>
                                        <ul class="reviews">
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li><i class="ti-star"></i></li>
                                        </ul>
                                    </div>
                                </div>
                                <!-- End Single Post -->
                                <!-- Single Post -->
                                <div class="single-post first">
                                    <div class="image">
                                        <img src="https://via.placeholder.com/75x75" alt="#">
                                    </div>
                                    <div class="content">
                                        <h5><a href="#">Man Tshirt</a></h5>
                                        <p class="price">$99.50</p>
                                        <ul class="reviews">
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                            <li class="yellow"><i class="ti-star"></i></li>
                                        </ul>
                                    </div>
                                </div>
                                <!-- End Single Post -->
                            </div>
                            <!--/ End Single Widget -->
						</div>
					</div>
					<div class="col-lg-9 col-md-8 col-12">
                        <ProductsShowcase :data="products" />
					</div>
				</div>
			</div>
		</section>
		<!--/ End Product Style 1  -->
    </div>
</template>
<script>
import ProductsShowcase from '@/components/home/ProductsShowcase.vue'
export default {
    props: ['products'],
    components: {
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
            ]
        }
    }
}
</script>