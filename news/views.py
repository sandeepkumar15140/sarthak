from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.


def home(request):
    n = Product.objects
    return render(request, 'home.html', {'n':n})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'Products.html')


def product_detail(request, product_id):
    prod_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_details.html', {'prods': prod_detail})


def about(request):
    return render(request, 'about.html')