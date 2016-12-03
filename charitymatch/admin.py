from django.contrib import admin

from .models import Category, SubCategory, Organisation, Region, Country, Method

admin.site.register(Organisation)
admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(Country)
admin.site.register(Region)

admin.site.register(Method)
