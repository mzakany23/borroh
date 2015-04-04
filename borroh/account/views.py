from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from form import LoginForm,RegisterUserForm
from django.contrib.auth.decorators import login_required


def auth_login(request):
	form = LoginForm(request.POST or None)
	form2 = RegisterUserForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		
		user = authenticate(username=username,password=password)
		
		if user:
			login(request,user)
		else:
			print 'does not exist try again'
			return HttpResponseRedirect('login')
		return HttpResponseRedirect('/')

	if form2.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = User.objects.create_user(username,email,password)
		user.save()
		authenticated_user = authenticate(username=username,password=password)
		login(request,authenticated_user)
		return HttpResponseRedirect('/')

	context = {'login' : LoginForm, 'register' : RegisterUserForm}
	template = 'account/auth/authentication.html'
	return render(request,template,context)

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
		return HttpResponseRedirect('/')

	if form2.is_valid():
		username = form2.cleaned_data['username']
		password = form2.cleaned_data['password']
		
		user = authenticate(username=username,password=password)
		
		if user:
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
def add_address(request,id):
	try:
		user = User.objects.get(id=id)
	except: 
		user = None

	template = 'account/address/add-address.html'
	context = {}
	return render(request,template,context)

@login_required(login_url='/account/login')
def show_address(request):
	template = 'account/address/my-address.html'
	context = {}
	return render(request,template,context)

@login_required(login_url='/account/login')
def edit_auth(request):
	template = 'account/auth/authentication.html'
	context = {}
	return render(request,template,context)

@login_required(login_url='/account/login')
def profile_info(request):
	template = 'account/profile/user-information.html'
	context = {}
	return render(request,template,context)

@login_required(login_url='/account/login')
def user_wishlist(request):
	template = 'account/wishlist/wishlist.html'
	context = {}
	return render(request,template,context)















