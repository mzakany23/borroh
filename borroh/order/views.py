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
from shipping.models import Shipping
import easypost

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
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# Order steps and actions
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
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


	context = {
		'user_addresses' : user_addresses, 
		'is_addresses_to_show': is_addresses_to_show, 
		'new_address_form' : form
	}
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

	try:
		shipping_cost = address.shipping_cost()
		new_shipping, created = Shipping.objects.get_or_create(order=order)
		
		if created:
			new_shipping.carrier = shipping_cost['rates'][0]['carrier']
			new_shipping.carrier_account_id = shipping_cost['rates'][0]['id']
			new_shipping.rate = shipping_cost['rates'][0]['rate']
			new_shipping.service = shipping_cost['rates'][0]['service']
			new_shipping.buyer_address_id = shipping_cost['buyer_address']['id']
			new_shipping.seller_address_id = shipping_cost['from_address']['id']
			new_shipping.save()
	except: 
		shipping = None

	try:
		current_orders_shipping_info = Shipping.objects.get(order=order)
	except:
		current_orders_shipping_info = None

	
	context = {
			'address' : address, 
			'order' : order, 
			'shipping' : current_orders_shipping_info
	}

	template = 'order/checkout-shipping.html'
	return render(request,template,context)

# payment
@login_required(login_url='/account/login')
def order_payment(request):
	try:
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.get(user=user)
		user_credit_cards = profile.all_credit_cards_on_file()
	except:
		user_credit_cards = None

	context = {'user_credit_cards' : user_credit_cards}

	template = 'order/checkout-payment.html'
	return render(request,template,context)

# order
@login_required(login_url='/account/login')
def order_show(request):
	try:
		card = request.POST['creditCardToken']
	except:
		card = None

	try:
		order = Order.objects.get(id=request.session['order_id'])
	except:
		order = None

	try:
		shipping_cost_form = request.POST['optionsRadios']
	except:
		shipping_cost_form = None

	try:
		shipping_cost = Shipping.objects.get(order=order)
	except:
		shipping_cost = None

	if shipping_cost_form:
		if shipping_cost_form == 'free':
			order.free_shipping = True
			order.save()
			
	
	borroh_order = order.type_of_cart == 'Borroh'
	context = {'order' : order, 'borroh_order' : borroh_order, 'shipping_cost' : shipping_cost}
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
		request.session['order_id'] = None
		profile = Profile.objects.get(user=request.user)
		profile.points -= order.cart.total_points
		if order.free_shipping:
			profile.free_shipping_count -= 1
		profile.save()
		del request.session['cart_id']

		for item in order.cart.lineitem_set.all():
			if order.type_of_cart == 'Borroh':
				product = item.product
				product.borrohed = True
				product.save()
			elif order.type_of_cart == 'Buy':
				product = item.product
				product.sold = True
				product.save()
			

	return HttpResponseRedirect(reverse('account_order_list'))









