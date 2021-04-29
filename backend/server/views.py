from django.http import JsonResponse
from django.views.generic import ListView

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactResponseSerializer, ProductSerializer, CategorySerializer, SubCategorySerializer
from .models import ContactResponse, Product, Category, SubCategory

class ContactView(APIView):
    model = ContactResponse

    def get(self, request, *args, **kwargs):
        qs = ContactResponse.objects.all()

        serializer = ContactResponseSerializer(qs, many=True) 

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ContactResponseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

class ProductView(APIView):
    model = Product

    def get(self, request, *args, **kwargs):
        qs = Product.objects.all()

        serializer = ProductSerializer(qs, many=True) 

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.data['type'] == 'fetch' and request.data['to'] == 'all_products':
            qs = Product.objects.all()
            
            serializer = ProductSerializer(qs, many=True)
             
            return Response(serializer.data)

class CategoryView(APIView):
    model = Category

    def get(self, request, *args, **kwargs):
        qs = Category.objects.all()

        serializer = CategorySerializer(qs, many=True) 

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        qs = Category.objects.all()

        serializer = CategorySerializer(qs, many=True)

        return Response(serializer.data)

class SubCategoryView(APIView):
    model = SubCategory

    def get(self, request, *args, **kwargs):
        qs = SubCategory.objects.all()

        serializer = SubCategorySerializer(qs, many=True) 

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        qs = SubCategory.objects.all()
        
        serializer = SubCategorySerializer(qs, many=True)
            
        return Response(serializer.data)
