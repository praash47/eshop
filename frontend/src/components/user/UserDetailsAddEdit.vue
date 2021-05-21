<template>
    <div>
      <span class="text-danger">* - all fields required</span>
      <form v-on:submit.prevent="sendDetails">
        <div class="form-row">
            <div class="form-group col-md-6">
            <label for="inputEmail4">Email</label>
            <input type="email" v-model="user.email"
            class="form-control" placeholder="Email" required="required">
            <span :class="error.email_valid[1]" v-if="error.email_valid[0]">
                <!-- 0 - status text & 1 - bootstrap class -->
                {{ error.email_valid[0] }}
            </span>
            </div>
            <div class="form-group col-md-6">
            <label for="inputPassword4">Password</label>
            <input type="password" v-model="user.password"
            class="form-control" placeholder="Password" required="required"
            minlength="8" maxlength="16">
            <span :class="error.password_valid[1]" v-if="error.password_valid[0]">
                <!-- 0 - status text & 1 - bootstrap class -->
                {{ error.password_valid[0] }}
            </span>
            </div>
        </div>
        <div class="form-group">
            <label for="inputAddress2">Username</label>
            <input type="text" class="form-control" placeholder="Username"
            v-model="user.username" required="required" minlength="2" name="username-su">
            <span :class="error.username_exists[1]" v-if="error.username_exists[0]">
                <!-- 0 - status text & 1 - bootstrap class -->
                {{ error.username_exists[0] }}
            </span>
        </div>
        <div class="form-group">
            <label for="inputAddress">Address (at least 10 characters)</label>
            <input type="text" v-model="user.address" required="required" 
             class="form-control" placeholder="Eg.: Tichhu Galli Street, Haugal-19"
             minlength="10">
        </div>
        <div class="form-row">
            <div class="form-group col-md-6">
            <label for="inputCity">City (at least 3 characters)</label>
            <input type="text" required="required" placeholder="City"
            v-model="user.city" class="form-control" minlength="3">
            </div>
            <div class="form-group col-md-4">
            <label for="inputState">State</label>
            <select class="form-control" required="required" 
            v-model="user.state">
                <option selected disabled value="">Choose...</option>
                <option>Bagmati</option>
                <option>Karnali</option>
                <option>Lumbini</option>
                <option>Pradesh 2</option>
                <option>Pradesh 1</option>
                <option>Pradesh 5</option>
                <option>Pradesh 7</option>
            </select>
            </div>
            <div class="form-group col-md-2">
            <label for="inputZip">Zip</label>
            <input type="number" class="form-control" required="required" 
            v-model="user.zip" placeholder="Zip" minlength="5"
            min="10000" max="99999">
            <span :class="error.zip_valid[1]" v-if="error.zip_valid[0]">
                <!-- 0 - status text & 1 - bootstrap class -->
                {{ error.zip_valid[0] }}
            </span>
            </div>
            <button type="submit" class="btn btn-primary">{{ type }}</button>
        </div>
      </form>
      <span class="text-danger" v-if="error.general[0]">
        <!-- 0 - general error there or not, 1 - general error message -->
        {{ error.general[1] }}
      </span>
    </div>
</template>
<script>
import { sendRequest, createCookie } from '../../views/functions'

export default {
  name: 'UserDetailsAddEdit',
  props: ['type'],
  emits: ['successAuthMessage'],
  data () {
      return {
          user: {
            username: "",
            email: "",
            password: "",
            address: "",
            city: "",
            state: "",
            zip: "",
          },
          error: {
            username_exists: ["", ""],  //  status text, bootstrap class
            email_valid: ["", ""],
            password_valid: ["", ""],
            zip_valid: ["", ""],
            general: [false, "Please correct errors to continue"]  // there or not, text
          },
      }
  },
  mounted () {
      if (this.type == "Update") {  
        this.fetchDetails()
      }
  },
  computed: {
      username_exists () {
          return this.user.username
      },
      email_valid () {
          return this.user.email
      },
      password_valid () {
          return this.user.password
      },
      zip_valid () {
          return this.user.zip
      }
  },
  watch: {
      username_exists () {
          this.checkIfUsernameExists()
      },
      email_valid () {
          this.checkEmailValidity()
      },
      password_valid () {
          this.checkPasswordValidity()
      },
      zip_valid () {
          this.checkZipValidity()
      }
  },
  methods: {
      checkIfUsernameExists: async function () {
          let data = {
              purpose: "username_check",
              user: this.user
          }
          let req = await sendRequest('http://127.0.0.1:8000/server/customer/', data)
          let exists = req.data.exists || this.user.username.length < 2 ? "true" : ""

          if (this.type == "Update") {
            exists = (req.data.user == localStorage.getItem("old_username")) ? "" : exists
          }
    
          let status_message = [
            // 0, 1 - error_message, success_message  
              "",
              "Username available!"
          ]
          status_message[0] = this.user.username.length < 2 ? 
                            "Username should be at least 2 characters" :
                            "Username exists"
          this.showStatus(
              exists, this.error.username_exists,
              this.user.username, status_message
          )
      },
      checkEmailValidity () {
          let re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
          let email_valid = re.test(this.user.email)
          email_valid = email_valid ? "" : "true"
          let status_message = [
            // 0, 1 - error_message, success_message  
              "Email is not valid!",
              "Email looks good!"
          ]
          this.showStatus(
              email_valid, this.error.email_valid,
              this.user.email, status_message
          )
      },
      checkPasswordValidity() {
          let password_not_valid = this.user.password.length < 8 || this.user.password.length > 16
          password_not_valid = password_not_valid ? "true" : "" 
          let status_message = [
            // 0, 1 - error_message, success_message  
              "8 - 16 characters!",
              "Looks strong now!"
          ]
          this.showStatus(
              password_not_valid, this.error.password_valid,
              this.user.password, status_message
          )
      },
      checkZipValidity() {
          let zip_not_valid = this.user.zip.length != 5
          zip_not_valid = zip_not_valid ? "true" : "" 
          let status_message = [
            // 0, 1 - error_message, success_message  
              "5 digits!",
              "Ok!"
          ]
          this.showStatus(
              zip_not_valid, this.error.zip_valid,
              this.user.zip, status_message
          )
      },

      // Towards Backend!
      async sendDetails () {
        let error_count = document.querySelectorAll('.text-danger').length
        // Filter out other text-danger elements.
        if(document.querySelectorAll('.text-danger').length > 1){
            for (let i=0; i<document.querySelectorAll('.text-danger').length; i++) {
                if(document.querySelectorAll('.text-danger')[i].textContent == this.error.general[1]) {
                    error_count -= 1
                }
                else if(document.querySelectorAll('.text-danger')[i].textContent == "Invalid login") {
                    error_count -= 1
                }
                else if(document.querySelectorAll('.text-danger')[i].textContent == "* - all fields required") {
                    error_count -= 1
                }
            }
        }
        // 2 implies one all required fields, and general error itself
        if (error_count < 1) {
          this.error.general[0] = false

          let username
          if(this.type == "Update") {  
             username = localStorage.getItem("old_username") + '+' + this.user.username
          }

          let data = {
            purpose: this.type.toLowerCase(),
            user: {
                username: this.type == "Update" ? username : this.user.username,
                email: this.user.email,
                address: this.user.address,
                state: this.user.state,
                city: this.user.city,
                zip: this.user.zip,
                password: this.user.password
            }
          }

          let req = await sendRequest('http://127.0.0.1:8000/server/customer/', data)
          let success = req.data.success
          let user = req.data.user
          if (success == "true") {
            this.user.password = ""
            if (this.type.toLowerCase() == "signup") {    
                this.user.username = ""
                this.user.email = ""
                this.user.address = ""
                this.user.city = ""
                this.user.state = ""
                this.user.zip = ""
            } else {   
                this.user.username = user.username
                this.user.email = user.email
                this.user.address = user.address
                this.user.city = user.city
                this.user.state = user.state
                this.user.zip = user.zip
                localStorage.setItem("old_username", user.username)
                createCookie("user", user.username, 2)
                this.$store.state.user = user.username
                this.$emit('successAuthMessage', "Successfully Updated!")
            }
            this.error.username_exists[0] = ""
            this.error.email_valid[0] = ""
            this.error.password_valid[0] = ""
            this.error.zip_valid[0] = ""
            if (this.type.toLowerCase() == "signup") { 
                let signUpModal = document.getElementById('signupModal')
                signUpModal.classList.remove('show')
                signUpModal.style.display = "none"
                let backdrop = document.getElementsByClassName('modal-backdrop')[0]
                if (backdrop) {
                    backdrop.classList.remove('show')
                    backdrop.style.display = "none"
                }
                let body = document.querySelector('body')
                body.classList.remove('modal-open')
                this.$emit('successAuthMessage', "Successfully Signed Up!")
            }
          }
        } else {
          this.error.general[0] = true
        }
      },
      async fetchDetails () {
          let data = {
            purpose: "",
            user: {
                "username": this.$store.state.user
            }
          }

          let req = await sendRequest('http://127.0.0.1:8000/server/customer/', data)
          let user = req.data
          this.user.username = user.username
          this.user.email = user.email
          this.user.address = user.address
          this.user.state = user.state
          this.user.city = user.city
          this.user.zip = user.zip.toString()
          localStorage.setItem("old_username", user.username)
      },

      // UTILITIES
      showStatus (status, user_show, checking_box, status_message) {
          /*
          status: condition matches or not, if error occurs, true
          user_show: the class and message shown to users
          checking_box: the box we are checking validation for.
          status_message:
           */
          if (status == "true") {  // If error occurs
              // user_show | 0 - status text & 1 - bootstrap class
              user_show[0] = status_message[0]
              user_show[1] = "text-danger"
          } else {
              user_show[0] = status_message[1]
              user_show[1] = "text-success"
          }
          if (!checking_box) {  // If checking_text empty, then empty message console
              user_show[0] = ""
          }
      },
  }
}
</script>
<style scoped>
form {
    padding: 20px;
    text-align: center;
}
form button[type="submit"] {
  margin: 0 auto;
}
</style>