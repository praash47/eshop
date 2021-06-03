<template>
<!-- Start Footer Area -->
    <footer class="footer">
        <!-- Footer Top -->
        <div class="footer-top section">
            <div class="container">
                <div class="row">
                    <div class="col-lg-5 col-md-6 col-12">
                        <!-- Single Widget -->
                        <div class="single-footer about">
                            <div class="logo">
                                <img src="images/logo2.png" alt="#">
                            </div>
                            <p class="text">Presenting with you best valued products at the cheapest rate.</p>
                            <p class="call">Got Question? Call us 24/7<span><a href="tel:014437123">+977 01 4437123</a></span></p>
                        </div>
                        <!-- End Single Widget -->
                    </div>
                    <div class="col-lg-2 col-md-6 col-12">
                        <!-- Single Widget -->
                        <div class="single-footer links">
                            <h4>Information</h4>
                            <ul>
                                <li><router-link to="about">About Us</router-link></li>
                                <li><router-link to="contact">Contact Us</router-link></li>
                            </ul>
                        </div>
                        <!-- End Single Widget -->
                    </div>
                    <div class="col-lg-2 col-md-6 col-12">
                    </div>
                    <div class="col-lg-3 col-md-6 col-12">
                        <!-- Single Widget -->
                        <div class="single-footer social">
                            <h4>Get In Touch</h4>
                            <!-- Single Widget -->
                            <div class="contact">
                                <ul>
                                    <li>Nepal ko naya bato street</li>
                                    <li>Nepal pradesh no. 4</li>
                                    <li>support@eshop.com</li>
                                    <li><a href="tel: +977014437123">+977 01 4437123</a></li>
                                </ul>
                            </div>
                            <!-- End Single Widget -->
                            <ul>
                                <li><a href="#"><i class="ti-facebook"></i></a></li>
                                <li><a href="#"><i class="ti-twitter"></i></a></li>
                                <li><a href="#"><i class="ti-flickr"></i></a></li>
                                <li><a href="#"><i class="ti-instagram"></i></a></li>
                            </ul>
                        </div>
                        <!-- End Single Widget -->
                    </div>
                </div>
            </div>
        </div>
        <!-- End Footer Top -->
        <div class="copyright">
            <div class="container">
                <div class="inner">
                    <div class="row">
                        <div class="col-lg-6 col-12"></div>
                        <div class="col-lg-6 col-12">
                            <div class="right">
                                <img src="images/payments.png" alt="#">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
<!-- /End Footer Area -->
</template>
<script>
export default {
  name: 'Footer'
}
</script>
<style scoped>
/*=============================
	Footer CSS
===============================*/
.footer{
	background:#222;
}
.footer .about {
	padding-right: 50px;
}
.footer .single-footer h4 {
	font-size: 17px;
	font-weight: 600;
	color: #fff;
	text-transform: capitalize;
	margin-bottom: 30px;
}
.footer .about .logo{
	margin-bottom:20px;
}
.footer .about .text{
	color:#fff;
	font-weight: 400;
}
.footer .about .call {
	color: #fff;
	margin-top: 15px;
	font-weight: 400;
}
.footer .about .call span{
	display: block;
}
.footer .about .call a {
	color: #f7941d;
	font-size: 20px;
	font-weight: 600;
}
.footer .links ul li {
	display: block;
	margin-bottom: 8px;
}
.footer .links ul li:last-child{
	margin-bottom:0;
}
.footer .links ul li a{
	color:#fff;
	font-weight: 400;
}
.footer .links ul li a:hover{
	color:#F7941D;
	padding-left:10px;
}
.footer .social .contact ul li {
	color: #fff;
	display: block;
	margin-bottom: 4px;
	font-weight: 400;
}
.footer .contact ul li:last-child{
	margin-bottom:0;
}
.footer .social ul {
	margin-top: 20px;
}
.footer .social ul li{
	display:inline-block;
	margin-right:25px;
}
.footer .social ul li:last-child{
	margin-right:0;
}
.footer .social ul li a{
	color:#fff;
	display:block;
	font-size:16px;
}
.footer .social ul li a:hover{
	color:#F7941D;
}
.footer .copyright .inner{
	border-top:1px solid #eeeeee3d;
	padding:20px 0;
}
.footer .copyright .right{
	float:right;
}
.footer .copyright p{
	color:#fff;
}
.footer .copyright p a{
	color:#fff;
	text-decoration:underline;
}
/*=============================
	End Footer CSS
===============================*/
</style>