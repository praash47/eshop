<template>
<!-- Header-->
<header class="header shop">
    <!-- Topbar -->
    <div class="topbar">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 col-md-12 col-12">
                    <!-- Top Left -->
                    <div class="top-left">
                        <ul class="list-main">
                            <li>
                                <i class="ti-headphone-alt"></i> <a href="tel:+977014437123">+977 01 4437123</a> | <i class="ti-email"></i> <a href="mailto:support@eshop.com">support@eshop.com</a>
                            </li>
                        </ul>
                    </div>
                    <!--/ End Top Left -->
                </div>
                <div class="col-lg-8 col-md-12 col-12">
                    <!-- Top Right -->
                    <div class="right-content" v-if="!user_logged_in">
                        <ul class="list-main">
                            <li><i class="ti-power-off"></i><a href="#" data-toggle="modal" data-target="#loginModal">Login</a></li>
                            <li><i class="ti-slice"></i><a href="#" data-toggle="modal" data-target="#signupModal">Signup</a></li>
                        </ul>
                    </div>
                    <div class="right-content" v-else>
                      Logged in as <router-link to="/profile"><b>{{ user_logged_in }}</b></router-link>
                      <button class="btn btn-sm btn-danger" @click="logout">Logout</button>
                    </div>
                    <!-- End Top Right -->
                </div>
            </div>
        </div>
    </div>
    <!-- End Topbar -->
    <div class="middle-inner">
        <div class="container">
            <div class="row">
                <div class="col-lg-2 col-md-2 col-12">
                    <!-- Logo -->
                    <div class="logo">
                        <router-link to="/"><img src="@/assets/logo.png" alt="logo"></router-link>
                    </div>
                    <!--/ End Logo -->
                    <!-- Search Form -->
                    <div class="search-top">
                        <div class="top-search"><a href="#0"><i class="ti-search"></i></a></div>
                        <!-- Search Form -->
                        <div class="search-top">
                            <form class="search-form">
                                <input type="text" placeholder="Search here..." id="searchmobile"
                                    v-model="search">
                            </form>
                        </div>
                        <!--/ End Search Form -->
                    </div>
                    <!--/ End Search Form -->
                    <div class="mobile-nav"></div>
                </div>
                <div class="col-lg-8 col-md-7 col-12">
                    <div class="search-bar-top">
                        <div class="search-bar">
                            <input name="search" id="search" placeholder="Search here..." type="search" v-model="search">
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-3 col-12">
                    <div class="right-bar">
                        <!-- Search Form -->
                        <div class="sinlge-bar">
                            <router-link to="/wishlist" class="single-icon"><i class="fa fa-heart-o" aria-hidden="true" title="Wishlist"></i></router-link>
                        </div>
                        <div class="sinlge-bar">
                            <router-link to="/profile" class="single-icon"><i class="fa fa-user-circle-o" aria-hidden="true" title="Profile"></i></router-link>
                        </div>
                        <Cart />
                    </div>
                </div>
            </div>

            <!-- Login Modal -->
            <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="LoginModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="LoginModalLabel">Login</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <form v-on:submit.prevent="login">
                                <div class="form-group">
                                    <label for="username">Username</label>
                                    <input type="text" class="form-control" v-model="user.username"
                                    placeholder="Enter your username" required="required">
                                </div>
                                <div class="form-group">
                                    <label for="password">Password</label>
                                    <input type="password" class="form-control" v-model="user.password"
                                    placeholder="Enter your password" required="required">
                                </div>
                                <div class="text-danger" v-if="error.invalid_login">
                                    {{ error.invalid_login }}
                                </div><br>
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button> 
                                <button type="submit" class="btn btn-primary ml-1">Login</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Signup Modal -->
            <div class="modal fade" id="signupModal" tabindex="-1" role="dialog" aria-labelledby="SignupModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="SignupModalLabel">Signup</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <UserDetailsAddEdit type="SignUp" @successAuthMessage="showSuccessModal"/>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Success modal -->
            <div class="modal fade" id="successModal" tabindex="-1">
                <div class="modal-dialog modal-sm">
                    <div class="modal-content">
                        <div class="model-header">
                            <button type="button" class="btn btn-sm btn-secondary"
                            @click="closeSuccessModal()"
                            style="padding: 4px 8px; text-transform: lowercase">x</button>
                        </div>
                        <div class="model-body">
                            <img src="../assets/success-tick.gif" alt="success-tick">
                            {{ success_message }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div> 
  <Navigation />
</header>
<!--/ End Header -->
</template>

<script>
import Navigation from './Navigation.vue'
import Cart from './Cart.vue'
import UserDetailsAddEdit from './user/UserDetailsAddEdit.vue'
import { sendRequest, createCookie, showOrHide, clearKeys } from '../views/functions'
import stateMixins from '../mixins/stateMixins'


export default {
  name: 'Header',
  mixins: [stateMixins],
  props: ['message'],
  emits: ['modalclosed'],
  components: {
    Navigation,
    Cart,
    UserDetailsAddEdit
  },
  data () {
      return {
          search: '',
          success_message: '',
          user: {
              username: '',
              password: ''
          },
          error: {
              invalid_login: ''
          }
      }
  },
  computed: {
      username () {
        return this.user.username
      },
      password () {
        return this.user.password
      },
  },
  watch: {
      search () {
          let path = this.$router.currentRoute.value.fullPath
          let searchQuery = "?search=" + this.search
          if (path.search('/shop-grid') == -1) {
              if(this.search) {
                this.$router.push('/shop-grid' + searchQuery)
              }
          }
          else {
              this.$router.push(searchQuery)
          }
      },
      username () {
          this.clearErrors()
      },
      password () {
          this.clearErrors()
      },
      message () {
          if(this.message) {
            this.showSuccessModal(this.message)
          }
      }
  },
  methods: {
      async login () {
          let data = {
              purpose: "login",
              user: this.user
          }

          let req = await sendRequest('server/customer/', data)
          let logged_in = req.data.logged_in

          if (logged_in == "Invalid login") {
            this.error.invalid_login = logged_in
          } else {
            this.error.invalid_login = ""
            clearKeys(this.user)

            let loginModal = document.getElementById('loginModal')
            showOrHide(loginModal, false)

            this.showSuccessModal(logged_in)
            this.$store.state.user = req.data.username
            createCookie("user", req.data.username, 2)
          }
      },
      async logout() {
        let data = {
          purpose: "logout",
          user: {}
        }
        let req = await sendRequest('server/customer/', data)
        let logout = req.data.logout
        // Logout message
        if (logout == "Sucessfully Logged Out!") {
          this.$store.state.user = ""
          createCookie("user", "", 0)
          this.showSuccessModal(logout)
        }
      },
      closeSuccessModal () {
          let el = document.getElementById('successModal')
          showOrHide(el, false)
          this.success_message = ""

          // Clear all bootstrap classes
          let backdrop = document.getElementsByClassName('modal-backdrop')[0]
          if (backdrop) {
              showOrHide(backdrop, false)
          }
          let backdrop2 = document.querySelectorAll('.modal-backdrop.show')[0]
          if (backdrop2) {
              showOrHide(backdrop2, false)
          }
          let body = document.querySelector('body')
          body.classList.remove('modal-open')
          body.style.paddingRight = "0"

          // Emit modalclosed to App.vue
          this.$emit('modalclosed')
      },
      showSuccessModal (message) {
          this.success_message = message

          // Show Bootstrap classes
          let successModal = document.getElementById('successModal')
          showOrHide(successModal, true)
        
          let backdrop = document.getElementsByClassName('modal-backdrop')[0]
          if (backdrop) {
              showOrHide(backdrop, false)
          }
      },
      clearErrors () {
          if (this.user.username == "" || this.user.password == "") {
            this.error.invalid_login = ""
          }
      }
  }
}
</script>

<style>
/*======================================
    01. Header CSS
========================================*/
/* Topbar */
.topbar {
    background-color: #fff;
    border-bottom: 1px solid #e2e2e2;
    padding: 15px 0;
}
/* Logo */
.header .logo {
    float: left;
    margin-top: 35px;
    -webkit-transition: all 0.4s ease;
    -moz-transition: all 0.4s ease;
    transition: all 0.4s ease;
}
.header .navbar {
    padding: 0;
}
.header-inner {
    background: #333;
}
/* Main Menu */
.navbar-expand-lg .navbar-collapse{
    display:block !important;
}
.header.v3 .navbar-expand-lg .navbar-collapse{
    display:block !important;
    background:#333;
}
.header .nav li a i {
    margin-left: 6px;
    font-size: 10px;
}
/* Dropdown Menu */
.header .nav li .dropdown {
    background: #fff;
    width: 220px;
    position: absolute;
    top: 100%;
    z-index: 999;
    -webkit-box-shadow: 0px 3px 5px #3333334d;
    -moz-box-shadow: 0px 3px 5px #3333334d;
    box-shadow: 0px 3px 5px #3333334d;
    transform-origin: 0 0 0;
    transform: scaleY(0.2);
    -webkit-transition: all 0.3s ease 0s;
    -moz-transition: all 0.3s ease 0s;
    transition: all 0.3s ease 0s;
    opacity: 0;
    visibility: hidden;
    padding: 10px;
    left: 0;
    margin: 0;
}
.header .nav li:hover .dropdown{
    opacity:1;
    visibility:visible;
    transform:translateY(0px);
}
.header .nav li .dropdown li{
    float:none;
    margin:0;
}
.header .nav li .dropdown li a {
    text-decoration: none;
    padding: 8px 15px;
    color: #666;
    display: block;
    font-weight: 400;
    text-transform: capitalize;
    background: transparent;
}
.header .nav li .dropdown li a:before{
    display:none;
}
.header .nav li .dropdown li:last-child a{
    border-bottom:0px;
}
.header .nav li .dropdown li:hover a{
    color:#fff;
    background:#F7941D;
}
.header .nav li .dropdown li a:hover{
    border-color:transparent;
}
.header .nav li .dropdown li i {
    float: right;
    margin-top: 8px;
    font-size:10px;
    z-index:5;
}
.header .nav li .dropdown.sub-dropdown {
    background: #fff;
    width: 220px;
    position: absolute;
    left: 186px;
    top: 0;
    z-index: 999;
   -webkit-box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2);
    -moz-box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2);
    box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.2);
    box-shadow: 0px 3px 5px #3333334d;
    transform-origin: 0 0 0;
    transform: scaleY(0.2);
    -webkit-transition: all 0.3s ease 0s;
    -moz-transition: all 0.3s ease 0s;
    transition: all 0.3s ease 0s;
    opacity: 0;
    visibility: hidden;
    padding: 10px;
}
.header .nav li .dropdown li:hover .dropdown.sub-dropdown{
    opacity:1;
    visibility:visible;
    transform:translateY(0px);
}
.header .nav li .dropdown.sub-dropdown li a{
    padding: 8px 15px;
    color: #666;
    display: block;
    font-weight: 400;
    text-transform: capitalize;
    background: transparent;
}
.header .nav li .dropdown li:hover .dropdown.sub-dropdown li a{
    background:transparent;
}
.header .nav li .dropdown li .dropdown.sub-dropdown li a:hover{
    color:#fff;
    background:#F7941D;
}
.header .nav li .dropdown.sub-dropdown li:last-child a{
    border-bottom:0px solid;
}
.mobile-search{
    display:none;
}
.header.shop .topbar {
    border: none;
    padding: 12px 0px;
}
.header.shop .nav-inner {
    margin-right: 188px;
}
.header.shop .logo {
    float: left;
    margin-top: 35px;
}
.header.shop .top-contact {
    margin-top:0px;
}
.header.shop .topbar p {
    color: #ccc;
}
.header.shop .topbar .login a {
    color: #F7941D;
}
/* Topbar Left Nav */
.header.shop .top-left .list-main li:first-child{
    padding-left:0;
}
.header.shop .top-left .list-main li i{
    display: inline-block;
    margin-right: 4px;
    font-size: 15px;
    color: #F7941D;
    position: relative;
    top: 3px;
}
.header.shop .right-content{
    float:right;
}
.header.shop .list-main li {
    display: inline-block;
    color: #333;
    font-size: 13px;
    font-weight: 500;
    border-right: 1px solid #f0f0f0;
    padding: 0px 13px;
}
.header.shop .list-main li i {
    display: inline-block;
    margin-right: 4px;
    font-size: 15px;
    color: #F7941D;
    position: relative;
    top: 1px;
}
.header.shop .list-main li:last-child{
    padding-right:0;
    border:none;
}
.header.shop .list-main li a{
    color:#333;
}
.header.shop .list-main li a:hover{
    color:#F7941a;
}
.header.shop .nav li {
    margin-right: 40px;
    float: left;
    position: relative;
}
.header.shop .nav li {
    margin-right: 38px;
    position: relative;
}
.header.shop .nav li:last-child {
    margin: 0 !important;
}
.header.shop .nav li .new {
    background: #F7941D;
    color: #fff;
    text-transform: uppercase;
    font-size: 10px;
    padding: 0px 9px;
    position: absolute;
    left: 0;
    top: 6px;
    font-weight: 500;
}
.header.shop .nav li .new::before {
    position: absolute;
    content: "";
    left: 4px;
    bottom: -8px;
    border: 4px solid #F7941D;
    border-bottom-color: transparent;
    border-left-color: transparent;
    border-right-color: transparent;
}
/* Shopping Cart */
.header .shopping {
    display: inline-block;
    z-index: 9999;
}
.header .shopping .icon {
    position: relative;
    cursor:pointer;
    color:#222;
}
.header .shopping .shopping-item {
    position: absolute;
    top: 68px;
    right: 0;
    width: 300px;
    background: #fff;
    padding: 20px 25px;
    -webkit-transition: all 0.3s ease 0s;
    -moz-transition: all 0.3s ease 0s;
    transition: all 0.3s ease 0s;
    -webkit-transform: translateY(10px);
    -moz-transform: translateY(10px);
    transform: translateY(10px);
    -webkit-box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
    -moz-box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
    opacity:0;
    visibility:hidden;
    z-index:99;
}
.header .shopping:hover .shopping-item{
    transform: translateY(0px);
    opacity:1;
    visibility:visible;
}
.header .shopping .dropdown-cart-header{
    padding-bottom: 10px;
    margin-bottom: 15px;
    border-bottom:1px solid #e6e6e6;
}
.header .shopping .dropdown-cart-header span {
    text-transform: uppercase;
    color: #222;
    font-size: 13px;
    font-weight: 600;
}
.header .shopping .dropdown-cart-header a {
    float: right;
    text-transform: uppercase;
    color: #222;
    font-size: 13px;
    font-weight: 600;
}
.header .shopping .dropdown-cart-header a:hover{
    color:#F7941D;
}
.header .shopping-list li {
    overflow: hidden;
    border-bottom: 1px solid #e6e6e6;
    padding-bottom: 15px;
    margin-bottom: 15px;
    position:relative;
}
.header .shopping-list li .remove {
    position: absolute;
    left: 0;
    bottom: 16px;
    margin-top: -20px;
    height: 20px;
    width: 20px;
    line-height: 18px;
    text-align: center;
    background: #fff;
    color: #222;
    border-radius: 0;
    font-size: 11px;
    border: 1px solid #ededed;
}
.header .shopping-list li .remove:hover{
    background:#222;
    color:#fff !important;
    border-color:transparent;
}
.header .shopping-list .cart-img {
    float: right;
    border: 1px solid #ededed;
    overflow:hidden;
}
.header .shopping-list .cart-img img {
    width: 70px;
    height: 70px;
    border-radius:0;
    
}
.header .shopping-list .cart-img:hover img{
    transform:scale(1.09);
}
.header .shopping-list .quantity{
    line-height: 22px;
    font-size: 13px;
    padding-bottom: 30px;
}
.header .shopping-list h4 {
    font-size: 14px;
}
.header .shopping-list h4 a {
    font-weight: 600;
    font-size: 13px;
    color: #333;
}
.header .shopping-list h4 a:hover{
    color:#F7941D;
}
.header .shopping-item .bottom {
    text-align: center;
}
.header .shopping-item .total {
    overflow:hidden;
    display: block;
    padding-bottom: 10px;
}
.header .shopping-item .total span {
    text-transform:uppercase;
    color:#222;
    font-size:13px;
    font-weight:600;
    float:left;
}
.header .shopping-item .total .total-amount {
    float:right;
    font-size:14px;
}
.header .shopping-item .bottom .btn {
    background: #222;
    padding: 10px 20px;
    display: block;
    color: #fff;
    margin-top: 10px;
    border-radius: 0px;
    text-transform: uppercase;
    font-size: 14px;
    font-weight: 500;
}
.header .shopping-item .bottom .btn:hover{
    background:#F7941D;
    color:#fff;
}
.header.shop{
    background:#fff;
}
.header.shop .topbar {
    background-color: #fff;
    border: none;
}
.header.shop.v3 .topbar{
    padding:0;
}
.header.shop.v3 .topbar .inner-content{
    border-bottom:1px solid #eee;
    padding: 12px 0px;
}
.header.shop .right-nav li a {
    color: #333;
}
.header.shop .logo {
    float: left;
    margin: 19px 0 0;
}
.header.shop .top-contact {
    margin-top:0px;
}
/* Header Middle */
.header.shop .search-bar-top {
    text-align: center;
    margin-top: 10px;
}
.header.shop .search-bar {
    margin-top: 33px;
    width: 460px;
    height: 40px;
    display: inline-block;
    background: #fff;
    position: relative;
}
.header.shop .search-bar {
  width: 400px;
  height: 50px;
  display: inline-block;
  background: #fff;
  position: relative;
  margin: 0;
  line-height: 45px;
  border-radius: 5px;
  border: 1px solid #ececec;
}
.header.shop .search-bar form {
    float: left;
    width: 260px;
}
.header.shop .search-bar input {
  height: 48px;
  background: transparent;
  color: #666;
  border-radius: 0;
  border: none;
  font-size: 14px;
  font-weight: 400;
  padding: 0 25px 0 20px;
  width: 338px;
  outline: none;
}
.header.shop .search-bar a {
    height: 50px;
    line-height: 53px;
    width: 62px;
    text-align: center;
    font-size: 18px;
    color: #fff;
    background: #333333;
    position: absolute;
    right: -2px;
    top: -1px;
    border: none;
    border-radius: 0 5px 5px 0;
    -webkit-transition: all 0.4s ease;
    -moz-transition: all 0.4s ease;
    transition: all 0.4s ease;
}
.header.shop .search-bar a:hover{
    color:#fff;
    background:#F7941D;
}
/* Search Form */
.header.shop .search-top {
    opacity: 1;
    visibility: visible;
    top: 0;
    background: transparent;
    border: none;
    box-shadow: none;
    padding: 0;
    top: 0;
}
.header.shop .middle-inner {
    padding: 20px 0;
    background: #fff;
    border-top: 1px solid #eee;
}
.header.shop.v3 .middle-inner {
    border:none;
}
.header.shop.v3 .header-inner {
    background: transparent;
}
.header.shop.v2 .header-inner {
    background: #fff;
    border-top:1px solid #eee;
}
.header.shop .topbar p {
    color: #333;
}
.header.shop .menu-origin {
    float:none;
    float: right;
}
.header.shop .right-bar {
    padding: 0;
    margin: 0;
    top: 20px;
    float: right;
    position: relative;
}
.header.shop .right-bar .sinlge-bar.top-search a {
    transform: translateY(3px);
}
.header.shop .right-bar .sinlge-bar.top-search a:hover {
    color:#F7941D;
}
.header.shop .right-bar .sinlge-bar .single-icon{
    color:#333;
    font-size:20px;
    position:relative;
}
.header.shop .right-bar .sinlge-bar .single-icon:hover{
    color:#F7941D;
}
.header.shop .right-bar .sinlge-bar .single-icon .total-count {
    position: absolute;
    top: -7px;
    right: -8px;
    background: #f6931d;
    width: 18px;
    height: 18px;
    line-height: 18px;
    text-align: center;
    color: #fff;
    border-radius: 100%;
    font-size: 11px;
}
.header.shop .right-bar .sinlge-bar{
    display:inline-block;
    margin-right:25px;
}
.header.shop .right-bar .sinlge-bar:last-child{
    margin-right:0px;
}
.header.shop .right-bar .sinlge-bar li a:hover{
    color:#F7941D;
}
.mobile-search{
    display:none;
}
/* Header Search */
/* Search */
.header .search-top{
    display:none;
}
.header .search-top a{
    font-size:17px;
}
.header .search-top a:hover{
    color:#F7941D;
}
.header .search-form {
    position: absolute;
    left: -128px;
    z-index: 9999;
    opacity: 0;
    visibility: hidden;
    -webkit-transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    transition: all 0.5s ease;
    top: 46px;
    background: #ffffff75;
    padding: 7px;
    border-radius: 5px;
    transform: scaleY(0);
    box-shadow: 0px 4px 7px #0000003b;
    padding: 0;
    border-radius: 0;
}
.header .search-top.active .search-form {
    opacity:1;
    visibility:visible;
    transform: scaleY(1);
}
.header .search-form input {
    width: 220px;
    height: 45px;
    line-height: 45px;
    padding: 0 60px 0 15px;
    -webkit-transition: all 0.4s ease;
    -moz-transition: all 0.4s ease;
    transition: all 0.4s ease;
    border-radius: 3px;
    border: none;
    background: #fff;
    color: #333;
    border-radius: 0;
}
.header .search-form button {
    position: absolute;
    right: 0;
    height: 45px;
    top: 0;
    width: 45px;
    background: transparent;
    border: none;
    color: #3353ea;
    border-radius: 0 3px 3px 0;
    border-radius: 0;
    border-left: 1px solid #eee;
    font-size: 15px;
    color: #333;
    -webkit-transition: all 0.4s ease;
    -moz-transition: all 0.4s ease;
    transition: all 0.4s ease;
}
.header .search-form button:hover{
    color:#fff;
    background:#F7941D;
    border-color:transparent;
}
/* Login Modal CSS */
#loginModal .modal-title {
    text-align: center;
}
#successModal .modal-content {
    align-items: flex-end;
}
#successModal .model-body {
    padding-bottom: 15px;
    font-size: 1.25em;
    align-self: center;
}
#successModal .model-body img {
    width: 50px;
}
.btn.btn-sm.btn-danger {
    background: red;
    color: white;
    padding: 5px 10px;
    margin-left: 5px;
}
/*======================================
    End Header CSS
========================================*/
</style>
