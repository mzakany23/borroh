from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
	user = models.ForeignKey(User,blank=True,null=True)
	total_price = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
	total_points = models.IntegerField(default=0)
	
	def __unicode__(self):
		return "Cart: " + str(self.id)
	
	def already_contains(self,line_item):
		products = [item.product for item in self.lineitem_set.all()]
		return line_item.product in products
	
	def has_both_buy_and_borroh_items(self):
		borroh = self.lineitem_set.all().filter(borroh=True)
		buy = self.lineitem_set.all().filter(borroh=False)
		return buy.count > 0 and borroh.count > 0

	def buy_items_total(self):
		total = 0
		for item in self.lineitem_set.all():
			if item.borroh == False:
				total += float(item.product.price)
		return total

	def borroh_items_total(self):
		total = 0
		for item in self.lineitem_set.all():
			if item.borroh == True:
				total += int(item.product.points_price)
		return total	

	def cart_has_contents(self):
		if self.total_points == 0 and self.total_price == 0:
			return False
		else:
			return True

	


class LineItem(models.Model):
	cart = models.ForeignKey(Cart)
	product = models.ForeignKey(Product,null=True,blank=True)
	borroh = models.BooleanField(default=False)
	def __unicode__(self):
		return self.product.title
	def has_items(self):
		return self.count > 0			



