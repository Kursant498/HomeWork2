from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'product/product_details.html')

def listing(request):
    return render(request, 'product/listing.html')