from django import forms
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User
from account.models import Profile,Address

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

	
# -----------------------------------------------------------------------------------
# updating user info
# -----------------------------------------------------------------------------------
class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username','email','first_name','last_name']
		widgets = {
            'username': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'email': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'first_name': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'last_name': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
    
    }

class AddressForm(ModelForm):
	class Meta:
		model = Address
		fields = ['name','first','last','street','secondary','city','state','zip_code' ,'phone_number','primary_address','shipping_address']
		widgets = {
            'name': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'first': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'last': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'street': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'secondary': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'city': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'state': forms.Select(attrs={
            	'class': 'form-control', 
            }),
            'zip_code': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'phone_number': forms.TextInput(attrs={
            	'class': 'form-control', 
            }),
            'primary_address': forms.CheckboxInput(attrs={
            	'class': 'form-control', 
            }),
            'shipping_address': forms.CheckboxInput(attrs={
            	'class': 'form-control', 
            }),

        }


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

	