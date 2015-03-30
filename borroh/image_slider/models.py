from django.db import models

class Image(models.Model):
	name = models.CharField(max_length=40)
	image = models.ImageField(upload_to='image_slider')
	def __unicode__(self):
		return self.name
