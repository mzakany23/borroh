from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def start_order_process(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('order_address'))
	else:
		return HttpResponseRedirect(reverse('order_auth'))

# auth

def order_auth(request):
	context = {}
	template = 'order/checkout-auth.html'
	return render(request,template,context)

# address
@login_required
def order_address(request):
	context = {}
	template = 'order/checkout-address.html'
	return render(request,template,context)

# billing
@login_required
def order_billing(request):
	context = {}
	template = 'order/checkout-billing.html'
	return render(request,template,context)

# shipping
@login_required
def order_shipping(request):
	context = {}
	template = 'order/checkout-shipping.html'
	return render(request,template,context)

# payment
@login_required
def order_payment(request):
	context = {}
	template = 'order/checkout-payment.html'
	return render(request,template,context)

# order
@login_required
def order_show(request):
	context = {}
	template = 'order/checkout-order.html'
	return render(request,template,context)










