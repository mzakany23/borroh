from django.shortcuts import render
from account.form import LoginForm,RegisterUserForm
from product.models import Product
from django.template import *
from cart.models import Cart
from django.conf import settings

def home(request):
	featured_products = Product.objects.filter(featured=True)
	context = {
			'featured_products' : featured_products
	}
	template = 'home/index.html'
	return render(request,template,context,context_instance=RequestContext(request, processors=[get_home_variables]))


def get_home_variables(request):
	try:
		cart = Cart.objects.get(id=request.session['cart_id'])
		cart_items = cart.lineitem_set.all()
	except:
		cart = None	
		cart_items = None

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
		borrohed = cart.lineitem_set.order_by('borroh')
	except:
		borrohed = None

	try:
		mobile = cart.lineitem_set.order_by('borroh')
	except:
		mobile = None

	return {
			'login_form' : LoginForm, 
			'register' : RegisterUserForm, 
			'items' : cart_items,
			'cart' : cart, 
			'list' : list_set, 
			'mobile_items' : mobile,
			'sorted_by_borroh' : borrohed,
			'settings' : settings
	}

	




