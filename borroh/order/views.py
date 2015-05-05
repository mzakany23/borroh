from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from cart.models import Cart,LineItem
from order.models import Order
from product.models import Product
from subscription.models import Subscription
from home.views import get_home_variables
from django.template import RequestContext
from django.contrib.auth.models import User
from account.models import Profile
from django.conf import settings
from account.form import AddressForm
from account.models import Address
# -------------------------------------------------------------------------------------------------
# Start order process check
# -------------------------------------------------------------------------------------------------

'''
	Try to start order process, validates that user has account and at least some points to 
	get rolling. If not then will have to subscribe, and have an account (for now). If User
	deosn't have enought ponits then will have to put some stuff back, or add to basket for later.
'''

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
					order,created = Order.objects.get_or_create(
						user=request.user,
						cart=cart,
						status='started',
						type_of_cart=str(process).capitalize()
					)
					
					if created:
			 			request.session['order_id'] = order.id
			 			

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
# -------------------------------------------------------------------------------------------------
# end order start validation
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
# Order steps and actions
# -------------------------------------------------------------------------------------------------

# auth
def order_auth(request):
	template = 'order/checkout-auth.html'
	return render(request,template,context_instance=RequestContext(request, processors=[get_home_variables]))

# address
''' 
	Order address will look for any primary addresses in the profile. If not, then can manually enter address,
	which will save for later use in user's profile. 
'''
@login_required(login_url='/account/login')
def order_address(request):

	try:
		profile = Profile.objects.get(user=request.user)
		user_addresses = profile.address_set.all()
	except:
		profile = None
		user_addresses = None

	if user_addresses:
		is_addresses_to_show = True
	else:
		is_addresses_to_show = False

	form = AddressForm(request.POST or None)

	if form.is_valid():
		new_address = form.save(commit=False)
		new_address.profile = profile
		new_address.save()
		return HttpResponseRedirect(reverse('order_address'))


	context = {'user_addresses' : user_addresses, 'is_addresses_to_show': is_addresses_to_show, 'new_address_form' : form}
	template = 'order/checkout-address.html'
	return render(request,template,context)

# billing
'''
	not using billing right now. 
'''
def order_billing(request):
	try:
		address_id = request.POST['address_id']
	except: 
		address_id = None

	try:
		address =	Address.objects.get(id=address_id)
	except:
		address = None

	try:
		order = Order.objects.get(id=request.session['order_id'])
		order.address = address
		order.save()
	except:
		order = None

	context = {'address_to_use' : address, 'order' : order}
	template = 'order/checkout-billing.html'
	return render(request,template,context)

# shipping

@login_required(login_url='/account/login')
def order_shipping(request):
	try:
		address_id = request.POST['address_id']
		address =	Address.objects.get(id=address_id)
	except: 
		address = None

	try:
		order = Order.objects.get(id=request.session['order_id'])
	except:
		order = None

	if order.address is None:
		order.address = address
		order.save()

	context = {'address' : address, 'order' : order}
	template = 'order/checkout-shipping.html'
	return render(request,template,context)

# payment
@login_required(login_url='/account/login')
def order_payment(request):
	context = {}
	template = 'order/checkout-payment.html'
	return render(request,template,context)

# order
@login_required(login_url='/account/login')
def order_show(request):

	try:
		order = Order.objects.get(id=request.session['order_id'])
	except:
		order = None


	borroh_order = order.type_of_cart == 'Borroh'
	context = {'order' : order, 'borroh_order' : borroh_order}
	template = 'order/checkout-order.html'
	return render(request,template,context,context_instance=RequestContext(request, processors=[get_home_variables]))

@login_required(login_url='/account/login')
def order_submit(request):
	try:
		order = Order.objects.get(id=request.session['order_id'])
	except:
		order = None

	if order:
		order.status = 'pending'
		order.save()

	return HttpResponseRedirect(reverse('account_order_list'))









