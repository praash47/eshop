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

class ProductView(APIView):
    model = Product

    def get(self, request, *args, **kwargs):
        qs = Product.objects.all()

        serializer = ProductSerializer(qs, many=True) 

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        qs = Product.objects.all()

        if request.data['needed'] == 'filtered_orand_sorted':
            for filtering_with in request.data['filtering_by']:
                if filtering_with == "subcategory":
                    qs = qs.filter(sub_category_id__in=request.data['subcategory'])
                elif filtering_with == "price_low":
                    qs = qs.filter(price__gte=request.data['price_low'])
                elif filtering_with == "price_high":
                    qs = qs.filter(price__lte=request.data['price_high'])
                elif filtering_with == "search_term":
                    qs = qs.filter(product_name__icontains=request.data['search_term'])

            if request.data['sorting'] == 'True':
                if request.data['sorted_by'] == 'price':
                    qs = qs.order_by('price')
                else:
                    qs = qs.order_by('product_name')
                
                if request.data['order'] == 'desc':
                    qs = qs.reverse()
            
        serializer = ProductSerializer(qs, many=True)
            
        return Response(serializer.data)