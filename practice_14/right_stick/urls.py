from django.urls import path, re_path

from .views import *

app_name = 'right_stick'

urlpatterns = [
    path('', show_products, name='products'),
    path('product/<int:pk>/', show_product, name='product'),
]
