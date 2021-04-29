<template>
    <div>
    <!-- Breadcrumbs -->
    <div class="breadcrumbs">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="bread-inner">
                        <ul class="bread-list">
                            <li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
                            <li class="active"><router-link to="profile">Profile</router-link></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- End Breadcrumbs -->
    <h1>Profile</h1>
    <UserDetailsAddEdit />
    <button class="btn btn-primary">Edit</button><br><br>
    </div>
</template>

<script>
import UserDetailsAddEdit from '../../components/user/UserDetailsAddEdit.vue'


export default {
  name: 'Profile',
  components: {
    UserDetailsAddEdit
  }
}
</script>