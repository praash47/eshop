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
                                        <input type="number" placeholder="Lower Price" style="width: 90px;" v-model="toFilter.price_low"> - 
                                        <input type="number" placeholder="Higher Price" style="width: 90px;" v-model="toFilter.price_high">
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
                                <h3 class="title">Recommendations</h3>
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
                                            <select v-model="toFilter.sorted_by">
                                                <option selected="selected" value="">none</option>
                                                <option>name</option>
                                                <option>price</option>
                                            </select>
										</div>
										<div class="single-shorter">
											<label>Order :</label>
                                            <select v-model="toFilter.ordered_by">
                                                <option selected="selected" value="">asc</option>
                                                <option>desc</option>
                                            </select>
										</div>
									</div>
								</div>
								<!--/ End Shop Top -->
							</div>
						</div>
                        <!-- If Catname or search_query or price low or high set, then -->
                        <div v-if="$route.params.catName || $route.query.search || toFilter.price_low || toFilter.price_high" class="results">
                            Showing you results of
                            <!-- categories and sub-categories -->
                            <strong v-if="$route.params.catName">
                                {{ $route.params.catName }}
                                <span v-if="$route.params.subCatName"><i class="ti-arrow-right"></i>
                                    {{ $route.params.subCatName }}
                                </span>
                            </strong>
                            <!-- price range -->
                            <span v-if="toFilter.price_low || toFilter.price_high">
                                price range: 
                                <strong>
                                    {{ toFilter.price_low }} - {{ toFilter.price_high }} 
                                </strong>
                            </span>
                            <!-- search term -->
                            <span v-if="$route.query.search">
                                search term: 
                                <strong>'{{ $route.query.search }}'</strong>
                            </span>
                            <!-- close -->
                            <span class="close" @click="clear">x</span>
                        </div>
                        <div class="product-grid">
                            <SingleProduct class="product-item" v-for="product in productslist" :key="product.id" :product="product"
                            />
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
                ordered_by: "",
            },
            productslist: '',
            curr_cat_id : '',
            curr_subcat_id: ''
        }
    },
    computed: {
        price_low () {
            return this.toFilter.price_low
        },
        price_high () {
            return this.toFilter.price_high
        },
        sorted_by () {
            return this.toFilter.sorted_by
        },
        ordered_by () {
            return this.toFilter.ordered_by
        }
    },
    watch: {    
        $route () {
            this.search()
            this.fetchCategories()
        },
        price_low () {
            this.fetchCategories()
        },
        price_high () {
            this.fetchCategories()
        },
        sorted_by () {
            this.sort()
            this.fetchCategories()
        },
        ordered_by () {
            this.sort()
            this.fetchCategories()
        }
    },
    methods: {
        // Filtering
        filterByCategory: function () {
            let vm = this

            // If category is selected
            if (vm.curr_cat_id) {
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
                    // If subcategory array empty, cat not present.
                    // else for every subcategory check that all of
                    // the subcategory of current subcategory is present
                    // in the filtering array.
                    let catPresent = (filter.subcategory.length == 0 ) ?
                                        false :
                                        filter.subcategory.every(vm.checkSubCatPresent)
                    if (!catPresent) {
                        filter.subcategory = []
                        filter.subcategory = vm.getSubcatIdsByCatId()
                    }
                }
            }
        },
        checkSubCatPresent: function (id) {
            // checks if current subcat (id) is included in present
            // category id.
            let subcatids = this.getSubcatIdsByCatId()
            return subcatids.includes(id)
        },
        getSubcatIdsByCatId: function () {
            /*
            This function takes in current cat id from vue instance, and
            picks out ids of the current category.
            */
            let subcategoryids = [], vm = this
            for (const subcategoryIndex in vm.subcategories) {
                if (vm.subcategories[subcategoryIndex]['category'] == vm.curr_cat_id)
                    subcategoryids.push(vm.subcategories[subcategoryIndex]['id'])
            }
            return subcategoryids
        },
        // by price
        filterByPrice () {
            let vm = this
            let filter = vm.toFilter
            // If filtering prices are set
            if (filter.price_low || filter.price_high) {
                filter.needed = "filtered_orand_sorted"
                // price low set
                if (filter.price_low && !filter.filtering_by.includes("price_low"))
                    filter.filtering_by.push("price_low")
                // price high set
                if (filter.price_high && !filter.filtering_by.includes("price_high")) 
                    filter.filtering_by.push("price_high")
                if (!filter.price_low && filter.filtering_by.includes("price_low")){
                    // remove price_low
                    const pl_index = filter.filtering_by.indexOf("price_low")
                    filter.filtering_by.splice(pl_index, 1)
                }
                if (!filter.price_high && filter.filtering_by.includes("price_high")){
                    // remove price_high
                    const ph_index = filter.filtering_by.indexOf("price_high")
                    filter.filtering_by.splice(ph_index, 1)
                }
            }
            else {
                if(filter.filtering_by.includes("price_low")) {
                    // remove price_low
                    const pl_index = filter.filtering_by.indexOf("price_low")
                    filter.filtering_by.splice(pl_index, 1)
                }
                if(filter.filtering_by.includes("price_high")) {
                    // remove price_high
                    const ph_index = filter.filtering_by.indexOf("price_high")
                    filter.filtering_by.splice(ph_index, 1)
                }
            }
        },

        // SORTING
        sort: function () {
            let filter = this.toFilter

            // If user has selected to sort
            if(filter.sorted_by) {
                filter.needed = "filtered_orand_sorted"
                filter.sorting = 'True'
            } else {  // otherwise, reset the sorting
                filter.sorting = ''
            }
        },
        
        // SEARCHING
        search: function() {
            let vm = this
            vm.toFilter.search_term = vm.$route.query.search
            let filter = vm.toFilter
            if (!filter.filtering_by.includes("search_term") && filter.search_term) { // search term
                filter.needed = "filtered_orand_sorted"
                filter.filtering_by.push("search_term")
            } else if (!filter.search_term && filter.filtering_by.includes("search_term")) { // no search term
                // remove search_term from filtering by
                const s_index = filter.filtering_by.indexOf("search_term")
                filter.filtering_by.splice(s_index, 1)

                // remove ?search= from the url
                let current_route = vm.$router.currentRoute.value.fullPath
                current_route = current_route.replace("?search=", "")
                vm.$router.push(current_route)
            }
        },

        // Fetch Products
        fetchProducts: async function () {
            let products = await sendRequest('server/products/', this.toFilter)
            this.productslist = products.data
        },

        // Clear
        clear: function () {
            let filter = this.toFilter
            // empty al the filters
            filter.needed = "all_products"
            filter.filtering_by = []
            filter.subcategory = []
            filter.price_low = ''
            filter.price_high = ''
            filter.search_term = ''

            // clear the search box.
            let search = document.getElementById('search')
            let searchmobile = document.getElementById('searchmobile')
            search.value = ""
            searchmobile.value = ""
            
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