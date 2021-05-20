from rest_framework import serializers

from .models import ContactResponse, Product, Category, SubCategory, Customer

class ContactResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactResponse
        fields = ['name', 'email', 'phone', 'message']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'sub_category', 'product_name', 'description', 'price',
            'img1', 'in_stock', 'stock_num'
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