export default {
    computed: {
      user_logged_in () {
        return this.$store.state.user
      },
      cart_length () {
        return this.$store.state.cart.length
      },
      cart () {
        return this.$store.state.cart
      },
      cart_total () {
        return this.$store.getters.cartTotal
      }
    },
    methods: {
      updateCartFromLocalStorage () {
        const cart = localStorage.getItem('cart')

        if(cart) {
          this.$store.state.cart = JSON.parse(cart)
        }
      },
      item_total(item) {
        return this.$store.getters.productTotal(item)
      },
      plus (item) {
        if(item) {
          this.$store.commit('addToCart', item)
        } else {
          this.$store.commit('addToCart', this.product)
        }
      },
      minus (item) {
        if(item) {
          this.$store.commit('removeFromCart', item)
        } else {
          this.$store.commit('removeFromCart', this.product)
        }
      }
    }
}