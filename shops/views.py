from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'shops/index.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'shops/products.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shops/single-product.html', context)
