<template>
<div id="app">
  <Header />
  <router-view :cats="categories"/>
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
    this.fetchCategories()
  },
  methods: {
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
      })
      .finally(function() {
        setTimeout(vm.fetchCategories, 1000)
      });
    },
    formatCatsIntoDict: function() {
      var vm = this 

      let categories = {}
      for (var i = 0; i < vm.category_res.length; i++) {
          var specific_sub_cats = []
          var specific_sub_ids = []
          for (var j = 0; j < vm.subcategory_res.length; j++) {
              // find the matching categories and their sub categories
              if (vm.category_res[i]['id'] == vm.subcategory_res[j]['category']) {
                  specific_sub_cats.push(vm.subcategory_res[j]['subcat_name'])
                  specific_sub_ids.push(vm.subcategory_res[j]['id'])
              }
          }
          categories[vm.category_res[i]['cat_name']] = {}
          categories[vm.category_res[i]['cat_name']]['subcats'] = specific_sub_cats
          categories[vm.category_res[i]['cat_name']]['subcatids'] = specific_sub_ids
          categories[vm.category_res[i]['cat_name']]['image'] = vm.category_res[i]['cat_img']
      }
      return categories
    }
  }
}
</script>