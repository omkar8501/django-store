"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages import views as views_pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('products.urls')),
    path('advertise/', views_pages.advertise, name='advertise-page'),
    path('affiliate/', views_pages.affiliate, name='affiliate-page'),
    path('cart/', views_pages.cart, name='cart-page'),
    path('category/', include('pages.urls')),
    path('about/', views_pages.about, name='about-page'),
    path('conditions/', views_pages.conditions, name='conditions-page'),
    path('fulfilment/', views_pages.fulfilment, name='fulfilment-page'),
    path('help/', views_pages.help, name='help-page'),
    path('privacy_notice/', views_pages.privacy_notice, name='privacy_notice-page'),
    path('sell/', views_pages.sell_on_instashop, name='sell_on_instashop-page')
]
