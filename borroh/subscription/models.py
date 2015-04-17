from django.db import models

class Subscription(models.Model):
	name = models.CharField(max_length=40,blank=True,null=True)
	free_shipments = models.IntegerField(default=0)
	own_it_discount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	points_per_month = models.IntegerField(default=0)
	price_per_month = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	def __unicode__(self):
		return self.name
