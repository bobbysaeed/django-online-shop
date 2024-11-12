from django.urls import path

from .views import CommentCreateView, ProducListView, ProductDetailView


urlpatterns = [
    path('', ProducListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', CommentCreateView.as_view(), name='comment_create'),

]
