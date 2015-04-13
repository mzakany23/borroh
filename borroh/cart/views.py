from django.conf import settings
from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Cart,LineItem
from product.models import Product
from django.contrib.auth.models import User,AnonymousUser


def cart_show(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		cart_items = cart.lineitem_set.all()
	except:
		cart = None
		cart_items = None

	try:
		list_set = cart.lineitem_set.all().order_by('borroh')
	except:
		list_set = None

	context = {'cart' : cart, 'items' : cart_items, 'list' : list_set, 'settings' : settings}

	template = 'cart/show_cart.html'
	return render(request,template,context)

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
	elif request.POST['cart_to_add'] == 'borroh':
		line_item = LineItem(cart=cart,product=product,borroh=True)

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
	elif line_item.borroh == True:
		points = line_item.product.points_price
		cart.total_points -= points

	cart.save()
	line_item.delete()

	return HttpResponseRedirect(reverse('home'))











