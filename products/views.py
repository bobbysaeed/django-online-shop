from django.shortcuts import render
from django.views import generic

from .models import Product


class ProducListView(generic.ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_list.html'
    context_object_name = 'products'
