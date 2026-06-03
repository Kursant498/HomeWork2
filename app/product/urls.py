from django.urls import path

from app.product.views import product

urlpatterns = [
    path("product-detail/", product, name="product-detail"),
]
