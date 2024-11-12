from django.contrib import admin

from .models import Product, Comment


class CommentsInline(admin.StackedInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']

    inlines = [
        CommentsInline,
    ]


@admin.register(Comment)
class Commentadmin(admin.ModelAdmin):
    list_display = ['product', 'body', 'author', 'stars', 'active']
