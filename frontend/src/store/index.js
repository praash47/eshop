import { createStore } from "vuex"
import { accessCookie } from '../views/functions'

function updateCart (cart) {
    localStorage.setItem('cart', JSON.stringify(cart))
}

const store = createStore({
    state: {
        user: accessCookie("user"),
        cart: []
    },
    getters: {
        productQuantity: state => product => {
            const item = state.cart.find(i => i.id === product.id)

            if (item) return item.quantity
            else return null
        },
        productTotal: state => product => {
            const item = state.cart.find(i => i.id === product.id)

            if (item) return item.quantity * item.price
            else return null
        },
        cartTotal: state => {
            return state.cart.reduce((a, b) => a + (b.price * b.quantity), 0)
        }
    },
    mutations: {
        addToCart (state, product) {
            let item = state.cart.find(i => i.id === product.id)

            if (item) {
                if(item.quantity < item.stock_num) {
                    item.quantity++
                }
            } else {
                state.cart.push({...product, quantity: 1})
            }

            updateCart(state.cart)
        },
        removeFromCart (state, product) {
            let item = state.cart.find(i => i.id === product.id)

            if (item) {
                if(item.quantity > 1) {
                    item.quantity--
                } else {
                    item.quantity--
                    state.cart = state.cart.filter(i => i.id !== product.id)
                }
            } 

            updateCart(state.cart)
        }
    }
})

export default store