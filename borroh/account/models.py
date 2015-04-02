from django.db import models
from django.contrib.auth.models import Model

class Account(models.Model):
	user = models.OneToOneField(User)
	profile = models.OneToOneField('Profile',blank=True,null=True)

	def __unicode__(self):
		return self.user.name

class Profile(models.Model):
	profile_pic = models.ImageField(upload_to='profile_pics')
	street = city = models.CharField(max_length=40,blank=True,null=True)
	city = models.CharField(max_length=40,blank=True,null=True)
	state = models.CharField(max_length=40,blank=True,null=True)
	zip = models.CharField(max_length=40,blank=True,null=True)
	def __unicode__(self):
		return self.__user.name