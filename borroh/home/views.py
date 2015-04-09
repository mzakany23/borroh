from django.shortcuts import render
from account.form import LoginForm,RegisterUserForm
from product.models import Product
from django.template import *



def home(request):
	featured_products = Product.objects.filter(featured=True)
	context = {'login_form' : LoginForm, 'register' : RegisterUserForm}
	template = 'home/index.html'
	return render(request,template,context)

