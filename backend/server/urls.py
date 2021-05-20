from django.urls import path
from server.views import ContactView, ProductView, CategoryView, SubCategoryView, CustomerView

urlpatterns = [
    path('contact/', ContactView.as_view()),
    path('products/', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('subcategories/', SubCategoryView.as_view()),
    path('customer/', CustomerView.as_view()),
]
