<template>
    <div class="sinlge-bar shopping">
        <a href="#" class="single-icon"><i class="ti-bag"></i> <span class="total-count">{{ cart_length }}</span></a>
        <!-- Shopping Item -->
        <div class="shopping-item">
            <div class="dropdown-cart-header">
                <span>{{ cart_length }} Items</span>
                <router-link to="/cart">View Cart</router-link>
            </div>
            <ul class="shopping-list">
                <li v-for="item in cart" :key="item.id">
                    <router-link :to="'/product/' + item.product_name">
                        <img :src="'http://127.0.0.1:8000' + item.img1" :alt="item.product_name">
                    </router-link>
                    <router-link :to="'/product/' + item.product_name">
                        <h4>{{ item.product_name }}</h4>
                    </router-link>
                    <p class="quantity">
                        <button @click="plus(item)">+</button>
                         <input type="text" :value="item.quantity" readonly="readonly" style="width: 20px;"> 
                        <button @click="minus(item)">-</button>
                    x Rs. {{ item.price }} -<br> Rs. <span class="amount">{{ item_total(item) }} </span></p>
                </li>
            </ul>
            <div class="bottom">
                <div class="total">
                    <span>Total</span>
                    <span class="total-amount">Rs. {{ cart_total }}</span>
                </div>
                <router-link to="/checkout" class="btn animate">Checkout</router-link>
            </div>
        </div>
        <!--/ End Shopping Item -->
    </div>
</template>
<script>
import stateMixins from '../mixins/stateMixins'

export default {
    mixins: [stateMixins],
    mounted () {
        this.updateCartFromLocalStorage()
    },
}
</script>