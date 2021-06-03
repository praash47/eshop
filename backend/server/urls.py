from django.urls import path
from .views import ContactView, ProductView, CategoryView, SubCategoryView, CustomerView, \
    OrderView

urlpatterns = [
    path('contact/', ContactView.as_view()),
    path('products/', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('subcategories/', SubCategoryView.as_view()),
    path('customer/', CustomerView.as_view()),
    path('orders/', OrderView.as_view()),
]
