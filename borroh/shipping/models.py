from django.db import models
from order.models import Order

class Shipping(models.Model):
	order = models.ForeignKey(Order)
	carrier = models.CharField(max_length=40)
	carrier_account_id = models.CharField(max_length=40)
	buyer_address_id = models.CharField(max_length=40)
	seller_address_id = models.CharField(max_length=40)
	rate = models.CharField(max_length=40)
	service = models.CharField(max_length=40)
	tracking_code = models.CharField(max_length=40,blank=True,null=True)
	estimated_delivery_days = models.CharField(max_length=40,blank=True,null=True)

	def __unicode__(self):
		return self.carrier