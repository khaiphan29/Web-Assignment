import imp
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from base.models import Product
# Create your views here.

def home(request): 
    apple_name_list = ["iPhone 13 Pro Max", "iPhone 13", "iPhone 13 Mini", "iPhone 12"]
    apple = Product.objects.filter(name__in = apple_name_list)
    ss_name_list = ["Samsung Galaxy Z Fold 3", "Samsung Galaxy Z Flip 3", "Samsung Galaxy S22 Ultra", "Samsung Galaxy Note 20"]
    samsung = Product.objects.filter(name__in = ss_name_list)
    context = {'apples': apple, 'ss': samsung}
    return render(request, 'base/index.html', context= context)

def phone(request): 
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'base/phone.html', context= context)

def filterphone(request, pk): 
    products = Product.objects.filter(brand = pk)
    context = {'products': products}
    return render(request, 'base/phone.html', context= context)

def product_detail(request, br, pk): 
    product = Product.objects.filter(path = pk)
    context = {'product': product}
    return render(request, 'base/product-detail.html', context= context)

def contact(request): 
    context = {}
    return render(request, 'base/contact.html', context= context)

def cart(request): 
    apple_name_list = ["iPhone 13 Pro Max", "iPhone 12"]
    products = Product.objects.filter(name__in = apple_name_list)
    context = {'products': products}
    return render(request, 'base/cart.html', context= context)