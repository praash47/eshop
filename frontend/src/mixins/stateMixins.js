export default {
    computed: {
      user_logged_in () {
        return this.$store.state.user
      }
    },
}