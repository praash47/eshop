<template>
    <div class="row">
        <h1>{{ title }}</h1>
        <div class="card-deck">
            <div v-for="(product, index) in products" :key="product.id">
                <SingleProduct v-if="index < 4" :product="product"
                :img_path="'http://127.0.0.1:8000' + product.img1" class="product"/>
            </div>
        </div>
    </div>
</template>
<style scoped>
.row {
    margin: 0;
    display: block;
    padding: 10px;  
}
.row h1 {
    text-align: center;
    margin: 10px;
}
.card-deck {
    display: flex;
    justify-content: center;
    align-items: center;    
}
.product img {
    width: 100px;
}
</style>
<script>
import SingleProduct from '../SingleProduct.vue'
export default {
    props: ['title', 'products'],
    components: {
        SingleProduct
    }
}
</script>