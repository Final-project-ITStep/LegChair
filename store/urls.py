from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index),
    path('index', index),
    re_path('single/(?P<product_id>.*)$', single_product),
]

"""
    
"""
