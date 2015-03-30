from django.contrib import admin
from image_slider.models import Image


class ImageAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','image']
	class Meta:
		model = Image

admin.site.register(Image,ImageAdmin)
