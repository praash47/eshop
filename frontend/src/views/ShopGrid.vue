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
                                    <li v-for="(values, cat, index) in cats" :key="index">
                                        <router-link :to="'/shop-grid/' + cat.toLowerCase()">{{ cat }}</router-link>
                                    </li>
                                </ul>
                            </div>
                            <!--/ End Single Widget -->
                            <!-- Single Widget -->
                            <div class="single-widget category">
                                <h3 class="title">Sub Categories</h3>
                                <ul class="categor-list" v-if="cats">
                                    <p style="color: red; opacity: 0.5;">Select a category here to see the list of sub-categories</p>
                                </ul>
                                <ul class="categor-list" v-else>
                                    <li><a href="#">Forever</a></li>
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
                        <div class="row">
							<div class="col-12">
								<!-- Shop Top -->
								<div class="shop-top">
									<div class="shop-shorter">
										<div class="single-shorter">
											<label>Show :</label>
											<select style="display: none;">
												<option selected="selected">09</option>
												<option>15</option>
												<option>25</option>
												<option>30</option>
											</select><div class="nice-select" tabindex="0"><span class="current">09</span><ul class="list"><li data-value="09" class="option selected">09</li><li data-value="15" class="option">15</li><li data-value="25" class="option">25</li><li data-value="30" class="option">30</li></ul></div>
										</div>
										<div class="single-shorter">
											<label>Sort By :</label>
											<select style="display: none;">
												<option selected="selected">Name</option>
												<option>Price</option>
												<option>Size</option>
											</select><div class="nice-select" tabindex="0"><span class="current">Name</span><ul class="list"><li data-value="Name" class="option selected">Name</li><li data-value="Price" class="option">Price</li><li data-value="Size" class="option">Size</li></ul></div>
										</div>
									</div>
								</div>
								<!--/ End Shop Top -->
							</div>
						</div>
                        <div v-if="$route.params.catName" class="results">Showing you results of <strong>{{ $route.params.catName }}</strong><router-link class="close" to="/shop-grid">x</router-link></div>
                        <div class="product-grid">
                            <SingleProduct class="product-item" v-for="(item, index) in productslist" :key="index" :price="item.price" :name="item.product_name"
                            :img_path="'http://127.0.0.1:8000' + item.img1" />
                        </div>
					</div>
				</div>
			</div>
		</section>
		<!--/ End Product Style 1  -->
    </div>
</template>
<script>
import SingleProduct from '@/components/SingleProduct.vue'
export default {
    props: ['productslist', 'cats'],
    components: {
        SingleProduct
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
    },
    watch: {
        $route() {
            this.filterProductData()
        }
    },
    methods: {
        filterProductData: function () {
            // let subcats = ''
            // for (let cat in this.cats) {
            //     if(cat.toLowerCase() == this.$route.params.catName) {
            //         subcats = this.cats[cat]['subcatids']
            //     }
            // }
        }
    }
}
</script>
<style scoped>
.product-grid {
    width: 100%;
    margin: 20px auto;
    columns: 3;
    column-gap: 40px;
}
.product-grid .product-item {
    width: 100%;
    margin: 0 0 20px;
    padding: 10px;
    overflow: hidden;
    break-inside: avoid; 
}
@media (max-width: 1000px) {
    .product-grid {
        columns: 2;
    }
}
@media (max-width: 450px) {
    .product-grid {
        columns: 1;
    }
}
.results {
    background: lightgray;
    color: black;
    padding: 10px;
}
.close {
    cursor: pointer;
}
</style>