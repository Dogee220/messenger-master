from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView


class signupForm(UserCreationForm):
	password1= forms.CharField(widget=forms.PasswordInput, label='')
	password2= forms.CharField(widget=forms.PasswordInput, label='')
	email=forms.EmailField(label='')
	username=forms.CharField(label='')

	class Meta:
		model=User
		fields= ['username','email','password1','password2']

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['password1'].widget.attrs.update({
				"placeholder":"Пароль",
			})

		self.fields['password2'].widget.attrs.update({
				"placeholder":"Підтвердження паролю",
			})

		self.fields['email'].widget.attrs.update({
				"placeholder":"Пошта"
			})

		self.fields['username'].widget.attrs.update({
				"placeholder":"Ім'я користувача"
			})

class loginForm(forms.Form):
	username=forms.CharField(label='')
	password=forms.CharField(widget=forms.PasswordInput,label='')

	def __init__(self,*args,**kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({
				"placeholder":"Ім'я користувача"
			})
		self.fields['password'].widget.attrs.update({
				"placeholder":"Пароль"
			})
