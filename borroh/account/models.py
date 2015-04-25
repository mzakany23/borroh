from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from subscription.models import Subscription
from order.models import Order
import stripe
from django.conf import settings


class EmailReset(models.Model):
	user = models.ForeignKey(User)
	hash_key = models.CharField(max_length=200)
	confirmed = models.BooleanField(default=False)
	
	def __unicode__(self):
		return str(self.confirmed)

class UserCreditCard(models.Model):
	profile = models.ForeignKey('Profile',blank=True,null=True)
	credit_card_last_4 = models.CharField(max_length=4)
	type_of_credit_card = models.CharField(max_length=10)
	card_token = models.CharField(max_length=20,blank=True,null=True)

	def __unicode__(self):
		return str(type_of_credit_card) + " ending in " + str(credit_card_last_4)

class Profile(models.Model):
	user = models.OneToOneField(User,blank=True,null=True,unique=True)
	slug = models.SlugField(blank=True,null=True)
	points = models.IntegerField(default=0)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True)
	stripe_id = models.CharField(max_length=100,blank=True,null=True)
	favorites = models.ManyToManyField(Product,blank=True,null=True)
	subscription = models.ForeignKey(Subscription,null=True,blank=True)

	def __unicode__(self):
		return str(self.user)

	def wishlist_count(self):
		count = self.favorites.count()
		if count is None:
			return 0
		else:
			return count

	def has_no_subscription(self):
		if self.subscription is None:
			return True

	def has_subscription(self):
		if self.subscription is not None:
			return True

STATE_CHOICES = (
	('Ohio','Ohio'),
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
# signals
# -----------------------------------------------------------------------------------

def create_or_add_credit_card_at_stripe(sender,instance,created,*args,**kwargs):
	pass

def create_profile_receiver(sender,instance,created,*args,**kwargs):
	if created:
		try:
			stripe.api_key = settings.API_KEY
			new_stripe_id = stripe.Customer.create(email=instance.email)
			profile = Profile()
			profile.slug = instance	
			profile.user = instance
			profile.stripe_id = str(new_stripe_id['id'])
			profile.save()
		except:
			pass

def delete_stripe_account(sender,instance,created,*args,**kwargs):
	if created:
		try:
			profile = Profile.objects.get(user=instance)
			stripe_id = profile.stripe_id
			stripe.api_key = settings.API_KEY
			cu = stripe.Customer.retrieve(str(stripe_id))
			cu.delete()
			profile.delete()
		except:
			pass

post_save.connect(create_profile_receiver,sender=User)
post_delete.connect(delete_stripe_account,sender=User)
post_save.connect(create_or_add_credit_card_at_stripe,sender=UserCreditCard)