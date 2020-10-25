from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(label='Your name')   
    phone = forms.BigIntegerField(label='Your Whatsapp number')
    class Meta:
        model = User
        fields = ['username','email','name','phone','password1','password2']