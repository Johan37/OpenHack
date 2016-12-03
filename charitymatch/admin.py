from django.contrib import admin

from .models import Category, SubCategory, Organisation, Region, Country

admin.site.register(Organisation)
admin.site.register(Category)
admin.site.register(SubCategory)

admin.site.register(Country)
admin.site.register(Region)
