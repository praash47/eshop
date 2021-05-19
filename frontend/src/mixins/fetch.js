import { sendRequest } from '../views/functions'

export default {
  data() {
      return {
          categories: '',
          subcategories: ''
      }
  },
  created () {
    this.fetchCategories()
  },
  methods: {
    // FETCH CATEGORIES AND SUBCATEGORIES
    fetchCategories: async function () {
        this.search_term = this.$route.query.search
        let categories = await sendRequest('http://127.0.0.1:8000/server/categories/')
        let subcategories = await sendRequest('http://127.0.0.1:8000/server/subcategories/')
        this.categories = categories.data
        this.subcategories = subcategories.data
        let path = this.$router.currentRoute.value.fullPath
        if(path.search('/shop-grid') != -1) { // only run this when in shop-grid
          this.curr_cat_id = this.getId()   
          this.curr_subcat_id = this.getId('subcategory')
          this.filterByCategory()  // filter by category definition in ShopGrid.vue
          this.filterByPrice()
          this.search()
          this.fetchProducts()
        }
    },
    // Some utility functions to make the task easier
    subCatsThere(id) {
        let keys = this.getKeys()
        return keys.includes(id)
    },
    getKeys() {
        const vm = this
        let keys = []
        for (let index in vm.subcategories) {
          keys.push(vm.subcategories[index].category)
        }
        return keys
    },
    getId: function (toGet='') {
      const isSubcategory = (toGet == 'subcategory')
      let getIdFrom = (isSubcategory) ? this.subcategories : this.categories
      let nameKey = (isSubcategory) ? 'subcat_name' : 'cat_name'
      let nameParam = (isSubcategory) ? this.$route.params.subCatName : this.$route.params.catName
      
      if (nameParam == null) return null
      for (const index in getIdFrom) {
        if (getIdFrom[index][nameKey].toLowerCase() == nameParam)
        {return getIdFrom[index]['id']}
      }
      return null
    },
  }
}