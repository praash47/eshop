from rest_framework import serializers

from .models import ContactResponse, Product

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