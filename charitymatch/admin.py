from django.contrib import admin

from .models import Category, Organisation, Question

admin.site.register(Organisation)
admin.site.register(Category)

admin.site.register(Question)
