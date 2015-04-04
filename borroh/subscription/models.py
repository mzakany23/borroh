from django.db import models

class Subscription(models.Model):
	name = models.CharField(max_length=40)
	points = models.IntegerField(default=0)
	price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
	def __unicode__(self):
		return str(self.points) + " point " + "subscription" 
