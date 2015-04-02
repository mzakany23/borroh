from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from form import LoginForm,RegisterUserForm

def auth_login(request):
	form = LoginForm(request.POST or None)
	
	if form.is_valid():
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		
		user = authenticate(username=username,password=password)
		
		if user:
			login(request,user)
		else:
			print 'does not exist try again'

	return HttpResponseRedirect('/')

def auth_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def auth_create_account(request):
	form = RegisterUserForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = User.objects.create_user(username,email,password)
		user.save()
		authenticated_user = authenticate(username=username,password=password)
		login(request,authenticated_user)
	return HttpResponseRedirect('/')

