from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', index),
    path('index', index),
    re_path(r'^detail/(?P<item>[0-9]+)$', detail),
]
