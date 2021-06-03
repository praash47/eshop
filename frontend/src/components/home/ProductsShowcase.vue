<template>
    <div class="row">
        <h1>{{ title }}</h1>
        <div class="card-deck">
            <div v-for="(item, index) in data" :key="item.id">
                <SingleProduct v-if="index < 4" :price="item.price" :name="item.product_name"
                :img_path="'http://100.83.99.77:8000' + item.img1" class="product"/>
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
    props: ['title', 'data'],
    components: {
        SingleProduct
    }
}
</script>