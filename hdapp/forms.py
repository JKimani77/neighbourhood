from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import SelectMultiple

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email', 'password1','password2', 'role')

        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',  max_length=254)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)



class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('about','my_location')
