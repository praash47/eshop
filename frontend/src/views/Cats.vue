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
								<li class="active"><router-link to="/cats">Categories</router-link></li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- End Breadcrumbs -->
        <h1>Categories</h1>
        <div class="all-categories">   
            <div class="collapsible" v-for="cat in categories" :key="cat.id">
                <div class="imgBx">
                    <h2><router-link :to="'/shop-grid/' + cat.cat_name.toLowerCase()">{{ cat.cat_name }}</router-link></h2>
                    <img :src="'http://127.0.0.1:8000' + cat.cat_img">
                    <span @click="toggleCollapse" v-if="subCatsThere(cat.id)">▼</span>
                </div>
                <div class="collapsible-contents">       
                    <div class="category" v-for="subcat in subcategories" :key="subcat.id">
                    <router-link v-if="subcat.category == cat.id"
                    :to="'/shop-grid/' + cat.cat_name.toLowerCase() + '/' + subcat.subcat_name.toLowerCase()">
                        {{ subcat.subcat_name }} 
                    </router-link>
                    </div>
                </div>
            </div>  
        </div>
    </div>
</template>
<script>
import fetch from '../mixins/fetch'

export default {
    mixins: [fetch],
    methods: {
        toggleCollapse: function (event) {
           let arrow = event.target
           arrow.classList.toggle("active")
           let collapsingContent = arrow.parentNode.nextSibling
           collapsingContent.classList.toggle("active")
        },
    }
}
</script>
<style scoped>
h1 {
    margin: 10px;
}
.all-categories {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}
.collapsible .collapsible-contents {
    display: none;
}
.collapsible-contents.active {
    display: block;
}
.imgBx {
    position: relative;
}
.imgBx img {
    width: 60%;
}
.imgBx h2 {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #fff;
    background: rgba(0, 0, 0, 0.8);
}
.imgBx span {
    position: absolute;
    font-size: 1.2em;
    padding: 2px 3px;
    top: 50%;
    transform: translateY(-50%);
    color: #fff;
    background: rgba(0, 0, 0, 0.8);
    right: 5px;
    cursor: pointer;
}
.imgBx span.active {
    transform: rotateX(180deg) translateY(50%);
}
.collapsible {
    width: 18%;
    border: 1px solid gray;
    margin: 5px;
    border-radius: 5%;
}
@media (max-width: 750px) {
    .collapsible {
        width: 30%;
    }
}
@media (max-width: 500px) {
    .collapsible {
        width: 45%;
    }
}
@media (max-width: 350px) {
    .collapsible {
        width: 90%;
    }
}
</style>
