<template>
    <div class="card">
        <img class="card-img-top" :src="img_path" :alt="name">
        <div class="card-body">
            <h5 class="card-title">{{ name }}</h5>
            <p>Rs. {{ price }}</p>
            <a href="#" class="btn"><i class="ti-shopping-cart"></i> Add to Cart</a><br><br>
            <a href="#" class="btn" style="background: #FF4136;"><i class="fa fa-heart-o" aria-hidden="true"></i> Add to Wishlist</a>
        </div>
    </div>
</template>
<script>

export default {
    name: 'Single Product',
    props: ['price', 'name', 'img_path'],
}
</script>
<style scoped>
.card {
    width: 300px;
}
.card-body a {
    color: #fff;
    text-decoration: none;
}
</style>