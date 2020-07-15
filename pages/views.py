from django.shortcuts import render
from products.models import Product
from products.category_list import unique_category_list
from pages.models import Category


def category(request, category_id):
    products = Product.objects.all()
    category_list = Category.objects.all()
    context = {'products': products, 'category_list': category_list}
    return render(request, 'pages/category.html', context)


def cart(request):
    return render(request, 'pages/cart.html')


def about(request):
    return render(request, 'pages/about.html')


def help(request):
    return render(request, 'pages/help.html')


def conditions(request):
    return render(request, 'pages/conditions.html')


def privacy_notice(request):
    return render(request, 'pages/privacy_notice.html')


def sell_on_instashop(request):
    return render(request, 'pages/sell.html')


def affiliate(request):
    return render(request, 'pages/affiliate.html')


def advertise(request):
    return render(request, 'pages/advertise.html')


def fulfilment(request):
    return render(request, 'pages/fulfilment.html')
