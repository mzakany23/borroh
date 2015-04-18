from django.db import models
from cart.models import Cart

class Order(models.Model):
	cart = models.ForeignKey(Cart,blank=True,null=True)
	status = models.CharField(max_length=40,choices=(('pending','pending'),('shipped','shipped'),('done','done'),('cancel','cancel'),),blank=True,null=True)

	def total(self):
		return self.cart.total_price()

	def __unicode__(self):
		return str(self.cart.id)
