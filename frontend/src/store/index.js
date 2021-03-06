import { createStore } from "vuex"
import { accessCookie } from '../views/functions'

function updateItem (name, variable) {
    localStorage.setItem(name, JSON.stringify(variable))
}

const store = createStore({
    state: {
        user: accessCookie("user"),
        cart: [],
        views: [],
        wishlist: [],
        offers: []
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
        },
        isInWishlist: state => product => {
            const item = state.wishlist.find(i => i.id === product.id)

            if (item) return true
            else return false
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

            updateItem('cart', state.cart)
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
            
            updateItem('cart', state.cart)
        },
        updateViews (state, product) {
            let item = state.views.find(i => i.id === product.id)

            if (item) {
                item.user_views++
            } else {
                state.views.push(
                    {id: product.id, subcategory_id: product.sub_category, user_views: 1}
                )
            }
            updateItem('views', state.views)
        },
        addToWishlist (state, product) {
            state.wishlist.push({...product})

            updateItem('wishlist', state.wishlist)
        },
        removeFromWishlist (state, product) {
            let item = state.wishlist.find(i => i.id === product.id)
            if (item) state.wishlist = state.wishlist.filter(i => i.id !== product.id)

            updateItem('wishlist', state.wishlist)
        },
    }
})

export default store