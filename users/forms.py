from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import NewUser
from django.forms import  TextInput, EmailInput

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()

    class Meta:
        model = NewUser
        #fields = ['user_name', 'email','first_name','last_name','country', 'password1', 'password2']
        fields = ['user_name', 'email','first_name','last_name', 'password1', 'password2']
 