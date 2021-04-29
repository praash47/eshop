from django.db import models


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

class ContactResponse(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=50)
	phone = models.CharField(max_length=100)
	message = models.TextField()

	def __str__(self):
		return self.name

		