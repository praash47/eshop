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
        <div class="categories" v-for="cat in categories" :key="cat.catid">
            <h2>{{ cat.name }} </h2>
            <div class="sub-categories">
                <p v-for="(subcat, index) in cat.subcategories" :key="index">
                    {{ subcat }}
                </p>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data () {
        return {
            'categories': [{
                'catid': 1,
                'name': 'Jeans',
                'subcategories': ['Denim', 'Loose', 'Mom Jeans', 'Dad Jeans', 'Boyfriend Jeans', 'Belly',
                'Tight', 'Fitting'],
            }, {
                'catid': 2,
                'name': 'Gadgets',
                'subcategories': ['Laptop', 'Smartwatch', 'Mobile Phones', 'Earbuds', 'Tablets', 'Cameras',
                'Desktop PCs', 'Router'],
            }, {
                'catid': 3,
                'name': 'Stationery',
                'subcategories': ['Pen', 'Copy', 'Pencil']
            }, {
                'catid': 4,
                'name': 'BT21',
                'subcategories': ['RJ', 'Shooky', 'Mang', 'Koya', 'Chimmy', 'Tata', 'Cookie']
            }]
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
