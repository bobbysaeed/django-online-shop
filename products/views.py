from django.shortcuts import render
from django.views import generic

from .models import Product


class ProducListView(generic.ListView):
    model = Product
    template_name = 'products/list_view.html'
    context_object_name = 'product'