from django.shortcuts import render
from image_slider.models import Image
from account.form import LoginForm,RegisterUserForm

def home(request):
	slider_images = Image.objects.all()
	context = {'slider_images' : slider_images,'login_form' : LoginForm, 'register' : RegisterUserForm}
	template = 'home/index.html'
	return render(request,template,context)
