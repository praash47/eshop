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
        let vm = this
        let waitforcats = new Promise(function(resolved, rejected) {
          (async() => {
            let categories = await sendRequest('http://127.0.0.1:8000/server/categories/')
            let subcategories = await sendRequest('http://127.0.0.1:8000/server/subcategories/')
            if (categories && subcategories) {
              let response = {
                categories,
                subcategories
              }
              return resolved(response)
            } else {
              return rejected("categories or/and subcategories fetch failed.")
            }
          })()
        })
        waitforcats.then(
          function (response) {    
            vm.categories = response.categories.data
            vm.subcategories = response.subcategories.data
            let path = vm.$router.currentRoute.value.fullPath
            if(path.search('/shop-grid') != -1) { // only run this when in shop-grid
              vm.curr_cat_id = vm.getId()   
              vm.curr_subcat_id = vm.getId('subcategory')
              vm.filterByCategory()  // filter by category definition in ShopGrid.vue
            }
          },
          function (error) {
            console.log(error)
          }  
        )
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