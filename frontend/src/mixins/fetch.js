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

        // Fetch from server
        let categories = await sendRequest('server/categories/')
        let subcategories = await sendRequest('server/subcategories/')
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
    // Gets keys from subcategories
    getKeys() {
        const vm = this
        let keys = []
        for (let index in vm.subcategories) {
          keys.push(vm.subcategories[index].category)
        }
        return keys
    },
    // Get id from categories or subcategories
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
    getSubcatIdsByCatId: function () {
        /*
        This function takes in current cat id from vue instance, and
        picks out ids of the current category.
        */
        let subcategoryids = [], vm = this
        for (const subcategoryIndex in vm.subcategories) {
            if (vm.subcategories[subcategoryIndex]['category'] == vm.curr_cat_id)
                subcategoryids.push(vm.subcategories[subcategoryIndex]['id'])
        }
        return subcategoryids
    },
  }
}