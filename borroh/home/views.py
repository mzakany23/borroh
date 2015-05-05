from django.shortcuts import render
from account.form import LoginForm,RegisterUserForm
from product.models import Product
from account.models import Profile
from order.models import Order
from django.template import *
from cart.models import Cart
from django.conf import settings
import stripe

def home(request):
  
	featured_products = Product.objects.filter(featured=True).exclude(borrohed=True)
	context = {
			'featured_products' : featured_products,
	}
	template = 'home/index.html'
	return render(request,template,context,context_instance=RequestContext(request, processors=[get_home_variables]))


def get_home_variables(request):
	try:
		cart = Cart.objects.get(id=request.session['cart_id'])
	except:
		cart = None	
		
	try:
		cart_items = cart.lineitem_set.all()
	except:
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

	try:
		list_borroh_count = list_set['borroh'].count()
		list_buy_count = list_set['buy'].count()
	except:
		list_borroh_count = 0
		list_buy_count = 0

	try:
		profile = Profile.objects.get(user=request.user)
	except:
		profile = None
	
	try:
		points_balance = profile.points
	except:
		points_balance = 0

	try: 
		cart_points_balance = cart.borroh_items_total
	except:
		cart_points_balance = 0
		

	try:
		points_over_balance = cart.total_points - points_balance
		total_points_minus_individual_balance = 0
	except:
		points_over_balance = 0

	if points_over_balance > 0:
		total_points_minus_individual_balance = points_over_balance
	else:
		total_points_minus_individual_balance = 0

	try:
		wishlist_count = profile.wishlist_count
	except:
		wishlist_count = 0
	
	try:
		cart_has_contents = cart.cart_has_contents()
	except:
		cart_has_contents = None

	try:
		user_does_not_have_a_subscription = profile.has_no_subscription()
	except:
		user_does_not_have_a_subscription = True
	
	try:
		user_has_subscription = profile.has_subscription()
	except:
		user_has_subscription = False

	try:
		borroh_orders = Order.objects.filter(type_of_cart='Borroh').filter(status='pending')
	except:
		borroh_orders = None

	return {
			'total_points_minus_individual_balance' : total_points_minus_individual_balance,
			'login_form' : LoginForm, 
			'register' : RegisterUserForm, 
			'items' : cart_items,
			'cart' : cart, 
			'list' : list_set, 
			'mobile_items' : mobile,
			'sorted_by_borroh' : borrohed,
			'settings' : settings,
			'points_balance' : points_balance,
			'list_borroh_count' : list_borroh_count,
			'list_buy_count' : list_buy_count,
			'wishlist_count' : wishlist_count,
			'cart_has_contents' : cart_has_contents,
			'server' : settings.SERVER,
			'user_does_not_have_a_subscription' : user_does_not_have_a_subscription,
			'user_has_subscription' : user_has_subscription,
			'stripeKey' : settings.API_KEY2,
			'borroh_orders' : borroh_orders
	}

	
def error(request):
	context = {}
	template = 'home/404.html'
	return render(request,template,context)

