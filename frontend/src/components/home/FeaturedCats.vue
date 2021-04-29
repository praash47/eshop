<template>
    <div class="row">
        <h1>Featured Categories</h1>
        <div class="featured-cats">
            <div v-for="cat in cats" :key="cat.id">
                <div class="cat">
                    <img src="https://via.placeholder.com/100" alt="Category picture">
                    <a href="#">{{ cat.name }}</a>
                </div>
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
</style>
<script>
export default {
  data () {
      return {
          cats: [
              {'id': 0, 'product_name': 'Jeans'},
              {'id': 1, 'product_name': 'Laptops'},
              {'id': 2, 'product_name': 'Mobile Phones'},
              {'id': 3, 'product_name': 'Bags'},
              {'id': 4, 'product_name': 'Beauty'},
              {'id': 5, 'product_name': 'Drinks'},
              {'id': 6, 'product_name': 'Copies'},
          ]
      }
  }
}
</script>