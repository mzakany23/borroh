from django import forms
from django.contrib.auth.models import User

# -----------------------------------------------------------------------------------
# login
# -----------------------------------------------------------------------------------

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={
		"name" : "log",
		"id" : "login-user",
		"class" : "form-control input",
		"size" : "20",
		"placeholder" : "Enter Username",
		"type" : "text",
	}))

	password = forms.CharField(widget=forms.TextInput(attrs={
		"name" : "Password",
		"id" : "login-password",
		"class" : "form-control input",
		"size" : "20",
		"placeholder" : "Password",
		"type" : "password",
	}))

	# def clean(self):
	#   cleaned_data = super(LoginForm, self).clean()
	#   username = cleaned_data.get("username")
	#   password = cleaned_data.get("password")

	#   if username and password:
	#     if 'greg' not in username:
	#         raise forms.ValidationError("we love greg")





# -----------------------------------------------------------------------------------
# registration
# -----------------------------------------------------------------------------------

class RegisterUserForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={
		"name" : "login",
		"class" : "form-control input",
		"size" : "20",
		"placeholder" : "Enter Username",
		"type" : "text",
	}))
	email = forms.CharField(widget=forms.TextInput(attrs={
		"name" : "reg",
		"class" : "form-control input",
		"size" : "20",
		"placeholder" : "Enter Email",
		"type" : "email",
	}))
	password = forms.CharField(widget=forms.TextInput(attrs={
		"name" : "password",
		"class" : "form-control input",
		"size" : "20",
		"placeholder" : "Enter Password",
		"type" : "password",
	}))

	