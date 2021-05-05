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
								<li class="active"><router-link to="/shop-grid">Shop Grid</router-link></li>
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
                                    <p>Add your price range</p>
                                    <div class="price-filter-inner">
                                        <input type="text" placeholder="Lower Price" style="width: 90px;"> - 
                                        <input type="text" placeholder="Higher Price" style="width: 90px;">
                                    </div>
                                </div>
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
                                <ul class="categor-list" v-if="$route.params.catName">
                                    <span v-for="(values, cat, index) in cats" :key="index">
                                        <li v-for="subcat in values.subcats" :key="subcat">
                                        <router-link :to="'/shop-grid/' + cat.toLowerCase() + '/' + subcat.toLowerCase()" v-if="cat.toLowerCase() == $route.params.catName">{{ subcat }}</router-link>
                                        </li>
                                    </span>
                                </ul>
                                <ul class="categor-list" v-else>
                                    <p style="color: red; opacity: 0.5;">Select a category here to see the list of sub-categories</p>
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
											<label>Sort By :</label>
                                            <div class="nice-select" tabindex="0">
                                                <span class="current">None</span>
                                                <ul class="list">
                                                    <li class="option selected">None</li>
                                                    <li class="option">Name</li>
                                                    <li class="option">Price</li>
                                                </ul>
                                            </div>
										</div>
										<div class="single-shorter">
											<label>Order :</label>
                                            <div class="nice-select" tabindex="0">
                                                <span class="current">Ascending</span>
                                                <ul class="list">
                                                    <li class="option selected">Ascending</li>
                                                    <li class="option">Descending</li>
                                                </ul>
                                            </div>
										</div>
									</div>
								</div>
								<!--/ End Shop Top -->
							</div>
						</div>
                        <div v-if="$route.params.catName || $route.query.search" class="results">Showing you results of <strong>{{ $route.params.catName }} <span v-if="$route.params.subCatName"><i class="ti-arrow-right"></i> {{ $route.params.subCatName }}</span></strong>
                        <span v-if="$route.query.search">search term <strong>'{{ $route.query.search }}'</strong></span>
                        <span class="close" @click="clear">x</span></div>
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
import { sendRequest } from './functions'

export default {
    props: ['cats'],
    components: {
        SingleProduct
    },
    created () {
        this.filterByCategory()
        this.fetchProducts()
        setInterval(this.fetchProducts, 1000)
    },
    data () {
        return {
            needed: "all_products",
            filtering_by: [],
            search_term: "",
            subcategory: [],
            price_low: 5000,
            price_high: 80000,
            sorting: "False",
            sorted_by: "price",
            ordered_by: "desc",
            productslist: ''
        }
    },
    watch: {
        $route() {
            this.filterByCategory()
            this.filterBySearchTerm()
            console.log(this.filtering_by)                    
        }
    },
    methods: {
        fetchProducts: function () {
            let vm = this
            let data = {
                "needed": vm.needed,
                "filtering_by": vm.filtering_by,
                "search_term": vm.search_term,
                "subcategory": vm.subcategory, 
                "price_low": vm.price_low,
                "price_high": vm.price_high,
                "sorting": vm.sorting,
                "sorted_by": vm.sorted_by,
                "ordered_by": vm.ordered_by
            }
            let r = sendRequest('post', 'http://127.0.0.1:8000/server/products/', data);
            r.then(function(response) {
                vm.productslist = response['data']
            })  
        },
        filterByCategory: function () {
            let vm = this
            
            if (vm.$route.params.catName) {
                vm.needed = "filtered_orand_sorted"
                vm.filtering_by.push("subcategory")
                for (let cat in vm.cats) {
                    if(cat.toLowerCase() == vm.$route.params.catName && !vm.$route.params.subCatName){
                        vm.subcategory = vm.cats[cat]['subcatids']
                    }
                    else if(cat.toLowerCase() == vm.$route.params.catName && vm.$route.params.subCatName){
                        vm.filterBySubCategory(cat)
                    }
                }
            }
        },
        filterBySubCategory: function (cat) {
            let vm = this
            let index = -1
            let subcats = vm.cats[cat]['subcats']
            for (let subcat in subcats) {
                index += 1
                if(subcats[subcat].toLowerCase() == vm.$route.params.subCatName) {
                    vm.subcategory = []
                    vm.subcategory.push(vm.cats[cat]['subcatids'][index])
                }
            }
        },
        filterBySearchTerm: function () {
            let vm = this

            if (vm.$route.query.search) {
                vm.needed = "filtered_orand_sorted"
                vm.filtering_by.push("search_term")
                vm.searchTerm = vm.$route.query.search
            }
        },
        clear: function () {
            this.needed = 'all_products'
            this.$router.push('/shop-grid')
        }
    },
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