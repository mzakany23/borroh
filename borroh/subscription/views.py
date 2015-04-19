from django.shortcuts import render
from django.conf import settings
import stripe
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

	print request.POST
	# customer = stripe.Customer.create(
	#   source=token,
	#   plan="gold",
	#   email="payinguser@example.com"
	# )
	context = {'stripeKey' : settings.API_KEY2}
	template = 'subscription/subscribe.html'
	return render(request,template,context)
