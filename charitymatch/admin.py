from django.contrib import admin

from .models import Category, Organisation

admin.site.register(Organisation)
admin.site.register(Category)
