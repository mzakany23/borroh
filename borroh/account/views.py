from django.conf import settings
from django.shortcuts import render,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout

from form import LoginForm,RegisterUserForm
from django.contrib.auth.decorators import login_required

# borroh models
from django.contrib.auth.models import User,AnonymousUser
from product.models import Product
from account.models import Profile,Address, EmailReset, UserCreditCard

from django.contrib import messages
from home.views import get_home_variables
from django.template import RequestContext

# forms
from account.form import AddressForm, UserForm

from django.core.mail import send_mail,EmailMultiAlternatives
import hashlib
import stripe



def auth_login(request):
	form = LoginForm(request.POST or None)
	form2 = RegisterUserForm(request.POST or None)
	
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		
		user = authenticate(username=username,password=password)
		
		if user:
			login(request,user)
			messages.success(request,'You successfully logged in!')
			request.session['errors'] = None
		else:
			request.session['errors'] = 'Please try logging in again'
			template = 'account/auth/authentication.html'
			return HttpResponseRedirect('login')
		return HttpResponseRedirect(reverse('home'))

	if form2.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = User.objects.create_user(username,email,password)
		user.save()
		authenticated_user = authenticate(username=username,password=password)
		login(request,authenticated_user)
		messages.success(request, str(user.username) + ', You have successfully signed up!')
		return HttpResponseRedirect(reverse('home'))

	try: 
		request.session['errors']
	except: 
		request.session['errors'] = None

	context = {'login' : LoginForm, 'register' : RegisterUserForm, 'errors' : request.session['errors']}
	template = 'account/auth/authentication.html'
	return render(request,template,context)

def login_as_guest(request):
	request.user = AnonymousUser()
	return HttpResponseRedirect(reverse('start_order_process'))


def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def auth_create_account(request):
	form = RegisterUserForm(request.POST or None)
	form2 = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = User.objects.create_user(username,email,password)
		user.save()
		authenticated_user = authenticate(username=username,password=password)
		login(request,authenticated_user)
		messages.success(request, str(user.username) + ', You have successfully signed up!')
		return HttpResponseRedirect('/')

	if form2.is_valid():
		username = form2.cleaned_data['username']
		password = form2.cleaned_data['password']
		
		user = authenticate(username=username,password=password)
		
		if user:
			messages.success(request, 'You have successfully logged in!')
			login(request,user)
		else:
			print 'does not exist try again'
		return HttpResponseRedirect('/')

	template = 'account/auth/authentication.html'
	context = {'register' : RegisterUserForm, 'login' : LoginForm}
	return render(request,template,context)

@login_required(login_url='/account/login')
def user_profile(request):
	try:
		user = User.objects.get(id=request.user.id)
	except:
		user = None

	try:
		profile = Profile.objects.get(user=request.user)
	except:
		profile = None

	
	template = 'account/user_profile.html'
	context = {}
	return render(request,template,context)

@login_required(login_url='/account/login')
def add_address(request):
	
	try:
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.get(user=user)
		form = AddressForm(request.POST or None)
		address = Address()
	except: 
		pass

	if form.is_valid():
		address.profile = profile
		address.name = form.cleaned_data['name']
		address.first = form.cleaned_data['first']
		address.last = form.cleaned_data['last']
		address.street = form.cleaned_data['street']
		address.secondary = form.cleaned_data['secondary']
		address.city = form.cleaned_data['city']
		address.state = form.cleaned_data['state']
		address.zip_code = form.cleaned_data['zip_code']
		address.phone_number = form.cleaned_data['phone_number']
		address.primary_address = form.cleaned_data['primary_address']
		address.shipping_address = form.cleaned_data['shipping_address']
		address.save()
		return HttpResponseRedirect(reverse('show_address'))

		
	
	template = 'account/address/add-address.html'
	context = {'address_add_form' : form, 'address_edit_form' : form}
	return render(request,template,context)

@login_required(login_url='/account/login')
def delete_address(request,id):
	try:
		address = Address.objects.get(id=id)
	except:
		address = None

	if address:
		address.delete()
	
	return HttpResponseRedirect(reverse('show_address'))

@login_required(login_url='/account/login')
def show_address(request):
	try:
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.get(user=user)
		user_addresses = profile.address_set.all()
	except:
		user_addresses = None

	template = 'account/address/my-address.html'
	context = {'user_addresses' : user_addresses}
	return render(request,template,context)

@login_required(login_url='/account/login')
def edit_address(request,id):
	try:
		address = Address.objects.get(id=id)
		form = AddressForm(request.POST or None,instance=address)
	except:
		address = None
		form = None

	if form is not None:
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('show_address'))

	template = 'account/address/edit-address.html'
	context = {'address_edit_form' : form,'address' : address}
	return render(request,template,context)

@login_required(login_url='/account/login')
def edit_auth(request):
	template = 'account/auth/authentication.html'
	context = {}
	return render(request,template,context)

# -------------------------------------------------------------
# profile_info
# -------------------------------------------------------------
@login_required(login_url='/account/login')
def profile_info(request):
	try:
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.get(user=request.user)
		credit_card = profile.usercreditcard_set.all()
	except:
		user = None
		profile = None
		credit_card = None
		
	template = 'account/profile/user-information.html'
	context = {'user_info' : user, 'user_credit_card' : credit_card}
	return render(request,template,context)

def profile_info_edit(request):
	try:
		user = User.objects.get(id=request.user.id)
	except:
		user = None

	form = UserForm(request.POST or None,instance=user)

	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('user_profile'))

	template = 'account/profile/edit_information.html'
	context = {'user_form' : form}
	return render(request,template,context)

@login_required(login_url='/account/login')
def add_card_to_stripe(request):
	form = request.POST
	if form:
		try:
			profile = Profile.objects.get(user=request.user)
			stripe.api_key = settings.API_KEY
			customer = stripe.Customer.retrieve(str(profile.stripe_id))
			card = customer.sources.create(source=str(form['stripeToken']))
			credit_card = UserCreditCard()
			credit_card.profile = profile
			credit_card.credit_card_last_4 = card["last4"]
			credit_card.credit_card_last_4
			credit_card.type_of_credit_card = card["brand"]
			credit_card.card_token = card["id"]
			credit_card.save()
			return HttpResponseRedirect(reverse('profile_info'))
		except:
			pass



	template = 'account/profile/add_credit_card_form.html'
	context = {}
	return render(request,template,context)


@login_required(login_url='/account/login')
def delete_stripe_card(request):
	try:
		profile = Profile.objects.get(user=request.user)
		digits = request.POST['last_4']
	except:
		digits = None
		profile = None

	if profile and digits:
		card = UserCreditCard.objects.get(profile=profile,credit_card_last_4=digits)
		stripe.api_key = settings.API_KEY
		customer = stripe.Customer.retrieve(profile.stripe_id)
		customer.sources.retrieve(str(card.card_token)).delete()
		card.delete()
	return HttpResponseRedirect(reverse('profile_info'))


# -------------------------------------------------------------


@login_required(login_url='/account/login')
def user_wishlist(request):
	try:
		profile = Profile.objects.get(user=request.user)
		favorite_products = profile.favorites
	except:
		profile = None
		favorite_products = 0


	context = {'favorite_products' : favorite_products, 'settings' : settings}
	template = 'account/wishlist/wishlist.html'
	return render(request,template,context,context_instance=RequestContext(request, processors=[get_home_variables]))


@login_required(login_url='/account/login')
def show_borrohed(request):
	template = "account/borroh/borroh-show.html"
	context = {}
	return render(request,template,context,context_instance=RequestContext(request, processors=[get_home_variables]))


@login_required(login_url='/account/login')
def add_to_wishlist(request,id):
	try:
		product = Product.objects.get(id=id)
		profile = Profile.objects.get(user=request.user)
		profile.favorites.add(product)
		profile.save()
	except:
		pass
	return HttpResponseRedirect(reverse('user_wishlist'))

@login_required(login_url='/account/login')
def delete_from_wishlist(request,id):
	try:
		product = Product.objects.get(id=id)
		profile = Profile.objects.get(user=request.user)
		favorite = profile.favorites.filter(pk=product.id)
		favorite.delete()
		profile.save()
	except:
		pass
	
	return HttpResponseRedirect(reverse('user_wishlist'))

@login_required(login_url='/account/login')
def account_order_list(request):
	template = 'account/orders/order-list.html'
	context = {}
	return render(request,template,context)


@login_required(login_url='/account/login')
def user_password_reset(request):
	try:
		email_address = request.user.email
		user = request.user
	except:
		email_address = None
		user = None

	subject, from_email, to = 'hello', email_address, 'mzakany@gmail.com'
	text_content = 'This is an important message.'
	html_content = '<p>Hey does this work?This is an <strong>important</strong> message.</p><a href="www.google.com">Click to go to google'

	send_confirmation_email(user,subject,text_content, from_email,to, html_content)
	
	messages.success(request, "Password Rest Sent to " + str(email_address) )

	return HttpResponseRedirect(reverse('profile_info'))

def send_confirmation_email(user, subject,text_content,from_email, to, html):
		password_key = hashlib.sha224(str(user)).hexdigest()

		new_confirmation = EmailReset()
		new_confirmation.user = user
		new_confirmation.hash_key = password_key
		new_confirmation.save()

		msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
		msg.attach_alternative(html, "text/html")
		msg.send()







