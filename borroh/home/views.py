from django.shortcuts import render
from account.form import LoginForm,RegisterUserForm
from product.models import Product
from django.template import *
from cart.models import Cart

def home(request):
	try:
		cart = Cart.objects.get(id=request.session['cart_id'])
	except:
		cart = None


	featured_products = Product.objects.filter(featured=True)
	context = {'login_form' : LoginForm, 'register' : RegisterUserForm, 'featured_products' : featured_products, 'cart' : cart}
	template = 'home/index.html'
	return render(request,template,context)

