from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(label='Your name')   
    phone = forms.CharField(label='Your Whatsapp number',validators=[only_int])
    class Meta:
        model = User
        fields = ['username','email','name','phone','password1','password2']