from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from django.utils import timezone


class CardItem (models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date = models.DateTimeField(null=False, default=timezone.now)
	status = models.CharField(max_length=100)
	cart_wish = models.CharField(max_length=10, null=False, default='cart')

	def __str__(self) -> str:
		return f'{self.user} -> {self.product} -> {self.cart_wish} -> {self.date}'