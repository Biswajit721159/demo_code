from django.contrib import admin

from .models import Product,Photo,order
# Register your models here.
 
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(order)