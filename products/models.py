from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])


class ActiveCommentsManger(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManger, self).get_queryset().filter(active=True)


class Comment(models.Model):
    RATINGS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Alright'),
        ('4', 'Good'),
        ('5', 'Great'),
    ]


    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='comment author'
        )
    body = models.TextField(verbose_name='nazar')
    stars = models.CharField(max_length=10, choices=RATINGS, verbose_name='rating')

    date_time_created = models.DateTimeField(auto_now_add=True)
    date_time_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    # Manager
    objects = models.Manager()
    active_comments_manager = ActiveCommentsManger()

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])
