from django.urls import path

from app.product.views import product, listing

urlpatterns = [
    path("product_details/", product, name="product_details"),
    path("listing/", listing, name="listing"),
]
