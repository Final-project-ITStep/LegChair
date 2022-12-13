from django.db import models
from cart.models import CardItem
from django.contrib.auth.models import User


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	amound = models.IntegerField()
	create = models.DateTimeField(auto_now_add=True)
	complete = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=256)


class Purchase(models.Model):
	cart_item = models.ForeignKey(CardItem, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)