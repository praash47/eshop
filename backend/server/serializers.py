from rest_framework import serializers

from .models import ContactResponse, Product, Category, SubCategory, Customer, Order,\
    Rating, UserViews

class ContactResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactResponse
        fields = ['name', 'email', 'phone', 'message']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'sub_category', 'product_name', 'description', 'price',
            'img1', 'in_stock', 'stock_num', 'views'
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'cat_name', 'cat_img'
        ]
        

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = [
            'id', 'category', 'subcat_name'
        ]

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'user', 'address', 'city', 'state', 'zip'
        ]
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'details', 'total', 'status'
        ]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = [
            'id', 'product', 'user', 'rating_value'
        ]

class UserViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserViews
        fields = [
            'id', 'user', 'views'
        ]