<template>
  <div class="col-lg-3">
    <div class="all-category">
      <h3 class="cat-heading"><i class="fa fa-bars" aria-hidden="true"></i>CATEGORIES</h3>
      <ul class="main-category">
        <li><a href="#">New Arrivals <i class="fa fa-angle-right" aria-hidden="true"></i></a>
          <ul class="sub-category">
            <li><a href="#">accessories</a></li>
            <li><a href="#">best selling</a></li>
            <li><a href="#">top 100 offer</a></li>
            <li><a href="#">sunglass</a></li>
            <li><a href="#">watch</a></li>
            <li><a href="#">man’s product</a></li>
            <li><a href="#">ladies</a></li>
            <li><a href="#">westrn dress</a></li>
            <li><a href="#">denim </a></li>
          </ul>
        </li>
        <li class="main-category"><a href="#">best selling <i class="fa fa-angle-right" aria-hidden="true"></i></a>
          <ul class="sub-category">
            <li><a href="#">accessories</a></li>
            <li><a href="#">best selling</a></li>
            <li><a href="#">top 100 offer</a></li>
            <li><a href="#">sunglass</a></li>
            <li><a href="#">watch</a></li>
            <li><a href="#">man’s product</a></li>
            <li><a href="#">ladies</a></li>
            <li><a href="#">westrn dress</a></li>
            <li><a href="#">denim </a></li>
          </ul>
        </li>
        <li><a href="#">accessories</a></li>
        <li><a href="#">top 100 offer</a></li>
        <li><a href="#">sunglass</a></li>
        <li><a href="#">watch</a></li>
        <li><a href="#">man’s product</a></li>
        <li><a href="#">ladies</a></li>
        <li><a href="#">westrn dress</a></li>
        <li><a href="#">denim </a></li>
      </ul>
    </div>
  </div>
</template>
<style>
.all-category {
    color: #fff;
    background: transparent;
    position: relative;
    background: #f7941d;
}
.all-category h3{
    padding: 20px 25px;
}
.cat-heading {
    font-size: 20px;
    color: #fff;
}
.cat-heading i {
    color: #fff;
    display: inline-block;
    margin-right: 15px;
    font-size: 22px;
}
.main-category {
    background: #fff;
    width: 100%;
    -webkit-box-shadow: 0px 5px 15px #0000000a;
    -moz-box-shadow: 0px 5px 15px #0000000a;
    box-shadow: 0px 5px 15px #0000000a;
}
.main-category li{
    display:block;
    border-bottom:1px solid #f6f6f6;
}
.main-category li:last-child{
    border:none;
}
.main-category li a {
    font-size: 14px;
    font-weight: 600;
    color: #333;
    padding: 13px 25px 13px 25px;
    display: block;
    text-transform: uppercase;
}
.main-category li a i{
    display:inline-block;
}
.sub-category {
    background: #fff;
    width: 220px;
    position: absolute;
    left: 238px;
    top: 0;
    z-index: 999999;
    opacity: 0;
    visibility: hidden;
    -webkit-transition: all 0.4s ease;
    -moz-transition: all 0.4s ease;
    transition: all 0.4s ease;
    border-left: 3px solid #F7941D;
    -webkit-box-shadow: 0px 5px 15px #0000000a;
    -moz-box-shadow: 0px 5px 15px #0000000a;
    box-shadow: 0px 5px 15px #0000000a;
}
.main-category li:hover .sub-category{
    opacity:1;
    visibility:visible;
}
.main-category li a{
    text-transform:capitalize;
    font-weight:400;
}
.main-category li a:hover{
    color:#F7941D;
}
</style>