from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
            

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)

        

