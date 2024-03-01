from django.contrib import admin

from core.models import Shop, FoodItem, Order, UserProfile


# Register your models here.

admin.site.register(Shop)
admin.site.register(FoodItem)
admin.site.register(Order)
admin.site.register(UserProfile)
