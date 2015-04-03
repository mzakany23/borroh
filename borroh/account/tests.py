from django.test import TestCase
from models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserTestCase(TestCase):
	def setUp(self):
		User.objects.create(username='mzakany', email='mzakany@gmail.com' ,password='password')

	def test_create_profile_signal(self):
		user = User.objects.get(username='mzakany')
		


def create_profile_receiver(sender,instance,created,*args,**kwargs):
	if created:
		profile = Profile()
		profile.user = instance
		print str(profile.user) == 'mzakany'

post_save.connect(create_profile_receiver,sender=User)
