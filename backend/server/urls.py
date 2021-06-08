from django.urls import path
from .views import ContactView, ProductView, CategoryView, SubCategoryView, CustomerView, \
    OrderView, RatingView, UserViewsView, RecommendationView, FeaturedCategoryView, OfferView, \
     FeaturedProductView, SliderImageView

urlpatterns = [
    path('contact/', ContactView.as_view()),
    path('products/', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('subcategories/', SubCategoryView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('orders/', OrderView.as_view()),
    path('ratings/', RatingView.as_view()),
    path('views/', UserViewsView.as_view()),
    path('recommendations/', RecommendationView.as_view()),
    path('slider_images/', SliderImageView.as_view()),
    path('featured_products/', FeaturedProductView.as_view()),
    path('featured_categories/', FeaturedCategoryView.as_view()),
    path('offers/', OfferView.as_view()),
]
