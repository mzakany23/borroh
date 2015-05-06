from django.db import models
from cart.models import Cart
from account.models import Address
from django.contrib.auth.models import User

class Order(models.Model):
	user = models.ForeignKey(User,blank=True,null=True)
	address = models.ForeignKey(Address,null=True,blank=True)
	cart = models.ForeignKey(Cart,blank=True,null=True)
	status = models.CharField(max_length=40,choices=(('started','started'),('pending','pending'),('shipped','shipped'),('done','done'),('cancel','cancel'),),blank=True,null=True)
	type_of_cart = models.CharField(max_length=40,choices=(('Buy', 'Buy'),('Borroh','Borroh'),),blank=True,null=True)
	date_order_started = models.DateField(auto_now_add=True,blank=True,null=True)
	
	def total(self):	
		return self.cart.total_price()

	def __unicode__(self):
		return "Cart: " +  str(self.cart.id) + " "+ str(self.cart.user)
