from django.contrib import admin

from .models import Category
from .models import SubCategory
from .models import Product
from .models import ContactResponse
from .models import Customer
from .models import Order
from .models import Rating
from .models import UserViews
from .models import Cluster
from .models import SliderImage
from .models import FeaturedCategory
from .models import FeaturedProduct
from .models import Offer

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ContactResponse)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Rating)
admin.site.register(UserViews)
admin.site.register(Cluster)
admin.site.register(SliderImage)
admin.site.register(FeaturedCategory)
admin.site.register(FeaturedProduct)
admin.site.register(Offer)