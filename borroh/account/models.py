from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.db.models.signals import post_save
from django.utils.text import slugify
from subscription.models import Subscription
from order.models import Order

class Profile(models.Model):
	user = models.OneToOneField(User,blank=True,null=True,unique=True)
	slug = models.SlugField(blank=True,null=True)
	points = models.IntegerField(default=0)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True)
	strip_id = models.CharField(max_length=100,blank=True,null=True)
	favorites = models.ManyToManyField(Product,blank=True,null=True)
	subscription = models.ForeignKey(Subscription,null=True,blank=True)
	zip = models.CharField(max_length=40,blank=True,null=True)
	def __unicode__(self):
		return str(self.user)

STATE_CHOICES = (
	('OHIO','OHIO'),
)
class Address(models.Model):
	profile = models.ForeignKey(Profile,blank=True,null=True)
	name = models.CharField(max_length=40,blank=True,null=True)
	first = models.CharField(max_length=40,blank=True,null=True)
	last = models.CharField(max_length=40,blank=True,null=True)
	street = city = models.CharField(max_length=40,blank=True,null=True)
	secondary = models.CharField(max_length=40,blank=True,null=True)
	city = models.CharField(max_length=40,blank=True,null=True)
	state = models.CharField(choices=STATE_CHOICES, max_length=40,blank=True,null=True)
	zip_code = models.IntegerField(max_length=10,blank=True,null=True)
	phone_number = models.CharField(max_length=40,blank=True,null=True)
	primary_address = models.BooleanField(default=False)
	shipping_address = models.BooleanField(default=False)
	def __unicode__(self):
		return self.street


# -----------------------------------------------------------------------------------
# create profile signal
# -----------------------------------------------------------------------------------

def create_profile_receiver(sender,instance,created,*args,**kwargs):
	if created:
		try:
			profile = Profile()
			profile.slug = instance	
			profile.user = instance
			profile.save()
		except:
			pass

post_save.connect(create_profile_receiver,sender=User)
