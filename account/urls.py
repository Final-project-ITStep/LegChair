from django.urls import path
from .views import *


urlpatterns = [
	path('signup', signup),
    path('confirm', confirm),
    path('signin', signin),
    path('exit', exit),
    path('profile', profile),
    path('reset', reset),
]
