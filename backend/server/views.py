from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .serializers import ContactResponseSerializer, OrderSerializer, ProductSerializer, \
    CategorySerializer, RatingSerializer, SubCategorySerializer, CustomerSerializer, \
    UserViewsSerializer, SliderImageSerializer, OfferSerializer
from .models import ContactResponse, Product, Category, SubCategory, Customer, \
    Order, Rating, UserViews, SliderImage, FeaturedProduct, FeaturedCategory, \
    Offer
from .recommendation import Recommendation
from .kmeans import KMeansClustering

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
                
                if request.data['ordered_by'] == 'desc':
                    qs = qs.reverse()

        elif request.data['needed'] == 'single_product':
            qs = Product.objects.get(product_name=request.data['product_name'])
            qs.views += 1
            qs.save()
            qs = Product.objects.filter(product_name=request.data['product_name'])

        elif request.data['needed'] == 'latest_products':
            qs = Product.objects.order_by('-id')[:4]  # 4 latest products

        elif request.data['needed'] == 'trending_products':
            qs = Product.objects.order_by('-views')[:4]  # 4 trending products

        serializer = ProductSerializer(qs, many=True)
            
        return Response(serializer.data)

class CustomerView(APIView):
    model = Customer

    def get(self, request, *args, **kwargs):
        qs = Customer.objects.all()

        serializer = CustomerSerializer(qs, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        user = data['user']

        if data['purpose'] == 'username_check':
            user_object = User.objects.filter(username=user['username'])

            # If user exists, send its instance, else nothing
            if user_object:
                return Response({"exists": "true", "user": user['username']})
            else:
                return Response({})

        elif data['purpose'] == 'get_id_from_name':
            user_object = User.objects.get(username=data['user'])
            return JsonResponse({"id": user_object.id})

        elif data['purpose'] == "signup":
            user_object = User.objects.create_user(
                username=user['username'], password=user['password'],
                email=user['email']
            )
            user_object.save()
            customer_object = Customer.objects.create(
                user=user_object, address=user['address'],
                city=user['city'], state=user['state'],
                zip=user['zip']
            )
            customer_object.save()
            
            return Response({"success": "true"})

        elif data['purpose'] == "login":
            user_object = authenticate(request, username=user['username'], password=user['password'])
            
            if not user_object:
                return Response({"logged_in": "Invalid login"})
            else:
                login(request, user_object)
                return Response({"logged_in": "Successfully Logged In!", "username": request.user.username})

        elif data['purpose'] == "logout":
            logout(request)
            return Response({"logout": "Sucessfully Logged Out!"})

        elif data['purpose'] == "all_details":
            user_object = User.objects.filter(username=user["username"])[0]
            customer = Customer.objects.filter(user=user_object.id)[0]

            return Response({
                "email": user_object.email,
                "address": customer.address,
                "city": customer.city,
                "state": customer.state,
                "zip": customer.zip
            })

        elif data['purpose'] == "update":
            print(user)
            # Split from + into old and new username.
            old_username = user['username'].split('+')[0]
            user['username'] = user['username'].split('+')[1]
            user_object = User.objects.filter(username=old_username)[0]
            customer = Customer.objects.filter(user=user_object.id)[0]

            if user['password']:  # user wants to change password
                user_object.set_password(user['password'])
            user_object.username = user['username']
            user_object.email = user['email']
            user_object.save()
            
            customer.address = user['address']
            customer.city = user['city']
            customer.state = user['state']
            customer.zip = user['zip']
            customer.save()

            response = {
                "success": "true",
                "user": {
                    "username": user_object.username,
                    "email": user_object.email,
                    "address": customer.address,
                    "state": customer.state,
                    "city": customer.city,
                    "zip": customer.zip
                }
            }

            return Response(response)
        
        # Return customer details in default. 

        user_object = User.objects.get(username=user['username'])
        customer = Customer.objects.get(user=user_object)

        response = {
            "username": user_object.username,
            "password": "",
            "email": user_object.email,
            "address": customer.address,
            "state": customer.state,
            "city": customer.city,
            "zip": str(customer.zip)
        }
        
        return Response(response)

class OrderView(APIView):
    model = Order

    def get(self, request, *args, **kwargs):
        qs = Order.objects.all()

        serializer = OrderSerializer(qs, many=True) 

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.get(username=data['username'])
        qs = Order.objects.filter(user=user).order_by('-id')

        if (data['cancelId']):
            order = Order.objects.get(id=data['cancelId'])
            order.status = "Cancelled"
            order.save()

            return JsonResponse({"success": "true"})

        elif (data['data']):
            data = data['data']
            order = Order.objects.create(user=user, details=data['orderDetails'],
            total=data['total'], status="Pending")
            order.save()

            return JsonResponse({"success": "true"})
        
        serializer = OrderSerializer(qs, many=True) 
            
        return Response(serializer.data)

class RatingView(APIView):
    model = Rating

    def get(self, request, *args, **kwargs):
        qs = Rating.objects.all()

        serializer = RatingSerializer(qs, many=True) 

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        qs = Product.objects.all()
        product = Product.objects.get(product_name=data['product_name'])
        user = User.objects.get(username=data['user_name'])
        
        kmeans = KMeansClustering(user)

        if (data["rating_option"] == "add"):
            qs = Rating.objects.create(user=user, product=product, rating_value=data['rating_value'])

        elif (data["rating_option"] == "update"):
            qs = Rating.objects.get(user=user, product=product)
            qs.rating_value = data['rating_value']
            qs.save()
            
        elif (data["rating_option"] == "delete"):
            qs = Rating.objects.get(user=user, product=product)
            qs.delete()

        kmeans.update_clusters()
            
        qs = Rating.objects.filter(product=product)

        serializer = RatingSerializer(qs, many=True) 

        return Response(serializer.data)

class UserViewsView(APIView):   
    model = UserViews

    def get(self, request, *args, **kwargs):
        qs = UserViews.objects.all()

        serializer = UserViewsSerializer(qs, many=True) 

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.get(username=data['username'])
        try:
            qs = UserViews.objects.get(user=user)
            qs.views = data['views']
        except:
            qs = UserViews.objects.create(user=user, views=data['views'])
        qs.save()
        
        return JsonResponse({})

class RecommendationView(APIView):
    model = Product

    def post(self, request, *args, **kwargs):
        data = request.data
        recommendation = ''
        if len(data['wishlist']) > 0:
            recommendation = Recommendation(data['username'], data['wishlist'])
        else:
            recommendation = Recommendation(data['username'])

        recommended_products = recommendation.recommend()
        
        if not recommended_products:
            return JsonResponse({})
        
        serializer = ProductSerializer(recommended_products, many=True)

        return Response(serializer.data)

class SliderImageView(APIView):
    model = SliderImage

    def post(self, request, *args, **kwargs):
        qs = SliderImage.objects.all()

        serializer = SliderImageSerializer(qs, many=True)

        return Response(serializer.data)

class FeaturedCategoryView(APIView):
    model = FeaturedCategory

    def post(self, request, *args, **kwargs):
        qs = FeaturedCategory.objects.all()
        qs = Category.objects.filter(
            id__in = list(qs.values_list('category', flat=True))
        )
        
        serializer = CategorySerializer(qs, many=True)

        return Response(serializer.data)

class FeaturedProductView(APIView):
    model = FeaturedProduct

    def post(self, request, *args, **kwargs):
        qs = FeaturedProduct.objects.all()
        qs = Product.objects.filter(
            id__in = list(qs.values_list('product', flat=True))
        )
        
        serializer = ProductSerializer(qs, many=True)

        return Response(serializer.data)

class OfferView(APIView):
    model = Offer

    def post(self, request, *args, **kwargs):
        qs = Offer.objects.all()
        qs_product = Product.objects.filter(
            id__in = list(qs.values_list('product', flat=True))
        )

        offer_serializer = OfferSerializer(qs, many=True)
        product_serializer = ProductSerializer(qs_product, many=True)

        return Response({
            "offer_products" : product_serializer.data,
            "offer_info" : offer_serializer.data
        })