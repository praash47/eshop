<template>
<div class="contact">
    <!-- Breadcrumbs -->
    <div class="breadcrumbs">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="bread-inner">
                        <ul class="bread-list">
                            <li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
                            <li class="active"><router-link to="contact">Contact</router-link></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- End Breadcrumbs -->

    <!-- Start Contact -->
    <section id="contact-us" class="contact-us section">
        <div class="container">
                <div class="contact-head">
                    <div class="row">
                        <div class="col-lg-8 col-12">
                            <div class="form-main">
                                <div class="alert alert-dismissible fade show" v-bind:class="messageClass" role="alert" v-if="messageShow">
                                    {{ messageToDisp }}
                                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="title">
                                    <h4>Get in touch</h4>
                                    <h3>Write us a message</h3>
                                </div>
                                <form class="form">
                                    <div class="row">
                                        <div class="col-lg-12 col-12">
                                            <div class="form-group">
                                                <label>Your Name<span>*</span></label>
                                                <input v-model="name" type="text" placeholder="" >
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-12">
                                            <div class="form-group">
                                                <label>Your Email<span>*</span></label>
                                                <input v-model="email" type="email" placeholder="">
                                            </div>
                                        </div>
                                        <div class="col-lg-6 col-12">
                                            <div class="form-group">
                                                <label>Your Phone<span>*</span></label>
                                                <input v-model="phone" type="number" placeholder="">
                                            </div>
                                        </div>
                                        <div class="col-12">
                                            <div class="form-group message">
                                                <label>Your Message<span>*</span></label>
                                                <textarea v-model="message" placeholder=""></textarea>
                                            </div>
                                        </div>
                                        <div class="col-12">
                                            <div class="form-group button">
                                                <button type="submit" class="btn" @click.prevent="submitContactResponse">Send Message</button>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                        <div class="col-lg-4 col-12">
                            <div class="single-head">
                                <div class="single-info">
                                    <i class="fa fa-phone"></i>
                                    <h4 class="title">Call us Now:</h4>
                                    <ul>
                                        <li>+123 456-789-1120</li>
                                        <li>+977 01 4437123</li>
                                    </ul>
                                </div>
                                <div class="single-info">
                                    <i class="fa fa-envelope-open"></i>
                                    <h4 class="title">Email:</h4>
                                    <ul>
                                        <li><a href="mailto:info@eshop.com">info@eshop.com</a></li>
                                        <li><a href="mailto:support@eshop.com">support@eshop.com</a></li>
                                    </ul>
                                </div>
                                <div class="single-info">
                                    <i class="fa fa-location-arrow"></i>
                                    <h4 class="title">Our Address:</h4>
                                    <ul>
                                        <li>Nepal ko naya bato street</li>
                                        <li>Nepal pradesh no. 4</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    </section>
    <!--/ End Contact -->
</div>
</template>
<script>
import { sendRequest } from './request.js'

export default {
  data () {
    return {
      name: '',
      email: '',
      message: '',
      phone: '',
      messageShow: false,
      messageClass: '',
      messageToDisp: ''
    }
  },
  methods: {
    submitContactResponse () {
			var vm = this;
            // Send a POST request
            var data = {
                'name': vm.name,
                'email': vm.email,
                'message': vm.message,
                'phone': vm.phone
            };
            var r = sendRequest("post", 'http://127.0.0.1:8000/server/contact/', data)
            r.then(function(response) {
                console.log(response)
                if (response['status'] == 200) {
                    vm.messageToDisp = "Message successfully sent!"
                    vm.messageShow = true
                    vm.messageClass = 'alert-success'
                }
                else {
                    vm.messageToDisp = response['statusText']
                    vm.messageShow = true
                    vm.messageClass = 'alert-danger'
                }
            })
            r.catch(function (error) {
                vm.messageToDisp = error['message']
                vm.messageShow = true
                vm.messageClass = 'alert-danger'
            });
      vm.clearFormData()
    },
    clearFormData () {
      this.name = ''
      this.email = ''
      this.message = ''
      this.phone = ''
    }
  }
}
</script>