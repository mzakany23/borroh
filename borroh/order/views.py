from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from cart.models import Cart,LineItem
from product.models import Product
from subscription.models import Subscription
from home.views import get_home_variables
from django.template import RequestContext
from django.contrib.auth.models import User
from account.models import Profile
from django.conf import settings

def start_order_process(request):
	try:
		process = request.POST['checkout_process']
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.get(user=user)
		cart = Cart.objects.get(id=request.session['cart_id'])
	except:
		process = None

	if request.user.is_authenticated():
		if process == 'borroh':
			if profile.subscription is not None:
				if profile.points >= cart.borroh_items_total():
					return HttpResponseRedirect(reverse('order_address'))
				else:
					return HttpResponseRedirect(reverse('too_many_items_in_borroh_cart'))
			else:
				return HttpResponseRedirect(reverse('subscribe'))
		elif process == 'buy':
			print 'buy'
			return HttpResponseRedirect(reverse('order_address'))
	else:
		return HttpResponseRedirect(reverse('order_auth'))

def too_many_items_in_borroh_cart(request):
	context = {}
	template = 'order/too_many_items_in_cart.html'
	return render(request,template,context_instance=RequestContext(request, processors=[get_home_variables]))

def add_to_wishlist_and_remove_from_cart(request,id):
	try:
		line_item = LineItem.objects.get(id=request.POST['cart_line_item'])
	except:
		line_item = None

	try:
		cart = Cart.objects.get(id=request.session['cart_id'])
		product = Product.objects.get(id=id)
		profile = Profile.objects.get(user=request.user)
		profile.favorites.add(product)
		profile.save()
		
	except:
		pass

	points = line_item.product.points_price
	cart.total_points -= points
	cart.save()
	line_item.delete()

	if profile.points >= cart.borroh_items_total():
		return HttpResponseRedirect(reverse('order_address'))
	else:
		return HttpResponseRedirect(reverse('too_many_items_in_borroh_cart'))

def remove_from_cart_and_back_to_borroh(request,id):
	try:
		cart = Cart.objects.get(id=request.session['cart_id'])
		line_item = LineItem.objects.get(id=id)
		profile = Profile.objects.get(user=request.user)
	except: 
		line_item = None
		profile = None
		cart = None
	
	points = line_item.product.points_price
	cart.total_points -= points

	cart.save()
	line_item.delete()

	if profile.points >= cart.borroh_items_total():
		return HttpResponseRedirect(reverse('order_address'))
	else:
		return HttpResponseRedirect(reverse('too_many_items_in_borroh_cart'))


# auth
def order_auth(request):
	template = 'order/checkout-auth.html'
	return render(request,template,context_instance=RequestContext(request, processors=[get_home_variables]))

# address
def order_address(request):
	context = {}
	template = 'order/checkout-address.html'
	return render(request,template,context)

# billing
def order_billing(request):
	context = {}
	template = 'order/checkout-billing.html'
	return render(request,template,context)

# shipping
def order_shipping(request):
	context = {}
	template = 'order/checkout-shipping.html'
	return render(request,template,context)

# payment
def order_payment(request):
	context = {}
	template = 'order/checkout-payment.html'
	return render(request,template,context)

# order
def order_show(request):
	context = {}
	template = 'order/checkout-order.html'
	return render(request,template,context,context_instance=RequestContext(request, processors=[get_home_variables]))











