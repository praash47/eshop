<template>
    <div class="order-containers">
        <!-- Breadcrumbs -->
		<div class="breadcrumbs">
			<div class="container">
				<div class="row">
					<div class="col-12">
						<div class="bread-inner">
							<ul class="bread-list">
								<li><router-link to="/">Home<i class="ti-arrow-right"></i></router-link></li>
								<li class="active"><router-link to="/orders">Orders</router-link></li>
							</ul>
						</div>
					</div>
				</div>
			</div>
		</div>
		<!-- End Breadcrumbs -->
        <h1>Orders</h1>
        <table class="table">
            <thead class="our-theme">
                <tr>
                <th scope="col">Order ID</th>
                <th scope="col">Product ID</th>  
                <th scope="col">Product Name</th>
                <th scope="col">Qty</th>
                <th scope="col">Payment Mode</th>
                <th scope="col">Total</th>
                <th scope="col">Status</th>
                <th scope="col">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                <th scope="row">1</th>
                <td>2</td>
                <td>Laptop</td>
                <td>4</td>
                <td>Cash On Delievery</td>
                <td>4000</td>
                <td>Pending</td>
                <td><button class="btn btn-danger"><i class="ti-close"></i> Cancel</button></td>
                </tr>
            </tbody>
            </table>
    </div>
</template>
<style scoped>
.our-theme {
    background: #F7941D;
    color: #fff;
}
h1 {
    margin: 10px;
}
</style>