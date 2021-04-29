from django.urls import path
from server.views import ContactView, ProductView

urlpatterns = [
    path('contact/', ContactView.as_view()),
    path('products/', ProductView.as_view()),
]
