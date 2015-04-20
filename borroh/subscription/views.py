import stripe
from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from account.models import Profile

def subscribe(request):
	stripe.api_key = settings.API_KEY
	try:
		token = request.POST['stripeToken']
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.get(user=user)
	except:
		token = None
		profile = None

	try:
		variables = request.POST
	except:
		return HttpResponseRedirect(reverse('error'))
	
	if variables:
		print variables
		return HttpResponseRedirect(reverse('subscription_thank_you'))

	context = {'stripeKey' : settings.API_KEY2}
	template = 'subscription/subscribe.html'
	return render(request,template,context)

def subscription_thank_you(request):
	context = {}
	template = 'subscription/subscription_confirmation.html'
	return render(request,template,context)