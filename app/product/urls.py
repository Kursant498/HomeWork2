from django.urls import path

from app.product.views import product, listing

urlpatterns = [
    path("product-detail/", product, name="product-detail"),
    path("listing/", listing, name="listing"),
]
