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
                                        <input type="text" placeholder="Lower Price" style="width: 90px;" v-model="toFilter.price_low"> - 
                                        <input type="text" placeholder="Higher Price" style="width: 90px;" v-model="toFilter.price_high">
                                    </div>
                                </div>
                            </div>
                            <!--/ End Shop By Price -->
                            <!-- Single Widget -->
                            <div class="single-widget category">
                                <h3 class="title">Categories</h3>
                                <ul class="categor-list">
                                    <li v-for="cat in categories" :key="cat.id">
                                        <router-link :to="'/shop-grid/' + cat.cat_name.toLowerCase()">{{ cat.cat_name }}</router-link>
                                    </li>
                                </ul>
                            </div>
                            <!--/ End Single Widget -->
                            <!-- Single Widget -->
                            <div class="single-widget cat-egory">
                                <h3 class="title">Sub Categories</h3>
                                <ul class="categor-list" v-if="$route.params.catName">
                                    <span v-for="subcategory in subcategories" :key="subcategory.id">
                                        <li v-if="subcategory.category == curr_cat_id">
                                            <router-link :to="'/shop-grid/' + $route.params.catName.toLowerCase()
                                            + '/' + subcategory.subcat_name.toLowerCase()">
                                                {{ subcategory.subcat_name }}
                                            </router-link>
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
                                <h3 class="title">Recommendations</h3>f
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
                        <div v-if="$route.params.catName || $route.query.search || toFilter.price_low || toFilter.price_high" class="results">Showing you results of <strong>{{ $route.params.catName }}
                        <span v-if="$route.params.subCatName"><i class="ti-arrow-right"></i> {{ $route.params.subCatName }} </span></strong>
                        <span v-if="price_low || price_high">price range: <strong>{{ toFilter.price_low }} - {{ toFilter.price_high }} </strong></span>
                        <span v-if="$route.query.search">search term <strong>'{{ $route.query.search }}'</strong></span>
                        <span class="close" @click="clear">x</span></div>
                        <div class="product-grid">
                            <SingleProduct class="product-item" v-for="(item, index) in productslist" :key="index" :price="item.price" :name="item.product_name"
                            :img_path="'-http://127.0.0.1:8000' + item.img1" />
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
import { sendRequest } from '../views/functions'
import fetch from '../mixins/fetch'

export default {
    name: 'ShopGrid',
    mixins: [fetch],   
    components: {
        SingleProduct
    },
    created () {
        // fetching products
        this.fetchProducts()
    },
    data () {
        return {
            toFilter: {    
                needed: "all_products",
                filtering_by: [],
                search_term: "",
                subcategory: [],
                price_low: "",
                price_high: "",
                sorting: "",
                sorted_by: "",
                ordered_by: "desc",
            },
            productslist: '',
            curr_cat_id : '',
            curr_subcat_id: ''
        }
    },
    watch: {
        $route () {
            this.fetchCategories()
            this.filterByCategory()
            this.fetchProducts()
        }
    },
    methods: {
        // Filtering
        filterByCategory: function () {
            let vm = this
            console.log("filtering by ")

            // If category is selected
            if (vm.curr_cat_id) {
                console.log("category ")
                const filter = vm.toFilter
                filter.needed = "filtered_orand_sorted"

                // If it is not already filtering by subcategory, then add subcategory to filtering by
                if (!filter.filtering_by.includes("subcategory")) {
                    filter.filtering_by.push("subcategory")
                }

                // If subcategory is selected
                if (vm.curr_subcat_id) {
                    filter.subcategory = []  // empty it
                    filter.subcategory.push(vm.curr_subcat_id)
                }

                // If only category
                else {
                    console.log("only c")
                    let catPresent = (filter.subcategory.length == 0 ) ?
                                        false :
                                        filter.subcategory.every(vm.checkSubCatPresent)
                    console.log(catPresent)
                    if (!catPresent) {
                        filter.subcategory = []
                        filter.subcategory = vm.getSubcatIdsByCatId()
                    }
                }
            }

            // If no category or sub-category selected
            else {
                vm.needed = "all_products" 
            }
        },
        checkSubCatPresent: function (id) {
            let subcatids = this.getSubcatIdsByCatId()
            return subcatids.includes(id)
        },

        // Fetch Products
        fetchProducts: async function () {
            let products = await sendRequest('http://127.0.0.1:8000/server/products/', this.toFilter)
            this.productslist = products.data
        },

        getSubcatIdsByCatId: function () {
            let subcategoryids = [], vm = this
            for (const subcategoryIndex in vm.subcategories) {
                if (vm.subcategories[subcategoryIndex]['category'] == vm.curr_cat_id)
                    subcategoryids.push(vm.subcategories[subcategoryIndex]['id'])
            }
            return subcategoryids
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