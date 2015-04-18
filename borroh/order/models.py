from django.db import models
from cart.models import Cart

class Order(models.Model):
	cart = models.ForeignKey(Cart,blank=True,null=True)
	status = models.CharField(max_length=40,choices=(('pending','pending'),('shipped','shipped'),('done','done'),('cancel','cancel'),),blank=True,null=True)
	type_of_cart = models.CharField(max_length=40,choices=(('Buy', 'Buy'),('Borroh','Borroh'),),blank=True,null=True)
	date_order_started = models.DateField(auto_now_add=True,blank=True,null=True)

	def total(self):
		return self.cart.total_price()

	def __unicode__(self):
		return "Cart: " +  str(self.cart.id) + " "+ str(self.cart.user)
