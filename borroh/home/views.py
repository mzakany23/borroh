from django.shortcuts import render
from account.form import LoginForm,RegisterUserForm

def home(request):
	context = {'login_form' : LoginForm, 'register' : RegisterUserForm}
	template = 'home/index.html'
	return render(request,template,context)
