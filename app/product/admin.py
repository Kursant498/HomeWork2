from django.contrib import admin

from app.product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):   
    list_display = ("id", "title", "price")
    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    ordering = ("-created_at",)