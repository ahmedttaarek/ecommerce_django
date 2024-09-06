from django.shortcuts import render, get_object_or_404
from products.models import Product

def product_list(request):
    """View to display a list of all products."""
    products = Product.objects.filter(active=True)  
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    """View to display details of a specific product."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
