<template>
    <div class="card">
        <img class="card-img-top" :src="img_path" :alt="name">
        <div class="card-body">
            <h5 class="card-title">{{ name }}</h5>
            <p>Rs. {{ price }}</p>
            <div class="cart-qty" v-if="qty > 0">
                <button class="btn btn-sm" @click="plus">+</button>
                <input type="number" :value="qty" id="qty">
                <button class="btn btn-sm" @click="minus">-</button>
            </div>
            <button class="btn" @click="plus" v-else><i class="ti-shopping-cart"></i> Add to Cart</button><br><br>
            <button class="btn" style="background: #FF4136;"><i class="fa fa-heart-o" aria-hidden="true"></i> Add to Wishlist</button>
        </div>
    </div>
</template>
<script>

export default {
    name: 'Single Product',
    props: ['price', 'name', 'img_path'],
    data () {
        return {
            qty: 0
        }
    },
    methods: {
        plus () {
            this.qty += 1
        },
        minus () {
            if (this.qty >= 0) {
                this.qty -= 1
            }
        }
    }
}
</script>
<style scoped>
.card-body button {
    color: #fff;
    text-decoration: none;
}
.cart-qty {
    margin: 0;
}
.btn.btn-sm {
    padding: 15px 30px;
}
#qty {
    width: 50px;
    height: 50px;
    margin: 0 5px 0 5px;
}
</style>