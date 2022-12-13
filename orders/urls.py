from django.urls import re_path
from .views import order, confirm


urlpatterns = [
	re_path(r'^order/(?P<sel_list>[0-9\,]+)$', order),
	re_path(r'^confirm/(?P<init_list>[0-9\,]+)$', confirm),
]
