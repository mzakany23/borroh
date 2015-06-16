from django.conf import settings
from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Cart,LineItem
from product.models import Product
from django.contrib.auth.models import User,AnonymousUser
from home.views import get_home_variables
from django.template import RequestContext
from django.contrib import messages

def cart_show(request):
	template = 'cart/show_cart.html'
	return render(request,template,context_instance=RequestContext(request, processors=[get_home_variables]))

def cart_show_buy(request):
	template = 'cart/show_buy_cart.html'
	return render(request,template,context_instance=RequestContext(request, processors=[get_home_variables]))

def cart_show_borroh(request):
	template = 'cart/show_borroh_cart.html'
	return render(request,template,context_instance=RequestContext(request, processors=[get_home_variables]))

def add_item(request,id):
	try:
		product = Product.objects.get(id=id)
	except Product.DoesNotExist:
		product = None
	except:
		product = None

	try:
		user = User.objects.get(username=request.user.username)
	except:
		user = None

	try:
		request.session['cart_id']
	except:
		cart = Cart()
		if user:
			cart.user = user
		cart.save()
		request.session['cart_id'] = cart.id

	cart_id = request.session['cart_id']
	cart = Cart.objects.get(id=cart_id)

	if request.POST['cart_to_add'] == 'buy':
		line_item = LineItem(cart=cart,product=product)
		cart.buycount += 1
		cart.contains_buy_order = True
		cart.save()

		if cart.already_contains(line_item):
			messages.error(request, str(product) + " already is in your cart." )
			return HttpResponseRedirect(reverse('home'))
		else:
			line_item.save()
			
	elif request.POST['cart_to_add'] == 'borroh':
		line_item = LineItem(cart=cart,product=product,borroh=True)
		cart.contains_borroh_order = True
		cart.borrohcount += 1
		cart.save()

		if cart.already_contains(line_item):
			messages.error(request, str(product) + " already is in your cart." )
			return HttpResponseRedirect(reverse('home'))
		else:
			line_item.save()
	
			


	# set the session buy item total
	try: 
		request.session['buy_items_total']
		request.session['borroh_items_total']
	except:
		request.session['buy_items_total'] = 0
		request.session['buy_items_total'] = 0

	buy_total = cart.buy_items_total()
	borroh_total = cart.borroh_items_total()

	cart.total_price = buy_total
	cart.total_points = borroh_total
	cart.save()

	return HttpResponseRedirect(reverse('home'))

def delete_item(request,id):
	
	cart = Cart.objects.get(id=request.session['cart_id'])
	line_item = LineItem.objects.get(id=id)
	if line_item.borroh == False:
		price = line_item.product.price
		cart.total_price -= price
		cart.buycount -= 1
		if cart.buycount > 0:
			cart.contains_buy_order = True
		else:
			cart.contains_buy_order = False

	elif line_item.borroh == True:
		points = line_item.product.points_price
		cart.total_points -= points
		cart.borrohcount -= 1
		if cart.borrohcount > 0:
			cart.contains_borroh_order = True
		else:
			cart.contains_borroh_order = False

	cart.save()
	line_item.delete()

	return HttpResponseRedirect(reverse('home'))











