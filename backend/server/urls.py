from django.urls import path
from server.views import ContactView, ProductView, CategoryView, SubCategoryView

urlpatterns = [
    path('contact/', ContactView.as_view()),
    path('products/', ProductView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('subcategories/', SubCategoryView.as_view()),
]
