<template>
    <div class="card">
        <router-link :to="'/product/' + productToShow.product_name">
        <div class="offer" v-if="checkIsOffer">
            <i class="fa fa-money"></i> Offer
        </div>
        <img class="card-img-top" :src="'http://127.0.0.1:8000' + productToShow.img1" :alt="productToShow.name">
        </router-link>
        <div class="card-body">
            <router-link :to="'/product/' + productToShow.product_name">
                <h5 class="card-title">{{ productToShow.product_name }}</h5>
                <span v-if="checkIsOffer">
                    <p><del>Rs. {{ productToShow.price }}</del></p>
                    <p>Rs. {{ productToShow.offer_price }}</p>
                </span>
                <p v-if="!checkIsOffer">Rs. {{ productToShow.price }}</p>
            </router-link>
            <div class="cart-qty" v-if="quantity || quantity > 0">
                <button class="btn btn-sm" @click="plus()">+</button>
                <input type="number" :value="quantity" id="qty" readonly="readonly">
                <button class="btn btn-sm" @click="minus()">-</button>
            </div>
            <button class="btn" @click="plus()" v-else-if="productToShow.in_stock">
                <i class="ti-shopping-cart"></i> Add to Cart
            </button><br><br>
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
    props: ['product', 'isOffer'],
    mixins: [stateMixins],
    data () {
        return {
            'productToShow': ''
        }
    },
    computed: { 
        quantity() {
            return this.$store.getters.productQuantity(this.productToShow)
        },
        checkIsOffer() {
            if (this.productToShow.offer_price) return true 
            return false
        }
    },
    mounted() {
        this.productToShow = this.product
        this.addOffer()
    },
    methods: {
        addOffer() {
            let offer_item = this.$store.state.offers.find(i => i.id === this.productToShow.id)

            if (offer_item) {
                this.productToShow.offer_price = offer_item.offer_price
                return true
            }
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
.card {
    position: relative;
}
.offer {
    position: absolute;
    top: 5%;
    left: -15px;
    width: 80px;
    padding: 5px 10px;
    background: #da0808;
    color: #fff;
}
.offer:before {
    content: '';
    position: absolute;
    height: 100%;
    width: 15px;
    top: 20px;
    z-index: -1;
    left: 0;
    transform: skewY(50deg);
    transform-origin: top right;
    background: rgb(117, 14, 14);
}
</style>