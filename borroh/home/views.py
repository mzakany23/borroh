from django.shortcuts import render
from image_slider.models import Image

def home(request):
	slider_images = Image.objects.all()
	context = {'slider_images' : slider_images}
	template = 'home/index.html'
	return render(request,template,context)
