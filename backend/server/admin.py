from django.contrib import admin

from .models import Category
from .models import SubCategory
from .models import Product
from .models import ContactResponse
from .models import Customer

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ContactResponse)
admin.site.register(Customer)