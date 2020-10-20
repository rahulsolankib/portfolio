from django import forms
from django.contrib.auth.models import user
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['Username','email','password1','password2']