<template>
    <div class="cats-container">
        <!-- Breadcrumbs -->
		<div class="breadcrumbs">
			<div class="container">
				<div class="row">
					<div class="col-12">
						<div class="bread-inner">
							<ul class="bread-list">
								<li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
								<li class="active"><router-link to="cats">Categories</router-link></li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- End Breadcrumbs -->
        <h1>Categories</h1>
        <div class="categories" v-for="(cat_name, index) in categories.category" :key="cat_name">
            <h2>{{ cat_name }} </h2>
            <div class="sub-categories">
                <p v-for="subcat in categories.subcategories[index]" :key="subcat">
                    {{ subcat }}
                </p>
            </div>
        </div>
    </div>
</template>
<script>
import { sendRequest } from './request'

export default {
    data () {
        return {
            'categories': {
                'category': [],
                'subcategories': []
            },
            'category_res': '',
            'subcategory_res': '',
        }
    },
    created () {
        this.fetchCategories()
    },
    methods: {
        fetchCategories: function() {
            var vm = this
            
            let rtocats = sendRequest('post', 'http://127.0.0.1:8000/server/categories/')
            rtocats.then(function(response) {
                vm.category_res = response['data']
     
                let rtosubcats = sendRequest('post', 'http://127.0.0.1:8000/server/subcategories/')
                rtosubcats.then(function(response) {
                    vm.subcategory_res = response['data']

                    for (var i=0; i<vm.category_res.length; i++) {
                        vm.categories['category'].push(vm.category_res[i]['cat_name'])
                        var specific_sub_cats = []
                        for (var j=0; j<vm.subcategory_res.length; j++) {
                            if (vm.category_res[i]['id'] == vm.subcategory_res[j]['category']) {
                                specific_sub_cats.push(vm.subcategory_res[j]['subcat_name'])
                            }
                        }
                        vm.categories['subcategories'].push(specific_sub_cats)
                    }

                    console.log(vm.categories)
                });
            });
        }
    }
}
</script>
<style scoped>
h1 {
    margin: 10px;
}
.categories {
    border: 1px solid black;
    border-radius: 20px;
    margin: 20px;
}
.sub-categories {
    display: flex;
    flex-wrap: wrap;
    margin: 20px
}
.sub-categories p {
    width: 200px;
    margin: 20px 0;
}
</style>
