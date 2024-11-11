from django.contrib import admin

from .models import Product, Commment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']


@admin.register(Commment)
class Commentadmin(admin.ModelAdmin):
    list_display = ['product', 'body', 'author', 'stars', 'active']
