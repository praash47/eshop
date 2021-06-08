<template>
    <div class="row">
        <h1>Featured Categories</h1>
        <div class="featured-cats">
            <div v-for="cat in featured_categories" :key="cat.id">
                <router-link :to="'/shop-grid/' + cat.cat_name.toLowerCase()">
                <div class="cat">
                    <img :src="'http://127.0.0.1:8000' + cat.cat_img" alt="Category picture">
                    <a href="#">{{ cat.cat_name }}</a>
                </div>
                </router-link>
            </div>
        </div>
    </div>
</template>
<style scoped>
.row {
    margin: 0;
    display: block;
    padding: 10px;
}
.row h1 {
    text-align: center;
}
.featured-cats {
    margin: 20px;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
}
.cat {
    width: 300px;
    display: flex;
    background: #eee;
    border: 1 px solid;
    margin: 10px;
}
.cat a {
    display: flex;
    width: 100%;
    height: 100px;
    justify-content: center;
    align-items: center;
    font-size: 1.5em;
}
.cat img {
    width: 100px;
}
</style>
<script>
import { sendRequest } from '@/views/functions'

export default {
  data () {
      return {
          featured_categories: ""
      }
  },
  mounted () {
      this.fetchFeaturedCategories()
  },
  methods: {
      async fetchFeaturedCategories () {
        let req = await sendRequest('server/featured_categories/')
        this.featured_categories = req.data
      }
  }
}
</script>