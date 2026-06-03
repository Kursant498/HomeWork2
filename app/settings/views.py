from django.shortcuts import render

from app.settings.models import Category, ProductImage
from app.product.models import Product

# Create your views here.
def home(request):
    category_all = Category.objects.all()
    product_image_all = ProductImage.objects.all()
    product_all = Product.objects.all()
    return render(request, 'home.html', locals())

