from django import forms

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
		"type" : "text",
	}))
	password = forms.CharField(widget=forms.TextInput(attrs={
		"name" : "password",
		"class" : "form-control input",
		"size" : "20",
		"placeholder" : "Enter Password",
		"type" : "text",
	}))

	