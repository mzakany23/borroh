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

	try:
		buy_items_set = cart.lineitem_set.filter(borroh=False)
		borroh_items_set = cart.lineitem_set.filter(borroh=True)
	except:
		buy_items_set = None
		borroh_items_set = None

	list_set = {
		'buy' : buy_items_set,
		'borroh' : borroh_items_set
	}

	try:
		mobile = cart.lineitem_set.order_by('borroh')
	except:
		mobile = None

	featured_products = Product.objects.filter(featured=True)
	context = {
			'login_form' : LoginForm, 
			'register' : RegisterUserForm, 
			'featured_products' : featured_products, 
			'cart' : cart, 'list' : list_set, 
			'mobile_items' : mobile
	}
	template = 'home/index.html'
	return render(request,template,context)

