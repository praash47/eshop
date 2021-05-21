<template>
    <div>
        <div v-if="user_logged_in">
            <!-- Breadcrumbs -->
            <div class="breadcrumbs">
                <div class="container">
                    <div class="row">
                        <div class="col-12">
                            <div class="bread-inner">
                                <ul class="bread-list">
                                    <li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
                                    <li class="active"><router-link to="/profile">Profile</router-link></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- End Breadcrumbs -->
            <h1>Profile</h1>
            <UserDetailsAddEdit type="Update" @successAuthMessage="emitToRoot" />
        </div>
		<LoginToView type="page" v-else/>
    </div>
</template>

<script>
import UserDetailsAddEdit from '../../components/user/UserDetailsAddEdit.vue'
import stateMixins from '../../mixins/stateMixins'
import LoginToView from '../../components/LoginToView.vue'


export default {
  name: 'Profile',
  mixins: [stateMixins],
  emits: ['successAuthMessage'],
  components: {
    UserDetailsAddEdit,
    LoginToView
  },
  methods: {
      emitToRoot: function (message) {
          this.$emit('successAuthMessage', message)
      }
  }
}
</script>