from django.shortcuts import render
from .models import Product

def product_list(request):
    # On filtre pour n'avoir que les produits disponibles (available=True)
    products = Product.objects.filter(available=True)
    return render(request, 'product_list.html', {'products': products})
