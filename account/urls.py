from django.urls import path
from .views import *


urlpatterns = [
	path('signup', signup),
    path('checkinput', checkinput),
    path('confirm', confirm),
    path('signin', signin),
    path('exit', exit),
    path('profile', profile),
    path('reset', reset),
    path('activation_sent', activation_sent),
    path('activate/<slug:uidb64>/<slug:token>', activate),
]
