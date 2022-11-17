from django.urls import path
from .views import *


urlpatterns = [
	path('logon', logon),
    path('confirm', confirm),
    path('login', login),
    path('exit', exit),
    path('profile', profile),
    path('reset', reset),
]
