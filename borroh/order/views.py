from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from home.views import get_home_variables
from django.template import RequestContext

def start_order_process(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('order_address'))
	else:
		return HttpResponseRedirect(reverse('order_auth'))

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











