from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def welcome_view(request):
    return render(request, 'welcome.html')

def product_list(request):
    """View to display a list of all products."""
    products = Product.objects.filter(active=True)  
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    """View to display details of a specific product."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def login_view(request):
    """View to handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('welcome')  # Redirect to a named URL after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})