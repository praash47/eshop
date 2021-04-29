<template>
    <form>
        <div class="form-row">
            <div class="form-group col-md-6">
            <label for="inputEmail4">Email</label>
            <input type="email" class="form-control" id="inputEmail4" placeholder="Email">
            </div>
            <div class="form-group col-md-6">
            <label for="inputPassword4">Password</label>
            <input type="password" class="form-control" id="inputPassword4" placeholder="Password">
            </div>
        </div>
        <div class="form-group">
            <label for="inputAddress2">Username</label>
            <input type="text" class="form-control" id="inputAddress2" placeholder="Username">
        </div>
        <div class="form-group">
            <label for="inputAddress">Address</label>
            <input type="text" class="form-control" id="inputAddress" placeholder="1234 Main St">
        </div>
        <div class="form-row">
            <div class="form-group col-md-6">
            <label for="inputCity">City</label>
            <input type="text" class="form-control" id="inputCity">
            </div>
            <div class="form-group col-md-4">
            <label for="inputState">State</label>
            <select id="inputState" class="form-control">
                <option selected>Choose...</option>
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
            <input type="text" class="form-control" id="inputZip">
            </div>
        </div>
    </form>
</template>
<script>
export default {
  name: 'UserDetailsAddEdit',
  components: {
  }
}
</script>
<style scoped>
form {
    padding: 20px;
}
</style>