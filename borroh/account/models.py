from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.db.models.signals import post_save

class Profile(models.Model):
	user = models.OneToOneField(User,blank=True,null=True)
	profile_pic = models.ImageField(upload_to='profile_pics',blank=True,null=True)
	strip_id = models.CharField(max_length=100,blank=True,null=True)
	favorites = models.ManyToManyField(Product,blank=True,null=True)
	street = city = models.CharField(max_length=40,blank=True,null=True)
	city = models.CharField(max_length=40,blank=True,null=True)
	state = models.CharField(max_length=40,blank=True,null=True)
	phone_numbrer = models.CharField(max_length=40,blank=True,null=True)
	zip = models.CharField(max_length=40,blank=True,null=True)
	def __unicode__(self):
		return str(self.user)


# -----------------------------------------------------------------------------------
# create profile signal
# -----------------------------------------------------------------------------------

def create_profile_receiver(sender,instance,created,*args,**kwargs):
	if created:
		try:
			profile = Profile()
			profile.user = instance
			profile.save()
		except:
			pass

post_save.connect(create_profile_receiver,sender=User)
