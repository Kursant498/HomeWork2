from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'product_details.html')

def listing(request):
    return render(request, 'listing.html')