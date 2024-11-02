from django.urls import path

from .views import ProducListView


urlpatterns = [
    path('', ProducListView.as_view(), name='products'),
]
