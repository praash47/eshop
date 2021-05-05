<template>
    <!-- Header Inner -->
    <div class="header-inner">
      <div class="container">
          <div class="cat-nav-head">
              <div class="row">
                  <div class="col-lg-9 col-12">
                      <div class="menu-area">
                          <!-- Main Menu -->
                          <nav class="navbar navbar-expand-lg">
                            <div class="navbar-collapse">
                              <div class="nav-inner">
                                <ul class="nav main-menu menu navbar-nav">
                                  <li><router-link to="/">Home</router-link></li>
                                  <li><router-link to="/cats">Categories</router-link></li>
                                  <li class="shop-allaga">Shop <i class="ti-angle-down"></i>
                                      <ul class="dropdown">
                                          <li><router-link to="/shop-grid">Shop Grid</router-link></li>
                                          <li><router-link to="/cart">Cart</router-link></li>
                                          <li><router-link to="/checkout">Checkout</router-link></li>
                                          <li><router-link to="/orders">Orders</router-link></li>
                                      </ul>
                                  </li>
                                  <li><router-link to="/about">About</router-link></li>
                                  <li><router-link to="/contact">Contact</router-link></li>
                                </ul>
                              </div>
                            </div>
                          </nav>
                          <!--/ End Main Menu -->
                      </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!--/ End Header Inner -->
</template>

<script>

export default {
  name: 'Navigation',
  components: {
  }
}
</script>

<style>
.header.shop .nav-inner {
    margin: 0;
    float: left;
}
.header.shop .nav li {
    margin-right: 40px;
    float: left;
    position: relative;
}
.header.shop .nav li {
    margin-right:5px;
    position: relative;
    float: none;
}
.header.shop .nav li:last-child{
    margin-right:0;
}
.header.shop .nav li .new {
    background: #F7941D;
    color: #fff;
    text-transform: uppercase;
    font-size: 9px;
    position: absolute;
    left: 21px;
    top: 2px;
    font-weight: 500;
    height: 18px;
    line-height: 18px;
    text-align: center;
    display: block;
}
.header.shop.v2 .nav li a{
    color:#333;
}
.header.shop .nav li a, .shop-allaga {
    color: #fff;
    text-transform: capitalize;
    font-size: 15px;
    padding: 20px 15px;
    font-weight: 500;
    display: block;
    position: relative;
    -webkit-transition: all 0.4s ease;
    -moz-transition: all 0.4s ease;
    transition: all 0.4s ease;
}
.header.shop .nav li:hover a, .shop-allaga:hover{
    color:#fff;
    background:#F7941D;
    cursor: pointer;
}
.header.shop.v2 .nav li:hover a{
    color:#F7941D;
    background:transparent;
}
.header.shop .nav li.active a{
    color:#fff;
    background:#F7941D;
}
.header.shop .nav li.active a{
    color:#fff;
    background:#F7941D;
}
.header.shop.v2 .nav li.active a{
    color:#333 !important;
    background:transparent !important;
}
.header.shop.v2 .nav li.active a{
    color:#F7941D !important;
}
.header.shop .nav .dropdown li{
    margin:0;
}
.header.shop .nav li .dropdown li:hover a{
    background:#F7941D;
}
.header.shop.v2 .nav li.active .dropdown li a{
    color:#333 !important;
}
.header.shop.v2 .nav li.active .dropdown li a:hover{
    color:#fff !important;
    background:#F7941D !important;
}
.header.shop.v2 .nav li.active .dropdown li a:hover{
    color:#fff !important;
}
.header.shop.v2 .nav li .dropdown li:hover a{
    color:#F7941D;
}
.header.shop .nav li .dropdown li a {
    color: #333;
    padding: 8px 15px;
    font-weight: 400;
    background:#fff;
}
.header.shop.v2 .nav li .dropdown li a {
    color: #333;
    background:#fff;
}
.header.shop .nav li .dropdown li a {
    font-weight: 400;
    font-size: 14px;
}
.header.shop .nav li .dropdown li a:hover{
    color:#fff;
}
.header.shop.v2 .nav li .dropdown li a:hover{
    color:#fff !important;
    background:#F7941D;
}
.header.shop .nav li .dropdown li .dropdown.sub-dropdown li a:hover{
    background:#F7941D;
}
.router-link-active {
    background:#F7941D;
    padding: 5px;
    color: #fff impo !important;
}
</style>
