from django.db import models
from django.contrib.auth.models import User


class ContactResponse(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=50)
	phone = models.CharField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.name

class Category(models.Model):
	cat_name = models.CharField(max_length=50)
	cat_img = models.ImageField(upload_to="shop/category-thumbs")

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.cat_name

class SubCategory(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	subcat_name = models.CharField(max_length=50)

	class Meta:
		verbose_name_plural = "Sub Categories"
	
	def __str__(self):
		return str(self.category) + ' - ' + self.subcat_name

class Product(models.Model):
	sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
	product_name = models.CharField(max_length=200)
	description = models.TextField()
	price = models.FloatField()
	img1 = models.ImageField(upload_to="shop/products")
	in_stock = models.BooleanField(default=True)
	stock_num = models.IntegerField()

	def __str__(self):
		return str(self.sub_category) + ' - ' + self.product_name

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=10)
	zip = models.IntegerField()

	def __str__(self):
		return str(self.user)

class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	details = models.JSONField()
	total = models.FloatField()

	STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
	
	status = models.CharField(
		max_length=10,
        choices=STATUS_CHOICES,
        default='Pending',
    )

	def __str__(self):
		return str('Order Id ' + str(self.id))

class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_value = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
	    return str(self.product) + ' - ' + str(self.user) + ' - ' + str(self.rating_value)
