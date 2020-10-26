from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from phonenumber_field.modelfields import PhoneNumberField


def only_int(value): 
    if value.isdigit()==False:
        raise ValidationError('ID contains characters')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(label='Your name')   
    phone = forms.CharField(label='Your Whatsapp number',validators=[only_int])
    class Meta:
        model = User
        fields = ['username','email','name','phone','password1','password2']