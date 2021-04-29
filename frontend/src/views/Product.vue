<template>
  <div class="container m-4">
    <!-- main product card -->
    <div class="card">
      <div class="card-body">
        <h1 class="card-title">Water Bottle</h1>

        <div class="row">
          <!-- product image section -->
          <div class="col-md-6 col-sm-12">
            <img src="https://via.placeholder.com/768" alt="water bottle image">
          </div>

          <!-- product description section -->
          <div class="col-md-6 col-sm-12">
            <span class="price">Rs. 1,24,500</span>
            <h2>Description</h2>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Itaque odit labore fuga iste eius doloremque
              laborum magnam fugit earum assumenda,voluptate doloribus provident id. Deleniti voluptas illo amet
              adipisci repellat.</p><br>
            <p><strong>In stock:</strong> 40</p>
            <span class="order-section">
              <form id="order">
                <label>Qty:</label><input type="number" name="quantity">
                <button type="submit" class="submit">Order</button>
              </form>
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}
.price, .order-section {
  display: block;
  margin: 50px 0;
}
.price {font-size: 3rem;}
.order-section input {
  width: 50px;
  margin-right: 20px;
  margin-left: 10px;
}
.order-section .submit {
  width: 100px;
  height: 40px;
  background: #2ECC40;
  color: #fff;
}
</style>
