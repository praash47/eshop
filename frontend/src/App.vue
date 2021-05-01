<template>
<div id="app">
  <Header />
  <router-view :productslist="products" :cats="categories"/>
  <Footer />
</div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
<script>
import {sendRequest} from './views/functions'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

export default {
  data() {
    return {
      products: [],
      categories: {},
      'category_res': '',
      'subcategory_res': '',
    }
  },
  components: {
    Header,
    Footer
  },
  mounted () {
    this.fetchProductsCategories()
  },
  methods: {
    fetchProductsCategories: function() {
      var vm = this;
      let data = {
        'type': 'fetch',
        'to': 'all_products'
      };
      vm.fetchCategories()
      let r = sendRequest('post', 'http://127.0.0.1:8000/server/products/', data);
      r.then(function(response) {
        vm.products = response['data']
      })
      .finally(function() {
        setTimeout(vm.fetchProductsCategories, 1000)
      });
    },
    fetchCategories: function() {
      var vm = this
      
      let rtocats = sendRequest('post', 'http://127.0.0.1:8000/server/categories/')
      rtocats.then(function(response) {
          vm.category_res = response['data']

          let rtosubcats = sendRequest('post', 'http://127.0.0.1:8000/server/subcategories/')
          rtosubcats.then(function(response) {
              vm.subcategory_res = response['data']
              vm.categories = vm.formatCatsIntoDict()
          });
        });
    },
    formatCatsIntoDict: function() {
      var vm = this

      let categories = {}
      for (var i = 0; i < vm.category_res.length; i++) {
          var specific_sub_cats = []
          for (var j = 0; j < vm.subcategory_res.length; j++) {
              // find the matching categories and their sub categories
              if (vm.category_res[i]['id'] == vm.subcategory_res[j]['category']) {
                  specific_sub_cats.push(vm.subcategory_res[j]['subcat_name'])
              }
          }
          categories[vm.category_res[i]['cat_name']] = specific_sub_cats
      }
      return categories;
    }
  }
}
</script>