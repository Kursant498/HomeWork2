from django.contrib import admin

from app.settings.models import Category, ProductImage

admin.site.register(Category)
admin.site.register(ProductImage)