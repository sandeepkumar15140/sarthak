from django.shortcuts import render
from .models import Product

# Create your views here.


def home(request):
    n = Product.objects
    return render(request, 'home.html', {'n':n})
