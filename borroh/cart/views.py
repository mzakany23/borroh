from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Cart,LineItem
from product.models import Product
from django.contrib.auth.models import User,AnonymousUser

def cart_show(request):
	try:
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
	except:
		pass

	context = {'cart' : cart, 'items' : cart.lineitem_set.all()}

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
	return HttpResponseRedirect(reverse('cart_show'))










