import stripe
from django.shortcuts import render,HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from account.models import Profile
from subscription.models import Subscription
from django.contrib import messages


def subscribe(request):
	stripe.api_key = settings.API_KEY2
	try:
		token = request.POST['stripeToken']
		profile = Profile.objects.get(user=request.user)
	except:
		token = None
		profile = None

	try:
		variables = request.POST
	except:
		return HttpResponseRedirect(reverse('error'))
	
	
	if variables:
		try:
			subscription = Subscription.objects.get(name=str(variables['planType']))
			user_to_subscribe = Profile.objects.get(user=request.user)
			user_to_subscribe.subscription = subscription
			user_to_subscribe.subscription
			user_to_subscribe.points += subscription.points_per_month
			user_to_subscribe.free_shipping_count += subscription.free_shipments
			user_to_subscribe.save()
		except:
			subscription = None
			user_to_subscribe = None

		if user_to_subscribe is not None and user_to_subscribe.subscription is not None:
			user_subscription_confirmation = {
				'user' : request.user,
				'plan' : variables['planType'],
				'email' : variables['stripeEmail'],
				'price' : subscription.price_per_month,
				'points' : subscription.points_per_month
			}

			context = {'user_subscription_confirmation' : user_subscription_confirmation}
			template = 'subscription/subscription_confirmation.html'
			return render(request,template,context)
		else:
			messages.error(request, "Please create account to subscribe." )
			return HttpResponseRedirect(reverse('home'))

	context = {'stripeKey' : settings.API_KEY2}
	template = 'subscription/subscribe.html'
	return render(request,template,context)

def subscription_thank_you(request):
	context = {}
	template = 'subscription/subscription_confirmation.html'
	return render(request,template,context)