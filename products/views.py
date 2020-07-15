from django.shortcuts import render
from .models import Product
from .category_list import unique_category_list
from pages.models import Category


def home(request):
    products = Product.objects.all()
    category_list = Category.objects.all()
    context = {'products': products, 'category_list': category_list}
    return render(request, 'products/home.html', context)