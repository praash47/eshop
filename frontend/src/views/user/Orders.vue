<template>
    <div>
        <div class="order-containers" v-if="user_logged_in">
            <!-- Breadcrumbs -->
            <div class="breadcrumbs">
                <div class="container">
                    <div class="row">
                        <div class="col-12">
                            <div class="bread-inner">
                                <ul class="bread-list">
                                    <li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
                                    <li class="active"><router-link to="/orders">Orders</router-link></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- End Breadcrumbs -->
            <h1>Orders</h1>
            <details v-for="(order, index) in orders" :key="order.id">
                <summary>
                    Order ID: {{ order.id }} | 
                    {{ order_details_length(index) }} item(s) |
                    <strong>Status: {{ order.status }} </strong> | 
                    Total: Rs. {{ order.total }} |
                    <i v-if="order_delivered(index)"><strong>{{ order.status }}</strong></i>
                    <button class="btn btn-danger btn-sm" @click="cancel(order.id)" v-else-if="!order_cancelled(index)">
                        <i class="ti-close"></i> Cancel
                    </button> 
                    <i v-else><strong>{{ order.status }}</strong></i>
                </summary>
                <table class="table">
                <thead class="our-theme">
                    <tr>
                    <th scope="col">Product ID</th>  
                    <th scope="col">Product Name</th>
                    <th scope="col">Qty</th>
                    <th scope="col">Unit</th>
                    <th scope="col">Total</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="product in order.details" :key="product.id">
                        <td>{{ product.id }}</td>
                        <td>{{ product.product_name }}</td>
                        <td>{{ product.quantity }}</td>
                        <td>Rs. {{ product.price }}</td>
                        <td>Rs. {{ product.quantity * product.price }}</td>
                    </tr>
                </tbody>
                </table>
            </details>
            <p v-if="orders.length == 0">Order to see your orders here</p>
            <br>
        </div>
		<LoginToView type="page" v-else />
    </div>
</template>
<script>
import stateMixins from '../../mixins/stateMixins'
import LoginToView from '../../components/LoginToView.vue'
import { sendRequest } from '../../views/functions'

export default {
    name: 'Orders',
    mixins: [stateMixins],
    emits: ['successAuthMessage'],
    components: {
		LoginToView
    },
    data () {
        return {
            orders: ""
        }
    },
    mounted () {
        if(this.$store.state.user) {
            this.fetchOrders()
        }
    },
    methods: {
        async fetchOrders() {
            let data = {
                "username": this.$store.state.user,
                "cancelId": "",
                "data": ""
            }
            let req = await sendRequest('server/orders/', data)
            this.orders = req.data
            if (this.orders) {
                for (let i=0; i < this.orders.length; i++) {
                    this.orders[i].details = JSON.parse(this.orders[i].details)
                }
            }
        },
        order_details_length (index) {
            return this.orders[index].details.length
        },
        
        order_cancelled (index) {
            return this.orders[index].status == "Cancelled" 
        },
        
        order_delivered (index) {
            return this.orders[index].status == 'Delivered' 
        },

        async cancel (id) {
            let data = {
                "username": this.$store.state.user,
                "cancelId": id.toString(),
                "data": ""
            }
            let req = await sendRequest('server/orders/', data)
            if (req.data.success == "true") {
                this.$emit('successAuthMessage', 'Cancelled the order id ' + id.toString())
                this.fetchOrders()
            }
        }
    }
}
</script>
<style scoped>
.our-theme {
    background: #F7941D;
    color: #fff;
}
h1 {
    margin: 10px;
}
details {
    margin-top: 10px;
}
details summary {
    cursor: pointer;
    margin-bottom: 5px;
}
</style>