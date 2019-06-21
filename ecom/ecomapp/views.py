from django.shortcuts import render
from ecomapp.models import Category, Product, CartItem, Cart


def base_view(request):
    categories = Category.objects.all(),
    products = Product.objects.all(),
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'base.html', context)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    context = {
        'product': product,
        'categories': categories,
    }
    return render(request, 'product.html', context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category
    }
    return render(request, 'category.html', context)


def cart_view(request):
    cart = Cart.objects.first()
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)
