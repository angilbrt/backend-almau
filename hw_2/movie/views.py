from django.shortcuts import render
from .models import Product


def get_ingex_page(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
