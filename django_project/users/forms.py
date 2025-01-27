from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() # required field; default is required

    class Meta: # gives a nested name space for configurations
        model = User
        fields = ["username", "email", "password1", "password2"]

# model form allows us to create a form that will work with a specific database model; in this case, to update user model

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() # required field; default is required

    class Meta:
        model = User
        fields = ["username", "email"] 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]