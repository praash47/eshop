<template>
    <div class="card">
        <router-link :to="'/product/' + product.product_name">
        <img class="card-img-top" :src="'http://192.168.5.113:8000' + product.img1" :alt="product.name">
        </router-link>
        <div class="card-body">
            <router-link :to="'/product/' + product.product_name">
                <h5 class="card-title">{{ product.product_name }}</h5>
                <p>Rs. {{ product.price }}</p>
            </router-link>
            <div class="cart-qty" v-if="quantity || quantity > 0">
                <button class="btn btn-sm" @click="plus()">+</button>
                <input type="number" :value="quantity" id="qty" readonly="readonly">
                <button class="btn btn-sm" @click="minus()">-</button>
            </div>
            <button class="btn" @click="plus()" v-else-if="product.in_stock"><i class="ti-shopping-cart"></i> Add to Cart</button><br><br>
            <button class="btn" v-if="isInWishlist" @click="removeFromWishlist">
                <i class="fa fa-times" aria-hidden="true"></i> Remove from Wishlist
            </button>   
            <button class="btn" style="background: #FF4136;" @click="addToWishlist" v-else>
                <i class="fa fa-heart-o" aria-hidden="true"></i> Add to Wishlist
            </button>
        </div>
    </div>
</template>
<script>
import stateMixins from '../mixins/stateMixins'

export default {
    name: 'Single Product',
    props: ['product'],
    mixins: [stateMixins],
    computed: { 
        quantity() {
            return this.$store.getters.productQuantity(this.product)
        },
        isInWishlist() {
            return this.$store.getters.isInWishlist(this.product)
        },
    },
    methods: {
        addToWishlist() {
            this.$store.commit('addToWishlist', this.product)
        },
        removeFromWishlist() {
            this.$store.commit('removeFromWishlist', this.product)
        }
    }
}
</script>
<style scoped>
.card img {
    max-width: 200px;
}
.card-body button {
    color: #fff;
    text-decoration: none;
}
.cart-qty {
    margin: 0;
}
.btn.btn-sm {
    padding: 10px 20px;
}
#qty {
    width: 50px;
    height: 50px;
    margin: 0 5px 0 5px;
}
</style>