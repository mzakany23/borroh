from django.conf import settings
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from form import LoginForm,RegisterUserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import Product
from account.models import Profile,Address
from home.views import get_home_variables
from django.template import RequestContext
from django.contrib.auth.models import AnonymousUser
from account.form import AddressForm




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
def user_profile(request,id):
	try:
		user = User.objects.get(id=id)
	except:
		user = None

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
		form = None

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

@login_required(login_url='/account/login')
def profile_info(request):
	try:
		user = User.objects.get(id=request.user.id)
		profile = Profile.objects.get(user=user)
		addresses = profile.address_set.all()
	except:
		profile = None
		list_object = None



	template = 'account/profile/user-information.html'
	context = {}
	return render(request,template,context)

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











