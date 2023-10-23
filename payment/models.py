from django.db import models


from django.contrib.auth.models import User
from home.models import Products
from purchase.models import CartItem, Cart

from model_utils.models import StatusModel
from model_utils import Choices


class Order(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	firstName = models.CharField(max_length=15)
	secondName = models.CharField(max_length=15)
	streethouseNumber = models.CharField(max_length=15)
	city = models.CharField(max_length=15)
	postal = models.CharField(max_length=15)		
	phone = models.CharField(max_length=15)
	items = models.ManyToManyField(Products, through='OrderItem')

	orderID = models.CharField(max_length=20)
	price = models.TextField(max_length=10)
	
	paid = models.BooleanField(default=False)
	processing_if_false = models.BooleanField(default=False)

	def __str__(self):
		return self.orderID

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	product =models.ForeignKey(Products, on_delete=models.CASCADE)

class PendingOrder(StatusModel):
	#order = models.CharField(max_length=50)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	STATUS = Choices('processing', 'completed')
